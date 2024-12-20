# Study Tracker Application

### Description:
The application is used to track your studyprogress. You can add courses and then add sessions to these courses. 
You can add, remove, edit and view elements from the tables.
You can also export the tables `Courses` and `Sessions` to a csv or excel file.

## How to install:

1. Clone the repository with `git clone https://github.com/AlyssaPuype/Assignment_Programming_in_Python_2024` in the folder you want the project to be
2. Navigate inside the project folder `cd Assignment_Programming_Python_2024`
3. Create a virtual environment with `python -m venv myvenv` or `python3 -m venv myvenv`
4. Activate the virtual environment with `source myvenv/bin/activate` on macOS/Linux or `myvenv\Scripts\activate` on Windows
5. Install the requirements with `pip install -r requirements.txt` or `pip3 install -r requirements.txt`. Check with `pip list`
6. Open `config/configuration.py` and adapt DATABASE_NAME and DATABASE_PATH if you like. If the path is invalid, the database will be located inside this projectfolder
7. Run the script with `python3 main.py` or `python main.py`

## Commands explained:

Courses:

- `add course [course name]` : Adds new course with name given. Argument required.
- `remove course [course id]` : Removes course with given id. When no parameter is given: prompts the user to clear table
- `edit course [course id] [new course name]` : Updates name of course with given id to new given name. All Arguments required.
- `view course [course id]`: Displays course with given id. When no parameter is given: displays all courses
- `export course [csv]/[excel] [file name]`: Exports all data to csv or excel file with given file name. All arguments required.

Sessions:

- `add session`:
- `remove session [session id]`: Removes session with given id. When no parameter is given: prompts the user to clear table.
- `edit session`: 
- `view session`: Displays session with given id. Use 'help' to see what arguments you can pass. No arguments prins all sessions, ordered by ascending `start_date`
- `export session [csv]/[excel] [file name]`: Exports all data to CSV or Excel file with given file name. All arguments required.

Database:
- `path db`: shows the path of the database
- `remove db`: deletes the database, asks for confirmation

## Files explained:

- **database_manager.py**: Module containing code that interacts with the database itself.
Imported modules: `sqlite3`, `pandas` and from models: `course.py`, `session.py`.
Imported by `application_manager` and `main.py`.
- **application_manager.py**: Module containing code that interacts with `database_manager`.
Imported modules: `datetime`, `database_manager`, `exporter`.
Imported by `main.py`.
- **main.py**: Executable file containing code that interacts with `application_manager` and the user via terminal.
- **models/course.py**: Module defining course object.
Imported by `database_manager`.
- **models/session.py**: Module defning session object.
Imported by `database_manager`
- **exporter.py**: Module containing functions to export database to csv or excel.
Imported by `application_manager`.
- **requirements.txt**: File containing all the required packages.
- **configuration.py**: Module containing database name, database path and status values. If path is invalid, current directory will be used as location for the database



