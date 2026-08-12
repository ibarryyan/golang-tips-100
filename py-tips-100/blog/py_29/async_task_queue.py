"""异步任务队列与后台处理示例"""
import uuid
import time
import threading
from dataclasses import dataclass, field
from typing import Optional, Callable, Any
from enum import Enum
from concurrent.futures import ThreadPoolExecutor, Future


class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Task:
    """任务对象"""
    id: str
    name: str
    status: TaskStatus = TaskStatus.PENDING
    result: Optional[Any] = None
    error: Optional[str] = None
    created_at: float = field(default_factory=time.time)
    completed_at: Optional[float] = None


class SimpleTaskQueue:
    """简单内存任务队列"""

    def __init__(self, max_workers: int = 4):
        self._tasks: dict[str, Task] = {}
        self._queue: list[tuple] = []
        self._max_workers = max_workers
        self._active_workers = 0
        self._lock = threading.Lock()

    def submit(self, name: str, func: Callable, *args, **kwargs) -> str:
        """提交任务"""
        task_id = str(uuid.uuid4())[:8]
        task = Task(id=task_id, name=name)
        with self._lock:
            self._tasks[task_id] = task
            self._queue.append((task, func, args, kwargs))
        self._try_dispatch()
        return task_id

    def get_status(self, task_id: str) -> Optional[Task]:
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> list[Task]:
        return list(self._tasks.values())

    def _try_dispatch(self):
        with self._lock:
            while self._queue and self._active_workers < self._max_workers:
                item = self._queue.pop(0)
                self._active_workers += 1
                thread = threading.Thread(target=self._run, args=(item,))
                thread.daemon = True
                thread.start()

    def _run(self, item):
        task, func, args, kwargs = item
        task.status = TaskStatus.RUNNING
        try:
            task.result = func(*args, **kwargs)
            task.status = TaskStatus.COMPLETED
        except Exception as e:
            task.error = str(e)
            task.status = TaskStatus.FAILED
        finally:
            task.completed_at = time.time()
            with self._lock:
                self._active_workers -= 1
            self._try_dispatch()


def demo_basic_queue():
    """基础任务队列"""
    print("=== 基础任务队列 ===")
    queue = SimpleTaskQueue(max_workers=3)

    def mock_llm_call(prompt: str) -> str:
        time.sleep(0.5)
        return f"分析结果: {prompt[:20]}..."

    # 提交多个任务
    task_ids = []
    for i in range(5):
        task_id = queue.submit(
            f"LLM任务-{i}",
            mock_llm_call,
            f"请分析这段文本内容第{i}段"
        )
        task_ids.append(task_id)
        print(f"  提交任务: {task_id} (LLM任务-{i})")

    # 等待所有任务完成
    while True:
        all_done = True
        for tid in task_ids:
            task = queue.get_status(tid)
            if task.status not in (TaskStatus.COMPLETED, TaskStatus.FAILED):
                all_done = False
                break
        if all_done:
            break
        time.sleep(0.2)

    # 打印结果
    print("\n  任务结果:")
    for tid in task_ids:
        task = queue.get_status(tid)
        duration = (task.completed_at - task.created_at) if task.completed_at else 0
        print(f"    {tid} [{task.name}] {task.status.value} ({duration:.2f}s)")
        if task.result:
            print(f"      -> {task.result}")
        if task.error:
            print(f"      -> ERROR: {task.error}")


def demo_error_handling():
    """错误处理"""
    print("\n=== 错误处理 ===")
    queue = SimpleTaskQueue(max_workers=2)

    def failing_task():
        time.sleep(0.3)
        raise ValueError("模拟LLM API调用失败")

    def success_task():
        time.sleep(0.3)
        return "成功"

    id1 = queue.submit("成功任务", success_task)
    id2 = queue.submit("失败任务", failing_task)

    time.sleep(1.0)

    for tid in [id1, id2]:
        task = queue.get_status(tid)
        print(f"  {task.name}: {task.status.value}")
        if task.result:
            print(f"    结果: {task.result}")
        if task.error:
            print(f"    错误: {task.error}")


def demo_thread_pool():
    """使用ThreadPoolExecutor（标准库方案）"""
    print("\n=== ThreadPoolExecutor方案 ===")

    def process_item(item: str) -> str:
        time.sleep(0.3)
        return f"processed: {item}"

    items = [f"item_{i}" for i in range(8)]
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(process_item, item): item for item in items}
        for future in futures:
            result = future.result()
            print(f"  {result}")


def demo_progress_tracking():
    """进度跟踪"""
    print("\n=== 进度跟踪 ===")
    queue = SimpleTaskQueue(max_workers=2)

    def long_task(n: int) -> str:
        time.sleep(0.1 * n)
        return f"task-{n} done"

    for i in range(6):
        queue.submit(f"任务-{i}", long_task, i + 1)

    while True:
        statuses = [t.status for t in queue.get_all_tasks()]
        done = sum(1 for s in statuses if s in (TaskStatus.COMPLETED, TaskStatus.FAILED))
        total = len(statuses)
        print(f"  进度: {done}/{total}", end="\r")
        if done == total:
            break
        time.sleep(0.1)

    print(f"  进度: {done}/{total} 全部完成")


if __name__ == "__main__":
    demo_basic_queue()
    demo_error_handling()
    demo_thread_pool()
    demo_progress_tracking()
