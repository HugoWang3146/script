#!/usr/bin/python3

import os

appDict={
        'idea':'/home/xx/Software/idea-IU-182.3911.36/bin/idea.sh',
        'dbeaver':'/home/xx/Software/dbeaver/dbeaver',
        'postman':'/home/xx/Software/Postman/Postman'
        }

paramDict={
        'exit':'q',
        'help':'help'
        }

def openApplication(param):
    if param in appDict:
        result=os.popen(appDict[param])
    else:
        print('{} is not exits'.format(param))
        print('Please input again')

def executeCommand(param):
    if param==paramDict['exit']:
        exit(0)
    elif param==paramDict['help']:
        showApplicationList()
    else:
        openApplication(param)
    return True

def showApplicationList():
    for i in appDict:
        print('{:<20} : {}'.format(i,appDict[i]))

def main():
    while(True):
        print('***START***')
        command=input()
        executeCommand(command)
        print('***END***\n')

main()
