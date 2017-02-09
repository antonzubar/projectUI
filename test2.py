import subprocess, psutil
from tkinter.filedialog import *
from tkinter import ttk
import xlrd, xlwt

# -------------------------------------------First Tab Functions--------------------------------------------------------
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
    elif window == "generating":
        horiz_placemnt = w / 11
        vert_placemnt = h / 7
    elif window == "commissions_panel":
        horiz_placemnt = w / 4.75
        vert_placemnt = h / 3.55
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
    generating_window = Toplevel()
    generating_window.overrideredirect(1)  # - убирает все элементы окна
    center(generating_window, "generating")
    generating_window.deiconify()
    generating_window.grab_set()
    generating_window.focus_force()
    generating_window.title('Generating Report')
    generating_window.resizable(False, False)
    generating_window.configure(bg="white")
    im2 = PhotoImage(file='D:/testing/soft/sciv/animation1.gif')

    def animation():
        processes = psutil.pids()
        if a not in processes:
            generating_window.destroy()
        i = 40
        label2.after(i, lambda: im2.configure(format="gif -index 0"))
        label2.after(i * 2, lambda: im2.configure(format="gif -index 1"))
        label2.after(i * 3, lambda: im2.configure(format="gif -index 2"))
        label2.after(i * 4, lambda: im2.configure(format="gif -index 3"))
        label2.after(i * 5, lambda: im2.configure(format="gif -index 4"))
        label2.after(i * 6, lambda: im2.configure(format="gif -index 5"))
        label2.after(i * 7, lambda: im2.configure(format="gif -index 6"))
        label2.after(i * 8, lambda: im2.configure(format="gif -index 7"))
        label2.after(i * 9, lambda: im2.configure(format="gif -index 8"))
        label2.after(i * 10, lambda: im2.configure(format="gif -index 9"))
        label2.after(i * 11, lambda: im2.configure(format="gif -index 10"))
        label2.after(i * 12, lambda: im2.configure(format="gif -index 11"))
        label2.after(i * 13, lambda: im2.configure(format="gif -index 12"))
        label2.after(i * 14, lambda: im2.configure(format="gif -index 13"))
        label2.after(i * 15, lambda: im2.configure(format="gif -index 14"))
        label2.after(i * 16, lambda: im2.configure(format="gif -index 15"))
        label2.after(i * 17, lambda: im2.configure(format="gif -index 16"))
        label2.after(i * 18, lambda: im2.configure(format="gif -index 17"))
        label2.after(i * 19, lambda: im2.configure(format="gif -index 18"))
        label2.after(i * 20, lambda: im2.configure(format="gif -index 19"))
        label2.after(i * 21, lambda: im2.configure(format="gif -index 20"))
        label2.after(i * 22, lambda: im2.configure(format="gif -index 21"))
        label2.after(i * 23, lambda: im2.configure(format="gif -index 22"))
        label2.after(i * 24, lambda: im2.configure(format="gif -index 23"))
        label2.after(i * 25, lambda: im2.configure(format="gif -index 24"))
        label2.after(i * 26, lambda: im2.configure(format="gif -index 25"))
        label2.after(i * 27, lambda: im2.configure(format="gif -index 26"))
        label2.after(i * 28, lambda: im2.configure(format="gif -index 27"))
        label2.after(i * 29, lambda: im2.configure(format="gif -index 28"))
        label2.after(i * 30, lambda: im2.configure(format="gif -index 29"))
        label2.after(i * 31, lambda: im2.configure(format="gif -index 30"))
        label2.after(i * 32, lambda: im2.configure(format="gif -index 31"))
        label2.after(i * 33, lambda: im2.configure(format="gif -index 32"))
        label2.after(i * 34, lambda: im2.configure(format="gif -index 33"))
        label2.after(i * 35, lambda: im2.configure(format="gif -index 34"))
        label2.after(i * 36, lambda: im2.configure(format="gif -index 35"))
        label2.after(i * 37, lambda: im2.configure(format="gif -index 36"))
        label2.after(i * 38, lambda: im2.configure(format="gif -index 37"))
        label2.after(i * 39, lambda: im2.configure(format="gif -index 38"))
        label2.after(i * 40, lambda: im2.configure(format="gif -index 39"))
        label2.after(i * 41, lambda: im2.configure(format="gif -index 40"))
        label2.after(i * 42, lambda: im2.configure(format="gif -index 41"))
        label2.after(i * 43, lambda: im2.configure(format="gif -index 42"))
        label2.after(i * 44, lambda: im2.configure(format="gif -index 43"))
        label2.after(i * 45, lambda: im2.configure(format="gif -index 44"))
        label2.after(i * 46, lambda: im2.configure(format="gif -index 45"))
        label2.after(i * 47, lambda: im2.configure(format="gif -index 46"))
        label2.after(i * 48, lambda: im2.configure(format="gif -index 47"))
        label2.after(i * 49, lambda: im2.configure(format="gif -index 48"))
        label2.after(i * 50, lambda: im2.configure(format="gif -index 49"))
        label2.after(i * 50, lambda: animation())

    cmd = 'cd /d d:/testing/ddt_testing' + ' & ' + 'D:/Automation/bin/allure generate D:/testing/ddt_testing/tests/rep'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    a = proc.pid

    label2 = Label(generating_window, image=im2, bg="white")
    label2.place(x=3, y=0)
    button1 = Button(generating_window, command=animation())

    generating_window.mainloop()


def open_last_report():
    cmd = 'd:/testing/ddt_testing/allure-report/index.html'
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


# ---------------------------------------------Second Tab Functions-----------------------------------------------------
def set_commissions():
    commissions_panel = Toplevel()
    center(commissions_panel, "commissions_panel")
    commissions_panel.deiconify()
    commissions_panel.grab_set()
    commissions_panel.focus_force()
    commissions_panel.resizable(False, False)

    # Constants
    main_orange = '#%02x%02x%02x' % (255, 184, 61)
    font = 'Anago 10 bold'
    text_box_color = 'antique white'
    x_placement = 127
    y_placement = 100
    x_step = 52
    y_step = 30

    n = ttk.Notebook(commissions_panel)
    stock_frame = ttk.Frame(n)  # first page, which would get widgets gridded into it
    option_frame = ttk.Frame(n)  # second page
    mf_frame = ttk.Frame(n)  # third page
    n.add(stock_frame, text='Stocks')
    n.add(option_frame, text='Options')
    n.add(mf_frame, text='Mutual Funds')
    n.place(x=0, y=0)

    # Create style of tabs
    ttk.Style().configure("TNotebook", background=main_orange)
    ttk.Style().map("TNotebook.Tab", background=[('selected', "grey")], foreground=[("selected", "grey")])
    ttk.Style().configure("TNotebook.Tab", background="white", foreground="DarkGoldenrod4")

    im = PhotoImage(file='D:/testing/soft/commission_of_stock.png')
    label1 = Label(stock_frame, image=im)
    label1.pack()
    im1 = PhotoImage(file='D:/testing/soft/commission_of_options.png')
    label2 = Label(option_frame, image=im1)
    label2.pack()
    im2 = PhotoImage(file='D:/testing/soft/commission_of_mutual_funds.png')
    label3 = Label(mf_frame, image=im2)
    label3.pack()

    class StockCommissionTextbox():  # textbox class
        def put_textbox(self, xx, yy, i):
            commission_text = Text(stock_frame, width=4, height=1, bg=text_box_color, font='Anago-Book 11',
                                   fg='gray38')
            # select commissions from excel
            stock_sheet = xlrd.open_workbook('D:/testing/ddt_testing/Data for testing/StocksTestData.xlsx')
            first_stock_sheet = stock_sheet.sheet_by_index(0)
            commissions = first_stock_sheet.row_values(i + 1)[1]
            commission_text.insert(END, commissions)
            commission_text.place(x=xx, y=yy)

    class OptionsCommissionTextbox():  # textbox class
        def put_textbox(self, xx, yy, i):
            commission_text = Text(option_frame, width=4, height=1, bg=text_box_color, font='Anago-Book 9',
                                   fg='gray38')
            # select commissions from excel
            options_sheet = xlrd.open_workbook('D:/testing/ddt_testing/Data for testing/OptionsTestData.xlsx')
            first_options_sheet = options_sheet.sheet_by_index(0)
            commissions = first_options_sheet.row_values(i + 1)[1]
            if (4<i<10) or (14<i<20):
                commissions = first_options_sheet.row_values(i-5 + 1)[2]
            if i>10 and (9<i<14) and (19<i<24):
                commissions = first_options_sheet.row_values(i - 5)[1]
            commission_text.insert(END, commissions)
            commission_text.place(x=xx, y=yy)

    class MFCommissionTextbox():  # textbox class
        def put_textbox(self, xx, yy):
            commission_text = Text(mf_frame, width=4, height=1, bg=text_box_color, font='Anago-Book 11',
                                   fg='gray38')
            commission_text.insert(END, "5.95")
            commission_text.place(x=xx, y=yy)

# -------------------------------------------------Stock tab -----------------------------------------------------------

    textbox_list = []
    count = 0
    xx = x_placement
    yy = y_placement
    for i in range(0, 25):
        textbox_object = StockCommissionTextbox()
        textbox_list.append(textbox_object)
        if count < 5:
            textbox_list[i].put_textbox(xx, yy + (y_step * count), i)
            count += 1
        else:
            count = 1
            xx = xx + x_step
            textbox_list[i].put_textbox(xx, yy, i)

    ok_st = Button(stock_frame, text="  Save  ", bg=main_orange, fg='white', font=font, bd=0,
                   command=lambda: commissions_panel.destroy())
    ok_st.place(x=146, y=250)
    ok_st.bind("<Enter>", lambda a: ok_st.configure(bg="burlywood1"))
    ok_st.bind("<Leave>", lambda a: ok_st.configure(bg=main_orange))

    cancel_st = Button(stock_frame, text="Cancel", bg="gray64", fg='white', font=font, bd=0,
                       command=lambda: commissions_panel.destroy())
    cancel_st.place(x=200, y=250)
    cancel_st.bind("<Enter>", lambda a: cancel_st.configure(bg="gray79"))
    cancel_st.bind("<Leave>", lambda a: cancel_st.configure(bg="gray64"))

# -------------------------------------------------Options tab ---------------------------------------------------------

    textbox_list = []
    count = 0
    count2 = 0
    xx = x_placement - 55
    yy = y_placement
    for i in range(0, 25):
        textbox_object = OptionsCommissionTextbox()
        textbox_list.append(textbox_object)
        if count < 5:
            textbox_list[i].put_textbox(xx, yy + (y_step * count), i)
            count += 1
        elif count == 5:
            if count2 == 10:
                xx = xx + x_step / 1.3
                textbox_list[i].put_textbox(xx, yy, i)
                count2 = 0
                count = 1
            else:
                xx = xx + x_step / 2
                textbox_list[i].put_textbox(xx, yy, i)
                count = 1
        count2 += 1
    ok_opt = Button(option_frame, text="  Save  ", bg=main_orange, fg='white', font=font, bd=0,
                    command=lambda: commissions_panel.destroy())
    ok_opt.place(x=146, y=250)
    ok_opt.bind("<Enter>", lambda a: ok_opt.configure(bg="burlywood1"))
    ok_opt.bind("<Leave>", lambda a: ok_opt.configure(bg=main_orange))

    cancel_opt = Button(option_frame, text="Cancel", bg="gray64", fg='white', font=font, bd=0,
                        command=lambda: commissions_panel.destroy())
    cancel_opt.place(x=200, y=250)
    cancel_opt.bind("<Enter>", lambda a: cancel_opt.configure(bg="gray79"))
    cancel_opt.bind("<Leave>", lambda a: cancel_opt.configure(bg="gray64"))

# -------------------------------------------------Mutual Funds tab ----------------------------------------------------

    textbox_list = []
    count = 0
    count2 = 0
    xx = x_placement - 44
    yy = y_placement
    for i in range(0, 30):
        textbox_object = MFCommissionTextbox()
        textbox_list.append(textbox_object)
        if count < 5:
            textbox_list[i].put_textbox(xx, yy + (y_step * count))
            count += 1
        elif count == 5:
            if count2 == 15:
                xx = xx + 1.3 * x_step
                textbox_list[i].put_textbox(xx, yy)
                count2 = 0
                count = 1
            else:
                xx = xx + x_step / 1.1
                textbox_list[i].put_textbox(xx, yy)
                count = 1
        count2 += 1
    ok_mf = Button(mf_frame, text="  Save  ", bg=main_orange, fg='white', font=font, bd=0,
                   command=lambda: commissions_panel.destroy())
    ok_mf.place(x=146, y=250)
    ok_mf.bind("<Enter>", lambda a: ok_mf.configure(bg="burlywood1"))
    ok_mf.bind("<Leave>", lambda a: ok_mf.configure(bg=main_orange))

    cancel_mf = Button(mf_frame, text="Cancel", bg="gray64", fg='white', font=font, bd=0,
                       command=lambda: commissions_panel.destroy())
    cancel_mf.place(x=200, y=250)
    cancel_mf.bind("<Enter>", lambda a: cancel_mf.configure(bg="gray79"))
    cancel_mf.bind("<Leave>", lambda a: cancel_mf.configure(bg="gray64"))

    commissions_panel.mainloop()
