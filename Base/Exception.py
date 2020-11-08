from datetime import datetime
import traceback
from functools import wraps

# �쳣���
def except_output(msg='�쳣'):
    # msg�����Զ��庯������ʾ��Ϣ
    def except_execute(func):
        @wraps(func)
        def execept_print(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                sign = '=' * 60 + '\n'
                print(f'{sign}>>>�쳣ʱ�䣺\t{datetime.now()}\n>>>�쳣������\t{func.__name__}\n>>>{msg}��\t{e}')
                print(f'{sign}{traceback.format_exc()}{sign}')
        return execept_print
    return except_execute



# @except_output('�쳣��Ϣ')
# def lig(a = "5",b = 0):
#     print(a+b)
# lig()