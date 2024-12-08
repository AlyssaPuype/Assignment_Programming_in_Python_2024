"""defining session"""

class Session:

	def __init__(self, id: int, course_id: int, date: str, subject: str, status: str, hours: int) -> None:
		self.id = id 
		self.course_id = course_id
		self.date = date
		self.subject = subject
		self.status = status
		self.hours = hours

	def get_id(sef):
		return self.id

	def __str__(self) -> str:
		return f"Id: {self.id} | Course_id: {self.course_id} | Date: {self.date} | Subject: {self.subject} | Status: {self.status} | Hours: {self.hours}"