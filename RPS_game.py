import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

# RPSGame 클래스 정의, QWidget을 상속받음
class RPSGame(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("가위바위보 게임")  # 창 제목 설정

        self.layout = QVBoxLayout()  # 수직 레이아웃 설정

        # 라벨 생성 및 레이아웃에 추가
        self.label = QLabel("가위, 바위, 보 중 하나를 선택하세요", self)
        self.layout.addWidget(self.label)

        # 바위 버튼 생성 및 클릭 이벤트 핸들러 연결
        self.rock_button = QPushButton("바위", self)
        self.rock_button.clicked.connect(lambda: self.play_game("바위"))
        self.layout.addWidget(self.rock_button)

        # 보 버튼 생성 및 클릭 이벤트 핸들러 연결
        self.paper_button = QPushButton("보", self)
        self.paper_button.clicked.connect(lambda: self.play_game("보"))
        self.layout.addWidget(self.paper_button)

        # 가위 버튼 생성 및 클릭 이벤트 핸들러 연결
        self.scissors_button = QPushButton("가위", self)
        self.scissors_button.clicked.connect(lambda: self.play_game("가위"))
        self.layout.addWidget(self.scissors_button)

        # 사용자 선택, 컴퓨터 선택, 결과를 표시할 라벨 생성 및 레이아웃에 추가
        self.user_choice_label = QLabel("", self)
        self.layout.addWidget(self.user_choice_label)

        self.computer_choice_label = QLabel("", self)
        self.layout.addWidget(self.computer_choice_label)

        self.result_label = QLabel("", self)
        self.layout.addWidget(self.result_label)

        # 메인 레이아웃을 위젯에 설정
        self.setLayout(self.layout)

    # 승자를 결정하는 메서드
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "무승부"  # 사용자와 컴퓨터 선택이 같은 경우
        elif (user_choice == "가위" and computer_choice == "보") or \
             (user_choice == "바위" and computer_choice == "가위") or \
             (user_choice == "보" and computer_choice == "바위"):
            return "사용자 승리"  # 사용자가 이기는 경우
        else:
            return "컴퓨터 승리"  # 컴퓨터가 이기는 경우

    # 게임 실행 메서드
    def play_game(self, user_choice):
        computer_choice = random.choice(["가위", "바위", "보"])  # 컴퓨터의 선택을 랜덤으로 결정
        result = self.determine_winner(user_choice, computer_choice)  # 승자 결정

        # 라벨을 업데이트하여 사용자 선택, 컴퓨터 선택, 결과 표시
        self.user_choice_label.setText(f"사용자 선택: {user_choice}")
        self.computer_choice_label.setText(f"컴퓨터 선택: {computer_choice}")
        self.result_label.setText(f"결과: {result}")

# 메인 함수
if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 객체 생성
    game = RPSGame()  # RPSGame 위젯 생성 및 표시
    game.show()  # 위젯을 화면에 표시
    sys.exit(app.exec_())  # 이벤트 루프 실행
