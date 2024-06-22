from PyQt5.QtWidgets import *


# from PyQt5.QtGui import QFont


def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(500, 500, 500, 500)
    window.setWindowTitle("Universal Interface")

    button = QPushButton(window)
    button.setText("AAA")
    button.move(100, 70)

    layout = QVBoxLayout()
    label = QLabel("Text")
    layout.addWidget(label)
    window.setLayout(layout)

    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
