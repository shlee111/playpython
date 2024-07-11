import sys
import os
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem

# 주소록 클래스 정의
class AddressBook:
    def __init__(self, filename='address_book.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    # 연락처 파일에서 로드
    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    # 연락처 파일에 저장
    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file)

    # 연락처 추가
    def add_contact(self, name, phone, email):
        contact = {'name': name, 'phone': phone, 'email': email}
        self.contacts.append(contact)
        self.save_contacts()

    # 연락처 삭제
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                self.save_contacts()
                return True
        return False

    # 연락처 검색
    def search_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                return contact
        return None

    # 연락처 목록 조회
    def list_contacts(self):
        return self.contacts

# 주소록 GUI 클래스 정의
class AddressBookGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.address_book = AddressBook()
        self.initUI()
        
    # GUI 초기화
    def initUI(self):
        self.setWindowTitle('주소록 관리 프로그램')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.name_label = QLabel('이름:')
        self.name_input = QLineEdit()

        self.phone_label = QLabel('전화번호:')
        self.phone_input = QLineEdit()

        self.email_label = QLabel('이메일:')
        self.email_input = QLineEdit()

        self.add_button = QPushButton('연락처 추가')
        self.add_button.clicked.connect(self.add_contact)

        self.delete_button = QPushButton('연락처 삭제')
        self.delete_button.clicked.connect(self.delete_contact)

        self.search_button = QPushButton('연락처 검색')
        self.search_button.clicked.connect(self.search_contact)

        self.list_button = QPushButton('연락처 목록 조회')
        self.list_button.clicked.connect(self.list_contacts)

        self.contacts_table = QTableWidget()
        self.contacts_table.setColumnCount(3)
        self.contacts_table.setHorizontalHeaderLabels(['이름', '전화번호', '이메일'])

        form_layout = QVBoxLayout()
        form_layout.addWidget(self.name_label)
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.phone_label)
        form_layout.addWidget(self.phone_input)
        form_layout.addWidget(self.email_label)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(self.add_button)
        form_layout.addWidget(self.delete_button)
        form_layout.addWidget(self.search_button)
        form_layout.addWidget(self.list_button)

        layout.addLayout(form_layout)
        layout.addWidget(self.contacts_table)

        central_widget.setLayout(layout)

    # 연락처 추가 함수
    def add_contact(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        
        if name and phone and email:
            self.address_book.add_contact(name, phone, email)
            QMessageBox.information(self, '알림', f'{name}님의 연락처가 추가되었습니다.')
            self.clear_inputs()
            self.list_contacts()  # 테이블 업데이트
        else:
            QMessageBox.warning(self, '오류', '모든 필드를 입력하세요.')

    # 연락처 삭제 함수
    def delete_contact(self):
        name = self.name_input.text()
        
        if name:
            if self.address_book.delete_contact(name):
                QMessageBox.information(self, '알림', f'{name}님의 연락처가 삭제되었습니다.')
                self.clear_inputs()
                self.list_contacts()  # 테이블 업데이트
            else:
                QMessageBox.warning(self, '오류', f'{name}님의 연락처를 찾을 수 없습니다.')
        else:
            QMessageBox.warning(self, '오류', '이름을 입력하세요.')

    # 연락처 검색 함수
    def search_contact(self):
        name = self.name_input.text()
        
        if name:
            contact = self.address_book.search_contact(name)
            if contact:
                QMessageBox.information(self, '연락처 검색 결과', f"이름: {contact['name']}\n전화번호: {contact['phone']}\n이메일: {contact['email']}")
            else:
                QMessageBox.warning(self, '오류', f'{name}님의 연락처를 찾을 수 없습니다.')
        else:
            QMessageBox.warning(self, '오류', '이름을 입력하세요.')

    # 연락처 목록 조회 함수
    def list_contacts(self):
        self.contacts_table.setRowCount(0)
        contacts = self.address_book.list_contacts()
        for contact in contacts:
            row_position = self.contacts_table.rowCount()
            self.contacts_table.insertRow(row_position)
            self.contacts_table.setItem(row_position, 0, QTableWidgetItem(contact['name']))
            self.contacts_table.setItem(row_position, 1, QTableWidgetItem(contact['phone']))
            self.contacts_table.setItem(row_position, 2, QTableWidgetItem(contact['email']))

    # 입력 필드 초기화 함수
    def clear_inputs(self):
        self.name_input.clear()
        self.phone_input.clear()
        self.email_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = AddressBookGUI()
    gui.show()
    sys.exit(app.exec_())
