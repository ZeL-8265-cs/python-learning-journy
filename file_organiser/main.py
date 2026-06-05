# python3_fileOrganiser
import os, shutil

os.chdir('/Users/lianzerui/Desktop')

os.makedirs('./sortFile/txt', exist_ok=True)
os.makedirs('./sortFile/pdf', exist_ok=True)
os.makedirs('./sortFile/png', exist_ok=True)
os.makedirs('./sortFile/jpg', exist_ok=True)

for filename in os.listdir('.'):

    src = os.path.join('.', filename)

    if os.path.isfile(src):

        if filename.endswith('.txt'):
            shutil.copy(src, './sortFile/txt')

        elif filename.endswith('.pdf'):
            shutil.copy(src, './sortFile/pdf')

        elif filename.endswith('.png'):
            shutil.copy(src, './sortFile/png')

        elif filename.endswith('.jpg'):
            shutil.copy(src, './sortFile/jpg')
