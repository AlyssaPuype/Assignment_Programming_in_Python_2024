""" interaction with database manager to add, remove, edit, fetch data from the database"""

from datetime import datetime
from database_manager import DatabaseManager
from exporter import Export

import traceback

class StudyTracker:

	def __init__(self, db: DatabaseManager) -> None:
		self.db = db

	def show_welcome_message(self) -> None:
		"""
		Shows a welcome message
		"""
		print("\nWelcome to study tracker!")
		print("To see the list of commands, type 'help'")
		print("To exit the application, type 'exit'\n")

	def show_commands(self) -> None:
		"""
		Shows a list of available commands that the user can use
		"""
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
	- 'add session [course id] [date], [subject], [status], [hours]]'
	- 'remove session [session id]'
	- 'view session [session id]'
	- 'view session for [course id]' - Prints all existing sessions for given course id
	- 'edit session [session id] [column] [new content]'
	- 'export session [csv]/[excel]'
		""")


	"""COURSE RELATED METHODS:"""

	def add_course(self, arg_list: list[str]) -> None:
		"""
		Adds a course to the table
		Arguments: list of strings

		In case of no arguments: prints out an error message to the user, asking for correct command format
		In case of one or more aguments: course name is made from the list of strings and given to the db_manager function
		"""

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
			return


	def view_course(self, arg_list: list[str]) -> None:
		"""
		Prints a course from the table
		Arguments: list of strings

		In case of no arguments: Prints all courses in table
		In case of one argument: course_id is needed as argument and given to the db_manager function
		In case of more than one argument: prints out an error message to the user, asking for correct command format
		"""

		if not arg_list:
			list_courses = self.db.read_all_courses()
			if list_courses is None: 
				print("Table is empty. Add courses to fill the table")
				return
			print(list_courses)
			return

		if len(arg_list) > 1:
			print("Too many arguments. Use command like: view course [course_id]")
			return

		course_id = arg_list[0]
		try:
			viewed_course = self.db.read_course(course_id)
			if viewed_course is None:
				print(f"Course with ID {course_id} does not exist")
				return
			print(f"{viewed_course}")
		except Exception as e:
			print(f"Error when trying to view course {course_id}: {e}")
			return


	def update_course(self, arg_list: list[str]) -> None:
		"""
		Updates the course name of a course to a new given name
		Arguments: list of strings

		In case of less than 2 arguments: Prints out an error message to the user, asking for correct command format
		In case of 2 arguments: First argument is course_id. Second argument is the new name of the course. Given to the db_manager function
		"""

		if len(arg_list) < 2:
			print("Arguments are missing. Use command like: edit course [course_id] [course_new_name]")
		else:
			course_id = arg_list[0]
			course_new_name = " ".join(arg_list[1:])
			try:
				updated_course = self.db.update_course(course_id, course_new_name)
				if not updated_course:
					print(f"Course {course_id} does not exist. Enter a valid course id")
					return
				print(f"Course edited to '{course_new_name}'\n")
				print(self.db.read_course(course_id))
			except Exception as e:
				print(f"Error when editing course {course_id} to '{course_new_name}'. Course probably already exists. \n")
				return


	def remove_course(self, arg_list: list[str]) -> None:
		"""
		Removes the course with given course id from table,
		Arguments: list of strings

		In case of no arguments: Prompts the user if they want to clear the table. If 'Yes' -> clear table. If 'No', do nothing.
		In case of 2 arguments: First argument is course_id. Second argument is the new name of the course. Given to the db_manager function
		"""
		if not arg_list:
			try:
				while True:
					confirmation = input("Are you sure you want to clear the Courses table? Confirm with 'Y'/'N': ")
					if confirmation.lower() == "y":
						if self.db.delete_all_courses():
							print("Table table cleared.")
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

		if len(arg_list) > 1:
			print("Too many arguments. Use command like: remove course  or remove course [course_id]")
			return

		course_id = arg_list[0]
		try:
			removed_course = self.db.delete_course(course_id)
			if not removed_course:
				print(f"Course {course_id} does not exist. Enter a valid course id")
				return
			print(f"Course {course_id} is removed from table")
		except Exception as e:
				print(f"Error when trying to remove course {course_id}")
				return

	

	"""SESSION RELATED MEHODS:"""

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
			print(f"Course {course_id} does not exist. Enter a valid course id")
			return

		if self.get_date(date) is None:
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
			added_session = self.db.create_session(course_id, date, subject, status, hours)
			if added_session is None:
				print(f"No sessions created. Check command")
				return
			print(f"{added_session} added for the course {course_id}")

		except Exception as e:
			print(f"Error when trying to create session: {e}")
			print(self.db.read_all_sessions())
			return


	def get_date(self, date: str) -> str:
		"""
		gets the date from input as a string, converts it to an object to check valid format and returns it as a string when correct, if not, returns None
		"""
		try:
			 date_object = datetime.strptime(date, "%d-%m-%Y").date()
			 return date_object.strftime("%d-%m-%Y")
		except ValueError:
			return None

	
	def view_session(self, arg_list: list[str]) -> None:
		if not arg_list:
			list_sessions = self.db.read_all_sessions()
			if list_sessions is None:
				print(f"table is empty. Add sessions to fill the table")
				return
			print(list_sessions)    
			return

		if len(arg_list) > 2:
			print("Too many arguments. Use command like: view session , view session [session id] or view session for [course id]")
			return

		if len(arg_list) == 2:

			action_name = arg_list[0]
			course_id = arg_list[1]
			if action_name != "for":
				print("Unknown command. Use command like: view session for [course id]")
				return

			try:
				viewed_session = self.db.read_all_sessions_for_course(course_id)
				if viewed_session is None:
					print(f"No sessions found for course {course_id}. Enter a valid course id")
					return
				print(f"{viewed_session}")
			except Exception as e:
				print(f"Error when trying to view sessions for course {course_id}: {e}")
				return

		if len(arg_list) == 1:

			session_id = arg_list[0]
			try:
				viewed_session = self.db.read_session(session_id)
				if viewed_session is None:
					print(f"Session {session_id} does not exist")
					return
				print(f"{viewed_session}")
			except Exception as e:
				print(f"Error when trying to view session {session_id}: {e}")
				return


	def remove_session(self, arg_list: list[str]) -> None:
		if not arg_list:
			try:
				while True:
					confirmation = input("Are you sure you want to clear the Session table? Confirm with 'Y'/'N': ")
					if confirmation.lower() == "y":
						if self.db.delete_all_sessions():
							print("Table cleared.")
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

		session_id = arg_list[0]
		try:
			removed_session = self.db.delete_session(session_id)
			if not removed_session:
				print(f"Session {session_id} does not exist. Enter a valid session id")
			print(f"Session {session_id} is removed from table")
		except Exception as e:
				print(f"Error when trying to remove session {session_id}")
				return


	def update_session(self, arg_list: list[str]) -> None:
		if not arg_list or len(arg_list) < 3:
			print("Arguments are missing. Use command like: edit session [session_id] [column] [new_content]")
			return

		session_id = arg_list[0]
		column_name = arg_list[1]
		new_content = " ".join(arg_list[2:])

		if column_name not in {"course_id", "date_created", "subject", "status", "hours"}:
			print(f"{column_name} does not exist in table. Enter valid column name: 'course_id', 'date_created', 'subject', 'status','hours'")
			return
		
		if column_name == "status" and new_content not in {"td", "ip", "d"}:
			print(f"{new_content} is an invalid status. Enter status as 'td' for 'to do', 'ip' for 'in progress' or 'd' for 'done' ")
			return

		if column_name == "course_id":
			pass

		if column_name == "date_created":
			pass
		
		try:
			session_to_update = self.db.read_session(session_id)
			updated_session = self.db.update_session(session_to_update, column_name, new_content)
			if not updated_session:
				print(f"Session {session_id} does not exist. Enter a valid session id")
			print(f"Column '{column_name}'' in Session {session_id} updated to '{new_content}'\n")
			print(self.db.read_session(session_id))
		except Exception as e:
			print(f"Error when trying to update session: {e}")
			return



	"""EXPORT METHODS"""

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
			exporter.export_course(export_name, export_type)
			print(f"Table Courses exported to {export_type} file as '{export_name}'")
		except Exception as e:
			print(f"Error when exporting data: {e}")
			return


	def export_session(self, arg_list: list[str])-> None:
		exporter = Export(self.db)

		if not arg_list or len(arg_list) < 2:
			print("Arguments are missing. Use command like: export session [csv]/[excel] [name_file]")
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
			exporter.export_session(export_name, export_type)
			print(f"Table Sessions exported to {export_type} file as '{export_name}'")
		except Exception as e:
			print(f"Error when exporting data: {e}")
			return

