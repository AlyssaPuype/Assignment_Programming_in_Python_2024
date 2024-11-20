""" interaction with database manager to add, remove, edit, fetch data from the database"""

from datetime import datetime
from database_manager import DatabaseManager
from exporter import Export


class StudyTracker:

	def __init__(self, db: DatabaseManager) -> None:
		self.db = db

	"""Application-related methods."""

	def show_commands(self) -> None:
		print("List of commands:")
		print("""
	Courses:
	- 'add course [course name]'
	- 'remove course [course id]' - When no course ID is given, it will prompt you to clear the table
	- 'edit course [course id] [new course name]' - Changes the name of the course to a new given one
	- 'view course [course id]' - When no course ID is given, it will show all courses'
	- 'export course' [csv]/[excel] - exports data of the course table into a cvs or excel
	-------------------------------------------------------------------------------------------
	Sessions:
	- 'add session [course_id, date, subject, status, hours]'
	- 'remove session [session id]'
	- 'view session [session id]'
	- 'edit session [column, new content]'
		""")


	"""course related methods:"""

	def add_course(self, arg_list: list[str]) -> None:
		if not arg_list:
			print(f"Course name is missing. Use command like: add course [course_name]")
			return
		course_name = " ".join(arg_list[0:]).lower()
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
			print("Arguments are missing. Use command like: edit course [course_id] [course_new_name]")
		else:
			course_id = arg_list[0]
			course_new_name = " ".join(arg_list[1:])
			try:
				updated_course = self.db.update_course(course_id, course_new_name)
				if not updated_course:
					return
				print(f"Course editing to {course_new_name}")
			except Exception as e:
				print(f"Error when editing course {course_id} to new name: {course_new_name}. Course probably already exists. \n")
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
	

	def add_session(self, arg_list: list[str])-> None:
		if not arg_list or len(arg_list) < 5:
			print(f"Arguments are missing. Use command like: add session [course_id] [date] [subject] [status] [hours]")
			return

		course_id = arg_list[0]
		course_df = self.db.read_course(course_id)
		date = arg_list[1]
		subject = " ".join(arg_list[2:-2])
		status = arg_list[-2] 
		hours = float(arg_list[-1])

		if course_df is None:
			print(f"Course id {course_id} does not exist. Enter a valid course id")
			return

		if date is None:
			print(f" {date} is an invalid date format. Enter date in format dd-mm-yyyy")
			return

		if not subject:
			print("Argument subject is missing . If you mean to specify no subject, you need to use '-' ")
			return

		if status.lower() not in {"td", "ip", "d"}:
			print(f" {status} is an invalid status. Enter status as 'td' for 'to do', 'ip' for 'in progress' or 'd' for 'done' ")
			return

		if not isinstance(hours, float):
			print(f"{hours} is an invalid type. Enter hours as a number")
			return

		try:
			pass
		except Exception as e:
			print("Error when trying to create session")


	def get_date(self, date: str) -> str:
		"""
		gets the date from input as a string, converts it to an object to check valid format and returns it as a string when correct, if not, returns None
		"""
		try:
			 date_object = datetime.strptime(date, "%d-%m-%y").date()
			 return date_object.strftime("%d-%m-%y")
		except ValueError as e:
			return None
		


	"""Export methods"""

	def export_course(self, arg_list: list[str])-> None:
		exporter = Export(self.db)

		if not arg_list or len(arg_list) < 2:
			print("Arguments are missing. Use command like: export course [csv]/[excel] [name_file]")
			return
		
		export_type = arg_list[0].lower()
		export_name = arg_list [1]
		if export_type not in {"csv", "excel"}:
			print("Invalid export type. Use [csv] or [exce] as export type")
			return
		if export_name in {"csv", "excel"}:
			print("Filename can not be export type. Please use a valid filename")
			return

		try:
			if export_type == "csv":
				exporter.export_to_csv(export_name)
				print(f"Table Courses exported to csv file with as {export_name}")
			elif export_type == "excel":
				exporter.export_to_excel(export_name)
				print(f"Table Courses exported to excel file with as {export_name}")
		except Exception as e:
			print(f"Error when exporting data: {e}")

	def export_session(self, arg_list: list[str]):
		pass

		course_id = arg_list[0]
		try:
			removed_course = self.db.delete_course(course_id)
			if not removed_course:
				return
			print(f"Course {course_id} is removed from table")
		except Exception as e:
				print(f"Error when trying to remove course {course_id}")
		



	"""session related methods:

	def updateCourse():

	def addSession():

	def removeSession():

	def getSession():

	def updateSession():
	"""

