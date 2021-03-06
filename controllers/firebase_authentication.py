#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

import json
import os
from argeweb import Controller, scaffold, route_menu, route
from ..models.firebase_authentication_model import ApplicationUserModel


class FirebaseAuthentication(Controller):
    class Scaffold:
        display_in_list = ['name', 'title', 'is_enable', 'category']

    @route
    @route_menu(list_name=u'system', group=u'帳號管理', text=u'Firebase 驗証設定', sort=9903)
    def admin_config(self):
        record = self.meta.Model.get_by_name('firebase_config')
        if record is None:
            record = self.meta.Model()
            record.put()
        return scaffold.edit(self, record.key)

    @route
    def sign_in(self):
        self.meta.change_view('json')
        self.context['data'] = {'msg': 'unauthorized'}
        try:
            user_object = json.loads(str(self.request.body), encoding='utf-8')
            record = self.meta.Model.get_by_name('firebase_config')
            if record is None:
                raise
            if os.environ.get('SERVER_SOFTWARE', '').startswith('Dev') is False:
                from ..firebase_helper import verify_auth_token
                claims = verify_auth_token(self.request, record.project_id)
                if not claims:
                    raise Exception('not claims')
        except:
            self.session['application_user_key'] = None
            return
        user = ApplicationUserModel.find_by_properties(firebase_uid=user_object['uid']).get()
        self.context['data'] = {'msg': 'user fined'}

        if user is None:
            from plugins.application_user.models.user_role_model import UserRoleModel
            user = ApplicationUserModel()
            user.name = user_object['displayName']
            user.firebase_uid = user_object['uid']
            user.account = user_object['email']
            user.password = user_object['apiKey'] + user_object['uid']
            user.put()
            user.bycrypt_password()
            roles = record.first_login_roles.split(',')
            if len(roles) == 0:
                roles = ['user']
            for item in roles:
                UserRoleModel.set_role(user, item.strip())
            self.context['data'] = {'msg': 'user create'}
        user.name = user_object['displayName']
        user.avatar = user_object['photoURL']
        user.email = user_object['email']
        user.emailVerified = user_object['emailVerified'] == u'true'
        user.isAnonymous = user_object['isAnonymous'] == u'true'
        user.put()
        self.session['application_user_key'] = user.key
