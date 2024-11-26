# -------------------------------------------------------------------------- #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes with structured error
#       handling.
# Change Log: (Who, When, What)
#   R.Root, 01/01/2030, Created Script
#   N.Greco, 11/25/2024, Updated Script for Assignment07
# -------------------------------------------------------------------------- #
import json

# Data --------------------------------------------------------------------- #
FILE_NAME: str = "Enrollments.json"
MENU: str = """
----- Course Registration Program -----
  Select from the following menu:
   1. Register a Student for a Course
   2. Show Current Data
   3. Save Data to a File
   4. Exit the Program
---------------------------------------
"""

menu_choice: str     # Hold the choice made by the user.
students: list = []  # Holds a table of student data.


class Person:
    """
    A class for an individual person.

    Properties:
        first_name (str): The student's first name.
        last_name (str): The student's last name.

    ChangeLog: (Who, When, What)
    N.Greco, 11/25/2024, Created Class
    """

    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self) -> str:
        """
        Returns the course name.
        :return: The course name.
        """
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str) -> None:
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should only contain letters!")

    @property
    def last_name(self) -> str:
        """
        Returns the last name.
        :return: The last name.
        """
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str) -> None:
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should only contain letters!")

    def __str__(self) -> str:
        """
        The string function for Person.
        :return: The string values.
        """
        return f"{self.first_name}, {self.last_name}"


class Student(Person):
    """
    A class for a person who is also a student.

    Properties:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        course_name (str): The enrolled course name.

    ChangeLog: (Who, When, What)
    N.Greco, 11/25/2024, Created Class
    """

    def __init__(self, first_name: str = "", last_name: str = "", \
                 course_name: str = ""):
        super().__init__(first_name = first_name, last_name = last_name)
        self.course_name = course_name

    @property
    def course_name(self) -> str:
        """
        Returns the course name.
        :return: The course name.
        """
        return self.__course_name.title()

    @course_name.setter
    def course_name(self, value: str) -> None:
        self.__course_name = value

    def __str__(self) -> str:
        """
        The string function for Student.
        :return: The string values.
        """
        return f'{super().__str__()}, {self.course_name}'


# Processing ---------------------------------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files.

    ChangeLog: (Who, When, What)
    R.Root, 01/01/2030, Created Class
    N.Greco, 11/25/2024, Updated for Assignment07
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list) -> list:
        """
        This function reads data from a JSON file and loads it into a list of
        dictionary rows.

        ChangeLog: (Who, When, What)
        R.Root, 01/01/2030, Created Class
        N.Greco, 11/25/2024, Updated for Assignment07

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with data

        :return: list
        """

        try:
            file = open(file_name, "r")
            list_of_dictionary_data = json.load(file)
            for student in list_of_dictionary_data:
                st_temp = Student(first_name = student["FirstName"], \
                                  last_name = student["LastName"], \
                                  course_name = student["CourseName"])
                student_data.append(st_temp)
            file.close()
        except Exception as e:
            IO.output_error_messages(message = "Error: There was a problem" \
                    "with reading the file.", error = e)
        finally:
            if not file.close:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list) -> None:
        """
        This function writes data to a json file with data from a list of
        dictionary rows.

        ChangeLog: (Who, When, What)
        R.Root, 01/01/2030, Created Class
        N.Greco, 11/25/2024, Updated for Assignment07

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be written

        :return: None
        """

        try:
            list_of_dictionary_data: list = []
            for student in student_data:
                st_temp: dict = {"FirstName": student.first_name, \
                                 "LastName": student.last_name, \
                                 "CourseName": student.course_name}
                list_of_dictionary_data.append(st_temp)
            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
            file.close()
            IO.output_student_courses(student_data = student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another" \
                    " program."
            IO.output_error_messages(message = message, error = e)
        finally:
            if not file.close:
                file.close()


# Presentation -------------------------------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and
    output.

    ChangeLog: (Who, When, What)
    R.Root, 01/01/2030, Created Class
    R.Root, 01/02/2030, Added menu output and input functions
    R.Root, 01/03/2030, Added a function to display the data
    R.Root, 01/04/2030, Added a function to display custom error messages
    N.Greco, 11/25/2024, Updated for Assignment07
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None)-> None:
        """
        This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        R.Root, 01/03/2030, Created function
        N.Greco, 11/25/2024, Updated for Assignment07

        :param message: string with message data to display
        :param error: exception object with technical message to display

        :return: None
        """
        print(message, end="\n")
        if error is not None:
            print("\n----------- Technical Error Message -----------")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str) -> None:
        """
        This function displays the menu of choices to the user.

        ChangeLog: (Who, When, What)
        R.Root, 01/01/2030, Created function
        N.Greco, 11/25/2024, Updated for Assignment07

        :return: None
        """
        print(menu)

    @staticmethod
    def input_menu_choice() -> str:
        """
        This function gets a menu choice from the user.

        ChangeLog: (Who, When, What)
        R.Root, 01/01/2030, Created function
        N.Greco, 11/25/2024, Updated for Assignment07

        :return: string with the users choice
        """
        choice: str = "0"
        try:
            choice = input("What would you like to do? ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("\n!!! Please choose a menu option " \
                                    "(1, 2, 3, or 4). !!!")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def output_student_courses(student_data: list) -> None:
        """
        This function displays the student and course names to the user.

        ChangeLog: (Who, When, What)
        R.Root, 01/01/2030, Created function
        N.Greco, 11/25/2024, Updated for Assignment07

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        # Process the data to create and display a custom message
        print("-" * 60)
        for student in student_data:
            print(f"\t{student.first_name} {student.last_name} "\
                  f"is enrolled in {student.course_name}")
        print("-" * 60)

    @staticmethod
    def input_student_data(student_data: list) -> list:
        """
        This function gets the student's first name and last name, with a
        course name from the user.

        ChangeLog: (Who, When, What)
        R.Root, 01/01/2030, Created function
        N.Greco, 11/25/2024, Updated for Assignment07

        :param student_data: list of dictionary rows to be filled with data

        :return: list
        """

        try:
            student = Student()
            student.first_name = input("Enter the student's first name: ")
            student.last_name = input("Enter the student's last name: ")
            student.course_name = input("Please enter the course name: ")
            student_data.append(student)
            print()
            print(f"You have registered {student.first_name} " \
                    f"{student.last_name} for {student.course_name}.")
        except ValueError as e:
            IO.output_error_messages(message = "Incorrect type of data!", \
                                     error = e)
        except Exception as e:
            IO.output_error_messages(message = "There was a problem with " \
                                               "your entered data.", \
                                     error = e)
        return student_data

# Main body of script. Starts by reading in JSON file data.
students = FileProcessor.read_data_from_file(file_name = FILE_NAME, \
                                             student_data = students)

# Repeat the following tasks.
while True:

    # Present the menu of choices and request user selection.
    IO.output_menu(menu = MENU)
    menu_choice = IO.input_menu_choice()

    # Input user student data.
    if menu_choice == "1":
        students = IO.input_student_data(student_data = students)
        continue

    # Present the current student data.
    elif menu_choice == "2":
        IO.output_student_courses(student_data = students)
        continue

    # Save the data to a JSON file.
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name = FILE_NAME, \
                                         student_data = students)
        continue

    # Stop the loop and exit the program.
    elif menu_choice == "4":
        print("\n" + "-" * 35)
        print("*** Exiting Program. Thank you! ***")
        print("-" * 35)
        break