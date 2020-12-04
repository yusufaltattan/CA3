import newsAPI
import weatherAPI
import covidAPI
'''Main Notifications'''
notification_list = []

def addNotification(notification):
    '''This adds notification to list of notifications'''
    if notification is not None:
        if notification['alarm_isNewsIncluded']:
            #Checks if news is ticked
            latest_news = newsAPI.extract(0)
            latest_corona = covidAPI.covid()
            notification_list.append({'title': notification['title'] +
            ' - News', 'content':latest_news['content']})
            notification_list.append({'title': notification['title']+
            ' - Corona', 'content':latest_corona['content']})
        if notification['alarm_isWeatherIncluded']:
            #Checks if weather was ticked
            latest_weather = weatherAPI.weather_today()
            notification_list.append({'title': notification['title']+
            ' - Weather', 'content':latest_weather['content']})
        # notification_list.append(notification)
    else:
        False

def getNotifications():
    '''Returns the list of notifications'''
    return notification_list

def findByTitle(searchTitle):
    '''Finds the nofication and returns it as an object'''
    return next((x for x in notification_list if x["title"] == searchTitle), None)

def deleteByTitle(notificationTitle):
    '''Deletes notification from list by name'''
    if notificationTitle is not None:
        actualNotification = findByTitle(notificationTitle)
        if actualNotification is not None:
            notificationIndex = -1
            try:
                notificationIndex = notification_list.index(actualNotification)
            except ValueError:
                notificationIndex = -1
            if notificationIndex > -1:
                deleteByIndex(notificationIndex)

def deleteByIndex(index):
    '''Deletes notification by position'''
    notification_list.pop(index)
