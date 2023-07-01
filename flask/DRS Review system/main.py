import tkinter
import cv2  #pip install opencv-python 
import PIL.Image , PIL.ImageTk  #pip install pillow

# width and hight of our screen 
SET_WIDTH = 650
SET_HIGHT = 368
cv_img = cv2.cvtColor(cv2.imread("anuj.png.jpg"),cv2.COLOR_BAYER_BG2GRAY)
Canvas = tkinter.Canvas (width= SET_WIDTH,hight= SET_HIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img) )
# Tkinter gui starts here 
window  = tkinter.Tk()
window.title("Thirde umpair decision Review ")


window.mainloop()