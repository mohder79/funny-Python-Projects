from pynput.mouse import Button, Controller
import time


first_mouse_position = (486, 879)
first_mouse_position1 = (486, 815)
first_mouse_position2 = (483, 749)
first_mouse_position3 = (483, 686)
first_mouse_position4 = (480, 621)
first_mouse_position5 = (486, 553)
first_mouse_position6 = (487, 490)
first_mouse_position7 = (483, 426)
first_mouse_position8 = (483, 360)
first_mouse_position9 = (483, 299)

second_mouse_position = (37, 962)

mouse = Controller()

count = 0

while True:
    mouse.position = first_mouse_position
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = second_mouse_position
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = first_mouse_position1
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = second_mouse_position
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = first_mouse_position2
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = second_mouse_position
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = first_mouse_position3
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = second_mouse_position
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = first_mouse_position4
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = second_mouse_position
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = first_mouse_position5
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = second_mouse_position
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = first_mouse_position6
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = second_mouse_position
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = first_mouse_position7
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = second_mouse_position
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = first_mouse_position8
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = second_mouse_position
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = first_mouse_position9
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = second_mouse_position
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(4)
    count += 9
    print(count)
