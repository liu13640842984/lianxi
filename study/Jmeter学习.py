# //1��prev����ȡǰ���sample���ص���Ϣ�����÷�����
# //
# //��������a��getResponseDataAsString(): ��ȡ��Ӧ��Ϣ��
# //
# //��������b)  getResponseCode(): ��ȡ��Ӧ���룻
# //
# //�ȷ����ӿ�����Ȼ��prev��ȡ������Ϣ�����Http����
# //String response = prev.getResponseDataAsString();
# //String code = prev.getResponseCode();
# //log.info("���"+response);
# //log.info("��õ�"+code);








# //2��props������jmeter���ԣ��ñ���������JMeter��������Ϣ�����Ի�ȡJmeter�����ԣ�����ʹ�÷�����vars���ƣ�����ֻ��put��ȥString���͵�ֵ����������һ�����󡣶�Ӧ��java.util.Properties��
# //props��ȫ���ԣ�
# //log.info("============11==============");
# //props.put("name","����");
# //String name = props.get("name");
# //log.info(name);









# //3��ʹ��vars��varsȷʵ�Ǹ��ֲ�����
# //log.info("==================22=====================");
# //vars.put("name","����");
# //String name = vars.get("name");
# //log.info(name);









# //4���򵥵�forѭ��ʹ��
# //for(int i=0; i<10; i++){
# //	System.out.println("123");
# //	}








# //5���Զ��庯�����ۼ�������
# //1��String.valueOf(result)
# //
# //2��Integer.toString(result)
# //
# //3��result+""
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



# 6�������ⲿ��java�ļ�
# source("E:\\BeanShell\\beanshell\\src\\beanshell\\Test.java");



# 7.����jar����ʽ������import beanshell.Test;
#   �����ڲ��Լƻ�������jar�������巽��������ʾ��
# ��ʽһ����jar�����뵽classpath
# ��ʽ������jar���ŵ�lib/ext��
# ��ʽ������jar���ŵ��Զ���Ŀ¼��
# https://www.cnblogs.com/uncleyong/p/11475577.html
# https://blog.csdn.net/timchen525/article/details/75675500


# 8��Jmeter������
# https://www.cnblogs.com/yaoteng/p/11019643.html
# ��������
# 1.�û�����
#
# 2.��������
#
# 3.CSV Data Set Config/CSV���������ļ�
#
# 4.�û��Զ������




#9. Beanshell����
# https://www.cnblogs.com/crystal1126/p/12011669.html
# https://recomm.cnblogs.com/blogpost/6124352



# coding=UTF-8

# BeanShell�ű���д
# https://www.cnblogs.com/Zfc-Cjk/p/10842307.html�����츴�ƻ�ȥ���ı�
# from Base.BasePage import * ����ģ�飬�����߹�ϵ
'''
һ��Jemter�Զ����ɲ��Ա���
    https://www.cnblogs.com/Zfc-Cjk/archive/2004/01/13/8286874.html


����Jmeter֮BeanShell�����Ҫ���Jarʹ��
    https://www.cnblogs.com/wangyi0419/p/12183407.html


����JmeterӦ�÷���
    https://www.cnblogs.com/xxyBlogs/p/5966194.html


�ģ�BeanShell�����﷨�淶��
   https://blog.csdn.net/hujyhfwfh2/article/details/80862134
    ����log��ʾ����ѡ��-Log Level
            log���4������
                log.debug("");
                log.info("");
                log.warn("");
                log.error("");


    https://blog.csdn.net/zhanghs11/article/details/90702602
    Jmeter��װ���������ã����ú�������


    Jmeterҵ�񳡾����
    https://www.cnblogs.com/Zfc-Cjk/p/10744212.html
    https://www.cnblogs.com/Zfc-Cjk/p/8462299.html




�壬ǰ���﷨
    react   hooks    jsx    axios  redux
    UI    antd design
    ���̻�����   npm   webpack

'''
