
### Tasks:
- [x] Add full implementation for `create_course` (works).
- [x] Add continuous request for input.
- [x] Add help command for the user to see a list of available commands.
- [x] Add the remaining queries in `database_manager.py`
  - [x] Add `read_course` query in `database_manager.py`.
  - [x] Add `view_course` query.
  - [x] Add `update_course` query.
  - [x] Add `remove_course` query.
- ![ ] Add a third column in the `Courses` table in `database_manager` that displays the number of linked sessions to each course.
- [ ] Add `try-except` blocks where needed.
- [x] Adapt `session.py`: Add the `__str__` function.
- [x] Replace # comments with docstrings
- [x] Add a remove all command that empties the table (for courses and sessions)
- ![ ] Finalize README.md file
- ![ ] Replace variables with constants where possible

### Extra's I can do
- ![ ] Add a count courses and count sessions that counts the amount of courses and sessions

### Viewing functionality:
- [x] Viewing a course with an `id` as a parameter shows: `id`, `name`, (amount of sessions).
- [x] Viewing a course with no parameters shows all courses.
- [x] Viewing a session with an `id` as a parameter shows: `id`, `course id` (name?), `date` (check format), `subject`, `status`, `hours`.
- [x] Viewing a session with `course_id` as a parameter shows all sessions for that course.
- [x] Viewing a session with `date` as a parameter shows all sessions for that date.
- [x] Viewing a session with `status` as a parameter shows all sessions with that status.
- [x] Viewing a session with no parameters shows all sessions.

## Important to fix:
- [x] Removing a course gives an error but closes the application. Make sure you stay in the application after removing a course.
-	[x] 'add course' does not take multiple strings as one course name
		Enter your command: add course Programming in Python
		ID: 7 Course Programming added
		Enter your command: view course
		4 | Biologie
		7 | Programming
- [x] 'update session [session_id] hours "something" -> allows string meanwhile only numbers are allowed
		Enter your command: update session 6 hours something
		Column 'hours'' in Session 6 updated to 'something'

		   id  course_id date_created  subject status      hours
		0   6          2   03-12-2024  Nothing      d  something
- [x] CSV extension missing
- [] when removing course -> all sessions from that course needs to be removed
- [x] check `remove db` function on windows (theres an error)
