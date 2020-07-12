import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BATON = {
    'SITE_HEADER': 'Baton',
    'SITE_TITLE': 'Baton',
    'INDEX_TITLE': 'Site administration',
    'SUPPORT_HREF': 'https://github.com/otto-torino/django-baton/issues',
    'COPYRIGHT': 'copyright © 2017 <a href="https://www.otto.to.it">Otto srl</a>', # noqa
    'POWERED_BY': '<a href="https://www.otto.to.it">Otto srl</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'MENU': (
        { 'type': 'title', 'label': 'main', 'apps': ('auth', ) },
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },
        { 'type': 'title', 'label': 'Contents', 'apps': ('flatpages', ) },
        { 'type': 'model', 'label': 'Pages', 'name': 'flatpage', 'app': 'flatpages' },
        { 'type': 'free', 'label': 'Custom Link', 'url': 'http://www.google.it', 'perms': ('flatpages.add_flatpage', 'auth.change_user') },
        { 'type': 'free', 'label': 'My parent voice', 'children': [
            { 'type': 'model', 'label': 'A Model', 'name': 'mymodelname', 'app': 'myapp' },
            { 'type': 'free', 'label': 'Another custom link', 'url': 'http://www.google.it' },
        ] },
    ),
    'ANALYTICS': {
        'CREDENTIALS': os.path.join(BASE_DIR, 'credentials.json'),
        'VIEW_ID': '12345678',
    }
}
