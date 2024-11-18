#defining course

class Course:

	def __init__(self, id, name):
		self.id = id
		self.name = name

	def __str__(self):
		return f"ID: {self.id} Course {self.name}"

