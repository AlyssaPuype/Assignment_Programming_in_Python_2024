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
### Completed tasks:
- [x] Add full implementation for `create_course` (works).
- [x] Add continuous request for input.
- [x] Add help command for the user to see a list of available commands.

### Remaining tasks:
- [ ] Add the remaining queries in `database_manager.py`
  - [x] Add `read_course` query in `database_manager.py`.
  - [x] Add `view_course` query.
  - [x] Add `remove_course` query.
- [ ] Add the remaining methods in `application_manager.py`.
- [ ] Add a third column in the `Courses` table in `database_manager` that displays the number of linked sessions to each course.
- [ ] Add `try-except` blocks where needed.
- [ ] Adapt `session.py`: Add the `__str__` function.

### Viewing functionality:
- [ ] Viewing a course with an `id` as a parameter shows: `id`, `name`, (amount of sessions).
- [ ] Viewing a course with no parameters shows all courses.
- [ ] Viewing a session with an `id` as a parameter shows: `id`, `course id` (name?), `date` (check format), `subject`, `status`, `hours`.
- [ ] Viewing a session with `course_id` as a parameter shows all sessions for that course.
- [ ] Viewing a session with `date` as a parameter shows all sessions for that date.
- [ ] Viewing a session with `status` as a parameter shows all sessions with that status.
- [ ] Viewing a session with no parameters shows all sessions.

## Important to fix:
- [ ] Removing a course gives an error but closes the application. Make sure you stay in the application after removing a course.

---
[ ] 
		Enter your command: add course Programming in Python
		ID: 7 Course Programming added
		Enter your command: view course
		4 | Biologie
		7 | Programming
	
