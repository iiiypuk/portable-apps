#!/usr/bin/env python3

import json

__author__ = 'Alexander Popov'
__version__ = '1.0.0'
__license__ = 'Unlicense'

README = '__Список программного обеспечения для ОС Windows, которое поддерживает режим portable__\n\n'
README += '__Типы активации portable__\n'
README += '- `Inst` - Режим portable выбирается во время установки\n'
README += '- `Conf` - Для активации portable необходимо создать файл\n'
README += '- `Zip` - На сайте присутствует прекомпилированная portable версия приложения\n'
README += '- `Portable` - Приложение самостоятельно хранит все файлы в директории\n\n'

if __name__ == '__main__':
    with open('apps.json', 'r', encoding='utf-8') as f:
        APPS = json.loads(f.read())
        APPS = sorted(APPS, key=lambda app: app['app_name'])

    TABLE_TEXT = str(README)
    TABLE_TEXT += '|   | App name | Portable type | App category | Site |\n'
    TABLE_TEXT += '| - | -------- | ------------- | ------------ | ---- |\n'

    for app in APPS:
        TABLE_TEXT += '| {icon} | {app_name} | {type} | {cat} | {site} |\n'.format(
            icon='![](https://raw.githubusercontent.com/iiiypuk/portable-apps/master/{0}/icon.png)'.format(app['directory']),
            app_name=app['app_name'], type=app['type'], cat=app['category'], site='[Go to]({0})'.format(app['homepage']))

    with open('README.md', 'w+', encoding='utf-8') as f:
        f.write(TABLE_TEXT)
