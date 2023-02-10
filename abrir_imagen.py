import cv2
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Abrir ventana para seleccionar archivo de imagen
file_path = filedialog.askopenfilename()

# Cargar imagen en variable
img = cv2.imread(file_path)

# Mostrar imagen en ventana
cv2.imshow("Imagen", img)

# Seleccionar ROI de la imagen
r = cv2.selectROI(img)

# Mostrar la imagen y el ROI seleccionado
imCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
cv2.imshow("ROI", imCrop)
cv2.waitKey(0)
cv2.destroyAllWindows()