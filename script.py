import os
from fileFolderMgmt import FileFolderManager
import json
import sys

with open("desktopPath.json") as pathToDesktop:
    initSettings=json.loads(pathToDesktop.read())
    desktopPath=initSettings["path"]
    if desktopPath=="NO_PATH":
        sys.exit("Please paste the path to your desktop in desktopPath.json\n")
    print("Desktop Path set as:\n"+desktopPath+"\n")

foldermanager=FileFolderManager(desktopPath)
foldermanager.getAgeAndMoveToAncient()
foldermanager.moveToDir()