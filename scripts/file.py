"""
File Utils
"""

from requests import get, post, head 
from tqdm import tqdm
from os import getcwd
from platform import system
from json import load

def getPrePathChar() -> str:
    if system() == 'Windows':
        return '\\'
    return '/'

def getCacheFolder() -> str:
    return getcwd() + getPrePathChar() + "cache" + getPrePathChar()

def download(_url: str, _filename: str) -> None:
    path = getCacheFolder()

    header = head(url = _url)
    length = int(header.headers['content-length'])

    bar = tqdm(total = length, unit = "B", unit_scale = True, unit_divisor = 1024, ascii = True, desc = _filename)
    with open(file = path + _filename, mode = "wb+") as f, get(url = _url, stream = True, allow_redirects = True) as r:
        for chunk in r.iter_content(chunk_size = 1024):
            if chunk:
                f.write(chunk)
                bar.update(len(chunk))

    bar.close()
    return

def loadApiJson() -> dict:
    with open(file = "api.json", mode = "r+") as f:
        data = load(f)
        f.close()
    return data
