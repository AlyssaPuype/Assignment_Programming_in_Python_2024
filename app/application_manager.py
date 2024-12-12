""" interaction with database manager to add, remove, update, fetch data from the database"""
import traceback #Helped with finding some errors (traceback.print_exc())
import os

from datetime import datetime
from app.database_manager import DatabaseManager
from app.exporter import Export

class StudyTracker:

	def __init__(self, db: DatabaseManager) -> None:
		self.db = db

	"""__WELCOME__"""

	def show_welcome_message(self) -> None:
		"""
		Shows a welcome message
		User can type exit to close the application or type 'help' to show a list of commands
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
	- 'update course [course id] [new course name]' - Changes the name of the course to a new given one
	- 'view course [course id]' - When no course ID is given, it will show all courses'
	- 'export course' [csv]/[excel] [filename] - exports data of the course table into a cvs or excel
	-------------------------------------------------------------------------------------------
	Sessions:
	- 'add session [course id] [date], [subject], [status], [hours]]'
	- 'remove session [session id]'
	- 'view session [session id]'
	- 'view session today' - Prints all sessions for today
	- 'view session [status]' - Where status can only be 'td', 'ip' or 'd' (todo, in progress, done)
	- 'view session for [course id]' - Prints all existing sessions for given course id
	- 'update session [session id] [column] [new content]' - specify column where you want to change the data
	- 'export session [csv]/[excel] [filename]'

	Database:
	- 'path db' - shows the path of your database
	- 'remove db' - deletes the database and ends the application, prompts for confirmation
		""")


	"""__COURSE RELATED METHODS__"""

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
			print(viewed_course)
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
			print("Arguments are missing. Use command like: update course [course_id] [course_new_name]")
		else:
			course_id = arg_list[0]
			course_new_name = " ".join(arg_list[1:])
			try:
				updated_course = self.db.update_course(course_id, course_new_name)
				if not updated_course:
					print(f"Course {course_id} does not exist. Enter a valid course id")
					return
				print(f"Course updated to '{course_new_name}'\n")
				print(self.db.read_course(course_id))
			except Exception as e:
				print(f"Error when updating course {course_id} to '{course_new_name}'. Course probably already exists. \n")
				return


	def remove_course(self, arg_list: list[str]) -> None:
		"""
		Removes the course with given course id from table,
		Arguments: list of strings

		In case of no arguments: Prompts the user if they want to clear the table. If 'Yes' -> clear table. If 'No', do nothing.
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
			except Exception as e:
				print("Error when trying to clear table")

		if len(arg_list) > 1:
			print("Too many arguments. Use command like: remove course  or remove course [course_id]")
			return

		course_id = arg_list[0]
		try:
			while True:
					confirmation = input(f"Are you sure you want to remove course {course_id}? All linked sessions will also be deleted.\nConfirm with 'Y'/'N': ")
					if confirmation.lower() == "y":
						removed_course = self.db.delete_course(course_id)
						if not removed_course:
							print(f"Course {course_id} does not exist. Enter a valid course id")
							return
						print(f"Course {course_id} is removed from table")
						return False
					elif confirmation.lower() == "n":
						return False
					else:
						print("invalid answer. Type 'Y' to remove course or 'N' to cancel")
		except Exception as e:
				print(f"Error when trying to remove course {course_id}")
				return

	
	"""__SESSION RELATED MEHODS__"""

	def add_session(self, arg_list: list[str])-> None:

		"""
		Adds a session to the table
		Arguments: list of strings

		In case of no arguments: prints out an error message to the user, asking for correct command format
		In case of one or more aguments: session is made from the list of strings and given to the db_manager function
		"""
		if not arg_list or len(arg_list) < 5:
			print(f"Arguments are missing. Use command like: add session [course_id] [date] [subject] [status] [hours]")
			return

		course_id = arg_list[0]
		course_df = self.db.read_course(course_id)
		date = arg_list[1]
		subject = " ".join(arg_list[2:-2])
		status = arg_list[-2] 
		hours = float(arg_list[-1])

		"""Checks if course exists"""
		if course_df is None:
			print(f"Course {course_id} does not exist. Enter a valid course id")
			return

		"""Checks date format"""
		if self.get_date(date) is None:
			print(f" {date} is an invalid date format. Enter date in format dd-mm-yyyy")
			return

		"""Checks if a subject is given"""
		if not subject:
			print("Argument subject is missing . If you mean to specify no subject, you need to use '-' ")
			return

		"""Checks if the status is either td, ip or d"""
		if status.lower() not in {"td", "ip", "d"}:
			print(f" {status} is an invalid status. Enter status as 'td' for 'to do', 'ip' for 'in progress' or 'd' for 'done' ")
			return

		"""Checks if hours is of type float"""
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


		"""
		view all sessions for specified course. !TO FIX. 
		"""
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
				print(viewed_session)
			except Exception as e:
				print(f"Error when trying to view sessions for course {course_id}: {e}")
				return

		"""
		views all sessions for today
		"""
		first_arg = arg_list[0]
		if first_arg == "today":
			try:
				viewed_session = self.db.read_all_session_today()
				if viewed_session is None:
					print("No sessions found for today.")
					return
				print(viewed_session)
			except Exception as e:
				print(f"Error when trying to view sessions for today: {e}.")
				return
		elif first_arg.lower() in {'td','ip','d'}:
			try:
				viewed_session =  self.db.read_all_session_for_status(first_arg)
				if viewed_session is None:
					print("Unknown status. Use status 'td', 'ip' or 'd'")
					return
				print(viewed_session)
			except Exception as e:
				print(f"Error when trying to view sessions with status {first_arg}: {e}.")
				return
		else:
			try:
				session_id = first_arg
				viewed_session = self.db.read_session(session_id)
				if viewed_session is None:
					print(f"Session {session_id} does not exist")
					return
				print(viewed_session)
			except Exception as e:
				print(f"Error when trying to view session {session_id}: {e}")
				return

		
	def remove_session(self, arg_list: list[str]) -> None:
		"""
		Removes the session with given session id from table,
		Arguments: list of strings

		In case of no arguments: Prompts the user if they want to clear the table. If 'Yes' -> clear table. If 'No', do nothing.
		"""
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

		"""
		Updates the data in specified column with specified new data
		Arguments: list of strings

		In case of less than 3 arguments: Prints out an error message to the user, asking for correct command format
		"""
		if not arg_list or len(arg_list) < 3:
			print("Arguments are missing. Use command like: update session [session_id] [column] [new_content]")
			return

		session_id = arg_list[0]
		column_name = arg_list[1]
		new_content = " ".join(arg_list[2:])

		"""
		check if column_name exists
		"""
		if column_name not in {"course_id", "start_date", "subject", "status", "hours"}:
			print(f"{column_name} does not exist in table. Enter valid column name: 'course_id', 'start_date', 'subject', 'status','hours'")
			return
		
		"""
		if column 'status' is selected, check if the new content is either 'td', 'ip' or 'd'
		"""
		if column_name == "status" and new_content not in {"td", "ip", "d"}:
			print(f"{new_content} is an invalid status. Enter status as 'td' for 'to do', 'ip' for 'in progress' or 'd' for 'done' ")
			return

		"""
		check if given course_id exists
		"""
		if column_name == "course_id":
			if self.db.read_course(new_content) is None:
				print(f"Course with {new_content} id does not exists.")
				return
		"""
		check if valid date?
		"""
		if column_name == "start_date":
			pass

		"""
		if column 'hours' is selected, check if the new content is a number
		"""
		if column_name == "hours":
			if not self.input_is_number(new_content):
				print("Use a number for hour.")
				return
		
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

	"""
	function to check if a given input is a number
	"""
	def input_is_number(self, input: str) -> bool:
		try:
			float(input)
			return True
		except ValueError as e:
			print(f"{input} is not a number.")
			return False

	"""__EXPORT METHODS__"""

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


	"""__DATABASE RELATED__"""

	"""prompts the user for confirmation if they want to delete database, if Y given, deletes database"""
	def remove_database(self)-> str:
		try:
			while True:
				confirmation = input("Are you sure you want to delete the database and end the application? Confirm with 'Y'/'N': ")
				if confirmation.lower() == "y":
					removed_db_file_name = self.db.remove_db()
					print(f"\n{removed_db_file_name} removed")
					print("Ending application...")
					return False
				elif confirmation.lower() == "n":
					return False
				else:
					print("invalid answer. Type 'Y' to delete the database or 'N' to cancel")
		except Exception as e:
			print("Error when trying to delete the database")
			return

	"""shows the user the path of the database"""
	def show_path_database(self)-> str:
		db_path = self.db.show_path()
		print(f"Database path: {db_path}")
