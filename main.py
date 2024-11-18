
# importing all necessary modules
from application_manager import StudyTracker
from database_manager import DatabaseManager

database = DatabaseManager()
tracker = StudyTracker(database)


print("Welcome to study tracker!")
print("To see the list of commands, type 'help'")

while True:
	command = input("Enter your command: ")

	if command == "exit":
		break

	if command == "help":
	    tracker.show_commands()

	else:
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
		        case "view":
		            tracker.getCourse(command_args)
		        case "update":
		            tracker.updateCourse(command_args)
		elif course_name == "session":
		    match action_name:
		        case "add":
		            tracker.addSession(command_args)
		        case "remove":
		            tracker.removeSession(command_args)
		        case "view":
		            tracker.getSession(command_args)
		        case "update":
		            tracker.updateSession(command_args)
		else:
			print("Unknown command. Type /help to see the list of commands")
