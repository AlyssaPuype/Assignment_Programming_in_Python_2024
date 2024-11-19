import sqlite3
import pandas as pd #using pandas for read queries


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


	"""CREATE"""
	"""adds a course when given a name as parameter"""
	def create_course(self, name: str) -> Course:	
		self.cursor.execute("INSERT INTO Courses (name) VALUES (?)", (name,))
		self.con.commit()
		if self.cursor.rowcount > 0:
			return Course(self.cursor.lastrowid, name)
		else:
			return None


	"""READ"""
	"""gets info about the course when given a course_id as parameter"""
	def read_course(self, course_id: int) -> pd.DataFrame:
		query = "SELECT id, name FROM Courses WHERE id=?"
		df = pd.read_sql_query(query, self.con, params=(course_id,))
		if df.empty:
			return None
		return df
			
	"""
	if no parameters are given, the command displays a list of all added courses.
	"""
	def read_all_courses(self) -> pd.DataFrame:
		query = "SELECT * FROM Courses"
		df = pd.read_sql_query(query, self.con)
		if df.empty:
			return None
		return df


	"""UPDATE"""
	"""updates the name of a course"""
	def update_course(self, course_id: int, course_new_name: str) -> bool:
		self.cursor.execute("UPDATE Courses SET name=? WHERE id=?", (course_new_name, course_id))
		self.con.commit()
		if self.cursor.rowcount > 0:
			return True
		else:
			return False

	"""DELETE"""
	def delete_course(self, course_id: int) -> bool:
		self.cursor.execute("DELETE FROM Courses WHERE id=?", (course_id,))
		self.con.commit()
		if self.cursor.rowcount > 0:
			return True
		else:
			return False


	def delete_all_courses(self) -> bool:
		self.cursor.execute("DELETE FROM Courses")
		self.cursor.commit()
		if self.cursor.rowcount > 0:
			return True
		else:
			return False


	"""close the connection"""
	def close(self) -> None:
		try:
			self.con.close()
		except sqlite3.Error as e:
			print(f"Error when trying to close the database: {e}")
