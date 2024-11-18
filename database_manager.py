import sqlite3

from models.course import Course
from models.session import Session

# Manage the database for the study tracker application

class DatabaseManager:
	
	def __init__(self, db_name="StudyTracker.db"):
		try:
			self.con = sqlite3.connect(db_name)
			self.cursor = self.con.cursor()
			self.create_tables()
		except sqlite3.Error as e:
			print(f"Error when trying to connect to {db_name} : {e}")
			raise


	def create_tables(self):
		try:
			self.cursor.execute("""
				CREATE TABLE IF NOT EXISTS Courses (
			    	id INTEGER PRIMARY KEY AUTOINCREMENT,
			    	name TEXT UNIQUE NOT NULL
			    	# amount_sessions, possible to add another column, counting how many sessions each course has, by default, upon making a course, it is set to 0
			    );
			""")

			self.cursor.execute("""
			    CREATE TABLE IF NOT EXISTS Sessions (
			        id INTEGER PRIMARY KEY AUTOINCREMENT,
			        course_id INTEGER NOT NULL,
			        date TEXT NOT NULL,
			        subject TEXT NOT NULL,
			        status TEXT CHECK(status IN ('to do', 'in progress', 'done')),
			        hours INTEGER NOT NULL,
			        FOREIGN KEY (course_id) REFERENCES Courses(id)
			    );
			""")

			self.con.commit()

		except sqlite3.Error as e:
			print(f"Error when creating tables for {db_name} : {e}")
			self.con.rollback()

	#queries:

	def create_course(self, name):
		try:
			self.cursor.execute("INSERT INTO Courses (name) VALUES (?)", (name,))
			return Course(self.cursor.lastrowid, name)
		except sqlite3.Error as e:
			print(f"Error when adding {name} to Courses: {e}")
			self.con.rollback()
	
	def read_course(self, course_id):
		try:
			self.cursor.execute("SELECT id, name FROM Courses WHERE id=?", (course_id,))
	

	def close(self):
		try:
			self.con.close()
		except sqlite3.Error as e:
			print(f"Error when trying to close the database: {e}")
