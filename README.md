## 《Go小技巧&易错点100例》

<a href="https://github.com/ibarryyan/golang-tips-100/blob/master/img/wechat.jpg"><img src="https://img.shields.io/badge/%E5%85%AC%E4%BC%97%E5%8F%B7-%E6%89%AF%E7%BC%96%E7%A8%8B%E7%9A%84%E6%B7%A1-blue" alt="公众号"></a>
[![](https://img.shields.io/github/watchers/ibarryyan/golang-tips-100.svg?style=flat)](https://github.com/ibarryyan/golang-tips-100/watchers)
[![](https://img.shields.io/github/stars/ibarryyan/golang-tips-100.svg?style=flat)](https://github.com/ibarryyan/golang-tips-100/stargazers)

![image-20231112185924824](img/logo.png)

#### 简介

《Go小技巧&易错点100例》博客专栏，主要是总结一下自己Coding过程中遇到的问题以及平时读一些博客的所得，因为做gopher也有了一段时间了，相比Java，有些问题想要利用搜索引擎排查出来可能不是那么的迅速，所以在这里以文章的形式总结出来，也方便各位gopher们能够顺利的解决所遇到的问题，并能够习得一些小技巧。

---

#### 专栏大纲（后面的括号内的数字为所在文章的序号）

> **在线地址**：https://www.processon.com/view/link/66913a1de7d7970dad42d812
> 
> 图片已更新到第25篇

![image-20231112190005980](img/main-25end.png)

---

#### 关注公众号获取最新更新

![image-20231112190005980](img/wechat.jpg)

#### 更新进度

| 标题                                                                                                                                                                                                        | 内容                                                                                              | 代码                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [开篇词](https://mp.weixin.qq.com/s/p4FEiaaxXn8JDEh0AfaAfA)                                                                                                                                                  | -                                                                                               | -                                                                             |
| [第一篇](https://mp.weixin.qq.com/s/2suBNq6RFN1INarY5pTkpA)                                                                                                                                                  | 1.函数返回值屏蔽<br />2.context继承特性<br />3.禁止main函数退出<br />4.map值的遍历次序                                 | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_01) |
| [第二篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247485221&idx=1&sn=35ba81fd1b3d7d029e071c2f40cfb083&chksm=97a3cac8a0d443dee4cf3615017f1ff970ad4a620db0d8a8393bc2df6c228e7361995d72fea4#rd)   | 5.fallthrough关键字<br />6.简式变量声明仅能在函数内部使用<br />7.防止main函数提前退出<br />8.包循环依赖错误                      | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_02) |
| [第三篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247485371&idx=1&sn=c0d43c4d50cb3fd198c1617742beeaa1&chksm=97a3ca56a0d44340e46742b2378e5c6ebcb32ce2edc0b8266a7356f92989c6cd2d5418e38db4#rd)   | 9.Go项目中对依赖库版本的升级与降级<br />10.goroutine异常<br />11.Go中slice作为参数是值传递                                | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_03) |
| [第四篇](https://mp.weixin.qq.com/s/8irznbZxQ1tiDCyzsJJDUQ)                                                                                                                                                  | 12.Go omitempty关键字<br />13.JSON Marshal需要注意的问题<br />14.Go iota关键字                               | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_04) |
| [第五篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247485391&idx=1&sn=034608e1cc1351436ff22cb0b5ebc45b&chksm=97a3ca22a0d44334b2b1f82ea81411ff1335b352f7ad35f8179ff3f0a7cf17b2175af007b67f#rd)   | 15.goroutine控制并发数量的方式<br />16.Go发起HTTP请求<br />17.断言                                             | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_05) |
| [第六篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247485413&idx=1&sn=c6520ac6911c598f86877c4155185f35&chksm=97a3ca08a0d4431e4d1c0135cc9ee951213222c155847794338f74d5126a6278ac1659f716eb#rd)   | 18.pprof查看运行时状态信息<br />19.goruntine使用后的销毁                                                       | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_06) |
| [第七篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247485446&idx=1&sn=ac2669c690efc4373f81515160269e70&chksm=97a3c5eba0d44cfdfd8238af5682220cfd979b4ae7fae10121ebe53c122a3b8d1abf7385168c#rd)   | 20.Go日志输出到文件<br />21.recover方式的异常处理<br />22.Go HTTP请求重定向                                        | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_07) |
| [第八篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247485558&idx=1&sn=b19a67e3a47d7098219d9aacdeb2e6ab&chksm=97a3c59ba0d44c8d51e763d63d1469deab5d5ce511d19b5efaa4a576bce77e5d8326129b371e#rd)   | 23.优雅的关闭Go程序<br />24.指针声明后未赋值前不能直接操作<br />25.channel方式代替time.Sleep                              | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_08) |
| [第九篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247485574&idx=1&sn=66a307a7b05e9a6784613a1891ecb736&chksm=97a3c56ba0d44c7d747ff0a28cd647f99aee835953b617c48448ba89da3a50a087c1edcea8c8#rd)   | 26.遍历指针数组<br />27.检查nil以提升程序安全性和健壮性                                                             | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_09) |
| [第十篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247485598&idx=1&sn=4eb0ad69d6031aa83a20f8d6d9c1b534&chksm=97a3c573a0d44c656213ba1109dc34e4e4bb1f112055ffd7b048dc89a9454ccfc4bb4059d56b#rd)   | 28.Go string的长度<br />29.Go优雅的Test方法<br />30.slice的各种截取                                          | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_10) |
| [第十一篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247485631&idx=1&sn=947fcd1308b469ab6a91ebba36e8dfc1&chksm=97a3c552a0d44c44ce63df8a55402c55711e073682b428d209e21fe401a4fe4301f1b79fc9bc#rd)  | 31.Go函数式编程<br />32.不建议map使用指针类型作为Key<br />33.直接使用值为nil的slice和map                                | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_11) |
| [第十二篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247485864&idx=1&sn=ed7b74e37eff86624d38ec018426e6e8&chksm=97a3c445a0d44d532a8863cadc65d3c636974dc9c2eee76692ac189a36e52d5aa64abab68e27#rd)  | 34.Go库函数和Protobuf函数在JSON序列化Message类型结构体上的不同<br />35.Go HTTP全局异常处理器                              | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_12) |
| [第十三篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247486035&idx=1&sn=fc5570fb9cd3726cbca24330135c3f90&chksm=97a3c7bea0d44ea86884de45f9b08a0d3702d6a3b8f47db80200cdd000b623771233e1a7dda1#rd)  | 36.Go HTTP文件上传下载<br />37.Go程序弹出浏览器                                                              | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_13) |
| [第十四篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247486075&idx=1&sn=47ca00c91c513dfcbfeceb6712c87d6a&chksm=97a3c796a0d44e80c1961cd90572e3c4a8b34db33b3022c873fcee3e73ddc4cdd8682e4b4f0f#rd)  | 38.init()函数的执行机制<br />39.sync.Once同步原语<br />40.Go进行保留小数的运算                                      | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_14) |
| [第十五篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247486091&idx=1&sn=d54ef1b75d10e73a7a5d8e6c6462315b&chksm=97a3c766a0d44e708d89b2e98b6c785fddad3f333711eace422f69e97dfda0025ef4420cff8d#rd)  | 41.Go程序跟踪函数的执行时间<br />42.Go链式编程<br />43.结构体值接收者和指针接收者实现接口的区别                                    | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_15) |
| [第十六篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247486178&idx=1&sn=42542503036027f2d59a8b4d0e0ef81e&chksm=97a3c70fa0d44e19415182b85579717790ddb7880376cb106e038f8c36896371649bc80f7a11#rd)  | 44.切片的长度和容量<br />45.for循环中使用defer<br />46.Go语言TrimLeft函数                                        | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_16) |
| [第十七篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247486758&idx=1&sn=e430a3f037aa926acfad8037d28434b2&chksm=97a3c0cba0d449dd6bd626a5707f32fe2a3f6e8652ccb2b8db49539389a7208da115c6b51571#rd)  | 47.Go定时任务<br />48.Cgo简单使用                                                                       | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_17) |
| [第十八篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247487042&idx=1&sn=4811102b28eae8c8c9c88ac2e86ba97d&chksm=97a3c3afa0d44ab96b57a435a49c473afb867b83d125c4662fe8f808548b0d3cc96eaf6e46eb#rd)  | 49.使用下划线增加数字可读性<br />50.格式化方法中多次使用相同参数<br />51.数组的模糊计数                                          | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_18) |
| [第十九篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247487204&idx=1&sn=7bf189222e5ccb10b89d7da50de10714&chksm=97a3c309a0d44a1fb1212ae0aadbf2288d0bdc475cfa25c9db65e4589b5fc8b208fdf60f0e02#rd)  | 52.goto语法和label的使用                                                                              | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_19) |
| [第二十篇](https://mp.weixin.qq.com/s/X02cUHcv8MtBfMYWrmuoqw)                                                                                                                                                 | 53.使用slice和map的内置函数<br />54.避免不必要的类型转换<br />55.优雅的字符串拼接方式                                       | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_20) |
| [第二十一篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247487559&idx=1&sn=de4eab08828a71e7d0344b63759eaf21&chksm=97a3ddaaa0d454bcc2088faa1473be59d6d7ce57b9d27659b33f1b454d73cb9e3e4c795e7cad#rd) | 56.`errors.Is`方法与`==`两种方式进行`error`比较<br />57.带缓冲channel和无缓冲channel区别<br />58.defer func() 函数返回值 | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_21) |
| [第二十二篇](https://mp.weixin.qq.com/s/aGMyTg7HAstfrG5O9h_xjA)                                                                                                                                                | 59.Go有符号类型和无符号类型<br />60.Go数组和切片<br />61.Go结构体类型比较                                              | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_22) |
| [第二十三篇](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247487736&idx=1&sn=b183069cbca46cffcbdcfce7b8cc6565&chksm=97a3dd15a0d454036e9dad64c82e323c3d24d87eb0c57b75b62c862838ca57c615207c053500#rd) | 62.Go Module控制Go版本<br />63.int转string注意事项<br />64.Go项目查看mod依赖关系                                 | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_23) |
| [第二十四篇](https://mp.weixin.qq.com/s/nUefNaAmi6bEAselB9QJmg)                                                                                                                                                | 65.go interface{}类型校验<br />66.go mod tidy验签失败                                                   | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_24) |
| [第二十五篇](https://mp.weixin.qq.com/s/noB16PTbMmykmQKda43FPA)                                                                                                                                                | 67.使用atomic包实现无锁并发控制<br />68.Gin框架的中间件机制<br />69.搞懂nil切片和空切片                                    | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_25) |
| [第二十六篇](https://mp.weixin.qq.com/s/7rA1nPan70Du3vQlEGrG8g)                                                                                                                                                | 70.string转[]byte是否会发生内存拷贝<br />71.Go程序获取文件的哈希值                                                       | [code](https://github.com/ibarryyan/golang-tips-100/tree/master/code/code_26) |
| DOING                                                                                                                                                                                                     |                                                                                                 |                                                                               |

---

#### 其他Go语言相关博客

##### 基础知识

- [浅谈Go语言内存模型](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247486736&idx=1&sn=963f0ae34cbd2a10d66670e387654a81&chksm=97a3c0fda0d449eb4b850f60b444150c5d90d4111ad87b8301d89720a7a33f5ef99b915f4057#rd)

- [Go错误处理方式真的不好吗？](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247485136&idx=1&sn=e27084c6d00697ef35e20922e3aaec02&chksm=97a3cb3da0d4422b30bfef8a0f0502e60a1b6f54270d27da7602323bf18798e9ba68db8fd4c2#rd)

- [莫非这就是Go最佳协程池](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247487266&idx=1&sn=fcdf02e4962ff1398a721ef3208a75e9&chksm=97a3c2cfa0d44bd9e9be7e426ef3f029e655e656468515123739849c5137c2d79b9c0dd4838b#rd)

- [原来go build命令有这么多学问](https://mp.weixin.qq.com/s/GiT6S-TSouTLZVBkftswuQ)

- [Go程序最多能创建多少个协程？](https://mp.weixin.qq.com/s/4c_6R4AEpg-9O_yrG1eyTg)

##### 框架技术

- [WebSocket原来还能这么玩](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247486120&idx=1&sn=7ae6a6cc6e14e588d76d3f92ef75fe0c&chksm=97a3c745a0d44e53f1c5e286ef9b3b4d8e0480595f5e78b57f30ecc8dad6395573475518671f#rd)

##### 工具使用

- [Go程序出问题了？有pprof！](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247486824&idx=1&sn=b536c61525ad422592eee9d57796aef6&chksm=97a3c085a0d4499309e0d6d85ca4c562cf1a98cf114bb5330470fdc2b86d7dbccebb1d56ac3c#rd)

- [听说它可以让代码更优雅](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247487332&idx=1&sn=e6bbe038d919af24dea28b6c19a250b6&chksm=97a3c289a0d44b9fb3f7b4353e320e33e8226c13953582ffda5cf2226cdb96efc74ccce51cae#rd)

##### 设计模式

- [搞懂策略模式和模板方法模式](https://mp.weixin.qq.com/s/8P_-KFSJvNtnkNSTx3DgAQ)

- [浅谈Go语言Optional模式和Builder模式](https://mp.weixin.qq.com/s/dGqaYg1TRhII6jytsfF1Vg)

##### 项目实践

- [带你用Go实现二维码小游戏（上）](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247487822&idx=1&sn=f56e87f5a0b7b9da8d0d1c3680586217&chksm=97a3dca3a0d455b5a25666ce75be69409feeedd165fb363456e70d7a7487ab50d59de41ef53a#rd)

- [带你用Go实现二维码小游戏（中）](https://mp.weixin.qq.com/s?__biz=MzIxNDc2ODc3MA==&mid=2247487835&idx=1&sn=2dbb73c69242602f75573bbe14535fd6&chksm=97a3dcb6a0d455a0e872bb1d417d33fed433d235ad506c49eaa0a7a57c7541d57fc0e1eda58a#rd)

- [带你用Go实现二维码小游戏（下）](https://mp.weixin.qq.com/s/D5mDlqWnnoJruVZbq2e2SQ)

- [带你用Go实现二维码小游戏（优化篇）](https://mp.weixin.qq.com/s/jWe49UJckujsQntZ_il2jg)

- [带你用Go实现二维码小游戏（扩展篇）](https://mp.weixin.qq.com/s/88UJQ3s1b-_rajWbDiAFoA)

- [手撸了一个文件传输工具](https://mp.weixin.qq.com/s/TX6HnIX8L_ubYDQf48SFtA)

- [手撸了一个文件传输工具（优化篇）](https://mp.weixin.qq.com/s/UlPcdmCyAmXBuxUA6O_Ayw)

---

#### 请作者喝杯咖啡

![image-20231112190005980](img/wxds.png)

#### 其他开源项目

- https://github.com/ibarryyan/FTransferor

- https://github.com/ibarryyan/QR-code-go