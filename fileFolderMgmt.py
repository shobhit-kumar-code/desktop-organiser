import os
import time
import json
import sys
class FileFolderManager:
    def __init__(self,path):
        self.path=path
        try:                    
            with open("config.json","r") as configContent:
                settings=json.loads(configContent.read())
                self.foldersList=settings["foldersList"]
                self.fileExtensions=settings["fileExtensions"]
                self.ancientValue=settings["ancientValue"]
                
            for foldername in self.foldersList:
                if not os.path.exists(self.path+"/"+foldername):
                    os.makedirs(self.path+"/"+foldername)
        except FileNotFoundError:
            sys.exit("config.json not found")
        except json.decoder.JSONDecodeError:
            sys.exit("Check the contents of config.json")

    def isAncient(self,mtime):
        if(time.time()-mtime>self.ancientValue):
            return True
        return False

    def getAgeAndMoveToAncient(self):
        flag=False
        for filename in os.listdir(self.path):
            if os.path.isfile(self.path+"/"+filename) and self.isAncient(os.path.getmtime(self.path+"/"+filename)):
                os.rename(self.path+"/"+filename , self.path+"/ancient/"+filename)
                flag=True
        if flag is True:
            print("Ancient files moved to the ancient directory. Please check the ancient directory.\n")
        

    def moveToDir(self):
        flag=False
        for filename in os.listdir(self.path):
            if os.path.isfile(self.path+"/"+filename):
                ext=os.path.splitext(filename)[-1].lower()
                for foldername in self.fileExtensions:
                    if ext in self.fileExtensions[foldername]:
                        os.rename(self.path+"/"+filename , self.path+"/"+foldername+"/"+filename)
                        flag=True
        if flag is True:
            print("Files have been moved. Check the directories.\n")
        else:
            print("There were no files to be moved.\n")
        