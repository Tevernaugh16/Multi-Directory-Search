import os
rootdir = "C:/Users/duperdays/Documents/maildir/allen-p"

phrase1 = "X-To:"
phrase2= "X-From:"

Sender = []
Reciever = []
for(path, dirs, files) in os.walk(rootdir, topdown=True): #topdown scans from top to bottom
    for filename in files:
        filepath = os.path.join(path, filename)
        with open(filepath, 'r') as currentfile:
            for line in currentfile:
                if phrase1 in line:
                    SenderName = line #SenderName = filename + line
                    Sender.append(SenderName)
                    print('Senders:\n' + str(Sender))
                if phrase2 in line:
                    RecieverName = line # RecieverName = filename + line
                    Reciever.append(RecieverName)
                    print('Recievers:\n' + str(Reciever))
                    