""" interaction with database manager to add, remove, edit, fetch data from the database"""

from database_manager import DatabaseManager

class StudyTracker:

	def __init__(self, db: DatabaseManager) -> None:
		self.db = db

	"""Application-related methods."""

	def show_commands(self) -> None:
		print("List of commands:")
		print("""
			Courses:
				- 'add course [course_name]'
				- 'remove course [course_id]'
				- 'view course [course_id]. When no course ID is given, it will show all courses'
				- 'update course [course_id]'
			-------------------------------------------------------------------------------------
			Sessions:
				- 'add session [course_id, date, subject, status, hours]'
				- 'remove session [session_id]'
				- 'view session [session_id]'
				- 'update session [column, new content]'
		""")


	"""course related methods:"""

	def add_course(self, arg_list: list[str]) -> None:
		course_name = " ".join(arg_list[0:])
		added_course = self.db.create_course(course_name)
		
		if added_course is None:
			return

		print(f"{added_course} added")

	def view_course(self, arg_list: list[str]) -> None:

		"""if no parameter is given, show all current courses"""
		if not arg_list:
			self.db.read_all_courses()
			return

		print("All courses shown")

		"""if course_id is given as parameter, show the course info"""
		course_id = arg_list[0]
		viewed_coursed = self.db.read_course(course_id)
		if viewed_coursed is None:
			return

		print(f"Shown course: viewed_coursed")


	"""updates name of the course"""
	def update_course(self, arg_list: list[str]) -> None:
		if len(arg_list) < 2:
			print("Arguments are missing. Use command like: update course [course_id] [course_new_name]")
		else:
			course_id = arg_list[0]
			course_new_name = " ".join(arg_list[1:])
			updated_course = self.db.update_course(course_id, course_new_name)
			if updated_course is None:
				return

			print(f"Course updated to {updated_course}")


	def remove_course(self, arg_list: list[str]) -> None:
		course_id = arg_list[0]
		removed_course = self.db.delete_course(course_id)
		if removed_course is None:
			return

		print(f"{removed_course} is removed from table")


	"""session related methods:
	def removeCourse():

	def getCourse():

	def updateCourse():

	def addSession():

	def removeSession():

	def getSession():

	def updateSession():
	"""
