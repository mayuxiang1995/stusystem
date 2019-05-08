from PyQt5.QtWidgets import *
import sys
from pymysql import connect


class StuSystem:

    def __init__(self):

        self.init_database()
        # 创建QApplication
        app = QApplication(sys.argv)

        # 创建窗口
        self.mainwindow = QMainWindow()
        # 设置窗口大小
        self.mainwindow.setFixedSize(800, 400)
        # 添加菜单
        menuBar = self.mainwindow.menuBar()
        menu = menuBar.addMenu("操作")
        # 给菜单添加动作
        login_action = QAction('登陆')
        # 给action绑定信号和槽
        login_action.triggered.connect(self.show_login)
        menu.addAction(login_action)
        # 给菜单添加动作
        register_action = QAction('注册')
        # 给action绑定信号和槽
        register_action.triggered.connect(self.show_register)
        menu.addAction(register_action)
        # 默认显示注册界面
        self.show_information()

        # 让窗口显示出来
        self.mainwindow.show()
        # 让应用一直出与运行状态
        sys.exit(app.exec())

    def show_information(self):
        from InformationWidget import InformationWidget
        informationWidget = InformationWidget()
        self.mainwindow.setCentralWidget(informationWidget)

    def show_login(self):
        from LoginWidget import LoginWidget
        loginwidget = LoginWidget()
        # 绑定信号和槽
        loginwidget.login_success.connect(self.show_information)
        self.mainwindow.setCentralWidget(loginwidget)

    def show_register(self):
        from RegisterWidget import RegisterWidget
        registerWidget = RegisterWidget()
        # 绑定信号和槽
        registerWidget.register_success.connect(self.show_login)
        self.mainwindow.setCentralWidget(registerWidget)

    def init_database(self):
        """
        项目初始：创建数据库，创建用户，只希望用户操作此数据库的内容，需要给用户限制权限
        :return: 
        """
        # 首先创建连接
        conn = connect(host="localhost", port=3306, user="root", password="123456")
        cursor = conn.cursor()
        # 首先创建数据库
        sql = 'create database if not exists stusystem'
        cursor.execute(sql)
        # 选择数据库
        cursor.execute('use stusystem')
        # 创建存储管理员账号信息的表
        sql = """
            create table if not exists user(
                id int primary key auto_increment,
                username varchar(20),
                user_password varchar(50),
                nickname varchar(20)
            )
        """
        cursor.execute(sql)
        # 创建存储学生信息的表
        sql = """
            create table if not exists student(
                id int primary key auto_increment,
                name varchar(20),
                age int,
                gender varchar(20)           
            )
        """
        cursor.execute(sql)
        # 释放资源
        cursor.close()
        conn.close()


if __name__ == '__main__':
    StuSystem()
