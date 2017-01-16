import subprocess
from tkinter.filedialog import *
from tkinter import ttk

path_to_test = open('D:/testing/soft/Settings.ini', 'r').readlines()
global run_tests_process


def browsecsv(listbox1, vert_placemnt, horiz_placemnt):
    global path_to_test
    listbox1.delete(0, END)
    path_to_test = askdirectory()
    setting = open('D:/testing/soft/Settings.ini', 'w')
    setting.write(path_to_test)
    a = os.listdir(path_to_test)
    setting.close()
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


def center(toplevel, window):  # центрирует появление окна
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    if window == "root":
        horiz_placemnt = w / 2.98
        vert_placemnt = h / 2.71
    elif window == "config":
        horiz_placemnt = w / 5
        vert_placemnt = h / 3.9
    toplevel.geometry(
        "%dx%d+%d+%d" % (horiz_placemnt, vert_placemnt, (w - horiz_placemnt) / 2, (h - vert_placemnt) / 2))
    return horiz_placemnt, vert_placemnt


def run_test(listbox1, path, run_tests_button, horiz_placemnt, stop_tests):
    global path_to_test, run_tests_process
    run_tests_button.place_forget()
    stop_tests.place(x=horiz_placemnt * 0.46, y=145)
    selected_item = listbox1.get(ACTIVE)
    if path_to_test != '':
        cmd = 'cd /d ' + path_to_test[0] + ' & ' + 'py.test ' + selected_item + ' -s --alluredir rep'
    else:
        cmd = 'cd /d ' + path[0] + ' & ' + 'py.test ' + selected_item + ' -s --alluredir rep'
    run_tests_process = subprocess.Popen(cmd, shell=True)


# kill RUN TESTS process
def kill_process(horiz_placemnt, run_tests_button, stop_tests):
    global run_tests_process
    subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=run_tests_process.pid))
    run_tests_button.place(x=horiz_placemnt * 0.46, y=145)
    stop_tests.place_forget()


def generate_report():
    cmd = 'cd /d d:/Automation/bin' + ' & ' + 'allure generate D:/testing/ddt_testing/tests/rep'
    subprocess.Popen(cmd, shell=True)


def open_last_report():
    cmd = 'cd /d d:/Automation/bin' + ' & ' + 'allure report open'
    subprocess.Popen(cmd, shell=True)


def setup_test_run():
    config_ini = open('D:/testing/ddt_testing/config.ini', 'r').readlines()
    config_readed = []
    launch_parameter = ''
    counter = 0
    for i in config_ini[1:]:
        for k in i:
            launch_parameter += k
            if k == ':' and counter == 0:
                counter = 1
                launch_parameter = ''
            if k == '\n':
                counter = 0
                config_readed.append(launch_parameter)
                launch_parameter = ''

    config = Toplevel()
    center(config, "config")
    config.deiconify()
    config.grab_set()
    config.focus_force()
    config.title('TIAA Automation')
    config.resizable(False, False)
    im = PhotoImage(file='D:/testing/soft/config_image.gif')
    label1 = Label(config, image=im)
    label1.pack()
    main_orange = '#%02x%02x%02x' % (255, 184, 61)
    font = 'Anago 10 bold'

    # ----------------------------Buttons----------------------------------------------------------------------------
    ok = Button(config, text="  Save  ", bg=main_orange, fg='white', font=font, bd=0,
                command=lambda: change_current_settings(link_text, variable, timeout_text, config))
    ok.place(x=141, y=220)
    ok.bind("<Enter>", lambda a: ok.configure(bg="burlywood1"))
    ok.bind("<Leave>", lambda a: ok.configure(bg=main_orange))

    cancel = Button(config, text="Cancel", bg="gray64", fg='white', font=font, bd=0,
                    command=lambda: close_settings(config))
    cancel.place(x=195, y=220)
    cancel.bind("<Enter>", lambda a: cancel.configure(bg="gray79"))
    cancel.bind("<Leave>", lambda a: cancel.configure(bg="gray64"))

    text_box_color = 'antique white'
    # Browser textbox
    browser_text = Text(config, width=15, height=1, bg=text_box_color)
    browser_text.place(x=200, y=75)

    # -----------------------------------------------------------------------------------------------------------------

    def func():
        if variable.get() == "Firefox":
            browser_dropdown.configure(image=firefox)
        elif variable.get() == "Chrome":
            browser_dropdown.configure(image=chrome)
        elif variable.get() == "PhantomJS":
            browser_dropdown.configure(image=phantom)

    # Browser dropdown
    browser_list = [
        "Firefox",
        "Chrome",
        "PhantomJS"
    ]

    variable = StringVar(config)
    dropdown_image = PhotoImage(file='dropdown_image.png')
    firefox = PhotoImage(file='dropdown_firefox.png')
    chrome = PhotoImage(file='chrome_dropdown.png')
    phantom = PhotoImage(file='phantom_dropdown.png')
    variable.set("Choose a Browser")

    dropdown_lighted_image = PhotoImage(file='dropdown_lighted.png')
    dropdown_lighted = Label(config, image=dropdown_lighted_image, bg="bisque", width=124, height=19)
    browser_dropdown = OptionMenu(config, variable, *browser_list, command=lambda x: func())
    browser_dropdown.configure(width=120, height=15, bd=0, indicator=0,
                               image=dropdown_image)  # if bg is picture width=92, height=15
    browser_dropdown.bind("<Enter>", lambda a: dropdown_lighted.place(x=198, y=73))
    browser_dropdown.bind("<Leave>", lambda a: dropdown_lighted.place_forget())

    # Set-up browser by default
    if config_readed[0] == " Firefox\n":
        variable.set(browser_list[0])
        browser_dropdown.configure(image=firefox)
    elif config_readed[0] == " Chrome\n":
        variable.set(browser_list[1])
        browser_dropdown.configure(image=chrome)
    elif config_readed[0] == " PhantomJS\n":
        variable.set(browser_list[2])
        browser_dropdown.configure(image=phantom)
    browser_dropdown.place(x=200, y=75)

    # Link textbox
    link_text = Text(config, width=17, height=1, bg=text_box_color, font='Anago-Book 10', fg='gray38')
    link_text.insert(END, config_readed[1])
    link_text.place(x=200, y=110)

    # Timeout
    timeout_text = Text(config, width=17, height=1, bg=text_box_color, font='Anago-Book 10', fg='gray38')
    timeout_text.insert(END, config_readed[3])
    timeout_text.place(x=200, y=145)

    # --------------------------Tooltips------------------------------------------------------------------------------------

    tooltip_image = PhotoImage(file='tooltip.gif')
    tooltip1_x = 116
    tooltip1_y = 66
    tooltip1 = Label(config, width=18, height=18, bg="white", im=tooltip_image)
    tooltip1.place(x=tooltip1_x, y=tooltip1_y)
    tooltip2_x = 153
    tooltip2_y = 100
    tooltip2 = Label(config, width=18, height=18, bg="white", im=tooltip_image)
    tooltip2.place(x=tooltip2_x, y=tooltip2_y)
    tooltip3_x = 116
    tooltip3_y = 139
    tooltip3 = Label(config, width=18, height=18, bg="white", im=tooltip_image)
    tooltip3.place(x=tooltip3_x, y=tooltip3_y)
    tooltip4_x = 96
    tooltip4_y = 174
    tooltip4 = Label(config, width=18, height=18, bg="white", im=tooltip_image)
    tooltip4.place(x=tooltip4_x, y=tooltip4_y)

    browser_tooltip_image = PhotoImage(file='tooltip1.png')
    browser_tooltip = Label(config, width=115, height=20, im=browser_tooltip_image, bd=0)
    link_tooltip_image = PhotoImage(file='tooltip_link.png')
    link_tooltip = Label(config, width=129, height=20, im=link_tooltip_image, bd=0)
    timeout_tooltip_image = PhotoImage(file='tooltip_timeout.png')
    timeout_tooltip = Label(config, width=220, height=20, im=timeout_tooltip_image, bd=0)
    timer_tooltip_image = PhotoImage(file='tooltip_timer.png')
    timer_tooltip = Label(config, width=115, height=20, im=timer_tooltip_image, bd=0)

    tooltip1.bind("<Enter>", lambda a: browser_tooltip.place(x=tooltip1_x + 22, y=tooltip1_y - 15))
    tooltip1.bind("<Leave>", lambda a: browser_tooltip.place_forget())
    tooltip2.bind("<Enter>", lambda a: link_tooltip.place(x=tooltip2_x + 22, y=tooltip2_y - 15))
    tooltip2.bind("<Leave>", lambda a: link_tooltip.place_forget())
    tooltip3.bind("<Enter>", lambda a: timeout_tooltip.place(x=tooltip3_x + 22, y=tooltip3_y - 15))
    tooltip3.bind("<Leave>", lambda a: timeout_tooltip.place_forget())
    tooltip4.bind("<Enter>", lambda a: timer_tooltip.place(x=tooltip4_x + 22, y=tooltip4_y - 15))
    tooltip4.bind("<Leave>", lambda a: timer_tooltip.place_forget())

    config.mainloop()


def change_current_settings(link_text, variable, timeout_text, window):
    config_open = open('D:/testing/ddt_testing/config.ini', 'w')
    data = [
        "[Launch parameters]",
        "browser: " + variable.get(),
        "link:" + link_text.get("1.0", 'end-2c'),
        "expired_link:" + link_text.get("1.0", 'end-2c') + "/Login/logout.php?message=sessionExpired",
        "implicity_wait:" + timeout_text.get("1.0", 'end-2c')
    ]
    for string in data:
        config_open.write(string + "\n")
    config_open.close()
    window.destroy()


def close_settings(window):
    window.destroy()
