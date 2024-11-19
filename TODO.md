
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
- [x] Add a remove all command that empties the table (for courses and sessions)

### Extra's I can do
- [ ] Add a count courses and count sessions that counts the amount of courses and sessions
- [ ] When clearing tables, prompt the user if they wanna export the data first

### Viewing functionality:
- [ ] Viewing a course with an `id` as a parameter shows: `id`, `name`, (amount of sessions).
- [ ] Viewing a course with no parameters shows all courses.
- [ ] Viewing a session with an `id` as a parameter shows: `id`, `course id` (name?), `date` (check format), `subject`, `status`, `hours`.
- [ ] Viewing a session with `course_id` as a parameter shows all sessions for that course.
- [ ] Viewing a session with `date` as a parameter shows all sessions for that date.
- [ ] Viewing a session with `status` as a parameter shows all sessions with that status.
- [ ] Viewing a session with no parameters shows all sessions.

## Important to fix:
- [x] Removing a course gives an error but closes the application. Make sure you stay in the application after removing a course.
-	[x] 
		Enter your command: add course Programming in Python
		ID: 7 Course Programming added
		Enter your command: view course
		4 | Biologie
		7 | Programming
