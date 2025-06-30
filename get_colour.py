import time
import pyautogui


print(pyautogui.pixel(-1005, 541))
time.sleep(4)

# Récupérer la position de la souris
pos = pyautogui.position()
print(f"Position de la souris: {pos}")

# Récupérer la couleur du pixel à cette position
couleur = pyautogui.pixel(pos.x, pos.y)
print(couleur)
