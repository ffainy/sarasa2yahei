import shutil as fs
import requests as req
import py7zr as sz
import os
import json
import wget


API_URL = 'https://api.github.com/repos/be5invis/Sarasa-Gothic/releases/latest'
DOWNLOAD_DIR = '/tmp/sarasafonts'


def get_latest_url():
    response = req.get(API_URL)
    details = json.loads(response.content)

    version = details['tag_name'][1:]
    name = 'sarasa-gothic-ttf-unhinted-' + version + '.7z'

    assets = details['assets']
    for asset in assets:
        if (asset['name'] == name):
            return asset['browser_download_url']

def get_latest_tag():
    response = req.get(API_URL)
    details = json.loads(response.content)
    tag = details['tag_name'][1:]

    return tag

def clear_dir(directory):
    if (os.path.exists(directory)):
        fs.rmtree(directory)
    os.makedirs(directory)

def download_sarasa(url):
    filename = url.split('/')[-1]
    filepath = DOWNLOAD_DIR + '/' + filename

    # wget.download(url, filepath)

    return filepath

def unzip_sarasa(filepath):
    with sz.SevenZipFile(filepath, 'r') as zip_file:
        zip_file.extract(targets=['sarasa-ui-cl-regular.ttf', 'sarasa-ui-cl-light.ttf', 'sarasa-ui-cl-bold.ttf'], path=DOWNLOAD_DIR)
