LOG_PATH = "logs/debug.log"

def loadLoadFile():
    return open(LOG_PATH,'r')

def getLoagList():
    logs = list()
    for line in loadLoadFile():
        logs.append(line)
    return logs

# print(getLoagList())
