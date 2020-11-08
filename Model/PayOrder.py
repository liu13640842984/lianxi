# ����:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from Base.BaseDb import BaseDb


# ��������Ļ���:
Base = declarative_base()

# ����User����:
class PayOrder(Base, BaseDb):
    # �������:
    __tablename__ = 'pay_order'
    # ��Ľṹ:
    id = Column(Integer, primary_key=True)
    pay_sn = Column(String(100))
    order_sn = Column(String(100))