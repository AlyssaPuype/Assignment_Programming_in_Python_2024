# interaction with database to add, remove, edit, fetch data from the database

from database_manager import DatabaseManager

class StudyTracker:

	def __init__(self, db: DatabaseManager):
		self.db = db

# application-related methods:

	# shows a list of commands
	def show_commands(self):
		print("List of commands:")
		print("""
		Courses:
			- 'add course [course_name]'
			- 'remove course [course_id]'
			- 'view course [course_id]'
			- 'update course [course_id]'
		-------------------------------------------------------------
		Sessions:
			- 'add session [course_id, date, subject, status, hours]'        
			- 'remove session [session_id]'
			- 'view session [session_id]'
			- 'update session [column, new content]'
		""")

# course related methods:
	def add_course(self, arg_list):
		course_name = arg_list[0]
		added_course = self.db.create_course(course_name)
		
		if added_course is None:
			return

		print(f"{added_course} added")

	def view_course(self, arg_list):
		
		if not arg_list:
			self.db.read_all_courses()
			return

		course_id = arg_list [0]
		viewed_coursed = self.db.read_course(course_id)

		if viewed_coursed is None:
			return

		print(f"{viewed_coursed.id} | {viewed_coursed.name} is shown")

# session related methods:
	"""
	def removeCourse():

	def getCourse():

	def updateCourse():

	def addSession():

	def removeSession():

	def getSession():

	def updateSession():
	"""
