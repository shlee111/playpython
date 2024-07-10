import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QTextCursor, QBrush
from PyQt5.QtCore import Qt

class WordIndexer(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.current_position = -1  # 현재 위치를 저장하는 변수

    def initUI(self):
        self.setWindowTitle("단어 색인 및 빈도수 계산 프로그램")  # 창 제목 설정
        
        # 메인 레이아웃
        self.layout = QVBoxLayout()

        # 텍스트 입력 영역
        self.textEdit = QTextEdit(self)
        self.layout.addWidget(self.textEdit)

        # 단어 입력 필드
        self.wordInput = QLineEdit(self)
        self.wordInput.setPlaceholderText("단어를 입력하세요")  # 단어 입력 안내 문구
        self.layout.addWidget(self.wordInput)

        # 색인 생성 버튼
        self.indexButton = QPushButton("색인 생성 및 빈도수 계산", self)
        self.indexButton.clicked.connect(self.create_index_and_count)  # 버튼 클릭 시 색인 생성 및 빈도수 계산 함수 호출
        self.layout.addWidget(self.indexButton)

        # 다음 위치로 이동 버튼
        self.nextButton = QPushButton("다음 위치로 이동", self)
        self.nextButton.clicked.connect(self.move_to_next_position)  # 버튼 클릭 시 다음 위치로 이동
        self.layout.addWidget(self.nextButton)

        # 결과 표시 라벨
        self.resultLabel = QLabel("", self)
        self.layout.addWidget(self.resultLabel)

        # 현재 위치 표시 라벨
        self.positionLabel = QLabel("", self)
        self.layout.addWidget(self.positionLabel)

        # 레이아웃을 위젯에 설정
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 600, 400)  # 창 크기 및 위치 설정

    def create_index_and_count(self):
        text = self.textEdit.toPlainText()  # 입력된 텍스트 가져오기
        target_word = self.wordInput.text()  # 검색할 단어 가져오기

        # 기존 하이라이트 제거
        self.textEdit.setExtraSelections([])
        self.current_position = -1  # 검색 위치 초기화

        if target_word:
            self.positions = self.find_word_positions(text, target_word)  # 단어 위치 색인 생성
            count = len(self.positions)  # 단어 빈도수 계산
            if self.positions:
                self.move_to_next_position()
                result_text = f"'{target_word}'의 빈도수: {count}, 위치: {self.positions}"
            else:
                result_text = f"'{target_word}' 단어가 텍스트에 없습니다."
        else:
            result_text = "단어를 입력하세요."  # 단어를 입력하지 않았을 경우 메시지

        self.resultLabel.setText(result_text)  # 결과를 라벨에 표시

    def find_word_positions(self, text, word):
        positions = []
        start = 0
        while start < len(text):
            start = text.find(word, start)
            if start == -1:
                break
            positions.append(start)
            start += len(word)  # 단어 길이만큼 이동하여 중복 위치 방지
        return positions

    def move_to_next_position(self):
        if not hasattr(self, 'positions') or not self.positions:
            return

        self.current_position += 1
        if self.current_position >= len(self.positions):
            self.current_position = 0  # 처음 위치로 돌아감

        pos = self.positions[self.current_position]
        self.highlight_word(pos, len(self.wordInput.text()))
        self.positionLabel.setText(f"현재 위치: {pos}")  # 현재 위치를 라벨에 표시

    def highlight_word(self, pos, length):
        extraSelections = []
        selection = QTextEdit.ExtraSelection()
        selection.cursor = self.textEdit.textCursor()
        selection.cursor.setPosition(pos)
        selection.cursor.setPosition(pos + length, QTextCursor.KeepAnchor)
        selection.format.setBackground(QBrush(Qt.yellow))  # 하이라이트 색상 설정
        extraSelections.append(selection)
        self.textEdit.setExtraSelections(extraSelections)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 객체 생성
    ex = WordIndexer()  # WordIndexer 객체 생성
    ex.show()  # 위젯 표시
    sys.exit(app.exec_())  # 이벤트 루프 실행
