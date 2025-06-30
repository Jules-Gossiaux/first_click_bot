import time 
import pyautogui

initial_pos = (-1000, 987)

item_height = 123

colour_items = [(93, 189, 2), (83, 169, 2)] #[(Non_survolé), (survolé)]


def improve():
    while pyautogui.pixel(*pyautogui.position()) in colour_items:
        pyautogui.click()
    return

def move():
    pyautogui.moveTo(initial_pos[0], initial_pos[1])
    pyautogui.scroll(-3000)
    while pyautogui.position()[1] > (pyautogui.size()[1]+150)/2:
        improve()
        pyautogui.moveRel(0, -item_height)
    pyautogui.scroll(3000)
    pyautogui.moveRel(0, item_height)
    while pyautogui.position()[1] > 100:
        improve()
        pyautogui.moveRel(0, -item_height)

while True:
    move()