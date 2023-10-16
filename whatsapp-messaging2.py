import keyboard
import sys
import csv
import time

message = sys.argv[1]
students_contacts = sys.argv[2]

keyboard.press_and_release('windows+s')
time.sleep(2)
keyboard.write("whatsapp")
time.sleep(2)
keyboard.send('enter')
time.sleep(5)
with open(students_contacts) as f:
    csv_reader = csv.reader(f, delimiter=',')
    with open(message, mode='r', encoding='UTF-8') as m:
        m = m.read()
        count = 0
        for row in csv_reader:
            if count != 0:
                custom_message = m.format(row[0])
                keyboard.send('ctrl+f')
                time.sleep(4)
                keyboard.send('ctrl+a')
                time.sleep(4)
                keyboard.write(row[1])
                time.sleep(4)           
                keyboard.send('tab')
                time.sleep(4)
                keyboard.send('enter')
                time.sleep(4)
                keyboard.write(custom_message)
                time.sleep(4)
                keyboard.send('enter')
                time.sleep(4)
                # keyboard.send('ctrl+w')
                # time.sleep(2)
                count = count + 1
            else:
                count = count + 1
        print("{} personalized messages have been sent!".format(count-1))
