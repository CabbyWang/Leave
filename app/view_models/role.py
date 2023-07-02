

class SectionInfo:

    def __init__(self, section):
        self.section_id = section.id
        self.section = section.name
        self.is_office = section.is_office and "机关" or ""
        self.parent_section = section.parent_section.name if section.parent_section else ""
        self.area = section.area.name if section.area else ""
        self.xuebu = section.xuebu.name if section.xuebu else ""


class AreaInfo:

    def __init__(self, area):
        self.area_id = area.id
        self.area = area.name


class XueBuInfo:

    def __init__(self, xuebu):
        self.xuebu_id = xuebu.id
        self.xuebu = xuebu.name


class OccupationInfo:

    def __init__(self, occupation):
        self.occupation_id = occupation.id
        self.occupation = occupation.name


class PositionInfo:

    def __init__(self, position):
        self.position_id = position.id
        self.position = position.name


class LevelInfo:

    def __init__(self, level):
        self.level_id = level.id
        self.level = level.name
