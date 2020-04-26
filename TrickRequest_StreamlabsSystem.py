import json
import os
import codecs
import sys
import clr
import time

ScriptName = "Trick Request"
Website = "cooldavidiscool.com"
Description = "trick request for skaterXL (or anything really)"
Creator = "cooldavidiscool"
Version = "0.0.0.1"

configFile = "settings.json"
trFile = "trickrequest.txt"
usFile = "usernames.txt"

settings = {}
path = ""

def ScriptToggled(state):
	return

def Init():
    global settings, path
    path = os.path.dirname(__file__)

    with codecs.open(os.path.join(path, configFile), encoding='utf-8-sig') as json_file:
            settings = json.load(json_file,encoding='utf-8-sig')

    return


def Execute(data):
    if data.GetParam(0).lower() == "!tr" and Parent.IsOnUserCooldown(ScriptName,"!tr",data.User) == False:
        username = data.UserName;
        trick = data.Message[len("!tr") + 1:]
        if trick == "":
            send_message(username + " you forgot a trick")
            return
        writetrick(trick, username)
        Parent.AddUserCooldown(ScriptName,"!tr",data.User, 10)
        send_message(username + " your trick request was added!")
        return
    elif data.GetParam(0).lower() == "!trick" and Parent.IsOnUserCooldown(ScriptName,"!tr",data.User) == False:
        username = data.UserName;
        trick = data.Message[len("!trick") + 1:]
        if trick == "":
            send_message(username + " you forgot a trick")
            return
        writetrick(trick, username)
        Parent.AddUserCooldown(ScriptName,"!tr",data.User, 10)
        send_message(username + " your trick request was added!")
        return
    elif data.GetParam(0).lower() == "!land":
        if data.UserName == whoisfirst() or data.UserName == settings['whoisstreaming']:
            if settings['tricklandmessage'] == "":
                send_message("* * T R I C K L A N D E D * *")
            else:
                send_message(settings['tricklandmessage'])
            if settings['sourceName'] != "" and settings['sceneName'] != "" and settings['duration'] != 0:
                Parent.SetOBSSourceRender(settings['sourceName'], True, settings['sceneName'], callback)
                time.sleep(settings['duration'])
                Parent.SetOBSSourceRender(settings['sourceName'], False, settings['sceneName'], callback)
            deletefirstlines()
            return
        else:
            send_message("only " + whoisfirst() + " can say !land for their trick request - ohp!")
        return
    elif data.GetParam(0).lower() == "!tr" or data.GetParam(0).lower() == "!trick" and Parent.IsOnUserCooldown(ScriptName,"!tr",data.User):
        send_message(" sorry, " + data.UserName + " you gotta wait another few seconds to request another trick - ohp")
        return
    else:
        return


def Tick():
    return

def send_message(message):
    Parent.SendStreamMessage(message)
    return

def writetrick(t, u):
    trLocation = os.path.join(path,trFile) #trick txt file location

    with open(trLocation, "a+") as myfile:
        myfile.write(t + "\n")

    userLocation = os.path.join(path, usFile) #username txt file location

    with open(userLocation, "a+") as myfile:
        myfile.write(u + "\n")

    return

def whoisfirst():
    userLocation = os.path.join(path, usFile)  #username txt file location

    with open(userLocation, "a+") as myfile:
        myfile.seek(0)
        firstuser = myfile.readline().strip() #strip to get rid of newline character ohp
    return firstuser

def deletefirstlines():
    trLocation = os.path.join(path, trFile)  # trick txt file location

    with open(trLocation, "r+") as f: # open in read / write mode
        f.readline()  # read the first line and throw it out
        data = f.read()  # read the rest
        f.seek(0)  # set the cursor to the top of the file
        f.write(data)  # write the data back
        f.truncate()  # set the file size to the current size

    userLocation = os.path.join(path, usFile)  # username txt file location

    with open(userLocation, "r+") as f:  # open in read / write mode
        f.readline()  # read the first line and throw it out
        data = f.read()  # read the rest
        f.seek(0)  # set the cursor to the top of the file
        f.write(data)  # write the data back
        f.truncate()  # set the file size to the current size
    return

def callback(response):
	return

def Unload():
    return