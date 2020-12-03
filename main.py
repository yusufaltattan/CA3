# Flask Imports
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
# External Packages
import time
import sched
import pyttsx3
from datetime import datetime
from announcement import announce
from time_conversions import hhmm_to_seconds
from time_conversions import current_time_hhmm
# Internal Packages
import main_notification
import main_alarm

app = Flask(__name__)

s = sched.scheduler(time.time, time.sleep)

@app.route('/index')
def main():
    '''
    Function for the whole system
    '''

    # Check if notification is sent to be deleted
    notification = request.args.get('notif')
    if notification:
        main_notification.deleteByTitle(notification)
        return redirect(request.path, code=302)
    
    # Check if alarm is sent to be deleted
    alarm = request.args.get('alarm_item')
    if alarm:
        main_alarm.deleteByTitle(alarm)
        return redirect(request.path, code=302)

    '''Function for the announcement alarm'''

    s.run(blocking=False)
   
    # check if alarm time has been submitted (to create an alarm with notification)
    alarm_time = request.args.get("alarm")
    if alarm_time:
        alarm_label = request.args.get('two')
        alarm_isNewsIncluded = request.args.get('news')
        alarm_isWeatherIncluded = request.args.get('weather')
        # convert to boolean
        alarm_isNewsIncluded = True if alarm_isNewsIncluded is not None else False
        alarm_isWeatherIncluded = True if alarm_isWeatherIncluded is not None else False
        AddAlarm(alarm_time, alarm_label, alarm_isNewsIncluded, alarm_isWeatherIncluded)

    return render_template('template.html', title='Daily update',
     notifications = main_notification.getNotifications(), 
     alarms= main_alarm.getAlarms(),
     image='af3ed088eb35793c077894f48f383e84.jpg')

def AddAlarm(alarm_time, alarm_label, alarm_isNewsIncluded, alarm_isWeatherIncluded):
    # Create Alarm Object
    alarm = {"alarm_time": alarm_time,
    "title": alarm_label,
    "content": alarm_label,
    "alarm_isNewsIncluded": alarm_isNewsIncluded,
    "alarm_isWeatherIncluded": alarm_isWeatherIncluded,
    }
    
    #convert alarm_time to a delay
    d1 = datetime.strptime(alarm_time, "%Y-%m-%dT%H:%M")
    d2 = datetime.now()
    delay = (d1 - d2).seconds - 50
    s.enter(int(delay), 1, main_alarm.addAlarm, [alarm ,])
    s.enter(int(delay), 1, main_notification.addNotification, [alarm ,])
    ##s.enter(int(delay)+5, 1, announce, [alarm['title'] ,])

if __name__ == '__main__':
    app.run()
