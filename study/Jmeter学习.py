# //1、prev：获取前面的sample返回的信息，常用方法：
# //
# //　　　　a）getResponseDataAsString(): 获取响应信息；
# //
# //　　　　b)  getResponseCode(): 获取响应代码；
# //
# //先发个接口请求，然后prev获取返回信息，添加Http请求：
# //String response = prev.getResponseDataAsString();
# //String code = prev.getResponseCode();
# //log.info("获得"+response);
# //log.info("获得的"+code);








# //2、props：操作jmeter属性，该变量引用了JMeter的配置信息，可以获取Jmeter的属性，它的使用方法与vars类似，但是只能put进去String类型的值，而不能是一个对象。对应于java.util.Properties。
# //props的全局性：
# //log.info("============11==============");
# //props.put("name","张三");
# //String name = props.get("name");
# //log.info(name);









# //3，使用vars：vars确实是个局部变量
# //log.info("==================22=====================");
# //vars.put("name","张三");
# //String name = vars.get("name");
# //log.info(name);









# //4，简单的for循环使用
# //for(int i=0; i<10; i++){
# //	System.out.println("123");
# //	}








# //5，自定义函数，累加整数和
# //1、String.valueOf(result)
# //
# //2、Integer.toString(result)
# //
# //3、result+""
# public static int add(int num){
# 	int sum = 0;
# 	for(int i=0; i<num; i++){
# 			sum+=i;
# 		}return sum;
# 	}
#
# log.info("===========1=================");
# int result = add(100);
# log.info(result+"");



# 6，引入外部的java文件
# source("E:\\BeanShell\\beanshell\\src\\beanshell\\Test.java");



# 7.导入jar包方式，例：import beanshell.Test;
#   可以在测试计划中引入jar包，具体方法如下所示：
# 方式一：把jar包加入到classpath
# 方式二：把jar包放到lib/ext下
# 方式三：把jar包放到自定义目录下
# https://www.cnblogs.com/uncleyong/p/11475577.html
# https://blog.csdn.net/timchen525/article/details/75675500


# 8，Jmeter参数化
# https://www.cnblogs.com/yaoteng/p/11019643.html
# 参数化：
# 1.用户参数
#
# 2.函数助手
#
# 3.CSV Data Set Config/CSV数据配置文件
#
# 4.用户自定义变量




#9. Beanshell断言
# https://www.cnblogs.com/crystal1126/p/12011669.html
# https://recomm.cnblogs.com/blogpost/6124352



# coding=UTF-8

# BeanShell脚本编写
# https://www.cnblogs.com/Zfc-Cjk/p/10842307.html，今天复制回去的文本
# from Base.BasePage import * 包，模块，类三者关系
'''
一，Jemter自动生成测试报告
    https://www.cnblogs.com/Zfc-Cjk/archive/2004/01/13/8286874.html


二，Jmeter之BeanShell命令，需要结合Jar使用
    https://www.cnblogs.com/wangyi0419/p/12183407.html


三，Jmeter应用方面
    https://www.cnblogs.com/xxyBlogs/p/5966194.html


四，BeanShell基本语法规范：
   https://blog.csdn.net/hujyhfwfh2/article/details/80862134
    设置log显示级别：选项-Log Level
            log输出4个级别：
                log.debug("");
                log.info("");
                log.warn("");
                log.error("");


    https://blog.csdn.net/zhanghs11/article/details/90702602
    Jmeter封装函数并调用，常用函数？？


    Jmeter业务场景设计
    https://www.cnblogs.com/Zfc-Cjk/p/10744212.html
    https://www.cnblogs.com/Zfc-Cjk/p/8462299.html




五，前端语法
    react   hooks    jsx    axios  redux
    UI    antd design
    工程化工具   npm   webpack

'''
