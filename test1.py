from tkinter.filedialog import *
from tkinter import ttk
import test2

root = Tk()
root.resizable(False, False)
root.title('TIAA Automation')
main_orange = '#%02x%02x%02x' % (255, 184, 61)

n = ttk.Notebook(root)
f1 = ttk.Frame(n)  # first page, which would get widgets gridded into it
f2 = ttk.Frame(n)  # second page
n.add(f1, text='Manage Tests')
n.add(f2, text='Manage Data')
n.place(x=0, y=0)

# Create style of tabs
ttk.Style().configure("TNotebook", background=main_orange)
ttk.Style().map("TNotebook.Tab", background=[('selected', "grey")], foreground=[("selected", "grey")])
ttk.Style().configure("TNotebook.Tab", background="white", foreground="DarkGoldenrod4")

horiz_placemnt, vert_placemnt = test2.center(root, "root")

im = PhotoImage(file='D:/testing/soft/2.gif')
label1 = Label(f1, image=im)
label2 = Label(f2, image=im)
label1.pack()
label2.pack()

listbox1 = Listbox(f1, selectmode=EXTENDED)
settings = open('D:/testing/soft/Settings.ini', 'r').readlines()
if settings != []:
    a = os.listdir(settings[0])
    for i in a:
        if i == ".cache" or i == "__pycache__" or i == "rep" or i == "BaseTestCase.py" or i == "ConfigParser.py" or i == "GetPage.py":
            continue
        elif i.endswith('.py'):
            listbox1.insert(END, i)
    listbox1.place(x=2, y=0, height=vert_placemnt * 0.87, width=horiz_placemnt * 0.4)
    scrollbar = Scrollbar(listbox1)
    scrollbar.place(x=horiz_placemnt * 0.4 - 19, y=-1, height=vert_placemnt * 0.87)
    scrollbar['command'] = listbox1.yview
    listbox1['yscrollcommand'] = scrollbar.set
else:
    print("bla")
    settings = ''

# ------------Button's style variables-----------------------------------------------------------------
button_font = 'Anago 12'
button_menu_width = 150  # 193
button_menu_height = 25  # 51
border_value = 0
# -----------------------------------------------------------------------------------------------------

# ------------Button's section-------------------------------------------------------------------------

# RUN TESTS button desc
run_tests_image = PhotoImage(file='D:/testing/soft/run_test.gif')
run_tests_image_lighted = PhotoImage(file='D:/testing/soft/run_test_lighted.gif')
run_tests_button = Button(f1, width=button_menu_width, height=button_menu_height, bd=border_value,
                          font=button_font, image=run_tests_image,
                          command=lambda: test2.run_test(listbox1, settings, run_tests_button, horiz_placemnt,
                                                         stop_tests_button))  # height = 3 == 65 pixels
run_tests_button.place(x=horiz_placemnt * 0.46, y=145)
run_tests_button.bind("<Enter>", lambda button: run_tests_button.configure(image=run_tests_image_lighted))
run_tests_button.bind("<Leave>", lambda button: run_tests_button.configure(image=run_tests_image))

# GENERATE REPORT button desc
generate_report_image = PhotoImage(file='D:/testing/soft/generate_report.gif')
generate_report_image_lighted = PhotoImage(file='D:/testing/soft/generate_report_lighted.gif')
generate_report_button = Button(f1, width=button_menu_width, height=button_menu_height, bd=border_value,
                                fg="white", image=generate_report_image, font=button_font,
                                command=lambda: test2.generate_report())
generate_report_button.place(x=horiz_placemnt * 0.702, y=114)
generate_report_button.bind("<Enter>",
                            lambda button: generate_report_button.configure(image=generate_report_image_lighted))
generate_report_button.bind("<Leave>", lambda button: generate_report_button.configure(image=generate_report_image))

# OPEN LAST REPORT button desc
open_last_report_image = PhotoImage(file='D:/testing/soft/open_last_report.gif')
open_last_report_image_lighted = PhotoImage(file='D:/testing/soft/open_last_report_lighted.gif')
open_last_report_button = Button(f1, width=button_menu_width, height=button_menu_height, bd=border_value,
                                 fg="white", image=open_last_report_image,
                                 command=lambda: test2.open_last_report(), font=button_font)
open_last_report_button.place(x=horiz_placemnt * 0.702, y=145)
open_last_report_button.bind("<Enter>",
                             lambda button: open_last_report_button.configure(image=open_last_report_image_lighted))
open_last_report_button.bind("<Leave>", lambda button: open_last_report_button.configure(image=open_last_report_image))

# SETUP TEST RUN button desc
setup_test_run_image = PhotoImage(file='D:/testing/soft/setup_test_run.gif')
setup_test_run_image_lighted = PhotoImage(file='D:/testing/soft/setup_test_run_lighted.gif')
setup_test_run_button = Button(f1, width=button_menu_width, height=button_menu_height, bd=border_value,
                               fg="white", image=setup_test_run_image,
                               command=lambda: test2.setup_test_run(), font=button_font)
setup_test_run_button.place(x=horiz_placemnt * 0.46, y=114)
setup_test_run_button.bind("<Enter>",
                           lambda button: setup_test_run_button.configure(image=setup_test_run_image_lighted))
setup_test_run_button.bind("<Leave>", lambda button: setup_test_run_button.configure(image=setup_test_run_image))

# BROWSE YOUR TESTS button desc
browse_tests_image = PhotoImage(file='D:/testing/soft/browse.gif')
browse_tests_image_lighted = PhotoImage(file='D:/testing/soft/browse_lighted.gif')
browse_tests_button = Button(f1, text="Browse Your Tests", height=19, image=browse_tests_image, bd=1,
                             command=lambda: test2.browsecsv(listbox1, vert_placemnt, horiz_placemnt))
browse_tests_button.place(x=2, y=vert_placemnt * 0.87, width=horiz_placemnt * 0.4)
browse_tests_button.bind("<Enter>", lambda button: browse_tests_button.configure(image=browse_tests_image_lighted))
browse_tests_button.bind("<Leave>", lambda button: browse_tests_button.configure(image=browse_tests_image))

# STOP TESTS button desc
stop_tests_image = PhotoImage(file='D:/testing/soft/stop_tests.png')
stop_tests_image_lighted = PhotoImage(file='D:/testing/soft/stop_tests_lighted.png')
stop_tests_button = Button(f1, width=150, height=25, image=stop_tests_image, bd=0,
                           command=lambda: test2.kill_process(horiz_placemnt, run_tests_button, stop_tests_button))
stop_tests_button.bind("<Enter>", lambda button: stop_tests_button.configure(image=stop_tests_image_lighted))
stop_tests_button.bind("<Leave>", lambda button: stop_tests_button.configure(image=stop_tests_image))

# ----------------------------------------------Second tab section------------------------------------------------------
# SET COMMISSIONS button desc
set_commissions_image = PhotoImage(file='D:/testing/soft/set_commissions.gif')
set_commissions_image_lighted = PhotoImage(file='D:/testing/soft/set_commissions_lighted.gif')
set_commissions_button = Button(f2, width=150, height=25, image=set_commissions_image, bd=0,
                                command=lambda: test2.set_commissions())
set_commissions_button.place(x=horiz_placemnt * 0.23, y=114)
set_commissions_button.bind("<Enter>",
                            lambda button: set_commissions_button.configure(image=set_commissions_image_lighted))
set_commissions_button.bind("<Leave>", lambda button: set_commissions_button.configure(image=set_commissions_image))

root.mainloop()
