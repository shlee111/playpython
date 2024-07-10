import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel

# Calculator 클래스 정의, QWidget을 상속받음
class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # UI 초기화 메서드 호출
        self.initUI()

    def initUI(self):
        # 메인 레이아웃 설정
        vbox = QVBoxLayout()

        # 결과를 보여줄 QLineEdit 위젯 추가
        self.result = QLineEdit(self)
        vbox.addWidget(self.result)

        # 계산기 버튼 정의
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # 버튼들을 배치할 레이아웃
        grid = QVBoxLayout()
        row = QHBoxLayout()

        # 버튼을 순차적으로 추가
        for i, button in enumerate(buttons):
            # 4개의 버튼마다 새로운 행(row) 레이아웃 추가
            if i % 4 == 0:
                row = QHBoxLayout()
                grid.addLayout(row)
            # 버튼 생성 및 클릭 이벤트 핸들러 연결
            btn = QPushButton(button, self)
            btn.clicked.connect(self.on_click)
            row.addWidget(btn)

        # 메인 레이아웃에 버튼 레이아웃 추가
        vbox.addLayout(grid)

        # 메인 레이아웃을 위젯에 설정
        self.setLayout(vbox)
        self.setWindowTitle('Calculator')
        self.show()

    # 버튼 클릭 이벤트 핸들러
    def on_click(self):
        sender = self.sender()  # 클릭된 버튼의 텍스트 가져오기
        text = sender.text()

        # '=' 버튼이 클릭된 경우
        if text == '=':
            try:
                expression = self.result.text()  # 입력된 수식 가져오기
                self.result.setText(str(eval(expression)))  # 수식을 평가하고 결과 표시
            except Exception as e:
                self.result.setText('Error')  # 오류 발생 시 'Error' 표시
        elif text == 'C':
            self.result.clear()  # 'C' 버튼이 클릭된 경우 입력 창 초기화
        else:
            current_text = self.result.text()  # 현재 입력된 텍스트 가져오기
            new_text = current_text + text  # 새로운 텍스트 추가
            self.result.setText(new_text)  # 입력 창 업데이트

# 메인 함수
if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication 객체 생성
    ex = Calculator()  # Calculator 위젯 생성 및 표시
    sys.exit(app.exec_())  # 이벤트 루프 실행
