import tkinter as tk

from matplotlib.pyplot import grid

root=tk.Tk()
root.geometry("600x360")
root.title("登录页")


page=tk.Frame(root)
page.pack()

username=tk.StringVar()
password=tk.StringVar()

tk.Label(page).grid(row=0,column=0)

tk.Label(page,text="账号：").grid(row=1,column=1)
tk.Entry(page,textvariable=username).grid(row=1,column=2)

tk.Label(page,text="密码：").grid(row=2, column=1)
tk.Entry(page,textvariable=password).grid(row=2,column=2)

tk.Button(page,text="登录").grid(row=3,column=1,pady=20)
tk.Button(page, text="退出").grid(row=3,column=2,padx=40)

root.mainloop()