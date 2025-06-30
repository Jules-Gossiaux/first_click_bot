import time
import pyautogui

time.sleep(4)

# Récupère la taille d'un élément avec les deux positions de la souris
pos1 = pyautogui.position()
print("Position 1:", pos1)
time.sleep(4)
pos2 = pyautogui.position()
print("Position 2:", pos2)


height = abs(pos2[1] - pos1[1])
print(f"Element height: {height}")