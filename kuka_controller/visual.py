import tkinter as tk
from client_lib import *

# Making a connection object.
robot = kuka_iiwa_ros_client()

# Wait until iiwa is connected zzz!
while (not robot.isready): pass
print('Started!')

window = tk.Tk()
window.title("Visual Aid")
window.geometry("300x300")
window.configure(background='grey')

window.mainloop()

def display(image):
    path = image+".jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(window, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
