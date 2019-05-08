from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5.QtCore import Qt


class InformationWidget(QWidget):

    def __init__(self):
        super(InformationWidget, self).__init__()
        # 定义最外层布局：水平布局
        hbox = QHBoxLayout(self)
        # 定义左侧的groupbox
        groupbox = QGroupBox("数据库操作")
        # 创建一个垂直布局放到groupbox中
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)
        # 添加操作按钮
        querybutton1 = QPushButton("查看数据")
        # 添加信号和槽
        querybutton1.clicked.connect(self.query)
        vbox.addWidget(querybutton1)
        addbutton = QPushButton("增加一行")
        addbutton.clicked.connect(self.add)
        vbox.addWidget(addbutton)
        removebutton = QPushButton("删除一行")
        removebutton.clicked.connect(self.remove)
        vbox.addWidget(removebutton)
        exitbutton = QPushButton("退出")
        exitbutton.clicked.connect(QApplication.exit)
        vbox.addWidget(exitbutton)

        hbox.addWidget(groupbox)

        # 定义右侧的tableview
        self.tableview = QTableView()
        hbox.addWidget(self.tableview)

        # 创建db
        db = QSqlDatabase.addDatabase("QMYSQL")
        # 设置参数
        db.setHostName('localhost')
        db.setPort(3306)
        db.setUserName('stu')
        db.setPassword('123456')
        db.setDatabaseName('stusystem')
        # 打开连接
        db.open()
        # tabelemodel封装了增删改查的操作
        self.tableModel = QSqlTableModel(db=db)
        self.tableModel.setTable('student')
        # 设置表头
        self.tableModel.setHeaderData(0, Qt.Horizontal, '学号')
        self.tableModel.setHeaderData(1, Qt.Horizontal, '姓名')
        self.tableModel.setHeaderData(2, Qt.Horizontal, '年龄')
        self.tableModel.setHeaderData(3, Qt.Horizontal, '性别')

        # 将tablemodel与tableview进行绑定
        self.tableview.setModel(self.tableModel)

    def query(self):
        print("查看所有数据")
        self.tableModel.select()

    def add(self):
        print("添加一行")
        # 获取出一共有多少行
        count = self.tableModel.rowCount()
        # 需要在哪一行插入
        self.tableModel.insertRow(count)

    def remove(self):
        print("删除一行")
        # 找到用户选中的行
        index = self.tableview.currentIndex().row()
        self.tableModel.removeRow(index)

