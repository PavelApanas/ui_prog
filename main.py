from PySide6.QtWidgets import QApplication,QWidget

from templates.window import Ui_Form


if __name__ == '__main__':
    import sys

    app = QApplication()
    form = Ui_Form()
    widget = QWidget()
    form.setupUi(widget)
    widget.show()
    sys.exit(app.exec())
