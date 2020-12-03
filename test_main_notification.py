import main_notification

def test_newAPI():
    # get list
    test_list = main_notification.getNotifications()
    assert test_list is not None
    
    # add item
    newNotification = {'title': 'Hello', 'content':'Goodbye', 'alarm_isNewsIncluded':True, 'alarm_isWeatherIncluded':True}
    main_notification.addNotification(newNotification)
    # get item
    getNotif = main_notification.findByTitle(newNotification['title'] + ' - News')
    assert getNotif is not None    

    # delete item
    main_notification.deleteByTitle(newNotification['title'] + ' - News')
    # get item
    getNotif = main_notification.findByTitle(newNotification['title'] + ' - News')
    assert getNotif is None

