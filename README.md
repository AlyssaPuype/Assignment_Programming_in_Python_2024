# Study Tracker application

The application is used to track your studyprogress, by adding courses and studysessions. 
You can then edit and export your sessions into a csv or excel file.
You can also add and remove and view sessions and courses.

### How to install:

- clone the repository with git clone https://github.com/AlyssaPuype/Assignment_Programming_in_Python_2024
- navigate to the project folder Assignment_Programming_Python_2024
- there are no requirements to install.
- run main.py

### How to use:



### Notes for myself (delete or adapt after):

- Database manager = handles how the interaction w the database is done, so the actual queries
- Application manager = handles what is done (add, remove, edit, view,...)
- interaction flow: *User -> main.py -> application_manager -> database_manager -> database*


## TODO:

[x] add full implementation for create_course (works)
[x] add continuous request for input 
[x] add help command for the user to see a list of available commands

[ ] add the remaining queries in database_manager.py
[ ] add the remaining methods in application_manager.py
[ ] add a third column in the table Courses in database_manager that displays the amount of linked sessions to each course
[ ] add try-excepts where needed
[ ] adapt session.py: add the __str__ function
[ ] viewing a course with id as parameter shows : id, name (, amount of sessions)
		viewing course with no parameters shows all courses
[ ] viewing a session with id as parameter shows: id, course id (name?), date (check format), subject, status, hours 
		viewing session with course_id as parameter shows all sessions for that course
		viewing session with date as parameter shows all sessions for that date
		viewing session with status as parameter shows all sessions with that status
		viewing session with no parameters shows all sessions
