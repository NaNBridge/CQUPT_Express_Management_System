from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Text, Button, PhotoImage

import pymysql


def run_yonghujiemian_page(studentnumber):

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    windownew = Tk()

    windownew.geometry("1024x633")
    windownew.configure(bg = "#FFFFFF")

    #TODO:定义登录时需要执行的函数

    def chaxunweiqu():
        #获取输入的密码和学号
        # password=entry_password.get()
        # student_id=entry_student_id.get()
        student_id = studentnumber
        #连接数据库
        myconn=pymysql.connect(host="localhost",
                            user="root",
                            password="liang1925tt",
                            database="cquptems_db",
                            port=3306,charset="utf8")
        #获取游标对象
        cur = myconn.cursor()
        #定义SQL语句
        sql_sentence=f"""

        Select express_station.package_ID,express_station.import_time 
        From express_station,users 
        where 
        users.user_student_ID = '{student_id}' and express_station.pickup_user_student_ID = '{student_id}' and express_station.error_status = 0;
        
        """
        # Select
        # packages.package_ID, packages.shipping_address
        # From
        # packages, users
        # where
        # packages.package_owner_phone_number = users.user_phone_number and users.user_student_ID = '{student_id}';
        # SELECT user_student_ID,user_password
        # FROM Users
        # WHERE user_student_ID='{student_id}'
        #执行SQL语句
        excute_result = cur.execute(sql_sentence)
        rows = cur.fetchall()
        new_text = ""
        for row in rows:
            new_text += str(row)
        xianshi = Text(
            windownew,
            width=500,
        )
        for row in rows:
            xianshi.insert("end",str(row)[2:51] + "\n")
            xianshi.insert("end", str(row)[54:-1] + "\n")
            xianshi.insert("end", "\n")
        new_text = ""
        xianshi.place(
            x=150.0,
            y=150.0,
            width=600.0,
            height=800.0
        )


        xianshi.place(
            x=60.0,
            y=60.0,
            width=480.0,
            height=520.0
        )
        gundongy = Scrollbar(xianshi, orient=VERTICAL)
        gundongy.pack(side=RIGHT, fill=Y)
        gundongy.config(command = xianshi.yview)

        print(excute_result)

        #如果数据库中存在输入的信息则提示登录成功
        # if excute_result==1:
        #     mgbox.showinfo(title="登录成功",
        #                 message="欢迎登录!")
        # else:
        #     mgbox.showwarning(title="登录失败",
        #                     message="登录失败!\n请重新尝试")
        #关闭连接
        myconn.close()
        pass

    def chaxunyiqu():
        student_id = studentnumber
        myconn = pymysql.connect(host="localhost",
                                 user="root",
                                 password="liang1925tt",
                                 database="cquptems_db",
                                 port=3306, charset="utf8")
        cur = myconn.cursor()
        sql_sentence = f"""

        Select express_station.package_ID,express_station.import_time 
        From express_station,users 
        where 
        users.user_student_ID = '{student_id}' and express_station.pickup_user_student_ID = '{student_id}' and express_station.error_status = 1;
        """
        excute_result = cur.execute(sql_sentence)
        rows = cur.fetchall()
        print(rows)
        rows = cur.fetchall()
        new_text = ""
        for row in rows:
            new_text += str(row)
        xianshi = Text(
            windownew,
            width=500,
        )
        for row in rows:
            xianshi.insert("end", str(row)[2:51] + "\n")
            xianshi.insert("end", str(row)[54:-1] + "\n")
            xianshi.insert("end", "\n")
        new_text = ""
        xianshi.place(
            x=150.0,
            y=150.0,
            width=600.0,
            height=800.0
        )

        xianshi.place(
            x=60.0,
            y=60.0,
            width=480.0,
            height=520.0
        )
        gundongy = Scrollbar(xianshi, orient=VERTICAL)
        gundongy.pack(side=RIGHT, fill=Y)
        gundongy.config(command=xianshi.yview)
        print(excute_result)
        myconn.close()
        pass

    def chaxuncuoqu():
        student_id = studentnumber
        myconn = pymysql.connect(host="localhost",
                                 user="root",
                                 password="liang1925tt",
                                 database="cquptems_db",
                                 port=3306, charset="utf8")
        cur = myconn.cursor()
        sql_sentence = f"""

        Select express_station.package_ID,express_station.import_time 
        From express_station,users 
        where 
        users.user_student_ID = '{student_id}' and express_station.pickup_user_student_ID = '{student_id}' and express_station.error_status = 2;
        """
        excute_result = cur.execute(sql_sentence)
        rows = cur.fetchall()
        print(rows)
        print(excute_result)
        myconn.close()
        pass

    def chaxunqujianma():
        student_id = studentnumber
        myconn = pymysql.connect(host="localhost",
                                 user="root",
                                 password="liang1925tt",
                                 database="cquptems_db",
                                 port=3306, charset="utf8")
        cur = myconn.cursor()
        sql_sentence = f"""

        Select unique_pickup_code 
        From users 
        where 
        users.user_student_ID = '{student_id}';
        """
        excute_result = cur.execute(sql_sentence)
        rows = cur.fetchall()
        new_text = ""
        for row in rows:
            new_text += str(row)[2:-3]
        xianshi = Message(
            windownew,
            anchor = "nw",
            justify = "left",
            width=500,
            text = new_text,
        )
        new_text = ""
        xianshi.place(
            x = 760.0,
            y=475.0,
            width=200.0,
            height=50.0
        )
        print(rows)

        print(excute_result)
        myconn.close()
        pass


    canvas = Canvas(
        windownew,
        bg = "#FFFFFF",
        height = 633,
        width = 1024,
        bd = 0,
        highlightthickness = 2,
        relief = "ridge"
    )
    image_image_1 = PhotoImage(
        file=relative_to_assets("pinkcloud4.png"))
    image_1 = canvas.create_image(
        0.0,
        0.0,
        image=image_image_1
    )
    canvas.place(x = 0, y = 0)

    # canvas.create_rectangle(
    #     0.0,
    #     0.0,
    #     512.0,
    #     634.0,
    #     fill="#FFFFFF",
    #     outline="")

    # image_image_1 = PhotoImage(
    #     file=relative_to_assets("cy.png"))
    # image_1 = canvas.create_image(
    #     256.0,
    #     317.0,
    #     image=image_image_1
    # )

    canvas.create_rectangle(
        600.0,
        0.0,
        1024.0,
        634.0,
        fill="#C8A2D3",
        outline="")

    # canvas.create_rectangle(
    #     750.0,
    #     0.0,
    #     1024.0,
    #     634.0,
    #     fill="#C8A2D3",
    #     outline="")

    # canvas.create_text(
    #     744.0,
    #     529.0,
    #     anchor="nw",
    #     text="登录",
    #     fill="#FFFFFF",
    #     font=("Inter Regular", 24 * -1)
    # )

    canvas.create_text(
        630.0,
        310.0,
        anchor="nw",
        text="已取快递",
        fill="#000000",
        font=("Inter Regular", 24 * -1)
    )
    canvas.create_text(
        630.0,
        220.0,
        anchor="nw",
        text="未取快递",
        fill="#000000",
        font=("Inter Regular", 24 * -1)
    )
    canvas.create_text(
        630.0,
        400.0,
        anchor="nw",
        text="错取快递",
        fill="#000000",
        font=("Inter Regular", 24 * -1)
    )

    # entry_image_1 = PhotoImage(
    #     file=relative_to_assets("entry_1.png"))
    # entry_bg_1 = canvas.create_image(
    #     850.5,
    #     419.0,
    #     image=entry_image_1
    # )
    # entry_password = Entry(
    #     bd=0,
    #     bg="#FFFFFF",
    #     highlightthickness=0
    # )
    # entry_password.place(
    #     x=740.0,
    #     y=396.0,
    #     width=239.0,
    #     height=44.0
    # )

    canvas.create_text(
        760.0,
        120.0,
        anchor="nw",
        text="欢迎    " + studentnumber,
        #name

        fill="#000000",
        font=("Inter", 20 * -1)
    )




    # entry_image_2 = PhotoImage(
    #     file=relative_to_assets("entry_2.png"))
    # entry_bg_2 = canvas.create_image(
    #     817.5,
    #     294.0,
    #     image=entry_image_2
    # )
    # entry_student_id = Entry(
    #     bd=0,
    #     bg="#FFFFFF",
    #     highlightthickness=0
    # )
    # entry_student_id.place(
    #     x=698.0,
    #     y=271.0,
    #     width=239.0,
    #     height=44.0
    # )
#

    canvas.create_text(
        730.0,
        28.0,
        anchor="nw",
        text="菜鸟小邮--错取快递管理系统",
        fill="#000000",
        font=("Inter", 14 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_chaxun1 = Button(
        #image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=chaxunweiqu,
        relief="flat",
        bg="#1eb9fa",
        text="查询",
        fg="#fafafa"
    )
    button_chaxun1.place(
        x=800.0,
        y=215.0,
        width=81.0,
        height=45.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_chaxun2 = Button(
        # image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=chaxunyiqu,
        relief="flat",
        bg="#1eb9fa",
        text="查询",
        fg="#fafafa"
    )
    button_chaxun2.place(
        x=800.0,
        y=300.0,
        width=81.0,
        height=45.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_chaxun3 = Button(
        # image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=chaxuncuoqu,
        relief="flat",
        bg="#1eb9fa",
        text="查询",
        fg="#fafafa"
    )
    button_chaxun3.place(
        x=800.0,
        y=395.0,
        width=81.0,
        height=45.0
    )

    new_text = ""
    xianshiqujianma = Message(
        windownew,
        anchor="nw",
        justify="left",
        width=500,
        text=new_text,
    )

    xianshiqujianma.place(
        x=760.0,
        y=475.0,
        width=200.0,
        height=50.0
    )
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_chaxun4 = Button(
        # image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=chaxunqujianma,
        relief="flat",
        bg="#1eb9fa",
        text="显示取件码",
        fg="#fafafa"
    )
    button_chaxun4.place(
        x=630.0,
        y=475.0,
        width=81.0,
        height=45.0
    )




    windownew.resizable(False, False)
    windownew.mainloop()

