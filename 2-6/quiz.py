''' Tracks all of the quizzes in a single class '''
class QuizTracker:

	''' List of Quizzes (see subclasses) '''
	quizzes = []

	def __init__(self, quizzes):
		self.quizzes = quizzes

	''' Add a new quiz to a particular class '''
	def add_quiz(self, quiz):
		this.quizzes.append(quiz)
	

''' Represents a single quiz '''
class Quiz:

	point_values = []
	grade_weight = 1.0

	def __init__(self, grade_weight = 1):
		self.grade_weight = grade_weight

''' Extends Quiz, only holds True/False quizzes '''
class True_False_Quiz(Quiz):

	''' Holds true/false questions '''
	questions = []
	''' Holds the series of T/F answers '''
	answers = []
	''' Choices for answers '''
	possible_answers = ['T', 'F']
	
	def __init__(self):
		super(True_False_Quiz, self).__init__()

	def add_question(self, question, response):
		this.questions.append(question)
		this.response.append(possible_responses[response])
	
''' Extends Quiz, holds multiple-choice response quizzes '''
class QA_Quiz(Quiz):

	''' Holds an open-ended question '''
	questions = []
	''' One all of the multiple-choice answers '''
	answers = []
	''' Choices of possible answers '''
	possible_answers = ['a','b','c','d']

	def __init__(self):
		super(QA_Quiz, self).__init__()

	''' Add new item by supplying the question, its answer, and how many points it's worth '''
	def add_QA(question, answer, points):
		self.questions.append(question)
		self.answers.append(answer)
		self.point_values.append(points)
