import unittest
import time,os,smtplib
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

#定义发送邮件
def send_mail(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()
    #构造附件
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename="latestResult.html"'
    msg = MIMEMultipart('related')
    msg['subject'] = Header("UI自动化测试报告", 'utf-8')
    msg.attach(att)
    #加邮件头
    #加邮件头
    msg['From'] = 'liu13640842984@126.com <liu13640842984@126.com>'
    msg['To'] = 'liu13640842984@126.com'
    smtp=smtplib.SMTP()
    smtp.connect("smtp.126.com",25)
    smtp.login("liu13640842984@126.com","GRIXZIAKDNFVBRNG")
    smtp.sendmail('liu13640842984@126.com','liu13640842984@126.com',msg.as_string())
    smtp.quit()
    print("email has send out!")

#查找测试报告目录，找到最新生成的测试报告文件，并发送
def new_report(test_report):
    lists=os.listdir(test_report)
    lists.sort(key=lambda fn :os.path.getmtime(test_report+'\\'+fn))
    print(('最新的文件为：'+lists[-1]))
    file_new=os.path.join(test_report,lists[-1])
    print(file_new)
    return file_new

def send_email_attch(module_name):
    dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    test_dir = r'%s\testcase'%(dir_path)  #测试用例
    result_dir = r'%s\result'%(dir_path)  #测试报告

    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = result_dir + '//' + now + 'result.html'
    fp = open(filename, 'wb')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test%s.py'%(module_name))
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例测试执行情况：')
    runner.run(discover)
    fp.close()

    newReport = new_report(result_dir)
    send_mail(newReport)


if __name__=='__main__':
    pass
    # dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # test_dir = r'E:\InterfaceProject\testcase'
    # result_dir = r'E:\InterfaceProject\result'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    # now = time.strftime("%Y-%m-%d %H-%M-%S")
    # filename = result_dir + '//' + now + 'result.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例测试执行情况：')
    # runner.run(discover)
    # fp.close()
    # newReport = new_report(result_dir)
    # send_mail(newReport)