
"""importing all necessary modules"""
from app.application_manager import StudyTracker
from app.database_manager import DatabaseManager

database = DatabaseManager()
tracker = StudyTracker(database)

tracker.show_welcome_message()

"""
Using While True for continious input unless the user types 'exit'
"""
while True:
	command = input("Enter your command: ")

	if command == "exit":
		break

	if command == "help":
	    tracker.show_commands()

	else:
		command_args = command.split()

		"""
		Arguments need to be minimum 2
		"""
		if len(command_args) < 2:
			print("Unknown command. Type 'help' to see the list of commands")
			continue

		"""
		action_name refers to what the user want to do
		model_name refers to what model the user want to perform the action on. Can only be 'Course' or 'Session'
		command_args refers to arguments needed for each function
		"""	
		action_name = command_args[0]
		model_name = command_args[1]
		command_args = command_args[2:]

		if model_name == "course":
		    match action_name:
		        case "add":
		            tracker.add_course(command_args)
		        case "remove":
		            tracker.remove_course(command_args)
		        case "view":
		            tracker.view_course(command_args)
		        case "update":
		            tracker.update_course(command_args)
		        case "export":
		        	tracker.export_course(command_args)
		        case _:
		        	print("Unknown command. Type 'help' to see the list of commands")
		elif model_name == "session":
		    match action_name:
		        case "add":
		            tracker.add_session(command_args)
		        case "remove":
		            tracker.remove_session(command_args)
		        case "view":
		            tracker.view_session(command_args)
		        case "update":
		            tracker.update_session(command_args)
		        case "export":
		        	tracker.export_session(command_args)
		        case _:
		        	print("Unknown command. Type 'help' to see the list of commands")
		elif model_name == "db":
			match action_name:
				case "remove":
					tracker.remove_database()
				case "path":
					tracker.show_path_database()

		else:
			print("Unknown command. Type 'help' to see the list of commands")

