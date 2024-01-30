"""
The Main Script
"""

import ruamel.yaml
import file, modrinth, curseforge
from multiprocessing.pool import ThreadPool
from os import cpu_count, makedirs

threadpool = ThreadPool(cpu_count())  # IO Tasks

def main() -> None:
    makedirs(name=str(file.getCacheFolder()), mode=0o777, exist_ok=True)
    
    url = 'https://z1.ax1x.com/2023/12/07/piglCBF.jpg'
    
    file.download(url, 'mc.png')

    modrinth.TestGetProject("fabric-api")
    return

main()
