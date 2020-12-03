import main_alarm

def test_newAPI():
    # get list
    test_list = main_alarm.getAlarms()
    assert test_list is not None
    
    # add item
    newAlarm = {'title': 'Hello', 'content':'Goodbye', 'alarm_isNewsIncluded':True, 'alarm_isWeatherIncluded':True}
    main_alarm.addAlarm(newAlarm)
    # get item
    getAlarms = main_alarm.findByTitle(newAlarm['title'] )
    assert getAlarms is not None    

    # delete item
    main_alarm.deleteByTitle(newAlarm['title'])
    # get item
    getAlarms = main_alarm.findByTitle(newAlarm['title'])
    assert getAlarms is None

