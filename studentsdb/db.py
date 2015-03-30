import os 


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
    #    'NAME': os.path.join(BASE_DIR, '..','db.sqlite3'),
        'HOST':'localhost',
        'USER':'stdents_db_user',
        'PASSWORD':'password',
        'NAME':'students_db',
    }
}
