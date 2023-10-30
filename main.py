import pywhatkit
lines = ''

def sendMessage(message):
    with open('readme.txt') as f:
        lines = f.readlines()

    for i in lines:
        i.replace('\n', '')
        print(i)
        pywhatkit.sendwhatmsg_instantly(i, message, 5, True)


print(lines)




