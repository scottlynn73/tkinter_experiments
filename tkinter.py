import Tkinter as tk
import ttk
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import urllib2
import json
import pandas as pd
import numpy as np


# constant for large font size
LARGE_FONT = ("Helvetica", 14)
style.use("ggplot")  # apply styling to plot


# constants for plot
f = Figure(figsize=(10, 5), dpi=100)

# Make a plot in the tkinter canvas
a = f.add_subplot(111)  # 111 means 1 by 1 size, plot 1


# make an animated plot from a text file- below could be any numerical data to plot
#def animate(i):
#    pullData = open("sampleData.txt", "r").read()
#    dataList = pullData.split('\n')
#    xList = []
#    yList = []
#    for eachLine in dataList:
#        if len(eachLine)>1:
#            x, y = eachLine.split(',')
#            xList.append(int(x))
#            yList.append(int(y))
#    a.clear()  # clear the last frame of the animation
#    a.plot(xList, yList)

# make an animated plot from a text file- below could be any numerical data to plot
def animate(i):
    # set counter
    x_axis = 0

    from time import gmtime, strftime
    #timestamp = pd.to_datetime(strftime("%Y-%m-%d %H:%M:%S"))

    while x_axis < 10:
        data_link = "https://api.coindesk.com/v1/bpi/currentprice.json"
        data = urllib2.urlopen(data_link).read()
        data = json.loads(data)

        data = data["bpi"]
        data = pd.DataFrame(data)

        buys = data.USD[3]

        a.clear()

        a.plot(x_axis, buys)

        x_axis += 1

# boilerplate code for initialising a tkinter window
class myapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self,*args,**kwargs)

        # main page title
        tk.Tk.wm_title(self, "RapidAir Graphical User Interface")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # for loop to show pages- needs to include all pages in the list= as new classes for each
        # page are made they need to be added to this list
        for F in (StartPage, BTC_Page, PageTwo, PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # function to show frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# now we add pages
# Start Page
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("Welcome to RapidAir\n "
                                     "Please click Proceed or Quit to leave"), font=LARGE_FONT)


        label.pack(pady=20, padx=20, )

        # add button1
        button1 = ttk.Button(self, text="Proceed",
                            command=lambda: controller.show_frame(BTC_Page))
        button1.pack()

        # add button1
        button2 = ttk.Button(self, text="Quit",
                            command=quit)
        button2.pack()


# Page One
class BTC_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=20, padx=20)

        # add button1
        button1 = ttk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        # add button1
        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


        # add button3
        button3 = ttk.Button(self, text="Graph Page",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()

# Page Two
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=20, padx=20)

        # add button1
        button1 = ttk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


        # add button1
        button2 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

        # add button1
        button3 = ttk.Button(self, text="Graph Page",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()


# Page Three
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=20, padx=20)

        # add button1
        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        # render in the tk canvas
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# call the app
app = myapp()
# send live graph animation frame to f, the plot, change the sampleData.txt file to see it update
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()