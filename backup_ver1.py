import os
import time

source = ['C:\\folder']
target_dir = ['D:\\target']

target = str(target_dir) + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
print((target))
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось')

print('###########')