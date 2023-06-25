from flask_login import login_required, current_user

from . import web
from flask import render_template, redirect, url_for
from app.models.leave import Apply
from ..view_models.apply import UserApplyInfo


@web.route('/')
@login_required
def hello():
    return render_template('new_base.html')


@web.route('/index')
@login_required
def index():
    if current_user.is_admin():
        # 管理员用户首页为?
        return render_template('new_base.html')
    elif current_user.is_approver():
        # TODO 审批用户首页为审批页
        return render_template('new_base.html')
    else:
        # 普通用户首页为请假详情页
        return render_template('new_apply_list.html')
        # current_user_applies = [UserApplyDetail(apply) for apply in current_user.applies]
        # return render_template('apply_list.html', applies=current_user_applies)
