import sys
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QListView, QListWidget, QTextBrowser, QVBoxLayout, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QPushButton)
from PyQt5.QtCore import Qt
from constants import *
from controller_interface import ControllerBase
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400

LIST_CONNECTED_CLIENTS = 0
LIST_CHAT_ROOMS = 1

class GroupchatBox(QWidget):
    def __init__(self, controller: ControllerBase):
        super().__init__()
        # who you are chatting with
        self.chatting_entity = None
        # the chat window
        self.chat_browser = None
        self.message_edit = None

        # controller, model
        self.controller = controller
        self.model = controller.getmodel()
        
        self.initUI()

    # refresh the chat
    def setChatWith(self, others_sockname):
        self.chatting_entity = others_sockname
        self.chat_browser.clear()

        msg_list: list[str] = self.model.get_indiv_message(self.chatting_entity)
        for msg in msg_list:
            self.chat_browser.append(msg)

    def createChatWindow(self):
        # HBOX (user input)
        if True:
            hbox = QHBoxLayout()
            self.message_edit = QLineEdit()

            def send_message():
                # send message
                self.model.add_indiv_message(self.chatting_entity, self.message_edit.text())
                self.setChatWith(self.chatting_entity)

            send_btn = QPushButton("Send", self)
            send_btn.clicked.connect(send_message)
            
            hbox.addWidget(self.message_edit)
            hbox.addWidget(send_btn)

        # VBOX (chat window)
        if True:
            vbox = QVBoxLayout()
            vbox.addWidget(QLabel("Chat with Alice"))
            self.chat_browser = QTextBrowser()
            
            vbox.addWidget(self.chat_browser)
            vbox.addLayout(hbox)
            close_btn = QPushButton("Close")
            def go_back_to_waitingroom():
                self.controller.connected.setGeometry(self.controller.chatbox.geometry())
                self.controller.changePageTo(PAGE_CONNECTED)

            close_btn.clicked.connect(lambda: go_back_to_waitingroom())
            vbox.addWidget(close_btn)
            return vbox


    def initUI(self):
        browser_member_list = QTextBrowser()
        browser_member_list.append("Alice (host)")
        browser_member_list.append("Bob")
        browser_member_list.append("Craig (Me)")
        
        vbox_member_list = QVBoxLayout()
        vbox_member_list.addWidget(QLabel("Members"))
        vbox_member_list.addWidget(browser_member_list)
        vbox_member_list.addWidget(QPushButton("Invite"))

        hbox = QHBoxLayout()
        hbox.addLayout(self.createChatWindow())
        hbox.addLayout(vbox_member_list)
        hbox.setStretch(0, 10)
        hbox.setStretch(1, 4)

        self.setLayout(hbox)
        self.setWindowTitle('Connection Page')
        self.setGeometry(300, 300, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.show()


