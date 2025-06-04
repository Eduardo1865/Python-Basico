import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Teste")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("c:/Users/augus/Desktop/INATEL/estudando para vaga/introGUI/fota.jpg"))

        label = QLabel("House", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: blue;"
                    "background-color: #000000;"
                    "font-weight: bold;"
                    "font-style: italic;"
                    "text-decoration: underline;")
        label.setAlignment(Qt.AlignCenter)

        label2 = QLabel(self)
        label2.setGeometry(50, 100, 400, 400)  
        pixmap = QPixmap("c:/Users/augus/Desktop/INATEL/estudando para vaga/introGUI/Black_square.jpg")  
        label2.setPixmap(pixmap)
        label2.setScaledContents(True)  

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 