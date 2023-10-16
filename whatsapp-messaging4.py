import keyboard
import sys
import csv
import time

message = sys.argv[1]
students_contacts = sys.argv[2]

keyboard.press_and_release('windows+s')
time.sleep(2)
keyboard.write("whatsapp")
time.sleep(1)
keyboard.send('enter')
time.sleep(5)
with open(students_contacts, mode='r', encoding='UTF-8') as f:
    csv_reader = csv.reader(f, delimiter=',')
    count = 0
    for row in csv_reader:
        print(row)
        with open(message, mode='r', encoding='UTF-8') as m:
            if count != 0:
                keyboard.send('ctrl+f')
                time.sleep(1)
                keyboard.send('ctrl+a')
                time.sleep(1)
                keyboard.write(row[1])
                time.sleep(2)           
                keyboard.send('tab')
                time.sleep(1)
                keyboard.send('enter')
                time.sleep(1)
                keyboard.write("Hi {}".format(row[0]))
                keyboard.send('enter')
                for line in m:
                    keyboard.write(line)
                    time.sleep(2)
                    keyboard.send('enter')
                time.sleep(2)
                keyboard.send('shift+tab')
                time.sleep(1)
                keyboard.send('enter')
                time.sleep(1)
                keyboard.send('enter')
                time.sleep(2)
                keyboard.write("qrcode.png")
                time.sleep(3)
                keyboard.send('enter')
                time.sleep(2)
                keyboard.send('enter')
                count = count + 1
            else:
                count = count + 1
    print("{} personalized messages have been sent!".format(count-1))
