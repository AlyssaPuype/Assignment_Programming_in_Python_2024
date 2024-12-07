"""Manage the database for the study tracker application"""

import sqlite3
import pandas as pd
import os

from app.models.course import Course
from app.models.session import Session
from config.configuration import DATABASE_NAME,DATABASE_PATH

class DatabaseManager:

	def __init__(self, db_name=DATABASE_NAME) -> None:

		self.db_path = os.path.join(DATABASE_PATH, db_name)

		if not os.path.exists(DATABASE_PATH):
			self.db_path = DATABASE_NAME
			print(f"Invalid path given. Database created in {os.getcwd()}")

		try:
			self.con = sqlite3.connect(self.db_path)
			self.cursor = self.con.cursor()
			self.create_tables()
		except sqlite3.Error as e:
			print(f"Error when trying to connect to {self.db_path} : {e}")
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
			        start_date TEXT NOT NULL,
			        subject TEXT NOT NULL,
			        status TEXT CHECK(status IN ('td', 'ip', 'd')),
			        hours REAL NOT NULL,
			        FOREIGN KEY (course_id) REFERENCES Courses(id)
			    );
			""")

			self.con.commit()

		except sqlite3.Error as e:
			print(f"Error when creating tables: {e}")
			self.con.rollback() 


	"""___COURSES___"""

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
		self.con.commit()
		if self.cursor.rowcount > 0:
			return True
		else:
			return False


	"""___SESSIONS___"""

	"""CREATE"""
	def create_session(self, course_id: int, start_date: str, subject: str, status: str, hours: float) -> Session:
		self.cursor.execute("INSERT INTO Sessions (course_id, start_date, subject, status, hours) VALUES(?,?,?,?,?)", (course_id, start_date, subject, status, hours))
		self.con.commit()
		if self.cursor.rowcount > 0:
			return Session(self.cursor.lastrowid, course_id, start_date, subject, status, hours)
		else:
			return None

	"""READ"""
	def read_session(self, session_id: int) -> pd.DataFrame:
		"""
		reads a single session
		"""
		query = "SELECT * FROM Sessions WHERE id=?"
		df = pd.read_sql_query(query, self.con, params=(session_id,))
		if df.empty:
			return None
		return df

	"""read all session for a specified course"""
	def read_all_sessions_for_course(self, course_id: int) -> pd.DataFrame:
		"""
		reads all sessions, linked to the given course_id
		"""
		query = "SELECT * FROM Sessions WHERE course_id=?"
		df = pd.read_sql_query(query, self.con, params=(course_id,))
		if df.empty:
			return None
		return df

	"""read all sessions"""
	def read_all_sessions(self) -> pd.DataFrame:
		"""
		reads all sessions from Session table
		"""
		query = "SELECT * FROM Sessions"
		df = pd.read_sql_query(query, self.con)
		if df.empty:
			return None
		return df

	"""read all sessions for date today"""
	def read_all_session_today(self) -> pd.DataFrame:
		query = "SELECT * FROM Sessions WHERE start_date = strftime('%d-%m-%Y', DATE('now'))"
		df = pd.read_sql_query(query, self.con)
		if df.empty:
			return None
		return df

	"""read all sessions for specified status"""
	def read_all_session_for_status(self, status: str) -> pd.DataFrame:
		query = f"SELECT * FROM Sessions WHERE status=?"
		df = pd.read_sql_query(query, self.con, params=(status,))
		if df.empty:
			return None
		return df

	"""UPATE"""
	def update_session(self, session: pd.DataFrame, column_name: str, new_content: str) -> bool:
		session_id = int(session.loc[0,"id"])
		query = f"UPDATE Sessions SET {column_name}=? WHERE id=?"
		self.cursor.execute(query,(new_content, session_id))
		self.con.commit()
		if self.cursor.rowcount > 0:
			return True
		else:
			return False

	"""DELETE"""
	def delete_session(self, session_id: int) -> bool:
		self.cursor.execute("DELETE FROM Sessions WHERE id=?", (session_id,))
		self.con.commit()
		if self.cursor.rowcount > 0:
			return True
		else:
			return False

	def delete_all_sessions(self) -> bool:
		self.cursor.execute("DELETE FROM Sessions")
		self.con.commit()
		if self.cursor.rowcount > 0:
			return True
		else:
			return False


	"""___DATABASE___"""

	"""show path of the databse"""
	def show_path(self) -> str:		
		return os.path.abspath(self.db_path)

	def remove_db(self) -> str:
		try:
			os.remove(self.db_path)
			return DATABASE_NAME
		except Exception as e:
			print(f"Error when trying to remove database: {e}")


	"""___CLOSE___"""
	"""close the connection"""
	def close(self) -> None:
		try:
			self.con.close()
		except sqlite3.Error as e:
			print(f"Error when trying to close the database: {e}")

	

