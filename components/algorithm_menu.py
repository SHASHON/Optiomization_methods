from PyQt5.QtWidgets import QWidget,QTextEdit,QVBoxLayout,QPushButton

class AlgorithmMenu(QWidget):
    def __init__(self,cfg, parent=None):
        super().__init__(parent)

        self.parent = parent
        layout = QVBoxLayout()

        # Создание кнопок
        greedy_button = QPushButton(cfg['text']['greedy_btn_text'])
        dp_button = QPushButton(cfg['text']['dp_btn_text'])
        branch_and_bound_btn = QPushButton(cfg['text']['branch_and_bound_btn_text'])
        brute_force_button = QPushButton(cfg['text']['bruteforce_btn_text'])
        all_paths = QPushButton(cfg['text']['all_paths_btn_text'])

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

        # Применение стиля к кнопкам
        greedy_button.setStyleSheet(button_style)
        dp_button.setStyleSheet(button_style)
        branch_and_bound_btn.setStyleSheet(button_style)
        brute_force_button.setStyleSheet(button_style)
        all_paths.setStyleSheet(button_style)

        # Подключение событий к кнопкам
        greedy_button.clicked.connect(self.calc_with_greedy_search)
        dp_button.clicked.connect(self.calc_with_dynamic_programming)
        branch_and_bound_btn.clicked.connect(self.calc_with_branch_and_bound)
        brute_force_button.clicked.connect(self.calc_with_brute_force)
        all_paths.clicked.connect(self.calc_all_paths)

        # Добавление кнопок на макет
        layout.addWidget(greedy_button)
        layout.addWidget(dp_button)
        layout.addWidget(branch_and_bound_btn)
        layout.addWidget(brute_force_button)
        layout.addWidget(all_paths)

        self.setLayout(layout)


    def calc_all_paths(self):
        self.parent.calc_all_paths()

    def calc_with_brute_force(self):
        self.parent.calc_with_brute_force()

    def calc_with_greedy_search(self):
        self.parent.calc_with_greedy_search()

    def calc_with_dynamic_programming(self):
        self.parent.calc_with_dynamic_programming()

    def calc_with_branch_and_bound(self):
        self.parent.calc_with_branch_and_bound()