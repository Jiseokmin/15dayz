# -*- coding: utf-8 -*-

# flask core settings
DEBUG = True
TESTING = False
SECRET_KEY = "99d7e201187334217ba4f1c51a72e412"  #각자 개인의 python키를 여기에다 넣으시면됩니다.
PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 30

# flask wtf settings
WTF_CSRF_ENABLED = True

# flask mongoengine settings
MONGODB_SETTINGS = {
    'DB': 'flaskexample'
}

TEST_USER_ID = '111@111.com'
TEST_USER_PW = '111'

# flask mail settings
MAIL_DEFAULT_SENDER = 'noreply@yourmail.com'

# project settings
PROJECT_PASSWORD_HASH_METHOD = 'pbkdf2:sha1'
PROJECT_SITE_NAME = u'Flask Example'
PROJECT_SITE_URL = u'http://127.0.0.1:5000'
PROJECT_SIGNUP_TOKEN_MAX_AGE = 60 * 60 * 24 * 7  # in seconds
PROJECT_RECOVER_PASSWORD_TOKEN_MAX_AGE = 60 * 60 * 24 * 7  # in seconds
