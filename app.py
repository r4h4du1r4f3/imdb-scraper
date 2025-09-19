from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

import imdb

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('IMDB Scraper')
		self.setFixedSize(800,500)

		vbox = QVBoxLayout()
		hbox = QHBoxLayout()

		self.input = QLineEdit()
		self.button = QPushButton("Search")
		self.button.setDisabled(True)
		self.label = QLabel()

		hbox.addWidget(self.input)
		hbox.addWidget(self.button)
		input_container = QWidget()
		input_container.setLayout(hbox)

		vbox.addWidget(input_container)
		vbox.addWidget(self.label)

		container = QWidget()
		container.setLayout(vbox)

		self.setCentralWidget(container)

		self.input.textChanged.connect(self.onInput)
		self.input.returnPressed.connect(self.onButton)
		self.button.pressed.connect(self.onButton)

	def onInput(self):
		if self.input.text().strip() == "":
			self.button.setDisabled(True)
		else:
			self.button.setEnabled(True)

	def onButton(self):
		film_name=self.input.text().lower()
		film_name = film_name.replace('-',' ')
		film_name = ''.join(char for char in film_name if char.isalnum() or char.isspace())
		film_name = '-'.join(film_name.split())

		data = imdb.getInfo(film_name)
		output = ''

		i = 0
		for chunk in data:
			i+=1
			output+=(f'{i}. {chunk.text}\n')

		self.label.setText(output)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()