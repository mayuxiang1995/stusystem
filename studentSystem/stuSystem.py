from PyQt5.QtWidgets import *
import sys


class StuSystem:

    def __init__(self):
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
        self.show_register()

        # 让窗口显示出来
        self.mainwindow.show()
        # 让应用一直出与运行状态
        sys.exit(app.exec())

    def show_information(self):
        print('显示信息')

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


if __name__ == '__main__':
    StuSystem()
