#!/usr/bin/env python
if __name__ == '__main__':
    import Tkinter as tk
    import PIL
    from PIL import ImageTk, Image
    from client_lib import *

    # Making a connection object.
    robot = kuka_iiwa_ros_client()

    # Wait until iiwa is connected zzz!
    while (not robot.isready): pass
    print('Started!')

    window = tk.Tk()
    window.title("Visual Aid")
    window.geometry("600x500")
    window.configure(background='grey')


    def display(image):
        path = "/home/kuka/catkin_ws/src/kuka_controller/src/"+image+".jpg"
        #path = "~/" + image + ".jpg"
        #img = tk.PhotoImage(file=path)
        img = ImageTk.PhotoImage(Image.open(path))
        cv = tk.Canvas(window,width=600,height=500)
        cv.pack(side='top', fill='both', expand='yes')
        cv.create_image(10, 10, image=img, anchor='nw')
        window.mainloop()


    display("001_touch")
    window.mainloop()
