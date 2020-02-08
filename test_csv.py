import os
import sys

lis = list()
pth = ""

with open('repos_task.txt','r',encoding='utf-8') as l:
    lis = l.readlines()

for x in lis:
    rep = str(x).replace("https://","").strip()
    calList = rep.split("/")
    if (os.path.exists('/opt/repos'+calList[len(calList)-1]) == False):
        os.mkdir('/opt/repos'+calList[len(calList)-1])