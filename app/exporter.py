# module for exporting data to csv or excel files, using pandas

import pandas as pd 

from app.database_manager import DatabaseManager

class Export:

	def __init__(self, db: DatabaseManager) -> None:
		self.db = db

	def _export_data(self, data: list, name_file: str, file_type: str) -> None:
		"""
		Exports data to CSV or Excel
		"""
		df = pd.DataFrame(data)

		if file_type == "csv":
			df.to_csv(f"{name_file}.csv", index=False)
		elif file_type == "excel":
			if not name_file.endswith(".xlsx"):
				name_file += ".xlsx"
			try:
				df.to_excel(name_file, index=False, engine="openpyxl")
			except ImportError:
				print("Error: openpyxl is required to export to Excel.")
				return

	def export_course(self, name_file: str, file_type: str) -> None:
		"""
		Exports course data to the specified file type (CSV or Excel)
		"""
		current_data = self.db.read_all_courses()
		self._export_data(current_data, name_file, file_type)

	def export_session(self, name_file: str, file_type: str) -> None:
		"""
		Exports session data to the specified file type (CSV or Excel)
		"""
		current_data = self.db.read_all_sessions()
		self._export_data(current_data, name_file, file_type)