import os;
import platform;

for root, dirs, files in os.walk('.'):
    for file in files:
        if file == 'requirements.txt':
            file_install = str('pip install -r '+root+'\\'+file);
            os.system(file_install);
            pass;
        pass;
    pass;

if platform.system() == 'Windows':
    print('aqui')
    os.system('pip freeze > windows_requirements.txt');
    pass;
elif platform.system() == 'Linux':
    os.system('pip freeze > linux_requirements.txt');
    pass;
