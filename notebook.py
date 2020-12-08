import datetime
import dbmanager

class Note(object):
	""" Note"""


	def __init__(self, title, author):
		self.title = title
		self.published_date = datetime.now()
		self.author = author
		self.alarm = None

	def save_note(self):
		"""Сохраняет запись в базе данных"""
		pass


	def edit_note(self, text):
		"""функция вводит тест записи(в дальнейшем необходимо 
		   проработать многострочный текст)"""
		
		self.text = text
		self.save_note()


	def read_note(self):
		"""функция читает запись"""
		return self.text

	def delete_note(self):
		"""Удаляет запись из базы данных"""
		