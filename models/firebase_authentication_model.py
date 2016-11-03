#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicModel
from argeweb import Fields
from plugins.application_user.models.application_user_model import ApplicationUserModel as BaseUserModel
from plugins.application_user.models.application_user_role_model import ApplicationUserRoleModel as BaseUoleModel


class FirebaseAuthenticationModel(BasicModel):
    class Meta:
        label_name = {
            "name": u"識別名稱",
            "initialization_snippet": u"初始化的 JS 語法片斷",
            "sing_in_flow":u"登入流程",
            "sing_in_success_url":u"成功登入後的網址",
            "terms_of_service_url":u"服務條款的網址",
            "custom_css":u"自行訂制CSS樣式",
            "use_google_auth_provider":u"顯示 Google 登入按鈕",
            "google_scopes":u"Google 存取範圍 (scopes)",
            "use_facebook_auth_provider":u"顯示 Facebook 登入按鈕",
            "facebook_scopes":u"Facebook 存取範圍 (scopes)",
            "use_twitter_auth_provider":u"顯示 Twitter 登入按鈕",
            "use_github_auth_provider":u"顯示 Github 登入按鈕",
            "use_email_auth_provider":u"顯示 Mail 登入按鈕",
            "signed_in_callback":u"登入後所呼叫的 function",
            # "signed_out_callback":u"登出後所呼叫的 function",
        }
    name = Fields.StringProperty()

    initialization_snippet = Fields.TextProperty()

    sing_in_flow = Fields.StringProperty(default="popup")
    sing_in_success_url = Fields.StringProperty()
    terms_of_service_url = Fields.StringProperty()
    custom_css = Fields.BooleanProperty(default=False)
    use_google_auth_provider = Fields.BooleanProperty(default=True)
    google_scopes = Fields.StringProperty(default="['https://www.googleapis.com/auth/plus.login']")
    use_facebook_auth_provider = Fields.BooleanProperty(default=True)
    facebook_scopes = Fields.StringProperty(default="['public_profile', 'email', 'user_likes', 'user_friends']")
    use_twitter_auth_provider = Fields.BooleanProperty(default=True)
    use_github_auth_provider = Fields.BooleanProperty(default=True)
    use_email_auth_provider = Fields.BooleanProperty(default=True)

    signed_in_callback = Fields.StringProperty(default=u"")
    signed_out_callback = Fields.StringProperty(default=u"", verbose_name=u"AAAA")
    test = Fields.StringProperty(default=u"", verbose_name=u"AAAA", choices=(
        "aaa", "bbb", "ccc"
    ))


class ApplicationUserModel(BaseUserModel):
    class Meta:
        label_name = {
            "name": u"名稱",
            "account": u"帳號",
            "password": u"密碼",
            "is_enable": u"啟用",
            "avatar": u"頭像",
            "role": u"角色"
            }
    name = Fields.StringProperty(required=True)
    account = Fields.StringProperty(required=True)
    password = Fields.StringProperty(required=True)
    avatar = Fields.ImageProperty()
    is_enable = Fields.BooleanProperty(default=True)
    role = Fields.CategoryProperty(kind=BaseUoleModel, required=True)

    firebase_uid = Fields.StringProperty()
    email = Fields.StringProperty()
    emailVerified = Fields.BooleanProperty(default=False)
    isAnonymous = Fields.BooleanProperty(default=True)
