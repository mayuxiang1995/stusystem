from PyQt5.QtWidgets import *
from PyQt5.Qt import QFont
from PyQt5.QtCore import pyqtSignal
from pymysql import connect


class LoginWidget(QWidget):
    # 定义一个信号
    login_success = pyqtSignal()

    def __init__(self):
        super(LoginWidget, self).__init__()

        # 首先定义一个水平布局
        hbox = QHBoxLayout(self)
        hbox.addStretch()
        # 定义一个垂直布局
        vbox = QVBoxLayout()
        hbox.addLayout(vbox)
        hbox.addStretch()
        q_label = QLabel('学生管理系统')
        font = QFont("微软雅黑", 30)
        font.setBold(True)
        q_label.setFont(font)
        vbox.addWidget(q_label)
        # 定义表单布局
        formlayout = QFormLayout()
        vbox.addLayout(formlayout)
        # 添加用户名:为什么用self，因为要用到次输入框
        self.user_nameEdit = QLineEdit()
        formlayout.addRow("用户名", self.user_nameEdit)
        self.user_passwordEdit = QLineEdit()
        self.user_passwordEdit.setEchoMode(QLineEdit.Password)
        formlayout.addRow("密码", self.user_passwordEdit)
        # 添加注册按钮
        button = QPushButton("登陆")
        button.clicked.connect(self.login_Success)
        formlayout.addRow("", button)

    def login_Success(self):
        # 获取登陆名
        name = self.user_nameEdit.text()
        # 获取登陆密码
        password = self.user_passwordEdit.text()
        # 创建连接
        conn = connect(host='localhost', port=3306, user='root', password='123456', database='stusystem')
        cursor = conn.cursor()
        sql = 'select * from user where username=%s and user_password=%s'
        ret= cursor.execute(sql, [name, password])
        if ret == 1:
            print('登陆成功')
            # 对外发送一个登陆成功的信号
            self.login_success.emit()
        else:
            print('登陆失败')
