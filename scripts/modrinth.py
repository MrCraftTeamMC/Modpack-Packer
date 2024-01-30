"""
Modrinth Api Impl
"""

import file
from requests import get, post, head 
from json import loads

def getProject(name: str) -> dict:
    datas = file.loadApiJson()
    api_url = datas["modrinth-v2"]["getProject"]
    r = get(url = api_url + name)
    return loads(r.json())

def TestGetProject(name: str) -> None:
    datas = file.loadApiJson()
    api_url = datas["modrinth-v2"]["getProject"]
    r = get(url = api_url + name)
    print(r.json())
