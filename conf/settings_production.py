# -*- coding: utf-8 -*-
"""
用于本地开发环境的全局配置
"""
import os
from settings import BASE_DIR


# ===============================================================================
# 数据库设置, 本地开发数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}