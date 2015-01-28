import glob
import os 
import re
import time

fileDir = os.getcwd ()
print fileDir
pythonFiles = glob.glob ("%s/*.txt" %fileDir)

while (True): 

#    time.sleep (10)


#rePattern = re.compile (r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}") 

    rePattern = re.compile (r"((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)")
    lineNo = 0

    for fileInput in pythonFiles:
        f0 = open(fileInput, "r")
        fileContent = f0.read()
        f0.close()

        singleLine = fileContent.split("\n")
        for line in singleLine:
            lineNo = lineNo + 1
            find = re.search (r"((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)", line)
            if find:
                print find.group(0), lineNo
                break
r"""       
        singleLine.remove(line)
#        print singleLine[lineNo-1]

        fileData = "\n".join(singleLine)
        
        os.remove(fileInput)
        f1 = open(fileInput, "w")
        f1.write(fileData)
        f1.close()
"""        
