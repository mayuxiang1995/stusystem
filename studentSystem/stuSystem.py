from PyQt5.QtWidgets import *
import sys


class StuSystem:

    def __init__(self):
        # 创建QApplication
        app = QApplication(sys.argv)

        # 创建窗口
        mainwindow = QMainWindow()
        # 设置窗口大小
        mainwindow.setFixedSize(800, 400)
        # 添加菜单
        menuBar = mainwindow.menuBar()
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
        # 让窗口显示出来
        mainwindow.show()
        # 让应用一直出与运行状态
        sys.exit(app.exec())

    def show_login(self):
        print('打开登陆页面')

    def show_register(self):
        print('打开注册页面')


if __name__ == '__main__':
    StuSystem()
