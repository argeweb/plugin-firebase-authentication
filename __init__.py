#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2016/07/08.

from argeweb import datastore
from .models.firebase_authentication_model import FirebaseAuthenticationModel

datastore.register('firebase_config', FirebaseAuthenticationModel.find_by_name)

plugins_helper = {
    'title': u'Firebase 驗証',
    'desc': u'透過 Firebase 來進行使用者身份的驗証',
    'controllers': {
        'firebase_authentication': {
            'group': u'Firebase 驗証',
            'actions': [
                {'action': 'config', 'name': u'驗証設定'},
            ]
        }
    }
}
