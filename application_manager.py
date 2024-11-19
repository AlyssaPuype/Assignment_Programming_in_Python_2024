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
		if not arg_list:
			print(f"Course name is missing. Use command like: add course [course_name]")
			return
		course_name = " ".join(arg_list[0:])
		added_course = self.db.create_course(course_name)
		
		if added_course is None:
			print(f"Error when trying to add {course_name}. Course probably already exists.\n")
			print(self.db.read_all_courses())
			return

		print(f"{added_course} added")

	def view_course(self, arg_list: list[str]) -> None:

		"""if no parameter is given, show all current courses"""
		if not arg_list:
			print(self.db.read_all_courses())
			return

		"""if course_id is given as parameter, show the course info"""
		course_id = arg_list[0]
		try:
			viewed_course = self.db.read_course(course_id)
			if viewed_course is None:
				print(f"Course with ID {course_id} does not exist.")
				return
			print(f"{viewed_course}")
		except Exception as e:
			print("hallo")


	"""updates name of the course"""
	def update_course(self, arg_list: list[str]) -> None:
		if len(arg_list) < 2:
			print("Arguments are missing. Use command like: update course [course_id] [course_new_name]")
		else:
			course_id = arg_list[0]
			course_new_name = " ".join(arg_list[1:])
			try:
				updated_course = self.db.update_course(course_id, course_new_name)
				if updated_course is None:
					return
				print(f"Course updated to {course_new_name} \n {updated_course}")
				try:
					self.view_course([])
				except Exception as e:
					print(f"Error when trying to show all courses")
			except Exception as e:
				print(f"Error when updating course {course_id} to new name: {course_new_name}")


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
