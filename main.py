import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QSize
from pet import DesktopPet
from settings import SettingsWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print("初始化 MainWindow")
        self.initUI()

    def initUI(self):
        print("初始化 UI")
        # 設置窗口屬性：無邊框、透明背景、始終置頂
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # 設置窗口大小為全屏
        self.setGeometry(0, 0, QApplication.desktop().screenGeometry().width(),
                         QApplication.desktop().screenGeometry().height())

        # 創建桌面寵物實例
        self.pet = DesktopPet(self)
        self.pet.show()
        print("寵物已顯示")

        # 創建系統托盤圖標
        self.create_tray_icon()

    def create_tray_icon(self):
        icon_path = 'icon.png'
        if not os.path.exists(icon_path):
            print(f"警告：找不到圖標文件 '{icon_path}'，使用替代圖標")
            icon = self.create_fallback_icon()
        else:
            icon = QIcon(icon_path)
            if icon.isNull():
                print(f"警告：無法加載圖標文件 '{icon_path}'，使用替代圖標")
                icon = self.create_fallback_icon()

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(icon)
        self.tray_menu = QMenu()
        self.tray_menu.addAction('設定', self.open_settings)
        self.tray_menu.addAction('退出', self.close)
        self.tray_icon.setContextMenu(self.tray_menu)
        
        if not self.tray_icon.isSystemTrayAvailable():
            print("錯誤：系統托盤不可用")
            QMessageBox.warning(self, "錯誤", "系統托盤不可用")
            return

        self.tray_icon.show()
        print("系統托盤圖標已顯示")

    def create_fallback_icon(self):
        # 創建一個帶有文字的彩色圖標
        pixmap = QPixmap(32, 32)
        pixmap.fill(QColor(255, 255, 0))  # 黃色背景
        painter = QPainter(pixmap)
        painter.setPen(QColor(0, 0, 0))
        painter.setFont(QFont('Arial', 10))
        painter.drawText(pixmap.rect(), Qt.AlignCenter, 'Pet')
        painter.end()
        return QIcon(pixmap)

    def open_settings(self):
        self.settings_window = SettingsWindow()
        self.settings_window.show()

if __name__ == '__main__':
    print("程式開始運行")
    app = QApplication(sys.argv)
    
    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "錯誤", "檢測不到系統托盤")
        sys.exit(1)

    window = MainWindow()
    window.show()
    print("主窗口已顯示")
    sys.exit(app.exec_())