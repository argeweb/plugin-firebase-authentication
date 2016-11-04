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
    name = Fields.StringProperty(verbose_name=u"識別名稱")
    project_id = Fields.StringProperty(verbose_name=u"Firebase Project ID")

    initialization_snippet = Fields.TextProperty(verbose_name=u"初始化的 JS 語法片斷")

    sing_in_flow = Fields.StringProperty(default="popup", verbose_name=u"登入流程", choices=(
        "popup", "redirect"
    ))
    sing_in_success_url = Fields.StringProperty(verbose_name=u"成功登入後的網址")
    terms_of_service_url = Fields.StringProperty(verbose_name=u"服務條款的網址")
    custom_css = Fields.BooleanProperty(default=False, verbose_name=u"自行訂制CSS樣式")
    use_google_auth_provider = Fields.BooleanProperty(default=True, verbose_name=u"顯示 Google 登入按鈕")
    google_scopes = Fields.StringProperty(default="['https://www.googleapis.com/auth/plus.login']", verbose_name=u"Google 存取範圍 (scopes)")
    use_facebook_auth_provider = Fields.BooleanProperty(default=True, verbose_name=u"顯示 Facebook 登入按鈕")
    facebook_scopes = Fields.StringProperty(default="['public_profile', 'email', 'user_likes', 'user_friends']", verbose_name=u"Facebook 存取範圍 (scopes)")
    use_twitter_auth_provider = Fields.BooleanProperty(default=True, verbose_name=u"顯示 Twitter 登入按鈕")
    use_github_auth_provider = Fields.BooleanProperty(default=True, verbose_name=u"顯示 Github 登入按鈕")
    use_email_auth_provider = Fields.BooleanProperty(default=True, verbose_name=u"顯示 Mail 登入按鈕")

    signed_in_callback = Fields.StringProperty(default=u"", verbose_name=u"登入後所呼叫的 function")
    signed_out_callback = Fields.StringProperty(default=u"", verbose_name=u"登出後所呼叫的 function")


class ApplicationUserModel(BaseUserModel):
    name = Fields.StringProperty(required=True, verbose_name=u"名稱")
    account = Fields.StringProperty(required=True, verbose_name=u"帳號")
    password = Fields.StringProperty(required=True, verbose_name=u"密碼")
    avatar = Fields.ImageProperty(verbose_name=u"頭像")
    is_enable = Fields.BooleanProperty(default=True, verbose_name=u"啟用")
    role = Fields.CategoryProperty(kind=BaseUoleModel, required=True, verbose_name=u"角色")

    firebase_uid = Fields.StringProperty()
    email = Fields.StringProperty()
    emailVerified = Fields.BooleanProperty(default=False)
    isAnonymous = Fields.BooleanProperty(default=True)
