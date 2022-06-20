
from cmath import pi
from pathlib import Path

from tkinter import *
import tkinter.messagebox as mgbox
from pyrsistent import b
import pymysql
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from cmath import pi
from pathlib import Path

from tkinter import *
import tkinter.messagebox as mgbox
from pyrsistent import b
import pymysql
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from CQUPTEMS_QT.TKINTER.sign_up import zhuce
from cmath import pi
from pathlib import Path
from kawayiQuasimodo import yonghujiemian
from tkinter import *
import tkinter.messagebox as mgbox
from pyrsistent import b
import pymysql
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage




def run_sign_in_page():

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("1024x633")
    window.configure(bg = "#FFFFFF")

    #todo:定义登录时需要执行的函数
    def login():
        #获取输入的密码和学号
        password=entry_password.get()
        student_id=entry_student_id.get()
        #连接数据库
        myconn=pymysql.connect(host="localhost",
                            user="root",
                            password="200149",
                            database="cquptems_db",
                            port=3306,charset="utf8")
        #获取游标对象
        cur = myconn.cursor()
        #定义SQL语句
        sql_sentence=f"""
        SELECT user_student_ID,user_password
        FROM Users
        WHERE user_student_ID='{student_id}' AND user_password='{password}';
        """
        #执行SQL语句
        excute_result = cur.execute(sql_sentence)
        print(excute_result)
        #如果数据库中存在输入的信息则提示登录成功
        if excute_result==1:
            mgbox.showinfo(title="登录成功",
                        message="欢迎登录!")
            studentnumber = student_id
            window.destroy()
            yonghujiemian.run_yonghujiemian_page(studentnumber)

        else:
            mgbox.showwarning(title="登录失败",
                            message="登录失败!\n请重新尝试")
        #关闭连接
        myconn.close()    
        pass



    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 633,
        width = 1024,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        512.0,
        634.0,
        fill="#FFFFFF",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        256.0,
        317.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        512.0,
        0.0,
        1024.0,
        634.0,
        fill="#C8A2D3",
        outline="")

    canvas.create_text(
        599.0,
        409.0,
        anchor="nw",
        text="密码",
        fill="#000000",
        font=("Inter Regular", 24 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        817.5,
        419.0,
        image=entry_image_1
    )
    entry_password = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_password.place(
        x=698.0,
        y=396.0,
        width=239.0,
        height=44.0
    )

    canvas.create_text(
        688.0,
        157.0,
        anchor="nw",
        text="欢迎登录",
        fill="#000000",
        font=("Inter", 40 * -1)
    )

    canvas.create_text(
        599.0,
        284.0,
        anchor="nw",
        text="学号",
        fill="#000000",
        font=("Inter Regular", 24 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        817.5,
        294.0,
        image=entry_image_2
    )
    entry_student_id = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_student_id.place(
        x=698.0,
        y=271.0,
        width=239.0,
        height=44.0
    )
#
    canvas.create_text(
        677.0,
        28.0,
        anchor="nw",
        text="菜鸟小邮--错取快递管理系统",
        fill="#000000",
        font=("Inter", 14 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_login = Button(
        #image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=login,
        relief="flat",
        bg="#1eb9fa",
        text="登录",
        fg="#fafafa"
    )
    button_login.place(
        x=755.0,
        y=460.0,
        width=81.0,
        height=45.0
    )


    def zhuanzhuce():
        window.destroy()
        zhuce.run_sign_up_page()

    canvas.create_text(
        700.0,
        545.0,
        anchor="nw",
        text="还没有账号？",
        fill="#000000",
        font=("Inter", 20 * -1)
    )
    sign_up_button = Button(
        # image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=zhuanzhuce,
        relief="flat",
        text="注册",
        bg="#54db79"
    )
    sign_up_button.place(
        x=820.0,
        y=530.0,
        width=82.0,
        height=42.0
    )


    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    run_sign_in_page()