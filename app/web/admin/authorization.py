from flask import render_template, redirect
from flask import request, url_for
from app.models import db

from app.web import web

from app.models.rule import Rule
from app.models.role import Section, Level, Occupation
from app.forms.admin import AddRuleForm


__author__ = 'cabbyw'

# TODO 给用户授权
# user_id => section_id + occupation_id


# @web.route('/rule/del/<int:rule_id>', methods=['GET', 'POST'])
# def rule_del(rule_id):
#     """
#     删除审批规则
#     :param rule_id:
#     :return:
#     """
#     rule = Rule.query.get(rule_id)
#     if rule:
#         # TODO 这里的删除是直接删除，是否需要改变status的方式来删除？
#         db.session.delete(rule)
#         db.session.commit()
#         # 删除成功
#         return redirect(url_for('web.rule'))
#     return render_template('admin/rule.html', rules=rule.get_all_rules())
#
#
# @web.route('/rule', methods=['GET', 'POST'])
# def rule():
#     sections = Section.get_all_sections()
#     occupations = Occupation.get_all_occupations()
#     levels = Level.get_all_levels()
#     rules = Rule.get_all_rules()
#     form = AddRuleForm(request.form)
#     if request.method == 'POST' and form.validate():
#         # 添加数据
#         v = Rule()
#         v.set_attrs(form.data)
#         db.session.add(v)
#         db.session.commit()
#         return redirect(url_for('web.rule'))
#     return render_template(
#         'admin/rule.html',
#         sections=Section.get_all_sections(),
#         occupations=Occupation.get_all_occupations(),
#         levels=Level.get_all_levels(),
#         rules=Rule.get_all_rules()
#     )



