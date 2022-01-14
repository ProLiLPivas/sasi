import sys
from sasi import Folder, File


APP_NAME = sys.argv[1]


APP_TEMPLATE = Folder(APP_NAME)\
    .folder(Folder('services')\
        .folder(Folder('tests')\
            .file(File(f'{APP_NAME}_test_case1.py'))\
            .file(File(f'{APP_NAME}_test_case2.py'))\
            .file(File(f'{APP_NAME}_test_case3.py'))
        )\
        .file(File('manager.py'))\
        .file(File('scemas.py'))
    )\
    .folder(Folder('utils', is_package=True) \
        .file(File(f'{APP_NAME}_utils.py'))\
        .file(File('db_utils.py'))
    )\
    .file(File('run.py'))\
    .file(File('models.py'))\
    .file(File('routes.py'))\
    .file(File('test.py'))


if __name__ == '__main__':
    # APP_TEMPLATE.create()
    print(f'create app "{APP_NAME} "with structure: ')
    print(APP_TEMPLATE.view())

