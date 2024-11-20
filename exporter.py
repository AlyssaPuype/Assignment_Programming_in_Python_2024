# module for exporting data to csv or excel files, using pandas

import pandas as pd 

from database_manager import DatabaseManager

class Export:

	def __init__(self, db: DatabaseManager) -> None:
		self.db = db

	def export_to_csv(self, name_file: str) -> None:
		"""
		Exports data into csv file 

		Needs filename as argument
		Uses method from database_manager to fetch the data
		"""
	
		current_data = self.db.read_all_courses()
		df = pd.DataFrame(current_data)
		df.to_csv(name_file, index=False)

	def export_to_excel(self,name_file: str) -> None:
		"""
		Exports data into excel file 

		Needs filename as argument
		Uses method from database_manager to fetch the data
		Checks if the file ends with extension .xlsx
		Openpyxl is required to be installed. Check requirements.txt
		"""
	
		current_data = self.db.read_all_courses()
		df = pd.DataFrame(current_data)
		if not name_file.endswith(".xlsx"):
			name_file += ".xlsx"
			df.to_excel(name_file, index=False)