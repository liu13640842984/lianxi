# 导入:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from Base.BaseDb import BaseDb


# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base, BaseDb):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    password = Column(String(100))





# 多条记录插入
# user = User()
# objs =[
#     User(id='12', name='Bob', password='AAA'),
#     User(id='13', name='Bob', password='AAA'),
#     User(id='14', name='Bob', password='AAA')
# ]
#
# user.add_all(objs)

# 单条记录插入
# user = User(id='15', name='Bob', password='AAA')
# user.add(user)


# #更新单条记录
# user = User()
# user.update(User, User.id>14,{'name':'123'})