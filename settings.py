from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QLabel, QPushButton
from PyQt5.QtGui import QPainterPath, QRegion
from PyQt5.QtCore import Qt, QRectF

class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowFlags(Qt.FramelessWindowHint)  # 移除窗口邊框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 設置背景透明

    def initUI(self):
        layout = QVBoxLayout()

        # AI模型選擇
        self.model_label = QLabel('選擇AI模型：')
        self.model_combo = QComboBox()
        self.model_combo.addItems(['輕量級模型', '其他模型'])
        layout.addWidget(self.model_label)
        layout.addWidget(self.model_combo)

        # 寵物外觀選擇
        self.appearance_label = QLabel('選擇寵物外觀：')
        self.appearance_combo = QComboBox()
        self.appearance_combo.addItems(['外觀1', '外觀2', '外觀3'])
        layout.addWidget(self.appearance_label)
        layout.addWidget(self.appearance_combo)

        # 系統提示詞設定
        self.prompt_label = QLabel('設定系統提示詞：')
        self.prompt_combo = QComboBox()
        self.prompt_combo.addItems(['預設1', '預設2', '自定義'])
        layout.addWidget(self.prompt_label)
        layout.addWidget(self.prompt_combo)

        # 保存按鈕
        self.save_button = QPushButton('保存設定')
        self.save_button.clicked.connect(self.save_settings)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        self.setWindowTitle('設定')

        # 設置樣式表，實現半透明磨砂玻璃效果
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(240, 240, 240, 180);
                border-radius: 20px;
            }
            QLabel {
                color: black;
                font-weight: bold;
            }
            QComboBox, QPushButton {
                background-color: rgba(255, 255, 255, 200);
                border: 1px solid rgba(0, 0, 0, 100);
                border-radius: 5px;
                padding: 5px;
                color: black;
            }
            QPushButton {
                background-color: rgba(76, 175, 80, 200);
                color: white;
            }
            QPushButton:hover {
                background-color: rgba(69, 160, 73, 200);
            }
        """)

    def save_settings(self):
        # TODO: 實現保存設定的功能
        pass

    # 重寫paintEvent方法來繪製圓角
    def paintEvent(self, event):
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), 20, 20)
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)

    # 實現視窗拖動
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()