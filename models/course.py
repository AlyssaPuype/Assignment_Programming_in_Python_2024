"""defining course"""

class Course:

	def __init__(self, id: int, name: str) -> None:
		self.id = id
		self.name = name

	def __str__(self) -> str:
		return f"Id: {self.id} Course: {self.name}"

