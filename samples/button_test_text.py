from gpiozero import Button
from signal import pause

from bandwidth import messaging, voice, account
api = messaging.Client('u-raebd2emcivwq27k5hufnfq', 't-5m66szdyhlq7suujju4q5oy', '5pjp6k5nvlsetakmph54zs2626d4yz7z6edf6ry')

def say_hello_blue():
    print("Hello Blue!")

    message_id = api.send_message(from_ = '+15412071838',
                                  to = '+12067349236',
                                  text = 'Blue button!')
    print(message_id)

def say_hello_yellow():
    print("Hello Yellow!")

def say_goodbye():
    print("Goodbye!")

button_blue = Button(2, pull_up=True )
button_yellow = Button(3, pull_up=True )

button_blue.when_pressed = say_hello_blue
button_blue.when_released = say_goodbye

button_yellow.when_pressed = say_hello_yellow
button_yellow.when_released = say_goodbye

print("Go!")
pause()

