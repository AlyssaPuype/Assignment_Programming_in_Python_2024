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
		try:
			added_course = self.db.create_course(course_name)
			if added_course is None:
				return
			print(f"{added_course} added")
		except Exception as e:
			print(f"Error when trying to add {course_name}. Course probably already exists.\n")
			print(self.db.read_all_courses())

	def view_course(self, arg_list: list[str]) -> None:

		"""if no parameter is given, show all current courses"""
		if not arg_list:
			list_courses = self.db.read_all_courses()
			if list_courses is None: 
				print("Table is empty. Add courses to fill the table")
				return
			print(list_courses)
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
			print(f"Error when trying to view course {course_id}")


	"""updates name of the course"""
	def update_course(self, arg_list: list[str]) -> None:
		if len(arg_list) < 2:
			print("Arguments are missing. Use command like: update course [course_id] [course_new_name]")
		else:
			course_id = arg_list[0]
			course_new_name = " ".join(arg_list[1:])
			try:
				updated_course = self.db.update_course(course_id, course_new_name)
				if not updated_course:
					return
				print(f"Course updated to {course_new_name}")
			except Exception as e:
				print(f"Error when updating course {course_id} to new name: {course_new_name}. Course probably already exists. \n")
				print(self.db.read_all_courses())


	def remove_course(self, arg_list: list[str]) -> None:
		if not arg_list:
			try:
				while True:
					confirmation = input("Are you sure you want to clear the Courses table? Confirm with 'Y'/'N': ")
					if confirmation.lower() == "y":
						if self.db.delete_all_courses():
							print("Course table cleared.")
							return False
						else:
							print("Table is already empty.")
					elif confirmation.lower() == "n":
						return False
					else:
						print("invalid answer. Type 'Y' to clear table or 'N' to cancel")
				else: 
					print("Unknown command. Use command like: remove course all")
			except Exception as e:
				print("Error when trying to clear table")
				return

		course_id = arg_list[0]
		try:
			removed_course = self.db.delete_course(course_id)
			if not removed_course:
				return
			print(f"Course {course_id} is removed from table")
		except Exception as e:
				print(f"Error when trying to remove course {course_id}")
		


	"""session related methods:
	def removeCourse():

	def getCourse():

	def updateCourse():

	def addSession():

	def removeSession():

	def getSession():

	def updateSession():
	"""

