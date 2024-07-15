# 基础

## 命名规范

1. 变量：变量尽量都小写，如果有多个单词用下划线隔开；
2. 类：类使用驼峰命名，首字母大写；其中私有类可以用一个下划线开头；
3. 函数：函数名一律小写，如有多个单词，用下划线隔开；
4. 常量：常量则全部大写；
5. 下划线开头的：
   - 单下划线开头的：如果类变量以单下划线“_”开头，代表这个变量不能被直接访问，类似于C++中的protected型，这样的变量也不能被 import
     module_name导入。 使用单下划线(one underline）开头的方法，则表示该方法不是AP的一部分,不要直接访问(虽然语法上访问也没有什么问题)。
   - 双下划线开头：以双下划线(two underlines)开头的类变量，表示为类的私有成员，不能被导入和其他类变量访问。对于类中的方法，使用双下划线开头开头表示子类不能覆写该方法。除非你真的知道你在干什么,否则不要使用这种方式。
   - 双下划线开头并结尾的：魔法方法是python内置方法，不需要主动调用，存在的目的是为了给python的解释器进行调用，几乎每个魔法方法都有一个对应的内置函数，或者运算符，当我们对这个对象使用这些函数或者运算符时就会调用类中的对应魔法方法，可以理解为重写这些python的内置函数。

## 快速上手

1. UNIX命令行执行python 程序：

​	让脚本的第一行以字符序列#!（称为pound bang或shebang）开始；并在它后面指定用于对脚本进行解释的程序（这里是Python）的绝对路径。

```unix
#!/usr/bin/env python
```

2. 要像普通程序一样运行脚本，还必须将其变成可执行的：

   ```
   $ chmod a+x hello.py
   $ hello.py
   程序后加上该句保证其不理吗退出：input("Press <enter>")、
   ```

## 字符串

1. 字符串有时候是单引号有时候是双引号，他俩作用完全一样，但是下面这种情况就要都用到了(多行可用三引号)

```
        >>> "Let's go!"
        "Let's go!"
        >>> '"Hello, world!" she said'
        '"Hello, world!" she said'
```

2. 转义符：反斜杠（\）转义

3. 字符串切片：`print(s[2:6])`，即包含下标味2，但不包含下标为6的字符串（包左不包右）；

4. 拼接字符串

   - 下面这种情况python会自动帮你拼接：

     ```python
     >>> "Let's say " '"Hello, world!"'
     'Let\'s say "Hello, world!"'
     ```

   - 一般拼接字符串用“+”

5. 函数`str()`和`repr()`：
   - `str()`:`str`能以合理的方式将值转换为用户能够看懂的字符串
   - `repr()`:使用`repr`时，通常会获得值的合法`Python`表达式表示

6. join（）和split()

   拆分和连接字符串

### eval函数

是Python中的一个内置函数，用于去掉字符串最外侧的引号，并按照Python语句方式执行去掉引号后的字符串

### startswith()函数

判断字符串以什么开头

### 闭包

1. 嵌套函数

   ```python
   def foo(): 
      #foo是外围函数 
      a = 1 
      # printer是嵌套函数 
      def printer(): 
          print(a)
       # 加上这行就是闭包
       return printer
      
   ```

2. 闭包和嵌套的区别是闭包将嵌套函数返回了

   闭包能访问定义体之外定义的非全局变量

3. 闭包的坑

   ```
   def create_multipliers():
      return [lambda x: x * i for i in range(5)]
       
   for multiplier in create_multipliers():
      print(multiplier(2))
       
   # 期望输出0, 2, 4, 6, 8
   # 结果是 8, 8, 8, 8, 8
   
   可以看到函数绑定的i值都成了4即循环后最终i的取值，这是因为Python 的闭包是延迟绑定 ，这意味着闭包中用到的变量的值，是在内部函数被调用时查询得到的。
   ```

   ```
   正确的使用方式是将i的值利用参数的方式进行传递：
   def create_multipliers():
      return [lambda x,i=i: x * i for i in range(5)]
    
   s = create_multipliers()
   for multiplier in s:
      print(multiplier(2))  # 0, 2, 4, 6, 8
   ```

   

## 模块

math模块中有各种各样的数学函数，而如果要处理复数，Python标准库提供了一个专门用于处理复数的模块。

# git

## 基本的操作流程

### 代码提交（同步）

```git
git status 查看修改的文件（红色的为修改的）
git add . 或者 git add 文件名   修改文件存入缓冲区
git commit -m "注释内容"	提交修改文件
git push origin master   本地推送到远程合并
git pull origin duanpen	 拉取远程的和本地合并

git pull --force origin 远程分支:要覆盖的本地分支

git branch -d 分支名    删除分支
git branch -D 分支名    强制删除分支

git merge 分支名        将分支合并到当前分支

git checkout -- b.txt  在没有add之前撤销对文件b.txt的修改（即丢弃工作区的修改）
git restore <file>     类似于上面的，但这个更好用

rm b.txt               删除文件
```

# wsl,docker等

## wsl

WSL的主要目的是提供一个与真正的Linux系统兼容的运行时环境，需要注意的是，WSL并非完全模拟一个完整的Linux系统；

## docker

- 什么是Docker：对进程进行封装隔离，是一个容器，类似于虚拟机，但是与虚拟机原理不同，docker平台就是一个软件集装箱化平台，是一个开源的应用容器引擎，让开发者可以打包他们的应用以及依赖包到一个可移植的镜像中，也可以实现虚拟化，并且容器之间不会有任何接口。
- Docker的镜像：打包的可运行的程序

# 网页请求（3.0平台（https://yht.zb-sx.cn:36359/））

以查询X号码为例：

```python
def getHeader():
    """获取请求头"""
    e = pp_env.getEnv()
    # 这些参数都可在浏览器F12网络中自行查看
    return {
        "Host": "yht.zb-sx.cn:36359",
        "Tenant-Id": "11304",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "X-Access-Token": e["token"],
    }
    
def get_x(params):
    e = pp_env.getEnv()
    # 发送get请求，用requests.get/post
    return requests.get(
        # 超时
        timeout=40,
        # url
        url="https://yht.zb-sx.cn:36359/call-system/zbNumx/list",
        # 需要传入的参数
        params = params,
        # 请求头
        headers= config.getHeader()
    )
def get_xNumber(number):
    '''xNUMBER'''
    params = {
        "xnumber": number,
        # "pageNo": 1,
    }
    return get_x(params)
```

# pandas

## 数据结构

### Series

Series 是 Pandas 中的一种基本数据结构，类似于一维数组或列表，但具有标签（索引）

创建 `Series`:`pd.Series(s) `，其中S是数组或者字典

==说白了，Series就是一个带有索引的一维数组==

### DataFrame

有索引的表格

```python
pandas.DataFrame( data, index, columns, dtype, copy)   # 构造方法
```

## loc 和 iloc

**loc：通过行、列的名称或标签来索引**

**iloc：通过行、列的索引位置来寻找数据**

```
data.loc[:,"country"]
data.loc[:["name","sex","age"]]

data.iloc[1,3]
data.iloc[1:4,3:4]

# 同样的，loc[]和iloc[]中参数也可以是数组
```



