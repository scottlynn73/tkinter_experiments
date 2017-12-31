# Embryonic RapidMet intergace in Tkinter
# The fields all work and the buttons trigger dummy functions
# TO DO:
#   put the UI code into RapidAir dir, import the read_params and update_setup functions
#   initialise the UI with the values from read_params
#   push values from the UI out to the SETUP file
#   set up the triggers in the buttons to set off the functions
#   sort out canvas plotting of the windrose so that this still works
#   plotting in separate matplotlib window would be ok
#   sort out a panelled UI with the other bits in it, maybe a file menu for loading up model run into the UI


# Notes
# Buttons and Labels don't need to be referenced as self- only the inputs where we want the values
# need to be referenced in this way.


import Tkinter as tk
import ttk
import tkFileDialog

# import dummy functions to test the buttons
from functions import func1, update_setup

# set up some pretend initialisation values for the cells
modeller= 'Scott'
project = 'new_run'
start_date = '2015/11/01'
end_date = '2015/12/31'
surf1 = '031710'
surf2 = '036000'
surf3 = '035302'
upper1 = '03238'
upper2 = '03999'

# font declarations
BIGFONT = 'System 24 bold'
smallfont = 'System 14 bold'
button_font = 'System 20'

# global spacing of items
pad_big = 5
pad_small = 2

# buttonx and buttony - sizes for buttons
buttonx = 20
buttony = 12

# master bg colour
bg_colour = 'SlateGray4'

# cell colour
cell_bg = 'gray60'

# font colour
font_colour = 'gray10'


class App(tk.Frame):
    def __init__(self, master):
        # ---------------------------------------
        # Set up global stuff for the main window
        # ---------------------------------------

        # establish main frame
        tk.Frame.__init__(self, master)
        self.pack()

        # set the title of the program window
        self.master.title("RapidAir urban dispersion model")
        self.master.resizable(False, False)

        # set the main frame background colour
        self.master.tk_setPalette(background=bg_colour)

        # Tab Control introduced here --------------------------------------
        tabControl = ttk.Notebook(self.master)  # Create Tab Control

        # add RapidMet tab
        rapidmet_tab = ttk.Frame(tabControl)  # Create a tab
        tabControl.add(rapidmet_tab, text='RapidMET')  # Add the tab

        # add RapidRoad tab
        rapidroad_tab = ttk.Frame(tabControl)  # Add a second tab
        tabControl.add(rapidroad_tab, text='RapidROAD')  # Make second tab visible
        tabControl.pack(expand=1, fill="both")  # Pack to make visible

        # -----------------------
        # SETUP RAPIDMET
        # -----------------------

        # add frames to the tabs
        dialog_frame0 = tk.Frame(rapidmet_tab)
        dialog_frame0.pack(padx=50, anchor='w', fill='x')

        # create a frame 1 for dialogs (putting in frames makes it easier to organise the page
        dialog_frame1 = tk.Frame(rapidmet_tab)
        dialog_frame1.pack(padx=50, anchor='w', fill='x')

        # create frame 2 for dialogs
        dialog_frame2 = tk.Frame(rapidmet_tab)
        dialog_frame2.pack(padx=50, anchor='w', fill='x')

        # create frame 2 for dialogs
        dialog_frame3 = tk.Frame(rapidmet_tab)
        dialog_frame3.pack(padx=50, anchor='w', fill='x')

        # create a frame for buttons
        button_frame = tk.Frame(rapidmet_tab)
        button_frame.pack(padx=50, anchor='w', fill='both')

        # place big font label with RapidAir font
        tk.Label(dialog_frame0, text="RapidMET setup",
                 font=BIGFONT, fg='Black').grid(padx=50, row=0, column=0, sticky='W', columnspan=True)

        # this function doesn't work on new version of OSX High Sierra
        # left in to show what it can do- looks like a useful file picker

        def browse_function():
            """ What to do when the Browse button is pressed """
            file_name = tkFileDialog.askopenfilename()
            browse_entry.delete(0, "end")
            browse_entry.insert(0, file_name)

        browse_file = tk.Button(dialog_frame0, text="Load file", command=browse_function).grid(row=0, column=1)
        browse_entry = tk.Entry(dialog_frame0).grid(row=0,column=2)


        def browse_directory():
            """ What to do when the Browse button is pressed """
            directory = tkFileDialog.askdirectory()
            browse_dir.delete(0, "end")
            browse_dir.insert(0, directory)

        browse_dir_button = tk.Button(dialog_frame0, text="Choose directory", command=browse_directory).grid(row=1, column=1)
        browse_dir = tk.Entry(dialog_frame0).grid(row=1,column=2)

        # ------------------------------------------
        # Set up dialog boxes for RapidMet parameters
        # -------------------------------------------
        # RAPIDMET DIALOG FRAME 1
        # set model name input box
        tk.Label(dialog_frame1, text="Model Project Name: ", fg=font_colour).grid(row=1, column=0, sticky='W')
        self.project_input = tk.Entry(dialog_frame1, background=cell_bg, width=68)
        self.project_input.insert(0, project)  # initialize with the project value (at top of script for now)
        self.project_input.grid(row=1, column=1, sticky='w', pady=pad_small, padx=pad_small)
        self.project_input.focus_set()

        # set user name input box
        tk.Label(dialog_frame1, text="Modeller Name:", fg=font_colour).grid(row=2, column=0, sticky='W')
        self.modeller_input = tk.Entry(dialog_frame1, background=cell_bg, width=68)
        self.modeller_input.insert(0, modeller) # initialize with the modeller value (at top of script for now)
        self.modeller_input.grid(row=2, column=1, sticky='w', pady=pad_small, padx=pad_small, columnspan=True)

        # RAPIDMET DIALOG FRAME 2
        # surface station 1 input area
        tk.Label(dialog_frame2, text="Surface met station 1 code:", fg=font_colour).grid(row=0, column=0, sticky='W')
        self.surface_code1 = tk.Entry(dialog_frame2, background=cell_bg)
        self.surface_code1.insert(0, surf1)  # initialize with the modeller value (at top of script for now)
        self.surface_code1.grid(row=0, column=1, sticky='w', columnspan=True)

        # surface station 2 input area
        tk.Label(dialog_frame2, text="Surface met station 2 code:", fg=font_colour).grid(row=1, column=0, sticky='W')
        self.surface_code2 = tk.Entry(dialog_frame2, background=cell_bg)
        self.surface_code2.insert(0, surf2)
        self.surface_code2.grid(row=1, column=1, sticky='w', pady=pad_small, padx=pad_small, columnspan=True)

        # surface station 2 input area
        tk.Label(dialog_frame2, text="Surface met station 3 code:", fg=font_colour).grid(row=2, column=0, sticky='W')
        self.surface_code3 = tk.Entry(dialog_frame2, background=cell_bg)
        self.surface_code3.insert(0, surf3)
        self.surface_code3.grid(row=2, column=1, sticky='w', pady=pad_small, padx=pad_small, columnspan=True)

        # upper station 1 input area
        tk.Label(dialog_frame2, text="Upper met station 1 code:", fg=font_colour).grid(row=0, column=2, sticky='W')
        self.upper_code1 = tk.Entry(dialog_frame2, background=cell_bg)
        self.upper_code1.insert(0, upper1)
        self.upper_code1.grid(row=0, column=3, sticky='w', pady=pad_small, padx=pad_small, columnspan=True)

        # upper station 2 input area
        tk.Label(dialog_frame2, text="Upper met station 2 code:", fg=font_colour).grid(row=1, column=2, sticky='W')
        self.upper_code2 = tk.Entry(dialog_frame2, background=cell_bg)
        self.upper_code2.insert(0, upper2)
        self.upper_code2.grid(row=1, column=3, sticky='w', pady=pad_small, padx=pad_small, columnspan=True)

        # AERMET start date
        tk.Label(dialog_frame2, text="AERMET start YYYY/MM/DD:", fg=font_colour).grid(row=3, column=0, sticky='W')
        self.aermet_start = tk.Entry(dialog_frame2, background=cell_bg)
        self.aermet_start.insert(0, start_date)
        self.aermet_start.grid(row=3, column=1, sticky='w', pady=pad_small, padx=pad_small, columnspan=True)

        # AERMET end date
        tk.Label(dialog_frame2, text="AERMET end YYYY/MM/DD:  ", fg=font_colour).grid(row=3, column=2, sticky='W')
        self.aermet_end = tk.Entry(dialog_frame2, background=cell_bg)
        self.aermet_end.insert(0, end_date)
        self.aermet_end.grid(row=3, column=3, sticky='w', pady=pad_small, padx=pad_small, columnspan=True)

        # Fill non cloud obs yes/no
        tk.Label(dialog_frame2, text="Fill non-cloud observations?", fg=font_colour).grid(row=4, column=0, sticky='W')
        self.fill_non_cloud_obs = tk.Checkbutton(dialog_frame2)
        self.fill_non_cloud_obs.grid(row=4, column=1, pady=pad_small, padx=pad_small, sticky='w')

        # Fill cloud cover obs yes/no
        tk.Label(dialog_frame2, text="Fill cloud observations?", fg=font_colour).grid(row=4, column=2, sticky='W')
        self.fill_cloud_obs = tk.Checkbutton(dialog_frame2, width=30)
        self.fill_cloud_obs.grid(row=4, column=3, pady=pad_small, padx=pad_small, sticky='w')

        # sumit button description
        tk.Label(dialog_frame2, text="Press SAVE when complete", fg=font_colour).grid(row=5, column=0,
                                                                                             sticky='W')

        # submit button
        tk.Button(dialog_frame2, text='SAVE', command=update_setup, font=button_font, width=10).grid(pady=pad_small,
                                                                                                row=5, column=1,
                                                                                                sticky='w')
        # Guidance text
        tk.Label(dialog_frame3, text="When you have completed the form, please hit the buttons "
                                     "in order to download and process\n your met data, and finally"
                                     " create and run the AERMET case").grid(row=0, column=0, sticky='w')

        # --------------------------------------------
        # Set up buttons to trigger RapidMet functions
        # --------------------------------------------
        # place buttons for RapidAir functions in the button frame command=func1 for example is calling func1
        tk.Button(button_frame, text='1.Download surface data', command=self.update_modeller).grid(row=0, column=0, ipadx=40)
        tk.Button(button_frame, text='2.Download upper air data', command=self.update_project_name).grid(row=0, column=1,ipadx=40)
        tk.Button(button_frame, text='3.Process met data', command=self.update_surface1).grid(row=0, column=2, ipadx=40)
        tk.Button(button_frame, text='4.Make AERMET run', command=self.update_project_name).grid(row=1, column=0, ipadx=55)
        tk.Button(button_frame, text='5.Perform AERMET run', command=self.update_project_name).grid(row=1, column=1, ipadx=50)
        tk.Button(button_frame, text='6.Perform filling', command=func1, width=19).grid(row=1, column=2,ipadx=18)
        tk.Button(button_frame, text='7.Create stats', command=func1).grid(row=2, column=0, ipadx=75)
        tk.Button(button_frame, text='8.Create windrose', command=func1).grid(row=2, column=1, ipadx=65)
        tk.Button(button_frame, text='Close RapidMET', command=self.click_cancel).grid(row=2, column=2, ipadx=53)

        # -----------------------------------
        # SETUP RAPIDROAD
        # -----------------------------------
        # add frames to the tabs
        dialog_frame0 = tk.Frame(rapidroad_tab)
        dialog_frame0.pack(padx=50, anchor='w', fill='x')

        # create a frame 1 for dialogs (putting in frames makes it easier to organise the page
        dialog_frame1 = tk.Frame(rapidroad_tab)
        dialog_frame1.pack(padx=50, anchor='w', fill='x')

        # create frame 2 for dialogs
        dialog_frame2 = tk.Frame(rapidroad_tab)
        dialog_frame2.pack(padx=50, anchor='w', fill='x')

        # create frame 2 for dialogs
        dialog_frame3 = tk.Frame(rapidroad_tab)
        dialog_frame3.pack(padx=50, anchor='w', fill='x')

        # create a frame for buttons
        button_frame = tk.Frame(rapidroad_tab)
        button_frame.pack(padx=50, anchor='w', fill='both')

        # place big font label with RapidAir font
        tk.Label(dialog_frame0, text="RapidROAD setup",
                 font=BIGFONT, fg='Black').grid(padx=50, row=0, column=0, sticky='W', columnspan=True)

        # this function doesn't work on new version of OSX High Sierra
        # left in to show what it can do- looks like a useful file picker

        def browse_function():
            """ What to do when the Browse button is pressed """
            file_name = tkFileDialog.askopenfilename()
            browse_entry.delete(0, "end")
            browse_entry.insert(0, file_name)

        browse_file = tk.Button(dialog_frame0, text="Load file", command=browse_function).grid(row=0, column=1)
        browse_entry = tk.Entry(dialog_frame0).grid(row=0, column=2)

        def browse_directory():
            """ What to do when the Browse button is pressed """
            directory = tkFileDialog.askdirectory()
            browse_dir.delete(0, "end")
            browse_dir.insert(0, directory)

        browse_dir_button = tk.Button(dialog_frame0, text="Choose directory", command=browse_directory).grid(row=1, column=1)
        browse_dir = tk.Entry(dialog_frame0).grid(row=1, column=2)

        # ------------------------------------------
        # Set up dialog boxes for RapidMet parameters
        # -------------------------------------------
        # RAPIDMET DIALOG FRAME 1
        # set model name input box
        tk.Label(dialog_frame1, text="Model Project Name: ", fg=font_colour).grid(row=1, column=0, sticky='W')
        self.project_input = tk.Entry(dialog_frame1, background=cell_bg, width=68)
        self.project_input.insert(0, project)  # initialize with the project value (at top of script for now)
        self.project_input.grid(row=1, column=1, sticky='w', pady=pad_small, padx=pad_small)
        self.project_input.focus_set()

        # set user name input box
        tk.Label(dialog_frame1, text="Modeller Name:", fg=font_colour).grid(row=2, column=0, sticky='W')
        self.modeller_input = tk.Entry(dialog_frame1, background=cell_bg, width=68)
        self.modeller_input.insert(0, modeller)  # initialize with the modeller value (at top of script for now)
        self.modeller_input.grid(row=2, column=1, sticky='w', pady=pad_small, padx=pad_small, columnspan=True)

        # RAPIDMET DIALOG FRAME 2
        # roughness
        tk.Label(dialog_frame2, text="Surface roughness (m):", fg=font_colour).grid(row=0, column=0, sticky='W')
        self.surface_rough = tk.Entry(dialog_frame2, background=cell_bg)
        self.surface_rough.insert(0, surf1)  # initialize with the modeller value (at top of script for now)
        self.surface_rough.grid(row=0, column=1, sticky='w', columnspan=True)

        # release height
        tk.Label(dialog_frame2, text="Emission release height (m):", fg=font_colour).grid(row=1, column=0, sticky='W')
        self.release_height = tk.Entry(dialog_frame2, background=cell_bg)
        self.release_height.insert(0, surf2)
        self.release_height.grid(row=1, column=1, sticky='w', pady=pad_small, padx=pad_small, columnspan=True)

        # initial depth
        tk.Label(dialog_frame2, text="Initial plume depth (m):", fg=font_colour).grid(row=2, column=0, sticky='W')
        self.initial_depth = tk.Entry(dialog_frame2, background=cell_bg)
        self.initial_depth.insert(0, surf3)
        self.initial_depth.grid(row=2, column=1, sticky='w', pady=pad_small, padx=pad_small, columnspan=True)

        # population
        tk.Label(dialog_frame2, text="Population (integer):", fg=font_colour).grid(row=0, column=2, sticky='W')
        self.upper_code1 = tk.Entry(dialog_frame2, background=cell_bg)
        self.upper_code1.insert(0, upper1)
        self.upper_code1.grid(row=0, column=3, sticky='w', pady=pad_small, padx=pad_small, columnspan=True)

        # emissions file
        tk.Label(dialog_frame2, text="Emissions shapefile (path):", fg=font_colour).grid(row=1, column=2, sticky='W')
        self.upper_code2 = tk.Entry(dialog_frame2, background=cell_bg)
        self.upper_code2.insert(0, upper2)
        self.upper_code2.grid(row=1, column=3, sticky='w', pady=pad_small, padx=pad_small, columnspan=True)

        # AERMET start date
        tk.Label(dialog_frame2, text="AERMOD start YYYY/MM/DD:", fg=font_colour).grid(row=3, column=0, sticky='W')
        self.aermet_start = tk.Entry(dialog_frame2, background=cell_bg)
        self.aermet_start.insert(0, start_date)
        self.aermet_start.grid(row=3, column=1, sticky='w', pady=pad_small, padx=pad_small, columnspan=True)

        # AERMET end date
        tk.Label(dialog_frame2, text="AERMOD end YYYY/MM/DD:  ", fg=font_colour).grid(row=3, column=2, sticky='W')
        self.aermet_end = tk.Entry(dialog_frame2, background=cell_bg)
        self.aermet_end.insert(0, end_date)
        self.aermet_end.grid(row=3, column=3, sticky='w', pady=pad_small, padx=pad_small, columnspan=True)

        # smooth road
        tk.Label(dialog_frame2, text="Smooth road emissions?", fg=font_colour).grid(row=4, column=0, sticky='W')
        self.fill_non_cloud_obs = tk.Checkbutton(dialog_frame2)
        self.fill_non_cloud_obs.grid(row=4, column=1, pady=pad_small, padx=pad_small, sticky='w')

        # road run
        tk.Label(dialog_frame2, text="Fill cloud observations?", fg=font_colour).grid(row=4, column=2, sticky='W')
        self.fill_cloud_obs = tk.Checkbutton(dialog_frame2, width=30)
        self.fill_cloud_obs.grid(row=4, column=3, pady=pad_small, padx=pad_small, sticky='w')

        # sumit button description
        tk.Label(dialog_frame2, text="Press SAVE when complete", fg=font_colour).grid(row=5, column=0,
                                                                                      sticky='W')

        # submit button
        tk.Button(dialog_frame2, text='SAVE', command=update_setup, font=button_font, width=10).grid(pady=pad_small,
                                                                                                     row=5, column=1,
                                                                                                     sticky='w')
        # Guidance text
        tk.Label(dialog_frame3, text="When you have completed the form, please hit the buttons "
                                     "in order to download and process\n your met data, and finally"
                                     " create and run the AERMET case").grid(row=0, column=0, sticky='w')

        # --------------------------------------------
        # Set up buttons to trigger RapidMet functions
        # --------------------------------------------
        # place buttons for RapidAir functions in the button frame command=func1 for example is calling func1
        tk.Button(button_frame, text='1.Download surface data', command=self.update_modeller).grid(row=0, column=0, ipadx=40)
        tk.Button(button_frame, text='2.Download upper air data', command=self.update_project_name).grid(row=0, column=1, ipadx=40)
        tk.Button(button_frame, text='3.Process met data', command=self.update_surface1).grid(row=0, column=2, ipadx=40)
        tk.Button(button_frame, text='4.Make AERMET run', command=self.update_project_name).grid(row=1, column=0, ipadx=55)
        tk.Button(button_frame, text='5.Perform AERMET run', command=self.update_project_name).grid(row=1, column=1, ipadx=50)
        tk.Button(button_frame, text='6.Perform filling', command=func1, width=19).grid(row=1, column=2, ipadx=18)
        tk.Button(button_frame, text='7.Create stats', command=func1).grid(row=2, column=0, ipadx=75)
        tk.Button(button_frame, text='8.Create windrose', command=func1).grid(row=2, column=1, ipadx=65)
        tk.Button(button_frame, text='Close RapidMET', command=self.click_cancel).grid(row=2, column=2, ipadx=53)

    # functions - need to get the update setup function in here and add a master 'UPDATE RAPIDMET' button to apply it

    def update_modeller(self):
        print("The modeller name is : {}".format(self.modeller_input.get()))

    def update_project_name(self):
        print("The project name is : {}".format(self.project_input.get()))

    def update_surface1(self):
        print("The surface code 1 is : {}".format(self.surface_code1.get()))

    # and so on

    # close window function

    def click_cancel(self):
        print("The user clicked cancel")
        # close the window
        self.master.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()
