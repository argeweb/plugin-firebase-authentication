#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicModel
from argeweb import Fields
from plugins.application_user.models.application_user_model import ApplicationUserModel as BaseUserModel
from plugins.application_user.models.role_model import RoleModel as BaseUoleModel


class FirebaseAuthenticationModel(BasicModel):
    name = Fields.StringProperty(verbose_name=u'識別名稱', default=u'firebase_config')
    project_id = Fields.StringProperty(verbose_name=u'Firebase Project ID')

    initialization_snippet = Fields.TextProperty(verbose_name=u'初始化的 JS 語法片斷')

    sing_in_flow = Fields.StringProperty(default='popup', verbose_name=u'登入流程', choices=(
        'popup', 'redirect'
    ))
    sing_in_success_url = Fields.StringProperty(verbose_name=u'成功登入後的網址')
    first_login_roles = Fields.StringProperty(verbose_name=u'首次登入後的角色', default=u'user')
    terms_of_service_url = Fields.StringProperty(verbose_name=u'服務條款的網址')
    custom_css = Fields.BooleanProperty(verbose_name=u'自行訂制CSS樣式', default=False)
    use_google_auth_provider = Fields.BooleanProperty(verbose_name=u'顯示 Google 登入按鈕', default=True)
    google_scopes = Fields.StringProperty(verbose_name=u'Google 存取範圍 (scopes)', default='[\'https://www.googleapis.com/auth/plus.login\']')
    use_facebook_auth_provider = Fields.BooleanProperty(verbose_name=u'顯示 Facebook 登入按鈕', default=True)
    facebook_scopes = Fields.StringProperty(verbose_name=u'Facebook 存取範圍 (scopes)', default='[\'public_profile\', \'email\', \'user_likes\', \'user_friends\']')
    use_twitter_auth_provider = Fields.BooleanProperty(verbose_name=u'顯示 Twitter 登入按鈕', default=True)
    use_github_auth_provider = Fields.BooleanProperty(verbose_name=u'顯示 Github 登入按鈕', default=True)
    use_email_auth_provider = Fields.BooleanProperty(verbose_name=u'顯示 Mail 登入按鈕', default=True)

    signed_in_callback = Fields.StringProperty(verbose_name=u'登入後所呼叫的 function', default=u'')
    signed_out_callback = Fields.StringProperty(verbose_name=u'登出後所呼叫的 function', default=u'')

    @classmethod
    def get_record(cls, name):
        return cls.query(cls.name==name)


class ApplicationUserModel(BaseUserModel):
    firebase_uid = Fields.StringProperty()
    emailVerified = Fields.BooleanProperty(default=False)
    isAnonymous = Fields.BooleanProperty(default=True)
