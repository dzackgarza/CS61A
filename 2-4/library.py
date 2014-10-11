class Book:

	__title = "" 				#string
	__authors = [""] 		#list of strings
	__ISBN = 0 					#int
	__deweyDecimal = "" #int
	__subjects = []			#list of strings
	__edition = 1  			#int
	__publishYear = 0 	#int
	__description = ""	#string
	__reviews = []			#list of strings
	__relatedBooks = []	#list of Books

	def __init__ (self, title, authors, isbn = 0, decimal = "0", subjects = [],  edition = "1", publishYear = "0", description = "", reviews = [], related = []):
		self.__title = title
		self.__authors = authors
		self.__ISBN = isbn
		self.__deweyDecimal = decimal
		self.__subjects = subjects
		self.__edition = edition
		self.__publishYear = publishYear
		self.__description = description
		self.reviews = reviews
		self.relatedBooks = related

	def printTitle(self):
		print("Title: \"" + self.__title + "\".")

	def printAuthor(self):
		desc = "Authors: \""	
		for i in range(0, len(self.__authors)):
			desc += self.__authors[i] + (", " if i<len(self.__authors)-1 else "")
		desc += "\"."
		print(desc)

	def getISBN(self): pass 									#returns String
	def hasSubject(self, subject): pass 			#returns boolean
	def wasPublishedInYear(self, year): pass 	#returns boolean
	def getReviews(self): pass								#returns list of strings
	def getRelatedBooks(self): pass 					#returns list of books

	def __str__ (self):
		desc = "Title: \"" + self.__title + "\", Author: \"" 
		for i in range(0, len(self.__authors)):
			desc += self.__authors[i] + (", " if i<len(self.__authors)-1 else "")
		desc += "\"."
		return desc


	def __eq__(self, b2):
		return self.__title == b2.__title and self.__authors == b2.__authors


b1 = Book("The title", ["a1", "a2"], "12345")
b1.printTitle()
b1.printAuthor()
b2 = Book("The title", ["a1", "a2"], "12345")
b3 = Book("The title", ["a1", "a3"], "12345")
print("Desciption of book 1: " + str(b1))
print ("b1 == b2? " + str(b1==b2))
print ("b2 == b3? " + str(b2==b3))
