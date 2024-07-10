import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel, QLineEdit

class WordFrequencyCounter(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("단어 빈도수 계산기")  # 창 제목 설정
        
        # 메인 레이아웃
        self.layout = QVBoxLayout()

        # 텍스트 입력 영역
        self.textEdit = QTextEdit(self)
        self.layout.addWidget(self.textEdit)

        # 단어 입력 필드
        self.wordInput = QLineEdit(self)
        self.wordInput.setPlaceholderText("단어를 입력하세요")  # 단어 입력 안내 문구
        self.layout.addWidget(self.wordInput)

        # 버튼 생성
        self.button = QPushButton("빈도수 계산", self)
        self.button.clicked.connect(self.calculate_frequency)  # 버튼 클릭 시 계산 함수 호출
        self.layout.addWidget(self.button)

        # 결과 표시 라벨
        self.resultLabel = QLabel("", self)
        self.layout.addWidget(self.resultLabel)

        # 레이아웃을 위젯에 설정
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 600, 400)  # 창 크기 및 위치 설정

    def calculate_frequency(self):
        text = self.textEdit.toPlainText()  # 입력된 텍스트 가져오기
        target_word = self.wordInput.text()  # 검색할 단어 가져오기
        
        if target_word:
            count = text.count(target_word)  # 입력된 텍스트에서 검색할 단어의 빈도수 계산
            result_text = f"'{target_word}'의 빈도수: {count}"  # 결과 문자열 생성
        else:
            result_text = "단어를 입력하세요."  # 단어를 입력하지 않았을 경우 메시지

        self.resultLabel.setText(result_text)  # 결과를 라벨에 표시

if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 객체 생성
    ex = WordFrequencyCounter()  # WordFrequencyCounter 객체 생성
    ex.show()  # 위젯 표시
    sys.exit(app.exec_())  # 이벤트 루프 실행
