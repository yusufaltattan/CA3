from announcement import announce

alarms_list = []

def addAlarm(alarm):
    '''This adds alarm to the list of alarms'''
    alarms_list.append(alarm)
    announce(alarm['content'])

def getAlarms():
    '''Returns alarm lists'''
    return alarms_list

def findByTitle(searchTitle):
    '''Searches for alarm and returns object'''
    return next((x for x in alarms_list if x["title"] == searchTitle), None)

def deleteByTitle(alarmTitle):
    '''This deletes from the list by title name'''
    if alarmTitle is not None:
        actualAlarm = findByTitle(alarmTitle)
        if actualAlarm is not None:
            alarmIndex = -1
            try:
                alarmIndex = alarms_list.index(actualAlarm)
            except ValueError:
                alarmIndex = -1
            if alarmIndex > -1:
                deleteByIndex(alarmIndex)

def deleteByIndex(index):
    '''This deletes from list by position'''
    alarms_list.pop(index)
