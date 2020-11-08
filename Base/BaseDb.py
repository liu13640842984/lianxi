from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from Common.var import *

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class BaseDb:
        print(user,pwd,host,db)
        # 初始化数据库连接:
        # engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1:3306/test')
        engine = create_engine('mysql+mysqlconnector://%s:%s@%s:3306/%s'%(user, pwd, host, db))
        print(engine)

        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)

        # 创建session对象:
        session = DBSession()

        def __init__(self):
                pass


        #提交并关闭数据连接
        def dbAction(self):
              # 提交即保存到数据库:
              self.session.commit()
              # 关闭session:
              self.session.close()


        #查询所有的行记录,Object为传入的相应Model类---->（对象组合）
        def query(self, Object):
               return self.session.query(Object).all()



        #按条件筛选，查询行记录，Object为传入的相应Model类， Condition过滤的条件---->（对象组合）
        def filterQuery(self, Object, Condition):
                # 使用说明： session.query(Users).filter(Users.id > 3)  # filter按条件筛选查询结果
                return self.session.query(Object).filter(Condition)



        #增加一条记录，Object为传入的类实例化---->（带多个参数）
        def add(self, Object):
                # 说明：Object(id='15', name='Bob', password='AAA')
                '''
                :param Object:需要增加的记录
                :return:
                '''
                # 添加到session:
                self.session.add(Object)
                self.dbAction()



        #增加多条记录，Object为传入的List类型实参，可添加多个类的实例化---->（带多个参数）
        def add_all(self, Object):
                # 说明
                #Object =[
                #     User(id='12', name='Bob', password='AAA'),
                #     User(id='13', name='Bob', password='AAA'),
                #     User(id='14', name='Bob', password='AAA')
                # ]
               self.session.add_all(Object)
               self.dbAction()



        #更新单条记录
        def update(self, Object, Condition, Content):
                # 说明：user.update(User, User.id > 14, {'name': '123'})
                '''
                :param Object: 传入的model类
                :param condition: 过滤的条件
                :param content: 需要更新的内容
                :return:
                '''
                self.session.query(Object).filter(Condition).update(Content)


        #此方法待完善中，晚上继续优化，更新多条记录
        def update_all(self, Object, condition, content):
                self.session.query(Object).filter(condition).update_all(content)



        #生成查询语句,Obejct为传入的相应Model类---->（生成的SQL查询语句）
        def querySql(self, Object):
                print(self.session.query(Object))



        #127.0.0.1 ip地址插入问题待处理
'''

        -----高级查询

        # 　条件
        ret = session.query(Users).filter_by(name='alex').all()
        伟哥一问：filter_by()
        传参数
        filter()
        后面跟表达式
        ret = session.query(Users).filter(Users.id > 1, Users.name == 'eric').all()
        ret = session.query(Users).filter(Users.id.between(1, 3), Users.name == 'eric').all()
        ret = session.query(Users).filter(Users.id.in_([1, 3, 4])).all()
        ret = session.query(Users).filter(~Users.id.in_([1, 3, 4])).all()
        ret = session.query(Users).filter(Users.id.in_(session.query(Users.id).filter_by(name='eric'))).all()
        from sqlalchemy import and_, or_
        ret = session.query(Users).filter(and_(Users.id > 3, Users.name == 'eric')).all()
        ret = session.query(Users).filter(or_(Users.id < 2, Users.name == 'eric')).all()
        ret = session.query(Users).filter(
                or_(
                        Users.id < 2,
                        and_(Users.name == 'eric', Users.id > 3),
                        Users.extra != ""
                )).all()

        # 通配符
        ret = session.query(Users).filter(Users.name.like('e%')).all()
        ret = session.query(Users).filter(~Users.name.like('e%')).all()

        # 限制
        ret = session.query(Users)[1:2]

        # 排序
        ret = session.query(Users).order_by(Users.name.desc()).all()
        ret = session.query(Users).order_by(Users.name.desc(), Users.id.asc()).all()

        # 分组
        from sqlalchemy.sql import func

        ret = session.query(Users).group_by(Users.extra).all()
        ret = session.query(
                func.max(Users.id),
                func.sum(Users.id),
                func.min(Users.id)).group_by(Users.name).all()

        ret = session.query(
                func.max(Users.id),
                func.sum(Users.id),
                func.min(Users.id)).group_by(Users.name).having(func.min(Users.id) > 2).all()

        # 连表

        ret = session.query(Users, Favor).filter(Users.id == Favor.nid).all()

        ret = session.query(Person).join(Favor).all()

        ret = session.query(Person).join(Favor, isouter=True).all()

        # 组合
        q1 = session.query(Users.name).filter(Users.id > 2)
        q2 = session.query(Favor.caption).filter(Favor.nid < 2)
        ret = q1.union(q2).all()

        q1 = session.query(Users.name).filter(Users.id > 2)
        q2 = session.query(Favor.caption).filter(Favor.nid < 2)
        ret = q1.union_all(q2).all()

        relationship
        连表


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, CHAR, VARCHAR
from sqlalchemy.orm import sessionmaker, relationship
'''