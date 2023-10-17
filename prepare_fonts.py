import os
import shutil as fs
import py7zr as sz
import glob


OUTPUT_DIR = '/tmp/sarasafonts/out'


def compress_files():
    with sz.SevenZipFile(OUTPUT_DIR + '/sarasa2yahei.7z', 'w') as archive:

        files = glob.glob(OUTPUT_DIR + '/*.tt[cf]')
        for file in files:
            path, name = os.path.split(file)
            archive.write(file, name)
