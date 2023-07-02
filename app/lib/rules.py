from app.models.role import Level, Section


class Rule:

    def __init__(self, applicant):
        self.applicant = applicant
        self._promise = {
            # 角色： 规则函数
            'QiTaChangWei': self.__qitachangwei_rule,
            'QinWuBaoZhangFenDuiFenDuiZhang': self._qinwubaozhangfendu_fenduizhang_rule,
            'QinWuBaoZhangFenDui': self._qinwubaozhangfendu_rule,
            'JiGuan': self._jiguan_rule,
            'YiXueBuZhuRen': self._yixuebuzhuren_rule,
            'YiXueBuFuZhuRen': self._yixuebufuzhuren_rule,
            'YiXueBuYaZhuanKeZhuRen': self._yixuebuyazhuankezhuren_rule,
            'KeShiZhuRen': self._keshizhuren_rule,
            'KeShiFuZhuRen': self._keshifuzhuren_rule,
            'HuShiZhang': self._hushizhang_rule,
            'HuShi': self._hushi_rule,
            'Other': self._other_rule
        }

    def __call__(self):
        """
        根据不同角色找到不同的审批规则
        :return:
        """
        is_committee_member = self.applicant.is_committee_member
        section_name = self.applicant.section.name
        position_name = self.applicant.position.name
        is_office = self.applicant.section.is_office
        xuebu = self.applicant.section.xuebu
        xuebu_name = xuebu and xuebu.name or None
        role_name = ''
        if is_committee_member:
            # 中心其他常委
            role_name = 'QiTaChangWei'
        elif section_name == '勤务保障分队' and position_name == '分队长':
            # 勤务保障分队分队长
            role_name = 'QinWuBaoZhangFenDuiFenDuiZhang'
        elif section_name == '勤务保障分队' and position_name != '分队长':
            # 勤务保障分队聘用、文职、军人等
            role_name = 'QinWuBaoZhangFenDui'
        elif is_office:
            # 机关各部副职领导、军官、文职人员、职工、聘用人员
            role_name = 'JiGuan'
        elif xuebu_name and position_name == '医学部主任':
            # 医学部主任
            role_name = 'YiXueBuZhuRen'
        elif xuebu_name and position_name == '医学部副主任':
            # 医学部副主任
            role_name = 'YiXueBuFuZhuRen'
        elif xuebu_name and position_name == '主任':
            # 医学部亚专科主任
            role_name = 'YiXueBuYaZhuanKeZhuRen'
        elif position_name == '主任':
            # 科室主任
            role_name = 'KeShiZhuRen'
        elif position_name == '副主任':
            # 科室副主任
            role_name = 'KeShiFuZhuRen'
        elif position_name == '护士长':
            # 护士长
            role_name = 'HuShiZhang'
        elif position_name == '护士':
            # 护士
            role_name = 'HuShi'
        else:
            # 其他军官、文职、聘用人员、工勤人员
            role_name = 'Other'
        return self._promise.get(role_name)()

    def _other_rule(self):
        """
        其他: 科室主任->协理员(联络员)->护理部主任->政治工作部主任
        :return:
        """
        xly_lly_level = Level.query.filter_by(name='协理员(联络员)').first()
        self_section = self.applicant.section
        area = self_section.area
        zr_level = Level.query.filter_by(name='主任').first()
        return [
            {'section': self_section, 'level': zr_level},
            {'area': area, 'level': xly_lly_level}
        ]

    def _hushi_rule(self):
        """
        科室护士: 科室护士长->科室主任->协理员(联络员)
        :return:
        """
        xly_lly_level = Level.query.filter_by(name='协理员(联络员)').first()
        self_section = self.applicant.section
        area = self_section.area
        hsz_level = Level.query.filter_by(name='护士长').first()
        zr_level = Level.query.filter_by(name='主任').first()
        return [
            {'section': self_section, 'level': hsz_level},
            {'section': self_section, 'level': zr_level},
            {'area': area, 'level': xly_lly_level}
        ]

    def _hushizhang_rule(self):
        """
        科室护士长: 科室主任->协理员(联络员)->护理部主任->政治工作部主任
        :return:
        """
        xly_lly_level = Level.query.filter_by(name='协理员(联络员)').first()
        self_section = self.applicant.section
        area = self_section.area
        hlb_section = Section.query.filter_by(name='护理部').first()
        zzgzb_section = Section.query.filter_by(name='政治工作部').first()
        zr_level = Level.query.filter_by(name='主任').first()
        bz_level = Level.query.filter_by(name='部长').first()
        return [
            {'section': self_section, 'level': zr_level},
            {'area': area, 'level': xly_lly_level},
            {'section': hlb_section, 'level': bz_level},
            {'section': zzgzb_section, 'level': bz_level}
        ]

    def _keshifuzhuren_rule(self):
        """
        科室副主任(亚专科副主任): 科室主任(亚专科主任)->协理员(联络员)->卫勤部部长->政治工作部主任
        :return:
        """
        xly_lly_level = Level.query.filter_by(name='协理员(联络员)').first()
        self_section = self.applicant.section
        area = self_section.area
        wqb_section = Section.query.filter_by(name='卫勤部').first()
        zr_level = Level.query.filter_by(name='主任').first()
        bz_level = Level.query.filter_by(name='部长').first()
        zzgzb_section = Section.query.filter_by(name='政治工作部').first()
        return [
            {'section': self_section, 'level': zr_level},
            {'area': area, 'level': xly_lly_level},
            {'section': wqb_section, 'level': bz_level},
            {'section': zzgzb_section, 'level': bz_level}
        ]

    def _keshizhuren_rule(self):
        """
        科室主任: 协理员(联络员)->卫勤部部长->政治工作部主任
        :return:
        """
        xly_lly_level = Level.query.filter_by(name='协理员(联络员)').first()
        area = self.applicant.section.area
        wqb_section = Section.query.filter_by(name='卫勤部').first()
        bz_level = Level.query.filter_by(name='部长').first()
        zzgzb_section = Section.query.filter_by(name='政治工作部').first()
        return [
            {'area': area, 'level': xly_lly_level},
            {'section': wqb_section, 'level': bz_level},
            {'section': zzgzb_section, 'level': bz_level}
        ]

    def _yixuebuyazhuankezhuren_rule(self):
        """
        医学部亚专科主任: 医学部主任->协理员(联络员)->卫勤部部长->政治工作部主任
        :return:
        """
        xuebu = self.applicant.xuebu
        yxb_zr_level = Level.query.filter_by(name='医学部主任').first()
        xly_lly_level = Level.query.filter_by(name='协理员(联络员)').first()
        area = self.applicant.section.area
        wqb_section = Section.query.filter_by(name='卫勤部').first()
        bz_level = Level.query.filter_by(name='部长').first()
        zzgzb_section = Section.query.filter_by(name='政治工作部').first()
        return [
            {'xuebu': xuebu, 'level': yxb_zr_level},
            {'area': area, 'level': xly_lly_level},
            {'section': wqb_section, 'level': bz_level},
            {'section': zzgzb_section, 'level': bz_level}
        ]

    def _yixuebufuzhuren_rule(self):
        """
        医学部副主任: 医学部主任->医学部协理员->卫勤部部长->政治工作部主任
        :return:
        """
        xuebu = self.applicant.section.xuebu
        # self_section = self.applicant.section
        yxb_zr_level = Level.query.filter_by(name='医学部主任').first()
        yxb_xly_level = Level.query.filter_by(name='医学部协理员').first()
        wqb_section = Section.query.filter_by(name='卫勤部').first()
        bz_level = Level.query.filter_by(name='部长').first()
        zzgzb_section = Section.query.filter_by(name='政治工作部').first()
        return [
            {'xuebu': xuebu, 'level': yxb_zr_level},
            # {'section': self_section, 'level': yxb_zr_level},
            {'level': yxb_xly_level},
            {'section': wqb_section, 'level': bz_level},
            {'section': zzgzb_section, 'level': bz_level}
        ]

    def _yixuebuzhuren_rule(self):
        """
        医学部主任: 协理员->卫勤部部长->政治工作部主任->中心主官(中心主任、政委)
        :return:
        """
        xly_level = Level.query.filter_by(name='协理员').first()
        wqb_section = Section.query.filter_by(name='卫勤部').first()
        bz_level = Level.query.filter_by(name='部长').first()
        zzgzb_section = Section.query.filter_by(name='政治工作部').first()
        zxzr_level, zw_level = Level.query.filter_by().filter(Level.name.in_(('中心主任', '政委'))).all()
        return [
            {'level': xly_level},
            {'section': wqb_section, 'level': bz_level},
            {'section': zzgzb_section, 'level': bz_level},
            {'level': zxzr_level},
            {'level': zw_level}
        ]

    def _jiguan_rule(self):
        """
        机关: 机关各办公室主任->机关各部副职领导->机关各部主官
        :return:
        """
        self_section = self.applicant.section
        zr_level = Level.query.filter_by(name='主任').first()
        fbz_level = Level.query.filter_by(name='副部长').first()
        bz_level = Level.query.filter_by(name='部长').first()
        bangongshi_section = self_section
        bumen_section = self_section.parent_section
        return [
            {'section': bangongshi_section, 'level': zr_level},
            {'section': bumen_section, 'level': fbz_level},
            {'section': bumen_section, 'level': bz_level}
        ]

    def _qinwubaozhangfendu_rule(self):
        """
        联勤保障分队: 分队长->保障部副部长->保障部部长
        :return:
        """
        fdz_level = Level.query.filter_by(name='分队长').first()
        fbz_level = Level.query.filter_by(name='副部长').first()
        bz_level = Level.query.filter_by(name='部长').first()
        lqbzfd_section = Section.query.filter_by(name='勤务保障分队').first()
        bzb_section = Section.query.filter_by(name='保障部').first()
        return [
            {'section': lqbzfd_section, 'level': fdz_level},
            {'section': bzb_section, 'level': fbz_level},
            {'section': bzb_section, 'level': bz_level}
        ]

    def _qinwubaozhangfendu_fenduizhang_rule(self):
        """
        联勤保障分队分队长: 保障部副部长->保障部部长
        :return:
        """
        fbz_level = Level.query.filter_by(name='副部长').first()
        bz_level = Level.query.filter_by(name='部长').first()
        bzb_section = Section.query.filter_by(name='保障部').first()
        return [
            {'section': bzb_section, 'level': fbz_level},
            {'section': bzb_section, 'level': bz_level}
        ]

    def __qitachangwei_rule(self):
        """
        其他常委审批规则:   中心其他常委-》中心主任、政委
        :return: [{'section': Section, 'level': Level, 'area': Area}, {'section': Section, 'level': Level, 'area': Area}]
        """
        zxzr_level, zw_level = Level.query.filter_by().filter(Level.name.in_(('中心主任', '政委'))).all()
        return [
            {'level': zxzr_level},
            {'level': zw_level}
        ]


# approve_rule = Rule()
