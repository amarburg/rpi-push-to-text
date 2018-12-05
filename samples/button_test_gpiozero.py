from gpiozero import Button
from signal import pause

def say_hello_blue():
    print("Hello Blue!")

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

