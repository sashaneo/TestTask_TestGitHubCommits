import os
import time

source = ['/home/sasha_neo/selenium_driver']
target_dir = ['/media/sasha_neo/Sistem/target_dir']

target = str(target_dir) + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
print((target))
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось')

print('###########')