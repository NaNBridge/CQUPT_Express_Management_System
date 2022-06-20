# CQUPT_Express_Management_System
# 错取快递快递管理系统  


该项目用于参加重庆邮电大学数据库比赛.获得二等奖 
The project is used to participate in the database competition of Chongqing University of Posts and telecommunications

## 项目简介  
## Project Introduction
### 项目结构 
###  Project structure
项目的主体在文件夹CQUPTEMS_QT中.文件夹之所以叫这个名字是因为最初我们是想使用QT来做GUI但是QT的学习成本较高,所以就放弃了.但是最初的有个界面是用pyqt写的,代码在文件件Student-Record-Maintainer-In-PyQT5中(有两个文件夹,一个叫Student-Record-Maintainer-In-PyQT5,另一个叫Student Record Maintainer In Pyqt5,这两个文件夹并没有本质的区别.但是一个是GitHub上别人的源码,一个是我们自己在源码上做出的改动).  


The body of the project is in the folder CQUPTEMS_QT. The folder is called this because originally we wanted to use QT to do THE GUI but QT cost more to learn, so we gave up. But the original interface was written in pyqt, and the code was in the file piece Studio-Record-Maintainer-In-PyQT5 (there are two folders, one is called Studio-Record-Maintainer-In-PyQT5, and the other is called Student Record Maintainer In Pyqt5, and there is no essential difference between the two folders. But one is someone else's source code on GitHub, and the other is a change we've made on the source code ourselves).)  

本项目一共有三个主要界面:用户界面,快递驿站界面和人脸识别取件界面.这三个界面都非常丑,而且虽说是错取快递管理系统,但是这个我们作为核心的功能我们并没有完全实现,可以说这个项目只是徒有其名.各位看官就当看个笑话就好.  

The project has a total of three main interfaces: user interface, courier station interface and face recognition pickup interface. These three interfaces are very ugly, and although it is said that it is a wrong express delivery management system, but this function we as the core of us has not fully realized, it can be said that this project is just in vain. You guys just look at a joke.  


人脸识别界面在文件CQUPTEMS_QT\TKINTER\real_time_face_recongnition\face_recognition_all_function\gui.py中.其中的人脸图片需要各位自行添加.压缩裁剪后的图片放到CQUPTEMS_QT\TKINTER\img\face_pictures\fixed文件夹中就好.代码中的一些路径我图省事使用的是我自己电脑上的绝对路径,如果想要运行代码则需要各位自行修改.   


The face recognition interface is in the file CQUPTEMS_QTTKINTERreal_time_face_recongnitionface_recognition_all_functiongui.py. The face picture needs to be added by yourself. The compressed and cropped picture is placed in the CQUPTEMS_QTTKINTERimgface_picturesfixed folder. Some of the paths in the code I figure use the absolute path on my own computer, if you want to run the code you need to modify it yourself.  


用户界面在文件kawayiQuasimodo\yonghujiemian.py中.这部分代码不是我本人写的,是队友写的.命名极不规范,望见谅.其中连接数据库的部分需要根据自己的电脑来设置.哦对了,数据库我们使用的是mysql.  
涉及到数据库的语句在文件夹MySQL_query中,注意不要一次性全部执行,只需要执行那些创建表,修改表和创建触发器的语句即可,最好逐条执行.  
登录界面和注册界面在文件夹CQUPTEMS_QT\TKINTER\sign_in和文件夹CQUPTEMS_QT\TKINTER\sign_up中.  


快递驿站界面在CQUPTEMS_QT\Student-Record-Maintainer-In-PyQT5文件夹中.   


The user interface is in the file kawayiQuasimodoyonghujiemian.py. This part of the code was not written by myself, it was written by my teammates. The naming is extremely irregular, I hope to forgive. The part of the connection to the database needs to be set up according to your computer. Oh yes, the database we use is mysql.  
Statements involving databases are in the folder MySQL_query, be careful not to execute them all at once, only need to execute those statements that create tables, modify tables and create triggers, it is best to execute them one by one.  
The login screen and registration interface are in the folder CQUPTEMS_QTTKINTERsign_in and folder CQUPTEMS_QTTKINTERsign_up.  

The courier station interface is in the CQUPTEMS_QTStudent-Record-Maintainer-In-PyQT5 folder. 



### 项目依赖  
### Project dependencies  
本项目有近400个包,非常多,都已经在文件requirements.txt中声明.可以只挑选实际用到的包安装,如果嫌麻烦,可以在项目文件夹的控制台中直接运行  
``` python
pip install -r requirements.txt  
```  
This project has nearly 400 packages, very many, have been declared in the file requires .txt. You can only pick the packages that are actually used to install, if you are troublesome, you can run it directly in the console of the project folder  
``` python
pip install -r requirements.txt  
```   

### 其他说明  
### Additional Instructions   
项目中涉及一些隐私信息,例如照片什么的,都已将删除了.   
项目的文档都已经写好了,就是文件  说明文档\CQUPT错取快递管理系统.docx   
如果有需要可以直接用.学弟学妹们,你们要抄的话需要谨慎,至少需要等到2024年之后才可以抄.  
如果是要直接拿去参加数据库比赛的话,建议修改一下GUI的颜色之类的,项目名字也最好重新起一个,以免被发现.  


Some of the privacy information involved in the project, such as photos or whatever, will be deleted.   
The documentation of the project has been written, that is, the document description document  CQUPT mistaken express delivery management system .docx   
Can be used directly if needed. Students, if you want to copy it, you need to be cautious, at least until after 2024.  
If you want to take it directly to participate in the database competition, it is recommended to modify the color of the GUI or the like, and the project name is best restarted to avoid being discovered.  


### 总之,代码写的很垃圾.见谅见谅!  

哦,对了,参赛的文档是在  
说明文档\CQUPT错取快递管理系统.docx