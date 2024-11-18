"""defining session"""

class Session:

	def __init__(self, id: int, course_id: int, date: str, subject: str, status: str, hours: int) -> None:
		self.id = id 
		self.course_id = course_id
		self.date = date
		self.subject = subject
		self.status = status
		self.hours = hours