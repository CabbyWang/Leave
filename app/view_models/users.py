from datetime import datetime


class UserInfo:

    def __init__(self, user):
        self.user_id = user.id
        self.username = user.username
        self.name = user.name
        self.phone_number = user.phone_number or ""
        self.id_card_number = user.id_card_number or ""
        self.section_id = user.section.id if user.section else ""
        self.section = user.section.name if user.section else ""
        self.position_id = user.position.id if user.position else ""
        self.position = user.position.name if user.position else ""
        self.xuebu_id = user.xuebu.id if user.xuebu else ""
        self.xuebu = user.xuebu.name if user.xuebu else ""
        self.area_id = user.area.id if user.area else ""
        self.area = user.area.name if user.area else ""
        self.occupation_id = user.occupation.id if user.occupation else ""
        self.occupation = user.occupation.name if user.occupation else ""
        self.level_id = user.level.id if user.level else ""
        self.level = user.level.name if user.level else ""
        self.is_committee_member = user.is_committee_member and 1 or 0
        self.committee_member = self.is_committee_member and '是' or '否'
        self.create_time = datetime.fromtimestamp(user.create_time)
