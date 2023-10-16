import keyboard
import sys
import csv
import time

message = sys.argv[1]
students_contacts = sys.argv[2]

def send_and_sleep(command, sleep_time):
    keyboard.send(command)
    time.sleep(sleep_time)

def write_and_sleep(text, sleep_time):
    keyboard.write(text)
    time.sleep(sleep_time)

message_list = []
with open(message, mode='r', encoding='UTF-8') as message_body:
    for line in message_body:
        message_list.append(line)

keyboard.press_and_release('windows+s')
time.sleep(2)
write_and_sleep('whatsapp', 1)
send_and_sleep('enter', 5)

with open(students_contacts, mode='r', encoding='UTF-8') as contacts_list:
    csv_reader = csv.reader(contacts_list, delimiter=',')
    count = 0
    for row in csv_reader:
        # print(row)
        if count != 0:
            send_and_sleep('ctrl+f', 1)
            send_and_sleep('ctrl+a', 1)
            write_and_sleep(row[1], 2)
            send_and_sleep('tab', 1)
            send_and_sleep('enter', 1)
            keyboard.write("Hello {}!".format(row[0]))
            keyboard.send('enter')
            for item in message_list:
                write_and_sleep(item, 1)
                keyboard.send('enter')
            time.sleep(1)
            print("Elupee! Message has been sent to {}".format(row[0]))
            count += 1
        else:
            count += 1
    print("{} personalized messages have been sent!".format(count-1))