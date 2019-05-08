from PyQt5.QtWidgets import *
from PyQt5.Qt import QFont
from PyQt5.QtCore import pyqtSignal
from pymysql import connect


class RegisterWidget(QWidget):
    # 创建一个信号
    register_success = pyqtSignal()

    def __init__(self):
        super(RegisterWidget, self).__init__()

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
        self.user_nicknameEdit = QLineEdit()
        formlayout.addRow("昵称", self.user_nicknameEdit)
        # 添加注册按钮
        button = QPushButton("注册")
        button.clicked.connect(self.register)
        formlayout.addRow("", button)

    def register(self):
        # 获取注册的用户名
        user_name = self.user_nameEdit.text()
        # 获取注册的密码
        user_password = self.user_passwordEdit.text()
        # 获取注册的昵称
        user_nickname = self.user_nicknameEdit.text()
        # 连接数据库将信息传入
        conn = connect(host='localhost', port=3306, user='root', password='123456', database='stusystem')
        cursor = conn.cursor()
        sql = 'insert into user values(null,%s,%s,%s)'
        ret = cursor.execute(sql, [user_name, user_password, user_nickname])
        if ret == 1:
            print("注册成功")
            # 对外发送一个注册成功的信号：
            self.register_success.emit()
        else:
            print('注册失败')
        conn.commit()
        cursor.close()
        conn.close()

