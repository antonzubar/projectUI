from tkinter.filedialog import *
from tkinter import ttk
import test2

root = Tk()

root.resizable(False, False)
root.title('TIAA Automation')
n = ttk.Notebook(root)
f1 = ttk.Frame(n)   # first page, which would get widgets gridded into it
f2 = ttk.Frame(n)   # second page
n.add(f1, text='One')
n.add(f2, text='Two')
n.place(x=0,y=0)
horiz_placemnt, vert_placemnt = test2.center(root)

im = PhotoImage(file='D:/testing/soft/2.gif')
label1 = Label(root)
label1["image"] = im
label1.place(x=0, y=0)

listbox1 = Listbox(root, width=42, height=20, selectmode=EXTENDED)

button_color = '#%02x%02x%02x' % (255, 184, 61)
button_font = 'Anago 12'
button_menu_width = 193  # 20
button_menu_height = 51  # 2

button1_image = PhotoImage(file='D:/testing/soft/run_test.gif')
button1 = Button(root, width=button_menu_width, height=button_menu_height, bg=button_color,
                 font=button_font, image=button1_image,
                 command=lambda: test2.run_test(listbox1))  # height = 3 == 65 pixels
button1.place(x=horiz_placemnt * 0.55, y=65)

button2_image = PhotoImage(file='D:/testing/soft/generate_report.gif')
button2 = Button(root, width=button_menu_width, height=button_menu_height, bg=button_color,
                 fg="white", image=button2_image,
                 command=test2.generate_report, font=button_font)
button2.place(x=horiz_placemnt * 0.55, y=121)

button3 = Button(root, width=button_menu_width, height=button_menu_height, bg=button_color,
                 fg="white",
                 command=test2.open_last_report, font=button_font)
button3.place(x=horiz_placemnt * 0.55, y=177)
button3_image = PhotoImage(file='D:/testing/soft/open_last_report.gif')
button3["image"] = button3_image

button4 = Button(root, text="Browse Your Tests", width=35, height=1,
                 command=lambda: test2.browsecsv(listbox1, vert_placemnt))
button4.place(x=0, y=vert_placemnt * 0.925)


root.mainloop()
