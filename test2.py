import subprocess
from tkinter.filedialog import *

global path_to_test


def browsecsv(listbox1, vert_placemnt):
    global path_to_test
    path_to_test = askdirectory()
    a = os.listdir(path_to_test)
    for i in a:
        if i == ".cache" or i == "__pycache__" or i == "rep" or i == "BaseTestCase.py" or i == "ConfigParser.py" or i == "GetPage.py":
            continue
        else:
            listbox1.insert(END, i)

    listbox1.place(x=0, y=0)
    scrollbar = Scrollbar(listbox1)
    scrollbar.place(x=236, y=0, height=vert_placemnt * 0.89)
    scrollbar['command'] = listbox1.yview
    listbox1['yscrollcommand'] = scrollbar.set


def center(toplevel):  # центрирует появление окна
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    horiz_placemnt = w / 3
    vert_placemnt = h / 3
    toplevel.geometry(
        "%dx%d+%d+%d" % (horiz_placemnt, vert_placemnt, (w - horiz_placemnt) / 2, (h - vert_placemnt) / 2))
    return horiz_placemnt, vert_placemnt


def run_test(listbox1):
    global path_to_test
    selected_item = listbox1.get(ACTIVE)
    cmd = 'cd /d ' + path_to_test + ' & ' + 'py.test ' + selected_item + ' -s --alluredir rep'
    subprocess.Popen(cmd, shell=True)


def generate_report():
    cmd = 'cd /d d:/Automation/bin' + ' & ' + 'allure generate D:/testing/ddt_testing/tests/rep' + ' & ' + 'allure report open'
    subprocess.Popen(cmd, shell=True)


def open_last_report():
    cmd = 'cd /d d:/Automation/bin' + ' & ' + 'allure report open'
    subprocess.Popen(cmd, shell=True)
