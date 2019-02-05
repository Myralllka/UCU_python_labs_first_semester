# module based on article (https://pythono.ru/threading/)

import os
import shutil
import threading

import requests


def down(url):
    """
    string -> None

    function using for download file from the Internet

    Arguments:
        url {[str]} -- [url on the file that you want to download from the
        Internet]
    """
    (dirname, filename) = os.path.split(url)
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        os.system("gzip -d " + filename)


def download_using_url(array_of_urls):
    """
    list -> None

    function using to download documents using threads
    """
    for i in range(len(array_of_urls)):
        threading.Thread(target=down, args=[array_of_urls[i]]).start()
    old = threading.active_count() + 1
    while True:
        if old != threading.active_count():
            old = threading.active_count()
            print("%s files to download and unpack" % str(old - 1))
        if threading.active_count() == 1:
            break
