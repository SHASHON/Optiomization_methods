from PyQt5.QtWidgets import QWidget,QTextEdit,QVBoxLayout,QPushButton

class InfoOutput(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)

                # Добавление стиля
                button_style = """
                        QPushButton {
                            background-color: #4CAF50; /* Цвет фона */
                            text-size
                            border: none;
                            color: white;
                            padding: 10px 24px;
                            text-align: center;
                            text-decoration: none;
                            font-size: 11px;
                            margin: 12px 1px;
                            width: auto; /* Автоматическая ширина */
                            height: auto; /* Автоматическая высота */
                        }
                        QPushButton:hover {
                            background-color: #45a049; /* Цвет фона при наведении */
                        }
                        """

                self.textEdit = QTextEdit()
                self.btnPress1 = QPushButton("Очистить поле")
                self.textEdit.setReadOnly(True)
                self.btnPress1.setStyleSheet(button_style)
                layout = QVBoxLayout()
                layout.setContentsMargins(0,0,0,0)
                layout.addWidget(self.textEdit)
                layout.addWidget(self.btnPress1)
                self.setLayout(layout)

                self.btnPress1.clicked.connect(self.btnPress1_Clicked)

        def append(self, text):
            self.textEdit.append(text + "\n")

        def clear(self):
            self.textEdit.setPlainText("")
                
        def btnPress1_Clicked(self):
                self.clear()
