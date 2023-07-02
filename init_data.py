from leave import app

with app.app_context():
    from app.models.auth import User
    from app.models.role import *
    from app.models.leave import *
    db.drop_all()
    db.create_all()
    # 生成测试数据
    # 护士长账号 科室主任账号 协理员账号
    with db.auto_commit():
        vehicle1 = Vehicle()
        # vehicle1.id = 1
        vehicle1.name = '火车'
        db.session.add(vehicle1)
        vehicle2 = Vehicle()
        # vehicle2.id = 2
        vehicle2.name = '高铁'
        db.session.add(vehicle2)
        vehicle3 = Vehicle()
        # vehicle3.id = 3
        vehicle3.name = '自驾'
        db.session.add(vehicle3)

        occupation_pinyong = Occupation()
        # occupation_pinyong.id = 1
        occupation_pinyong.name = '聘用人员'
        db.session.add(occupation_pinyong)
        occupation_js = Occupation()
        # occupation_js.id = 2
        occupation_js.name = '军士'
        db.session.add(occupation_js)
        occupation_jg = Occupation()
        # occupation_jg.id = 3
        occupation_jg.name = '军官'
        db.session.add(occupation_jg)
        occupation_ywb = Occupation()
        # occupation_ywb.id = 4
        occupation_ywb.name = '义务兵'
        db.session.add(occupation_ywb)
        occupation_wz = Occupation()
        # occupation_wz.id = 5
        occupation_wz.name = '文职'
        db.session.add(occupation_wz)
        occupation_gq = Occupation()
        # occupation_gq.id = 6
        occupation_gq.name = '公勤人员'
        db.session.add(occupation_gq)

        area1 = Area()
        # area1.id = 1
        area1.name = '一片区'
        db.session.add(area1)
        area2 = Area()
        # area2.id = 2
        area2.name = '二片区'
        db.session.add(area2)
        area3 = Area()
        # area3.id = 3
        area3.name = '三片区'
        db.session.add(area3)

        xuebu_gk = XueBu()
        # xuebu_gk.id = 1
        xuebu_gk.name = '骨科医学部'
        db.session.add(xuebu_gk)
        xuebu_ss = XueBu()
        # xuebu_ss.id = 2
        xuebu_ss.name = '烧伤医学部'
        xuebu_ss.name = '烧伤医学部'
        db.session.add(xuebu_ss)

        section_xhk = Section()
        # section_xhk.id = 1
        section_xhk.name = '消化科'
        section_xhk.area = area1
        db.session.add(section_xhk)
        section_wqb = Section()
        # section_wqb.id = 2
        section_wqb.name = '卫勤部'
        section_wqb.is_office = 1
        db.session.add(section_wqb)
        section_kyb = Section()
        # section_kyb.id = 3
        section_kyb.name = '科研办'
        section_kyb.is_office = 1
        section_kyb.parent_section = section_wqb
        db.session.add(section_kyb)
        section_hlb = Section()
        # section_hlb.id = 4
        section_hlb.name = '护理部'
        section_hlb.is_office = 1
        db.session.add(section_hlb)
        section_zz = Section()
        # section_zz.id = 5
        section_zz.name = '政治工作部'
        section_zz.is_office = 1
        db.session.add(section_zz)
        section_xxk = Section()
        # section_xxk.id = 6
        section_xxk.name = '信息科'
        section_xxk.area = area1
        db.session.add(section_xxk)
        section_bzb = Section()
        # section_bzb.id = 7
        section_bzb.name = '保障部'
        section_bzb.is_office = 1
        db.session.add(section_bzb)
        section_qw = Section()
        # section_qw.id = 8
        section_qw.name = '勤务保障分队'
        db.session.add(section_qw)
        section_gj = Section()
        # section_gj.id = 9
        section_gj.name = '关节外科'
        section_gj.area = area1
        section_gj.xuebu = xuebu_gk
        db.session.add(section_gj)
        section_ss = Section()
        # section_ss.id = 10
        section_ss.name = '烧一'
        section_ss.area = area2
        section_ss.xuebu = xuebu_ss
        db.session.add(section_ss)


        position_hs = Position()
        # position_hs.id = 1
        position_hs.name = '护士'
        db.session.add(position_hs)
        position_hsz = Position()
        # position_hsz.id = 2
        position_hsz.name = '护士长'
        db.session.add(position_hsz)
        position_fdz = Position()
        # position_fdz.id = 3
        position_fdz.name = '分队长'
        db.session.add(position_fdz)
        position_yxbzr = Position()
        # position_yxbzr.id = 4
        position_yxbzr.name = '医学部主任'
        db.session.add(position_yxbzr)
        position_yxbfzf = Position()
        # position_yxbfzf.id = 5
        position_yxbfzf.name = '医学部副主任'
        db.session.add(position_yxbfzf)
        position_zr = Position()
        # position_zr.id = 6
        position_zr.name = '主任'
        db.session.add(position_zr)
        position_fzr = Position()
        # position_fzr.id = 7
        position_fzr.name = '副主任'
        db.session.add(position_fzr)
        position_bz = Position()
        # position_bz.id = 8
        position_bz.name = '部长'
        db.session.add(position_bz)
        position_fbz = Position()
        # position_fbz.id = 9
        position_fbz.name = '副部长'
        db.session.add(position_fbz)
        position_zxzr = Position()
        # position_zxzr.id = 10
        position_zxzr.name = '中心主任'
        db.session.add(position_zxzr)
        position_zw = Position()
        # position_zw.id = 11
        position_zw.name = '政委'
        db.session.add(position_zw)
        position_xly = Position()
        # position_xly.id = 12
        position_xly.name = '协理员'
        db.session.add(position_xly)
        position_qt = Position()
        # position_qt.id = 13
        position_qt.name = '其他工作人员'
        db.session.add(position_qt)

        level_zw = Level()
        # level_zw.id = 1
        level_zw.name = '政委'
        db.session.add(level_zw)
        level_zxzr = Level()
        # level_zxzr.id = 2
        level_zxzr.name = '中心主任'
        db.session.add(level_zxzr)
        level_yxbzr = Level()
        # level_yxbzr.id = 3
        level_yxbzr.name = '医学部主任'
        db.session.add(level_yxbzr)
        level_yxbfzr = Level()
        # level_yxbfzr.id = 4
        level_yxbfzr.name = '医学部副主任'
        db.session.add(level_yxbfzr)
        level_zr = Level()
        # level_zr.id = 5
        level_zr.name = '主任'
        db.session.add(level_zr)
        level_fzr = Level()
        # level_fzr.id = 6
        level_fzr.name = '副主任'
        db.session.add(level_fzr)
        level_bz = Level()
        # level_bz.id = 7
        level_bz.name = '部长'
        db.session.add(level_bz)
        level_fbz = Level()
        # level_fbz.id = 8
        level_fbz.name = '副部长'
        db.session.add(level_fbz)
        level_fdz = Level()
        # level_fdz.id = 9
        level_fdz.name = '分队长'
        db.session.add(level_fdz)
        level_xly = Level()
        # level_xly.id = 10
        level_xly.name = '协理员'
        db.session.add(level_xly)
        level_yxbxly = Level()
        # level_yxbxly.id = 11
        level_yxbxly.name = '医学部协理员'
        db.session.add(level_yxbxly)
        level_lly = Level()
        # level_lly.id = 12
        level_lly.name = '协理员(联络员)'
        db.session.add(level_lly)
        level_hsz = Level()
        # level_hsz.id = 13
        level_hsz.name = '护士长'
        db.session.add(level_hsz)

        user_admin = User()
        user_admin.name = '管理员'
        user_admin.username = 'admin'
        user_admin.password = 'admin'
        user_admin.status = 1
        user_admin.occupation = occupation_jg
        user_admin.section = section_xxk
        user_admin.position = position_qt
        db.session.add(user_admin)

        user1 = User()
        user1.name = '护士长'
        user1.username = 'hsz'
        user1.password = 'hsz'
        user1.status = 1
        user1.occupation = occupation_wz
        user1.section = section_xhk
        user1.position = position_hsz
        user1.level = level_hsz
        db.session.add(user1)
        user2 = User()
        user2.name = '消化科主任'
        user2.username = 'xhkzr'
        user2.password = 'xhkzr'
        user2.status = 1
        user2.occupation = occupation_jg
        user2.section = section_xhk
        user2.position = position_zr
        user2.level = level_zr
        db.session.add(user2)
        user3 = User()
        user3.name = '一片区联络员'
        user3.username = 'lly'
        user3.password = 'lly'
        user3.status = 1
        user3.occupation = occupation_wz
        user3.area = area1
        user3.section = section_xhk
        user3.position = position_qt
        user3.level = level_lly
        db.session.add(user3)
        user4 = User()
        user4.name = '护理部主任'
        user4.username = 'hlbzr'
        user4.password = 'hlbzr'
        user4.status = 1
        user4.occupation = occupation_jg
        user4.section = section_hlb
        user4.position = position_bz
        user4.level = level_bz
        db.session.add(user4)
        user5 = User()
        user5.name = '政治工作部主任'
        user5.username = 'zzgzbzr'
        user5.password = 'zzgzbzr'
        user5.status = 1
        user5.occupation = occupation_jg
        user5.section = section_zz
        user5.position = position_bz
        user5.level = level_bz
        db.session.add(user5)
        user6 = User()
        user6.name = '保障部副部长'
        user6.username = 'bzbfbz'
        user6.password = 'bzbfbz'
        user6.status = 1
        user6.occupation = occupation_jg
        user6.section = section_bzb
        user6.position = position_bz
        user6.level = level_bz
        db.session.add(user6)
        user7 = User()
        user7.name = '保障部部长'
        user7.username = 'bzbbz'
        user7.password = 'bzbbz'
        user7.status = 1
        user7.occupation = occupation_jg
        user7.is_committee_member = 1
        user7.section = section_bzb
        user7.position = position_bz
        user7.level = level_bz
        db.session.add(user7)
        user8 = User()
        user8.name = '勤务保障分队分队长'
        user8.username = 'fdz'
        user8.password = 'fdz'
        user8.status = 1
        user8.occupation = occupation_js
        user8.section = section_qw
        user8.position = position_fdz
        user8.level = level_fdz
        db.session.add(user8)
        user9 = User()
        user9.name = '勤务保障分队义务兵'
        user9.username = 'ywb'
        user9.password = 'ywb'
        user9.status = 1
        user9.occupation = occupation_js
        user9.section = section_qw
        user9.position = position_qt
        db.session.add(user9)
        user10 = User()
        user10.name = '中心主任'
        user10.username = 'zxzr'
        user10.password = 'zxzr'
        user10.status = 1
        user10.occupation = occupation_jg
        user10.level = level_zxzr
        # user10.section = section_
        user10.position = position_qt
        db.session.add(user10)
        user11 = User()
        user11.name = '政委'
        user11.username = 'zw'
        user11.password = 'zw'
        user11.status = 1
        user11.occupation = occupation_jg
        # user11.section = section_zw
        user11.level = level_zw
        user11.position = position_qt
        db.session.add(user11)
        user12 = User()
        user12.name = '骨科医学部主任'
        user12.username = 'yxbzr'
        user12.password = 'yxbzr'
        user12.status = 1
        user12.occupation = occupation_jg
        user12.section = section_gj
        user12.xuebu = xuebu_gk
        user12.position = position_yxbzr
        user12.level = level_yxbzr
        db.session.add(user12)
        user13 = User()
        user13.name = '骨科医学部副主任'
        user13.username = 'yxbfzr'
        user13.password = 'yxbfzr'
        user13.status = 1
        user13.occupation = occupation_jg
        user13.section = section_gj
        user13.xuebu = xuebu_gk
        user13.position = position_yxbfzf
        user13.level = level_yxbfzr
        db.session.add(user13)
        user13 = User()
        user13.name = '关节外科主任'
        user13.username = 'yzkzr'
        user13.password = 'yzkzr'
        user13.status = 1
        user13.occupation = occupation_jg
        user13.section = section_gj
        user13.xuebu = xuebu_gk
        user13.position = position_zr
        user13.level = level_yxbfzr
        db.session.add(user13)
        user13 = User()
        user13.name = '关节外科副主任'
        user13.username = 'yzkfzr'
        user13.password = 'yzkfzr'
        user13.status = 1
        user13.occupation = occupation_jg
        user13.section = section_gj
        user13.xuebu = xuebu_gk
        user13.position = position_zr
        user13.level = level_zr
        db.session.add(user13)
        user14 = User()
        user14.name = '消化科副主任'
        user14.username = 'xhkfzr'
        user14.password = 'xhkfzr'
        user14.status = 1
        user14.occupation = occupation_jg
        user14.section = section_xhk
        user14.position = position_fzr
        user14.level = level_fzr
        db.session.add(user14)
        user15 = User()
        user15.name = '卫勤部部长'
        user15.username = 'wqbbz'
        user15.password = 'wqbbz'
        user15.status = 1
        user15.occupation = occupation_jg
        user15.section = section_wqb
        user15.position = position_bz
        user15.level = level_bz
        user15.is_committee_member = 1
        db.session.add(user15)
        user16 = User()
        user16.name = '协理员'
        user16.username = 'xly'
        user16.password = 'xly'
        user16.status = 1
        user16.occupation = occupation_jg
        user16.section = section_zz
        user16.position = position_xly
        user16.level = level_xly
        db.session.add(user16)
        user17 = User()
        user17.name = '医学部协理员'
        user17.username = 'yxbxly'
        user17.password = 'yxbxly'
        user17.status = 1
        user17.occupation = occupation_wz
        user17.section = section_zz
        user17.position = position_xly
        user17.level = level_yxbxly
        db.session.add(user17)
        user18 = User()
        user18.name = '消化科护士'
        user18.username = 'hs'
        user18.password = 'hs'
        user18.status = 1
        user18.occupation = occupation_wz
        user18.section = section_xhk
        user18.area = area1
        user18.position = position_hs
        # user18.level = level_q
        db.session.add(user18)
        user19 = User()
        user19.name = '王思勇'
        user19.username = 'wsy'
        user19.password = 'wsy'
        user19.status = 1
        user19.occupation = occupation_pinyong
        user19.section = section_xxk
        user19.area = area1
        user19.position = position_qt
        # user18.level = level_q
        db.session.add(user19)
        user20 = User()
        user20.name = '彭坤'
        user20.username = 'pk'
        user20.password = 'pk'
        user20.status = 1
        user20.occupation = occupation_jg
        user20.section = section_xxk
        user20.area = area1
        user20.position = position_zr
        user20.level = level_zr
        db.session.add(user20)
        user21 = User()
        user21.name = '杨文轩'
        user21.username = 'ywx'
        user21.password = 'ywx'
        user21.status = 1
        user21.occupation = occupation_pinyong
        user21.section = section_kyb
        # user21.area = area1
        user21.position = position_qt
        # user21.level = level_zr
        db.session.add(user21)
        user22 = User()
        user22.name = '科研办主任'
        user22.username = 'kybzr'
        user22.password = 'kybzr'
        user22.status = 1
        user22.occupation = occupation_jg
        user22.section = section_kyb
        # user22.area = area1
        user22.position = position_zr
        user22.level = level_zr
        db.session.add(user22)
        user23 = User()
        user23.name = '卫勤部副部长'
        user23.username = 'wqbfbz'
        user23.password = 'wqbfbz'
        user23.status = 1
        user23.occupation = occupation_jg
        user23.section = section_wqb
        # user23.area = area1
        user23.position = position_fbz
        user23.level = level_fbz
        db.session.add(user23)

