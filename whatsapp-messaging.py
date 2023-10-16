import pywhatkit
import sys
import csv
from datetime import datetime

students_contacts = sys.argv[2]
message = sys.argv[1]

with open(students_contacts) as f:
    csv_reader = csv.reader(f, delimiter=',')
    with open(message) as m:
        m = m.read()
        count = 0
        for row in csv_reader:
            try:
                if count != 0:
                    custom_message = m.format(row[0])
                    currentDateAndTime = datetime.now()
                    message_hour = currentDateAndTime.hour
                    message_minute = currentDateAndTime.minute
                    if message_minute == 59:
                        message_hour = message_hour + 1
                        message_minute = 0
                    else:
                        message_minute += 1
                    pywhatkit.sendwhatmsg(row[1], custom_message, message_hour, message_minute, 15, True, 3)
                    count = count + 1
                    #print(count)
                else:
                    count = count + 1
            except:
                if message_minute == 59:
                    message_hour = message_hour + 1
                    message_minute = 0
                else:
                    message_minute += 1
                pywhatkit.sendwhatmsg(row[1], custom_message, message_hour, message_minute, 15, True, 3)

