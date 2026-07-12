from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv) #start Qt app
    window = MainWindow() #create window
    window.show() #visible
    app.exec() #keeps window open, listen for clicks

    