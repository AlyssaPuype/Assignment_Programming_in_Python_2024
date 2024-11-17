# defining session

class Session:

	def __init__(self, id, course_id, date, subject, status, hours):
		self.id = id 
		self.course_id = course_id
		self.date = date
		self.subject = subject
		self.status = status
		self.hours = hours