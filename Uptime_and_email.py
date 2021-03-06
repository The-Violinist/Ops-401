#!/usr/bin/env python3

#Challenge: Uptime Sensor with email notification
#David Armstrong
#10-07-2020
#Detecting activity change for an IP using ping and sending an email notification

### Libraries ###
import os
import subprocess
import time
import smtplib


### Variables ###
#Target address
#addr = input("Please enter an IP address: ")
addr = "8.8.8.8"

#Default state of change
state1 = 0
state = 0

#Gather email information
sendemail = input("Please enter your sender email address: ")
password = input("Please enter your password: ")
recemail = input("Please enter the receiver email address: ")

### Functions ###
#Connect to server and send email
def notify():
    #Connect to the server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(sendemail, password)

    # Send the mail
    msg = "The following change has occured to host %s. %s. \n %s" % (addr, event, timestamp)
    server.sendmail(sendemail, recemail, msg)
    server.quit()

#Ping the host and determine if it is up or down
def ping():
    global timestamp
    t = time.localtime()
    timestamp = time.asctime(t)
    global upordown
    with open(os.devnull, 'w') as dnull:
        try:
            subprocess.check_call(
                ['ping', '-n', '1', '-w', '10', addr],
                stdout=dnull,  # suppresses output
                stderr=dnull,
                )
            upordown = "Success!"
        except subprocess.CalledProcessError:
            upordown = "Failure!"
    print(upordown)

#Create the host state
def updown():
    global state
    global state1
    if (upordown == "Success!"):
        state = 0
    if (upordown == "Failure!"):
        state = 1

#Define the change in the host state then send email
def eventch():
    global event
    if (state == 1):
        event = "This host is now offline."
    if (state == 0):
        event = "This host is now online."
    print(event)
    #Send notification to admin
    notify()

#Define change of state
def statech():
    global change
    if (state == state1):
        change = "no"
    else:
        change = "yes"

### Main ###

while True:
    ping()
    updown()
    statech()
    if (change == "yes"):
        eventch()
        #notify()
        state1 = state
    #Reset the state value
    state = 0

    time.sleep(2)
    print("\n---------\n")

### End ###
