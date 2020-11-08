# 导入:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from Base.BaseDb import BaseDb


# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class PayOrder(Base, BaseDb):
    # 表的名字:
    __tablename__ = 'pay_order'
    # 表的结构:
    id = Column(Integer, primary_key=True)
    pay_sn = Column(String(100))
    order_sn = Column(String(100))