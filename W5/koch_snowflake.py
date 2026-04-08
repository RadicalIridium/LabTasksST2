#mm

import math
from tkinter import *

from numpy import angle

from numpy import angle # Import tkinter

class kochSnowflake:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Koch Snowflake") # Set a title

        self.width = 200
        self.height = 200

        self.canvas = Canvas(window,
        width = self.width, height = self.height)
        self.canvas.pack()

        # Add a label, an entry, and a button to frame1
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()

        Label(frame1,
        text = "Enter an order: ").pack(side = LEFT)
        self.order = StringVar()
        entry = Entry(frame1, textvariable = self.order,
        justify = RIGHT).pack(side = LEFT)
        Button(frame1, text = "Display Koch Snowflake",
        command = self.display).pack(side = LEFT)

        window.mainloop() # Create an event loop

    def display(self):
        self.canvas.delete("line")
        p1 = [self.width / 2, 10]
        p2 = [10, self.height - 10]
        p3 = [self.width - 10, self.height - 10]

        self.drawKochLine(int(self.order.get()), p1, p2)
        self.drawKochLine(int(self.order.get()), p2, p3)
        self.drawKochLine(int(self.order.get()), p3, p1)


    def drawKochLine(self, order, p1, p2):
        if order == 0:
            self.drawLine(p1, p2)
        else:
            t1, t2 = self.thirdpoint(p1, p2)

            dx = t2[0] - t1[0]
            dy = t2[1] - t1[1]

            angle = math.radians(60)

            x_rot = dx * math.cos(angle) - dy * math.sin(angle)
            y_rot = dx * math.sin(angle) + dy * math.cos(angle)

            spike = [t1[0] + x_rot, t1[1] + y_rot]

            self.drawKochLine(order - 1, p1, t1)
            self.drawKochLine(order - 1, t1, spike)
            self.drawKochLine(order - 1, spike, t2)
            self.drawKochLine(order - 1, t2, p2)

    def drawLine(self, p1, p2):
        self.canvas.create_line(
            p1[0], p1[1], p2[0], p2[1], tags = "line")

    # Return the midpoint between two points
    def midpoint(self, p1, p2):
        p = 2 * [0]
        p[0] = (p1[0] + p2[0]) / 2
        p[1] = (p1[1] + p2[1]) / 2
        return p
    
    def thirdpoint(self, p1, p2):
        p_1 = 2 * [0]
        p_2 = 2 * [0]

        p_1[0] = (2*p1[0] + p2[0]) / 3
        p_1[1] = (2*p1[1] + p2[1]) / 3

        p_2[0] = (p1[0] + 2*p2[0]) / 3
        p_2[1] = (p1[1] + 2*p2[1]) / 3

        return p_1, p_2
    

        
    
kochSnowflake() # Create GUI