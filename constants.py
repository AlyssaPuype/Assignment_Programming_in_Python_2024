"""
TABLES & COLUMNS
"""

COURSE_TABLE_NAME = "Courses"
COURSE_COLUMNS = {
	"ID" : "id",
	"NAME" : "name"
}

SESSION_TABLE_NAME = "Sessions"
SESSION_COLUMNS = {
	"ID": "id",
	"COURSE_ID": "course_id",
	"DATE_CREATED": "date_created",
	"SUBJECT": "subject",
	"STATUS": "status",
	"HOURS": "hours"

}