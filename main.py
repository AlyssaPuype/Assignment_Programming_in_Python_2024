# integrating all modules, user interface interaction

from application_manager import StudyTracker
from database_manager import DatabaseManager

database = DatabaseManager()
tracker = StudyTracker(database)


command = input("what is your command: ")
command_args = command.split()


action_name = command_args[0]
course_name = command_args[1]
command_args = command_args[2:]

if course_name == "course":
    match action_name:
        case "add":
            tracker.add_course(command_args)
        case "remove":
            tracker.remove_course(command_args)
        case "get":
            tracker.getCourse(command_args)
        case "update":
            tracker.updateCourse(command_args)
elif course_name == "session":
    match action_name:
        case "add":
            tracker.addSession(command_args)
        case "remove":
            tracker.removeSession(command_args)
        case "get":
            tracker.getSession(command_args)
        case "update":
            tracker.updateSession(command_args)

