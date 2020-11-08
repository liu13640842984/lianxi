# coding=UTF-8
# python基础：


'''
一，对Self的理解
https://blog.csdn.net/qq_15158911/article/details/86413390
1. self代表类的实例，而非类
2. self总是指调用时的类的实例。 在继承时，
传入的是哪个实例，就是那个传入的实例，而不是指定义了self的类的实例。
3. Python中的self用于类的方法中，不可省略
4. self也可以换成其他自己喜欢的词
5.同一个类中调用其他的方法时需要加self
6. 一个独立的函数不需要加上self参数，当然，独立的函数加上self也不影响，但是没有必要
7. self的作用主要表示这个变量是类中的公共变量 #在类的一个方法定义了一个变量name1，这个变量就唯一的属于setname这个方法，其他方法无法使用这个变量 #使用self会告诉所有的方法，这个变量是我们共有的，可以随便用 9.self的属性，名称前加上两个下划线，就变成了一个私有变量（private），只有内部可以访问，外部不能访问




总结起来就是
1.self是指类的实例，
2.self用在类中方法时 或调用类的其他方法时，不可以省略，
3.在继承类中，如果调用了父类方法，self是指子类实例
4.self可以随便命名，无影响
5.非类中的方法，可加self也可不加self
6.Self.变量是公共方法，self.__变量是私有方法
'''

# coding=UTF-8
# https://mp.weixin.qq.com/s/XYe9ASOAOPfiTqUsYBfaiw，Python特殊写法


'''
一，raise关键字用法：
关键字raise是用来抛出异常的，
一旦抛出异常后，后续的代码将无法运行。
这实际上的将不合法的输出直接拒之门外，
避免黑客通过这种试探找出我们程序的运行机制，从而找出漏洞，获得非法权限。

a = '123'
type_list = ['str','int']
if type(a) not in type_list:
	raise TypeError
'''

'''
二，单下划线和双下划线的用法
    原网址——https://www.cnblogs.com/dogecheng/p/11461257.html
    1.访问私有属性=>a._A__name,  实例._类名__属性名

    2.双下划线 “__” 开头和结尾，它们是Python的魔法函数，
      比如__init__()和__str__等等。不用要这种方式命名自己的变量或者函数。

    3.一种约定(类名前面加上"_")，用来指定变量私有。
      程序员用来指定私有变量的一种方式。不能用from module import * 导入，
      其他方面和公有一样访问。  可以这样访问：文件名.私有类名
'''

'''
三，类方法，实力方法和静态方法
    原网址——https://www.cnblogs.com/dogecheng/p/11441088.html

      类方法——>特点：传递的是类本身，可以直接用类本身调用，或使用类实例调用
    1.当我们需要和类直接进行交互，而不需要和实例进行交互时，
      类方法是最好的选择。类方法与实例方法类似，但是传递的不是类的实例，而是类本身，
      第一个参数是cls。我们可以用类的实例调用类方法，也可以直接用类名来调用。


      静态方法——>特点：好处就是参数里面不需要self，可直接用类调用，或使用类实例调用
    2.静态方法类似普通方法，参数里面不用self。
      这些方法和类相关，但是又不需要类和实例中的任何信息、属性等等。
      如果把这些方法写到类外面，这样就把和类相关的代码分散到类外，
      使得之后对于代码的理解和维护都是巨大的障碍。而静态方法就是用来解决这一类问题的。
'''

'''
四，正则表达式
    原网址——https://www.cnblogs.com/dogecheng/p/11466687.html
    (?:pattern)、(?=pattern)、(?!pattern)、(?<=pattern)和(?<!pattern) 
'''

'''
五，特殊写法
    原网址——https://mp.weixin.qq.com/s/XYe9ASOAOPfiTqUsYBfaiw
     1.for - else

     2.输出结果A  if 条件 else 输出结果B
          例如：print(1 if 1==1 else 2) 等价于 print(1) if 1==1 else print(2)

     3.*args：元组类型参数  **args：字典类型参数
          例如：
               def do_something(name, age, gender='男', *args, **kwds)
                   do_something('xufive', 50, '男', 175, 75, math=99, english=90)

     4.with - as
               with 语句适合一些事先需要准备，事后需要处理的任务，
               比如，文件操作，需要先打开文件，操作完成后需要关闭文件。如果不使用with，文件操作通常得这样


      5.列表推导式 
                  a = [1,2,3,4]
                  result = [i*i for i in a]


      6.列表索引的各种骚操作
                 [::2]，步长为2，按顺序依次加2，显示元素
                 [::-1]，步长为1，逆序依次减1，显示元素
                 例如：a = [0,1,2,3,4,5]
                       b = ["a", "b"]
                       a[2:-1]=b，表示从第二个位置开始插入两个元素并保留最后一个元素



                       service=['a','http','firewalld','ssh','ftp']
                       service[:2]=['samba','dns']，从左边开始算起的第三个元素进行切片，然后插入新的列表元素并  代替切片后的前半部分列表元素
                       ['samba','dns','firewalld','ssh','ftp']

                       切片规则
                       [2:],从第三个元素开始切，保留左边
                       [:2],从第三个元素开始切，保留右边
                       [:-1],从倒数第一个元素开始切，保留右边
                       [-1:],从倒数第一个元素开始切，保留左边
                       针对列表元素赋值，以上规则均适用

                       a=[1,2,3,4]
                       b=[5,6]
                       a[2:2]=b，打印出a的值为——1,2,5,6,3,4
                        [2:3]——1,2,5,6,4
                        [2:4]—1,2,5,6                 
'''

'''
六，lambda函数
    https://www.cnblogs.com/tianqianlan/p/11082183.html
    a = lambda x:x*x
    print(a(3))
    注意：有多种逻辑关系表达式的时候不能使用lambda函数。


    案例1：函数内嵌套lambda表达式
    def new_func(x):
    return(lambda y:x + y)
    t = new_func(3)
    print(t(2))==>  其中，x=3,y=2


    案例2：Lambda函数 + filter函数，返回一个具体数字的列表
           data = list(filter(lambda a:a/3==2, newList))


    案例3：Lambda函数 + map函数，返回一个True 或 False的列表
           data = map(lambda a:a/3==2,myList)


    案例4：Lambda函数 + reduce函数,对列表元素进行累计操作，from functools import reduce
           data = reduce(lambda x,y:x+y,[1,2])

'''

'''
七，yaml配置文件的使用
    学习网址：https://www.cnblogs.com/shengulong/p/10371740.html
    语法规则：
            1.大小写敏感
            2.使用缩进表示层级关系
            3.缩进时不允许使用Tab键，只允许使用空格。
            4.缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
    # 表示注释，从这个字符一直到行尾，都会被解析器忽略
'''

'''
八，函数
    如果函数有默认值，内部可以忽略形参的先后顺序
    def test(a=1, b):
        os.path.join(b, a)
'''

'''
九，@property装饰器
     将类方法转换为类属性，可以用 . 直接获取属性值或者对属性进行赋值
    https://www.liaoxuefeng.com/wiki/897692888725344/923030547069856

    class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value ,int):
            raise ValueError('分数必须是整数')
        if value <0 or value>100:
            raise ValueError('分数必须0-100之间')
        self._score = value

student = Student()
student.score = 65
print(student.score)
'''

'''
十，写个元类自动装饰某个类的所有方法
    某个类(metaclass =自定义的元类) 
'''

'''
十一，https://blog.csdn.net/daidadeguaiguai/article/details/103930776
python进阶数据库之对象关系映射SQLAalchemy
pip install mysql-connector --index-url https://pypi.douban.com/simple
'''

'''
十二，断言截图
     https://www.cnblogs.com/yoyoketang/p/6719048.html
'''

'''
十三，with用法
https://www.cnblogs.com/pythonbao/p/11211347.html
'''

'''
十四，
使用unittest框架，主要是以下几个类的使用：
TestCase, TestSuite, TestLoader, TestResult, TextTestResult, TextTestRunner

'''

'''
十五，https://www.jianshu.com/p/3d2c0e092ffb，  BeautifulReport 测试报告生成
       https://blog.csdn.net/qq_37969201/article/details/86689940

       python安装beautifulsoup4

       https://www.cnblogs.com/xuzhongtao/p/11282430.html
'''

'''
十六，python的一些关键字：
      1.__slots__，限制类实例添加属性
        如果子类继承父类，则子类实例添加属性时，不受限制


      2.@property,将方法装饰成一个属性，供类实例进行调用
        至于内部逻辑如何，就需要根据业务场景进行编写

      3.多重继承类，定制类，元类，枚举类

        定制类：
        __getattr__()，当python调动不存在的属性时，解释器调用它来获得属性
                默认返回None

        __call__()，定义这个方法，可以直接对实例进行调用
                    判断一个对象是否能被调用，能被调用的对象就是一个Callable对象

        __str__()，返回用户看到的字符串

        __repr__()，返回程序开发者看到的字符串，
                   也就是说，__repr__()是为调试服务的,直接显示变量调用

       元类

       枚举类

'''

'''
十七，测试开发平台：https://www.oschina.net/search?scope=blog&q=%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91%E5%B9%B3%E5%8F%B0
'''

'''
十八，接口自动化
      https://blog.csdn.net/weixin_42262081/article/details/106751223
'''

'''
十九，通过python获得header中的session
      https://blog.csdn.net/weixin_34406796/article/details/92234793

      登陆处理cookie
      https://blog.csdn.net/panyu881024/article/details/80210772?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.add_param_isCf&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.add_param_isCf

        https://blog.csdn.net/GeekSnow/article/details/88899562
        session信息状态——保存用户的登录会话——接口会返回如token, jsession


        https://blog.csdn.net/GeekSnow/article/details/88899562
'''

'''
二十，postman使用
      https://blog.csdn.net/GeekSnow/article/details/88899562

      eval，将字符转为json格式
'''

'''
二十一，Tesseract-OCR下载和安装
https://blog.csdn.net/ever_peng/article/details/90547299
https://blog.csdn.net/qq_43317529/article/details/83340739?utm_medium=distribute.pc_relevant_download.none-task-blog-baidujs-2.nonecase&depth_1-utm_source=distribute.pc_relevant_download.none-task-blog-baidujs-2.nonecase
'''


'''
二十二，获取appPackage和appActivity的方法
          adb shell dumpsys window w |findstr \/ |findstr name=
        获取设备
        adb devices -l
'''

# file = open('F:\SeleniumProject\目录说明.txt','rb')
# ss = file.read()
# ss.encode('raw_unicode_escape')
# print(ss)

file = open('F:\SeleniumProject\目录说明.txt','rb')


ss = file.read()

print(ss)