import os
import sys
import subprocess
import re

lis = list()
mainpath = "/opt/repos/"
reposlistfile = "repos_task_.txt"

#if (os.path.exists(mainpath) == False):
#    os.mkdir(mainpath)

with open(reposlistfile,'r',encoding='utf-8') as l:
    lis = l.readlines()

for x in lis:
    if (len(re.findall(r"^#", x)) == 0):
        rep = str(x).replace("https://","").strip()
        calList = rep.split("/")
        if (os.path.exists(mainpath+calList[2]) == False):
            subprocess.call(["git","--bare","clone", x.strip(), mainpath+calList[2]])
            subprocess.call(["touch", mainpath+calList[2]+"/.git/git-daemon-export-ok"])
            calList = list()
        else:
            os.chdir(mainpath+calList[2])
            subprocess.call(["git", "pull"])
            print(mainpath+calList[2] + " is pulled.")
    else:
        print(x + " is in comment.")

