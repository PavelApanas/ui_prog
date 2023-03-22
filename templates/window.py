from threading import Thread
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont)
from PySide6.QtWidgets import (QCheckBox, QFrame, QGridLayout,
                               QPushButton, QVBoxLayout)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 380)
        Form.setMinimumSize(QSize(480, 320))
        Form.setMaximumSize(QSize(1280, 720))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(16)
        font.setStyleStrategy(QFont.PreferAntialias)
        Form.setFont(font)
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setStyleSheet(u"background-color: #457b9d;")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QCheckBox {\n"
"font-family: \"Arial\";\n"
"font-size: 14px;\n"
"font-style: bold;\n"
"\n"
"}\n"
"QPushButton{\n"
"bacground-color: #a8dadc;\n"
"border: solid;\n"
"border-width: 2px;\n"
"vorder-color: #1d3557;\n"
"border-radius: 25px;\n"
"height: 50px;\n"
"font-family: \"Arial\";\n"
"font-size: 40px;\n"
"font-style: bold;\n"
"color: #B22222;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_4 = QCheckBox(self.frame)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout.addWidget(self.checkBox_4, 1, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.frame)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 1)

        self.checkbox_data = {
            '202': self.checkBox,
            '154': self.checkBox_2,
            '194': self.checkBox_3,
            '198': self.checkBox_4,
        }

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self._check_data)

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0411\u0435\u043b\u043f\u043e\u0447\u0442\u0430", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u043f\u043b\u0430\u0442\u0430 \u043f\u0435\u043d\u0441\u0438\u0439 \u0438 \u043f\u043e\u0441\u043e\u0431\u0438\u0439", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0434\u0435\u043d\u0435\u0436\u043d\u044b\u0439 \u043f\u0435\u0440\u0435\u0432\u043e\u0434", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u0435\u043c \u043f\u043b\u0430\u0442\u0435\u0436\u0435\u0439", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u043a\u0440\u0435\u0434\u0438\u0442 \u041e\u0410\u041e \"\u0411\u0435\u043b\u0430\u0440\u0443\u0441\u0431\u0430\u043d\u043a\"", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c", None))
    # retranslateUi

    def _check_data(self):
        from utils import get_response
        res = ''
        for key, value in self.checkbox_data.items():
            if value.isChecked():
                res += f'&services[]={key}'

        thread = Thread(target=get_response, args=(res, ))
        thread.start()