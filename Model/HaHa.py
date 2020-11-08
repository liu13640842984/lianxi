# 导入:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from Base.BaseDb import BaseDb


# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class HaHa(Base, BaseDb):
    # 表的名字:
    __tablename__ = 'haha'
    # 表的结构:
    id = Column(Integer, primary_key=True)





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