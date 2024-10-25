from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer, QPoint  # 新增 QPoint 的導入

class DesktopPet(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 設置寵物圖片（暫時使用純色背景）
        self.setStyleSheet("background-color: yellow;")
        self.setFixedSize(100, 100)

        # 初始化拖動相關變量
        self.dragging = False  # 是否正在拖動
        self.offset = QPoint()  # 鼠標點擊位置相對於寵物左上角的偏移

        # 設置定時器，用於定期更新寵物狀態
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_pet)
        self.timer.start(1000)  # 每秒更新一次

        # 初始位置設置在屏幕中央
        self.move_to_center()

    def move_to_center(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def mousePressEvent(self, event):
        # 當左鍵按下時，開始拖動
        if event.button() == Qt.LeftButton:
            self.dragging = True
            # 記錄鼠標點擊位置相對於寵物左上角的偏移
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        # 如果正在拖動，則移動寵物
        if self.dragging:
            # 計算新位置並移動寵物
            self.move(self.mapToParent(event.pos() - self.offset))

    def mouseReleaseEvent(self, event):
        # 當左鍵釋放時，結束拖動
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def mouseDoubleClickEvent(self, event):
        # 當右鍵雙擊時，觸發AI對話功能
        if event.button() == Qt.RightButton:
            # TODO: 實現AI對話功能
            pass

    def update_pet(self):
        # TODO: 實現AI觀察螢幕並互動的功能
        # 這個方法會每秒被調用一次
        pass