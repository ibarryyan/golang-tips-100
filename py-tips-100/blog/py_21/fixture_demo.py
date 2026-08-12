"""pytest fixture 演示"""
import pytest
import os


# === 基本 fixture ===
@pytest.fixture
def sample_data():
    """提供测试数据"""
    return [1, 2, 3, 4, 5]


def test_sum(sample_data):
    assert sum(sample_data) == 15


def test_length(sample_data):
    assert len(sample_data) == 5


# === 带 teardown 的 fixture ===
@pytest.fixture
def db_connection():
    """模拟数据库连接"""
    print("\n  [setup] 建立连接")
    conn = {"connected": True, "data": []}
    yield conn  # yield 之前是 setup，之后是 teardown
    print("\n  [teardown] 关闭连接")
    conn["connected"] = False


def test_db_insert(db_connection):
    db_connection["data"].append("record1")
    assert db_connection["data"] == ["record1"]
    assert db_connection["connected"] is True


# === fixture 作用域 ===
@pytest.fixture(scope="module")
def module_config():
    """整个模块只创建一次"""
    print("\n  [module setup] 加载配置")
    return {"env": "test", "debug": True}


def test_config_env(module_config):
    assert module_config["env"] == "test"


def test_config_debug(module_config):
    assert module_config["debug"] is True


# === 内置 fixture ===
def test_tmp_path(tmp_path):
    """tmp_path 提供临时目录"""
    f = tmp_path / "test.txt"
    f.write_text("hello pytest")
    assert f.read_text() == "hello pytest"


def test_capsys(capsys):
    """capsys 捕获 stdout/stderr"""
    print("hello pytest")
    captured = capsys.readouterr()
    assert "hello pytest" in captured.out


def test_monkeypatch(monkeypatch):
    """monkeypatch 修改环境变量"""
    monkeypatch.setenv("TEST_KEY", "test_value")
    assert os.environ["TEST_KEY"] == "test_value"
    # 测试结束后环境变量自动恢复


if __name__ == "__main__":
    import subprocess
    result = subprocess.run(
        ["python", "-m", "pytest", __file__, "-v", "-s"],
        capture_output=True, text=True,
    )
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
