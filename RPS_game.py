import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

class RPSGame(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("가위바위보 게임")

        self.layout = QVBoxLayout()

        self.label = QLabel("가위, 바위, 보 중 하나를 선택하세요", self)
        self.layout.addWidget(self.label)

        self.rock_button = QPushButton("바위", self)
        self.rock_button.clicked.connect(lambda: self.play_game("바위"))
        self.layout.addWidget(self.rock_button)

        self.paper_button = QPushButton("보", self)
        self.paper_button.clicked.connect(lambda: self.play_game("보"))
        self.layout.addWidget(self.paper_button)

        self.scissors_button = QPushButton("가위", self)
        self.scissors_button.clicked.connect(lambda: self.play_game("가위"))
        self.layout.addWidget(self.scissors_button)

        self.user_choice_label = QLabel("", self)
        self.layout.addWidget(self.user_choice_label)

        self.computer_choice_label = QLabel("", self)
        self.layout.addWidget(self.computer_choice_label)

        self.result_label = QLabel("", self)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "무승부"
        elif (user_choice == "가위" and computer_choice == "보") or \
             (user_choice == "바위" and computer_choice == "가위") or \
             (user_choice == "보" and computer_choice == "바위"):
            return "사용자 승리"
        else:
            return "컴퓨터 승리"

    def play_game(self, user_choice):
        computer_choice = random.choice(["가위", "바위", "보"])
        result = self.determine_winner(user_choice, computer_choice)

        self.user_choice_label.setText(f"사용자 선택: {user_choice}")
        self.computer_choice_label.setText(f"컴퓨터 선택: {computer_choice}")
        self.result_label.setText(f"결과: {result}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = RPSGame()
    game.show()
    sys.exit(app.exec_())
