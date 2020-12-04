# CA3 - Reporting Alarm Clock
 
## Introduction

The Reporting Alarm Clock is a program that gathers relevent, updated news about the world such as the weather or COVID news, and has the functionality of an Alarm Clock. It can be used by anyone who wants to know information about the world at any time.

## Prerequisites 

Can be run with Python Version 3.8.6 and above. There are also two API keys needed, an Openweather API from  (https://openweathermap.org), and a News API from (https://newsapi.org/). Those can be changed from the apiconfigs.py file within the package. Finally, a stable internet connection is required to run the website.

## Installation

_Few internal Python modules need to be installed:_

Flask - pip install flask

Datetime - pip install DateTime

Schedule - pip install schedule

Logging - pip install logging

Text-to-Speech - pip install pyttsx3

COVID-19 Module - pip install uk-covid19

## Getting Started Tutorial

To use the actual program, you would need to run it and search the URL address http://127.0.0.1:5000/ to access the alarm clock. There will be a few inputs, the date and time when you want the alarm set, the label or name of the alarm, two checkboxes for whether you would like news or weather information. When the timer finishes, the alarm will be announced, and there will be an alarm in the alarm tab, and notifications for that alarm depending on what boxes you ticked. You can also delete notifications or alarms you are done with.

## Testing

There has been integrated testing within the package, if you would like to test the program, all you need to do in the same directory is use the command in the command prompt: "python -m pytest", the errors or passed items will be shown.

## Developer Documentation

Firstly, the main web page is found in the file main.py. This works as the main page for the website and calls other functions from other files in the package. 

The first file to talk about is the main_notification.py, this file has everything to do with notifications. The first function 'addNotification' checks with tick boxes were checked. If news box was checked, it would add relevent news to the notifications list, and same with the weather. Next, we have a function called getNotifications, all this does is return the list of notifications, this is in order to not call the list directly. Next function is the findByTitle, this searches the list for a title and returns the object. The function deleteByTitle is similar, it searches the list for a title but also deletes it. Finally, deleteByIndex function just deletes something from the list by position.

The second file is very similar to main_notification.py, and it is main_alarm.py because it does the same function but for alarms. There is a function addAlarm that adds any alarm to the list of alarms, but this time without taking check boxes into consideration since they are unrelated. Also, the main difference is that when addAlarm is used, it announces the alarm that has been created (no delay here). Next comes getAlarms, which returns the list of alarms, in order to not call the list directly. FindByTitle function searches the list for a title and returns the object. Next, deleteByTitle searches the list for a title, but deletes the object. Finally, deleteByIndex deletes the alarm in the list by the position.

The information or news that the notifications file receives is from three files, newsApi.py, weatherAPI.py, and covidAPI.py. NewsApi.py and weatherAPI.py have functions that extract the relevent data from the jsons of news and weather, then return them. CovidAPI.py uses a module that was shown in the installations section. It has four functions that extract the data, then one final function 'covid' that creates the finalized object.

Now, we can talk about the main page. Firstly, redirects the main page to the functionality page. Then it requests the tick boxes from the actual html, and uses deleteByTitle for both notifications and alarms. This makes sure you can delete notitications and alarms from the website. Next, we check if an alarm is being submitted, to create an actual alarm with its notifications. First, it gathers all the input from the website that the user will input, such as label, date, and the tick boxes. Then, it uses a function addAlarm that has been created below. This function applies all the input from the user, so it calls the alarm the label, and makes a delay depending on the date, and sends checks which boxes have been ticked. After that it uses the scheduler by using the delay created. After the delay or timer from the user has finished, it has two functionalities, firstly it calls a function from main_alarm.py that adds the alarm to the list and also announces it, and the second function is that it calls the function from main_notifications.py that adds notifications to the list. Therefore, when the delay finishes, both columns for alarms and notifications with have items, and the alarm will be announced.


## Details

Author : Author-Name

License: [MIT](https://choosealicense.com/licenses/mit/)

Link to Source: https://github.com/yusufaltattan/CA3


