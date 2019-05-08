from PyQt5.QtWidgets import *


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
        exitbutton.clicked.connect(self.exit)
        vbox.addWidget(exitbutton)

        hbox.addWidget(groupbox)
        # 定义右侧的tableview
        tableview = QTableView()
        hbox.addWidget(tableview)

    def query(self):
        pass

    def add(self):
        pass

    def remove(self):
        pass

    def exit(self):
        pass
