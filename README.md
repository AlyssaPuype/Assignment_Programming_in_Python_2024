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
5. Install the requirements with `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
6. Run the file with `python main.py` or `python3 main.py`

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
- `view session`: 
- `export session [csv]/[excel] [file name]`: Exports all data to CSV or Excel file with given file name. All arguments required.


