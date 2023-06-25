

# class RuleInfo:
#     def __int__(self, rules):
#         self.total = 0
#         self.rules = []
#
#     def _parse(self, rules):
#         self.total = len(rules)
#         self.rules = []
#
#     def _map_model_to_dict(self, model):
#         return dict(
#             section_id=model.section.id,
#             occupation_id=model.occupation.id
#         )


class RuleInfo:

    def __init__(self, rule):
        self.rule = rule
        # self.section = rule.section.name
        # self.occupation = rule.occupation.name
        # self.level = rule.level.name

    @property
    def id(self):
        return self.rule.id

    @property
    def section(self):
        section = self.rule.section
        return section.name if section else None

    @property
    def occupation(self):
        occupation = self.rule.occupation
        return occupation.name if occupation else None

    @property
    def level(self):
        level = self.rule.level
        return level.name if level else None
