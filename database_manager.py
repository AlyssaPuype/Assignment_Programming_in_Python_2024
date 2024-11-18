import sqlite3

from models.course import Course
from models.session import Session

"""Manage the database for the study tracker application"""

class DatabaseManager:
	
	def __init__(self, db_name="StudyTracker.db") -> None:
		try:
			self.con = sqlite3.connect(db_name)
			self.cursor = self.con.cursor()
			self.create_tables()
		except sqlite3.Error as e:
			print(f"Error when trying to connect to {db_name} : {e}")
			raise


	def create_tables(self) -> None:
		try:
			self.cursor.execute("""
				CREATE TABLE IF NOT EXISTS Courses (
			    	id INTEGER PRIMARY KEY AUTOINCREMENT,
			    	name TEXT UNIQUE NOT NULL
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
			print(f"Error when creating tables: {e}")
			self.con.rollback()


	"""queries"""

	"""adds a course when given a name as parameter"""
	def create_course(self, name: str) -> Course:
		try:
			self.cursor.execute("INSERT INTO Courses (name) VALUES (?)", (name,))
			self.con.commit()
			return Course(self.cursor.lastrowid, name)
		except sqlite3.Error as e:
			print(f"Error when adding {name} to Courses: {e}")
			self.con.rollback()

	"""gets info about the course when given a course_id as parameter"""
	def read_course(self, course_id: int) -> Course:
		try:
			self.cursor.execute("SELECT id, name FROM Courses WHERE id=?", (course_id,))
			row_result = self.cursor.fetchone()
			if row_result:
				return Course(row_result[0], row_result[1])
			else:
				print(f"No course found with ID: {course_id}")
				return None
		except sqlite3.Error as e:
			print(f"Error when reading {course_id}: {e}")
			self.con.rollback()

	"""if no parameters are given, the command should display a list of all added courses.
	   if no courses are found, a message is shown
	"""
	def read_all_courses(self) -> None:
		try:
			self.cursor.execute("SELECT * FROM Courses")
			show_result = self.cursor.fetchall()
			if show_result:
				for row in show_result:
					print(f"{row[0]} | {row[1]}")
			else:
				print("No courses were found")
		except sqlite3.Error as e:
			print(f"Error when reading all courses: {e}")
			self.con.rollback()

	def update_course(self, course_id: int):
		pass

	def delete_course(self, course_id: int) -> None:
		try:
			self.cursor.execute("DELETE FROM Courses WHERE id=?", (course_id,))
			self.con.commit()

			#row count return the amount of affected rows in last query, so we check if it was indeed removed, if not, means it did not exists:
			if self.cursor.rowcount > 0 :
				print(f"Course with ID {course_id} has been succesfully removed")
			else:
				print(f"No courses found to remove with ID: {course_id}")

		except sqlite3.Error as e:
			print(f"Error when deleting course with ID: {course_id}: {e}")
			self.con.rollback

	"""lose the connection"""
	def close(self) -> None:
		try:
			self.con.close()
		except sqlite3.Error as e:
			print(f"Error when trying to close the database: {e}")
