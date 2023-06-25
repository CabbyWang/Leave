# from app import app
"""
Created by cabbyw on 2023/06/04
"""
from app import create_app
from app.models import db
from app.models.base import Base


__author__ = 'cabbyw'

app = create_app()


with app.app_context():
    db.create_all()

# with app.app_context():
#     from app.models.auth import User
#     from app.models.role import *
#     from app.models.leave import *
#     db.drop_all()
#     db.create_all()
#     # 生成测试数据
#     # 护士长账号 科室主任账号 协理员账号
#     with db.auto_commit():
#         vehicle = Vehicle()
#         vehicle.id = 1
#         vehicle.name = '火车'
#         db.session.add(vehicle)
#
#         occupation_pinyong = Occupation()
#         occupation_pinyong.id = 1
#         occupation_pinyong.name = '聘用'
#         db.session.add(occupation_pinyong)
#
#         section_xhk = Section()
#         section_xhk.id = 1
#         section_xhk.name = '消化科'
#         db.session.add(section_xhk)
#
#         position_hushizhang = Position()
#         position_hushizhang.id = 1
#         position_hushizhang.name = '护士长'
#         db.session.add(position_hushizhang)
#
#         position_zhuren = Position()
#         position_zhuren.id = 2
#         position_zhuren.name = '主任'
#         db.session.add(position_zhuren)
#
#         position_xly = Position()
#         position_xly.id = 3
#         position_xly.name = '协理员'
#         db.session.add(position_xly)
#
#         level_zhuren = Level()
#         level_zhuren.id = 2
#         level_zhuren.name = '主任'
#         db.session.add(level_zhuren)
#
#         level_hushizhang = Level()
#         level_hushizhang.id = 1
#         level_hushizhang.name = '护士长'
#         db.session.add(level_hushizhang)
#
#         level_xly = Level()
#         level_xly.id = 3
#         level_xly.name = '协理员'
#         db.session.add(level_xly)
#
#         user1 = User()
#         user1.name = '消化科护士长'
#         user1.username = 'hushizhang'
#         user1.password = 'hushizhang'
#         user1.status = 1
#         user1.occupation = occupation_pinyong
#         user1.section = section_xhk
#         user1.position = position_hushizhang
#         user1.level = level_hushizhang
#         db.session.add(user1)
#
#         user2 = User()
#         user2.name = '消化科主任'
#         user2.username = 'zhuren'
#         user2.password = 'zhuren'
#         user2.status = 1
#         user2.occupation = occupation_pinyong
#         user2.section = section_xhk
#         user2.position = position_zhuren
#         user2.level = level_zhuren
#         db.session.add(user2)
#
#         user3 = User()
#         user3.name = '协理员'
#         user3.username = 'xieliyuan'
#         user3.password = 'xieliyuan'
#         user3.status = 1
#         user3.occupation = occupation_pinyong
#         user3.section = section_xhk
#         user3.position = position_xly
#         user3.level = level_xly
#         db.session.add(user3)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5000)
