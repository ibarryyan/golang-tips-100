## 《Python小技巧&易错点100例》

这个目录用于收集和整理我在开发 AI 项目过程中遇到的 Python 小技巧和易错点。

之前做 Go 开发时，很多问题会围绕工程结构、并发、类型、错误处理、依赖管理展开；而切到 Python 后，问题的形态会明显变化：语法更灵活、生态更庞大、动态类型更方便也更容易埋坑，尤其在 AI 项目里还会频繁接触虚拟环境、数据处理、异步调用、模型 SDK、配置管理、Notebook 与脚本混用等场景。

所以这里会参考 `Go小技巧&易错点100例` 的方式，把日常开发中反复遇到的问题拆成短小的知识点。每篇文章控制在 3~5 个点左右，尽量做到：

- 有问题场景：说明为什么会踩坑。
- 有可运行代码：用最小示例复现或演示。
- 有推荐写法：给出实际项目里更稳妥的做法。
- 有关键词标签：方便后续按主题检索和扩展。

---

### 专栏目录

| Python Tips | Python基础知识 | Python工程实践 | Python AI开发 | Python优化与调试 |
| --- | --- | --- | --- | --- |
| `收集和总结 Python 开发中常见的小技巧和易错点，每篇文章大概提供 3~5 个知识点` | `Python 语法、数据结构、函数、模块、面向对象等基础内容` | `虚拟环境、依赖管理、配置、日志、测试、项目结构等工程化内容` | `AI 项目中常见的数据处理、模型调用、异步任务、Prompt 组织等实践` | `性能分析、内存占用、异常排查、调试工具、代码质量等内容` |
| [专栏大纲](#专栏大纲) | [Python基础知识](#Python基础知识) | [Python工程实践](#Python工程实践) | [Python-AI开发](#Python-AI开发) | [Python优化与调试](#Python优化与调试) |

---

### Python Tips 100

#### 专栏大纲

| 分类 | 标签 | 计划内容 | 适合阶段 |
| --- | --- | --- | --- |
| 语法基础 | 变量、缩进、注释、输入输出 | 建立 Python 基本语法直觉，避免把其他语言习惯直接搬过来 | 新手入门 |
| 数据结构 | list、tuple、dict、set、str | 掌握常用容器的增删改查、复制、遍历和常见陷阱 | 新手入门 |
| 函数与作用域 | 参数、默认值、闭包、lambda、装饰器 | 理解 Python 函数是一等对象以及作用域规则 | 入门进阶 |
| 模块与包 | import、包结构、虚拟环境、依赖 | 能组织可维护的脚本和项目，减少环境问题 | 工程入门 |
| 面向对象 | class、dataclass、继承、魔术方法 | 了解 Python 风格的对象建模方式 | 入门进阶 |
| 异常处理 | try、except、raise、上下文管理器 | 写出可定位、可恢复、可清理资源的代码 | 工程入门 |
| 文件与数据 | pathlib、json、csv、yaml、编码 | 处理配置、文本、结构化数据和路径兼容性问题 | 工程入门 |
| 并发异步 | threading、multiprocessing、asyncio | 区分 IO 密集和 CPU 密集场景，避免异步误用 | 工程进阶 |
| AI项目实践 | SDK调用、Prompt、Token、流式响应、批处理 | 总结 AI 项目中高频工程技巧和易错点 | AI实践 |
| 测试与质量 | pytest、ruff、mypy、logging | 让脚本逐步演进为可靠项目 | 工程进阶 |
| 性能与调试 | timeit、cProfile、内存分析、调试器 | 定位慢代码、内存问题和线上异常 | 工程进阶 |

#### 更新进度

| 标题 | 文章 | 代码 | 关键词 | 数量 | 难度 |
| --- | --- | --- | --- | --- | --- |
| 开篇词 | [AI时代，我们重新出发：从Go小技巧到Python小技巧](blog/opening/README.md) | - | Go小技巧、Python小技巧、AI时代、重新出发 | 0 | ⭐ |
| 第一篇 | [变量、赋值与基础语法](blog/py_01/README.md) | [code](blog/py_01) | 1.动态类型不是没有类型<br/>2.缩进是语法的一部分<br/>3.链式赋值和解包赋值<br/>4.`is` 和 `==` 的区别<br/>`关键词：变量、缩进、赋值、对象身份` | 4 | ⭐ |
| 第二篇 | [列表、字典与可变对象](blog/py_02/README.md) | [code](blog/py_02) | 5.列表复制不能只用赋值<br/>6.函数默认参数不要使用可变对象<br/>7.遍历列表时不要直接删除元素<br/>8.字典取值推荐使用 `get` 和 `setdefault`<br/>`关键词：list、dict、可变对象` | 4 | ⭐⭐ |
| 第三篇 | [字符串、数字与常用内置能力](blog/py_03/README.md) | [code](blog/py_03) | 9.字符串拼接优先使用 `join` 或 f-string<br/>10.`len()` 统计的是字符数量不是字节数量<br/>11.浮点数计算存在精度问题<br/>12.真值判断要理解空值规则<br/>`关键词：str、float、bool、内置函数` | 4 | ⭐ |
| 第四篇 | [函数、异常与文件处理](blog/py_04/README.md) | [code](blog/py_04) | 13.函数返回多个值本质是 tuple<br/>14.异常不要直接吞掉<br/>15.文件读写优先使用 `with`<br/>16.路径处理优先使用 `pathlib`<br/>`关键词：函数、异常、文件、pathlib` | 4 | ⭐⭐ |
| 第五篇 | [闭包、lambda与作用域](blog/py_05/README.md) | [code](blog/py_05) | 17.闭包捕获的是变量引用而非值<br/>18.lambda是匿名函数但能力有限<br/>19.global和nonlocal的使用场景<br/>20.列表推导式vs生成器表达式<br/>`关键词：闭包、lambda、作用域、列表推导式、生成器` | 4 | ⭐⭐ |
| 第六篇 | [面向对象基础](blog/py_06/README.md) | [code](blog/py_06) | 21.class属性与实例属性的区别<br/>22.`__init__`不是构造函数，`__new__`才是<br/>23.私有变量靠约定不靠强制<br/>24.魔术方法`__str__`和`__repr__`的区别<br/>`关键词：class、实例属性、魔术方法、__repr__` | 4 | ⭐⭐ |
| 第七篇 | [迭代器、生成器与装饰器](blog/py_07/README.md) | [code](blog/py_07) | 25.自定义迭代器实现`__iter__`和`__next__`<br/>26.生成器函数用yield暂停执行<br/>27.装饰器本质是函数包装函数<br/>28.functools.wraps保留被装饰函数的元信息<br/>`关键词：迭代器、生成器、yield、装饰器、functools.wraps` | 4 | ⭐⭐⭐ |
| 第八篇 | [模块、包与导入机制](blog/py_08/README.md) | [code](blog/py_08) | 29.`__name__ == "__main__"`的作用<br/>30.from import和import的区别<br/>31.`__init__.py`的作用和包结构<br/>32.相对导入和绝对导入<br/>`关键词：import、模块、包结构、相对导入` | 4 | ⭐⭐ |
| 第九篇 | [虚拟环境与依赖管理](blog/py_09/README.md) | [code](blog/py_09) | 33.venv创建和激活虚拟环境<br/>34.requirements.txt和pip freeze<br/>35.pip install的常见问题<br/>36.uv/poetry等现代依赖管理工具<br/>`关键词：venv、requirements.txt、pip、uv、poetry` | 4 | ⭐⭐ |
| 第十篇 | [数据序列化与编码](blog/py_10/README.md) | [code](blog/py_10) | 37.json模块的序列化和反序列化<br/>38.json处理中文时的ensure_ascii参数<br/>39.yaml配置文件读取<br/>40.pickle序列化的注意事项<br/>`关键词：json、yaml、pickle、序列化、ensure_ascii` | 4 | ⭐⭐ |
| 第十一篇 | [集合与高级数据结构](blog/py_11/README.md) | [code](blog/py_11) | 41.set的去重原理和注意事项<br/>42.Counter统计元素频次<br/>43.namedtuple给元组起名字<br/>44.dataclass简化数据类定义<br/>`关键词：set、Counter、namedtuple、dataclass` | 4 | ⭐⭐ |
| 第十二篇 | [字符串进阶处理](blog/py_12/README.md) | [code](blog/py_12) | 45.字符串的split和partition<br/>46.正则表达式re模块基础<br/>47.字符串格式化的三种方式<br/>48.f-string的高级用法<br/>`关键词：split、partition、正则表达式、f-string、格式化` | 4 | ⭐⭐ |
| 第十三篇 | [日期时间处理](blog/py_13/README.md) | [code](blog/py_13) | 49.datetime模块基础操作<br/>50.时间戳与datetime互转<br/>51.时区处理与pytz/zoneinfo<br/>52.timedelta计算时间差<br/>`关键词：datetime、时间戳、时区、zoneinfo、timedelta` | 4 | ⭐⭐ |
| 第十四篇 | [文件与目录操作进阶](blog/py_14/README.md) | [code](blog/py_14) | 53.os.path vs pathlib选择<br/>54.递归遍历目录树<br/>55.读写CSV文件<br/>56.读写JSON文件与jsonl格式<br/>`关键词：pathlib、目录遍历、CSV、JSON、jsonl` | 4 | ⭐⭐ |
| 第十五篇 | [Python类型注解](blog/py_15/README.md) | [code](blog/py_15) | 57.基本类型注解语法<br/>58.Optional和Union的使用<br/>59.List/Dict/Tuple泛型注解<br/>60.TypedDict和Protocol<br/>`关键词：类型注解、Optional、Union、TypedDict、Protocol` | 4 | ⭐⭐ |
| 第十六篇 | [Python异常处理进阶](blog/py_16/README.md) | [code](blog/py_16) | 61.自定义异常类<br/>62.异常链：raise from的用法<br/>63.finally的执行时机和陷阱<br/>64.contextlib实现上下文管理器<br/>`关键词：自定义异常、raise from、finally、contextlib` | 4 | ⭐⭐⭐ |
| 第十七篇 | [并发编程基础](blog/py_17/README.md) | [code](blog/py_17) | 65.threading模块基础与GIL限制<br/>66.threading.Lock和RLock<br/>67.concurrent.futures线程池<br/>68.multiprocessing模块基础<br/>`关键词：threading、GIL、Lock、concurrent.futures、multiprocessing` | 4 | ⭐⭐⭐ |
| 第十八篇 | [asyncio异步编程](blog/py_18/README.md) | [code](blog/py_18) | 69.async/await基础语法<br/>70.asyncio事件循环和任务<br/>71.asyncio.gather和wait的区别<br/>72.asyncio中的超时和取消<br/>`关键词：asyncio、async/await、事件循环、gather、超时` | 4 | ⭐⭐⭐ |
| 第十九篇 | [Python与HTTP请求](blog/py_19/README.md) | [code](blog/py_19) | 73.requests库基础用法<br/>74.requests的session和cookie<br/>75.requests超时重试与异常处理<br/>76.httpx和aiohttp的异步请求<br/>`关键词：requests、session、cookie、httpx、aiohttp` | 4 | ⭐⭐ |
| 第二十篇 | [Python日志与调试](blog/py_20/README.md) | [code](blog/py_20) | 77.logging模块基础配置<br/>78.logging的handler和formatter<br/>79.pdb和ipdb调试技巧<br/>80.print调试vs logging调试<br/>`关键词：logging、handler、formatter、pdb、ipdb` | 4 | ⭐⭐ |
| 第二十一篇 | [Python测试基础](blog/py_21/README.md) | [code](blog/py_21) | 81.pytest基础用法<br/>82.pytest的fixture<br/>83.pytest的parametrize参数化测试<br/>84.mock和patch的使用<br/>`关键词：pytest、fixture、parametrize、mock、patch` | 4 | ⭐⭐ |
| 第二十二篇 | [Python性能优化](blog/py_22/README.md) | [code](blog/py_22) | 85.timeit测量代码执行时间<br/>86.cProfile分析性能瓶颈<br/>87.列表推导式vs map/filter性能<br/>88.`__slots__`减少内存占用<br/>`关键词：timeit、cProfile、__slots__、性能优化` | 4 | ⭐⭐⭐ |
| 第二十三篇 | [Python内存管理](blog/py_23/README.md) | [code](blog/py_23) | 89.引用计数与gc模块<br/>90.weakref弱引用的使用场景<br/>91.del语句和垃圾回收时机<br/>`关键词：引用计数、gc模块、weakref、del、垃圾回收` | 3 | ⭐⭐⭐ |
| 第二十四篇 | [Pythonic编码风格](blog/py_24/README.md) | [code](blog/py_24) | 92.enumerate替代range(len())<br/>93.zip并行遍历多个序列<br/>94.any()和all()的短路求值<br/>`关键词：enumerate、zip、any、all、Pythonic` | 3 | ⭐ |
| 第二十五篇 | [Python函数式编程技巧](blog/py_25/README.md) | [code](blog/py_25) | 95.map/filter/reduce的使用场景<br/>96.itertools常用工具函数<br/>97.operator模块简化函数式写法<br/>`关键词：map、filter、reduce、itertools、operator` | 3 | ⭐⭐ |
| 第二十六篇 | [Python与系统交互](blog/py_26/README.md) | [code](blog/py_26) | 98.subprocess执行外部命令<br/>99.os和sys模块常用功能<br/>100.环境变量读取的最佳实践<br/>`关键词：subprocess、os模块、sys模块、环境变量` | 3 | ⭐⭐ |
| 第二十七篇 | [AI项目实践-Prompt工程](blog/py_27/README.md) | [code](blog/py_27) | 101.Prompt模板管理与复用<br/>102.结构化输出解析（JSON mode）<br/>103.流式响应处理与SSE<br/>`关键词：Prompt模板、JSON mode、流式响应、SSE` | 3 | ⭐⭐ |
| 第二十八篇 | [AI项目实践-数据处理](blog/py_28/README.md) | [code](blog/py_28) | 104.大文件分块读取与处理<br/>105.批量请求与限流控制<br/>106.数据清洗与格式转换常用技巧<br/>`关键词：大文件处理、分块读取、限流控制、数据清洗` | 3 | ⭐⭐ |
| 第二十九篇 | [AI项目实践-工程化](blog/py_29/README.md) | [code](blog/py_29) | 107.API Key安全管理与环境变量注入<br/>108.异步任务队列与后台处理<br/>`关键词：API Key安全、环境变量注入、异步任务队列` | 2 | ⭐⭐⭐ |

Total：108

---

### Python基础知识

| 文章 | 关键词 | 难度 |
| --- | --- | --- |
| [变量、赋值与基础语法](blog/py_01/README.md) | 变量、缩进、赋值、对象身份 | ⭐ |
| [列表、字典与可变对象](blog/py_02/README.md) | list、dict、可变对象 | ⭐⭐ |
| [字符串、数字与常用内置能力](blog/py_03/README.md) | str、float、bool、内置函数 | ⭐ |
| [函数、异常与文件处理](blog/py_04/README.md) | 函数、异常、文件、pathlib | ⭐⭐ |
| [闭包、lambda与作用域](blog/py_05/README.md) | 闭包、lambda、作用域、生成器 | ⭐⭐ |
| [面向对象基础](blog/py_06/README.md) | class、实例属性、魔术方法 | ⭐⭐ |
| [迭代器、生成器与装饰器](blog/py_07/README.md) | 迭代器、生成器、yield、装饰器 | ⭐⭐⭐ |
| [模块、包与导入机制](blog/py_08/README.md) | import、模块、包结构、相对导入 | ⭐⭐ |
| [集合与高级数据结构](blog/py_11/README.md) | set、Counter、namedtuple、dataclass | ⭐⭐ |
| [字符串进阶处理](blog/py_12/README.md) | split、正则表达式、f-string、格式化 | ⭐⭐ |
| [日期时间处理](blog/py_13/README.md) | datetime、时间戳、时区、timedelta | ⭐⭐ |
| [Python类型注解](blog/py_15/README.md) | 类型注解、Optional、Union、Protocol | ⭐⭐ |
| [Pythonic编码风格](blog/py_24/README.md) | enumerate、zip、any、all、Pythonic | ⭐ |
| [Python函数式编程技巧](blog/py_25/README.md) | map、filter、reduce、itertools、operator | ⭐⭐ |

---

### Python工程实践

| 文章 | 关键词 | 难度 |
| --- | --- | --- |
| [虚拟环境与依赖管理](blog/py_09/README.md) | venv、requirements.txt、pip、uv、poetry | ⭐⭐ |
| [数据序列化与编码](blog/py_10/README.md) | json、yaml、pickle、序列化、ensure_ascii | ⭐⭐ |
| [文件与目录操作进阶](blog/py_14/README.md) | pathlib、目录遍历、CSV、JSON、jsonl | ⭐⭐ |
| [Python异常处理进阶](blog/py_16/README.md) | 自定义异常、raise from、finally、contextlib | ⭐⭐⭐ |
| [Python与HTTP请求](blog/py_19/README.md) | requests、session、cookie、httpx、aiohttp | ⭐⭐ |
| [Python日志与调试](blog/py_20/README.md) | logging、handler、formatter、pdb、ipdb | ⭐⭐ |
| [Python测试基础](blog/py_21/README.md) | pytest、fixture、parametrize、mock、patch | ⭐⭐ |
| [Python与系统交互](blog/py_26/README.md) | subprocess、os模块、sys模块、环境变量 | ⭐⭐ |

---

### Python-AI开发

| 文章 | 关键词 | 难度 |
| --- | --- | --- |
| [AI项目实践-Prompt工程](blog/py_27/README.md) | Prompt模板、JSON mode、流式响应、SSE | ⭐⭐ |
| [AI项目实践-数据处理](blog/py_28/README.md) | 大文件处理、分块读取、限流控制、数据清洗 | ⭐⭐ |
| [AI项目实践-工程化](blog/py_29/README.md) | API Key安全、环境变量注入、异步任务队列 | ⭐⭐⭐ |

---

### Python优化与调试

| 文章 | 关键词 | 难度 |
| --- | --- | --- |
| [Python性能优化](blog/py_22/README.md) | timeit、cProfile、__slots__、性能优化 | ⭐⭐⭐ |
| [Python内存管理](blog/py_23/README.md) | 引用计数、gc模块、weakref、垃圾回收 | ⭐⭐⭐ |
| [并发编程基础](blog/py_17/README.md) | threading、GIL、Lock、multiprocessing | ⭐⭐⭐ |
| [asyncio异步编程](blog/py_18/README.md) | asyncio、async/await、事件循环、gather | ⭐⭐⭐ |
