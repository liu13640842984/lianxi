# ����:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from Base.BaseDb import BaseDb


# ��������Ļ���:
Base = declarative_base()

# ����User����:
class HaHa(Base, BaseDb):
    # �������:
    __tablename__ = 'haha'
    # ��Ľṹ:
    id = Column(Integer, primary_key=True)





# ������¼����
# user = User()
# objs =[
#     User(id='12', name='Bob', password='AAA'),
#     User(id='13', name='Bob', password='AAA'),
#     User(id='14', name='Bob', password='AAA')
# ]
#
# user.add_all(objs)

# ������¼����
# user = User(id='15', name='Bob', password='AAA')
# user.add(user)


# #���µ�����¼
# user = User()
# user.update(User, User.id>14,{'name':'123'})