import os
import sys
import subprocess

lis = list()
mainpath = "/opt/repos/"
reposlistfile = "repos_task.txt"

if (os.path.exists(mainpath) == False):
    os.mkdir(mainpath)

with open(reposlistfile,'r',encoding='utf-8') as l:
    lis = l.readlines()

for x in lis:
    rep = str(x).replace("https://","").strip()
    calList = rep.split("/")
    subprocess.call(["git","--bare","clone", x.strip(), mainpath+calList[2]])
    subprocess.call(["touch", mainpath+calList[2]+"/.git/git-daemon-export-ok"])
    calList = list()
