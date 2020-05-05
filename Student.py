from array import Array


class Student:
    """ class constants """
    OG_DEFAULT_YEAR = 10
    MIN_YEAR = 0
    MAX_YEAR = 12
    ORIGINAL_DEFAULT_GPA = 1
    DEFAULT_NAME = "No Name"
    DEFAULT_DATE = "1/1/2000"

    """ class variable """
    next_id = 0
    default_year = OG_DEFAULT_YEAR
    default_gpa = ORIGINAL_DEFAULT_GPA
    default_classes = []

    def __init__(self, name=None, year=None, gpa=None):
        """ Initialize the student tracker"""
        self._classes = []
        if year is None:
            year = Student.default_year
        try:
            self.year = year
        except ValueError:
            self._year = Student.default_year

        if name is None:
            name = Student.DEFAULT_NAME
        try:
            self.name = name
        except TypeError:
            self._name = Student.DEFAULT_NAME

        if gpa is None:
            gpa = Student.default_gpa
        try:
            self.gpa = gpa
        except ValueError:
            self._gpa = self.default_gpa

        Student.update_next_id()
        self._id = Student.get_next_id()

        self._phone = self.PhoneNumber()

        self._address = self.Address()

        self._date = self.Date()

        self._classes = Array()

    def __str__(self):
        return f"Student ID: {self._id}, Name: {self._name}, Year: {self._year}, Phone: {self._phone}" \
               f" Address: {self._address} \n"

    @property
    def classes(self):
        """Gets self._classes"""
        return f"{self._classes}"

    def add_class(self, period, new_class):
        """Adds a class to the array in the Array class"""
        self._classes[period] = new_class

    @property
    def year(self):
        """ gets the year"""
        return self._year

    @year.setter
    def year(self, new_year):
        """ sets the final year"""
        if self.valid_year(new_year):
            self._year = new_year
        else:
            raise ValueError

    @classmethod
    def valid_year(cls, new_year):
        """ makes sure the year is valid AKA sanity checking"""
        if Student.MIN_YEAR <= new_year <= Student.MAX_YEAR:
            return True
        return False

    @classmethod
    def get_default_year(cls):
        """ gets the default year"""
        return cls.default_year

    @classmethod
    def set_default_year(cls, new_default_year):
        """ allows the used to change the default year"""
        valid_year = cls.valid_year(new_default_year)
        if valid_year:
            cls.default_year = new_default_year
        if valid_year == ValueError:
            cls.default_year = Student.default_year

    @property
    def name(self):
        """ gets the name"""
        return self._name

    @name.setter
    def name(self, new_name):
        """exception handling"""
        if type(new_name) is not str:
            raise TypeError
        else:
            self._name = new_name

    @classmethod
    def get_next_id(cls):
        """gets the student id"""
        return Student.next_id

    @classmethod
    def update_next_id(cls):
        """ updates the student id"""
        cls.next_id += 1
        return cls.next_id

    @property
    def gpa(self):
        """ gets the gpa"""
        return self._gpa

    @gpa.setter
    def gpa(self, gpa_given):
        """GPA for the student"""
        if self.valid_gpa(gpa_given) is False:
            raise ValueError
        self._gpa = gpa_given

    @classmethod
    def valid_gpa(cls, gpa_given):
        """Checks to see if the given gpa is valid"""
        if type(gpa_given) == float:
            return True
        else:
            return False

    @staticmethod
    def which_student_earlier(s1, s2):
        """ checks which student came earlier """
        if s1.year == s2.year:
            if s1.name > s2.name:
                return s1
            else:
                return s2

        if s1.year > s2.year:
            return s2
        else:
            return s1

    def same_grade(self, other):
        """ checks if it is the same year """
        if self.year == other.year:
            return True
        else:
            return False

    def __gt__(self, other):
        """ checks which student came older """
        if self.date.year == other.date.year:
            if self.date.month > other.date.month:
                return True
            if self.date.month < other.date.month:
                return False
            if self.date.month == other.date.month:
                if self.date.day > other.date.day:
                    return True
                else:
                    return False
        if self.year > other.year:
            return False
        else:
            return True

    @property
    def phone(self):
        """gets phone class"""
        return str(self._phone)

    @phone.setter
    def phone(self, new_number):
        """sets phone class"""
        self._phone = new_number

    class PhoneNumber:
        """ class constants"""
        DEFAULT_NUM = "0000000000"
        MAX_LEN = 20
        MIN_LEN = 10

        def __init__(self, number=DEFAULT_NUM):
            try:
                self.number = number
            except ValueError:
                self._number = self.DEFAULT_NUM

        @property
        def number(self):
            """ gets the year"""
            return self._number

        @number.setter
        def number(self, number):
            """ sets the final year"""
            if self.valid_number(number) is not None:
                self._number = self.valid_number(number)
            else:
                raise ValueError

        @property
        def set_number(self):
            """ gets the year"""
            return self._number

        @set_number.setter
        def set_number(self, new_num):
            """ allow user to change number"""
            if self.valid_number(new_num) is not None:
                print(f"from set {self.valid_number(new_num)}")
                self._number = new_num

        @classmethod
        def valid_number(cls, number):
            """ makes sure the year is valid AKA sanity checking"""
            if cls.MIN_LEN <= len(number) <= cls.MAX_LEN:
                new_num = cls.extract_digits(number)
                if len(new_num) == 10:
                    return new_num
            else:
                return None

        @staticmethod
        def extract_digits(number):
            """gives the digits of the string and takes everything else out"""
            num = "1234567890"
            digit_num = ""
            for char in number:
                if char in num:
                    digit_num += char
            return digit_num

        def __str__(self):
            """ returns the phone number nicely done """
            return f"({self._number[:3]}) {self._number[3:6]}-" \
                   f"{self._number[6:]}"

    @property
    def address(self):
        """ getter for the address class"""
        return f"{self._address.house} {self._address.street}," \
               f"#{self._address.apt}"

    @address.setter
    def address(self, new_address):
        """needed to unpack the tuples to get each part of address"""
        if type(new_address) is not tuple:
            raise ValueError
        house, street, apt = new_address
        self._address.house = house
        self._address.street = street
        self._address.apt = apt

    class Address:
        """ class constants"""
        DEFAULT_STREET = "No Street Given"
        DEFAULT_HOUSE = 1
        MIN_HOUSE = 1
        DEFAULT_APT = 1

        def __init__(self, house=DEFAULT_HOUSE, street=DEFAULT_STREET, apt=DEFAULT_APT):
            try:
                self.house = house
            except ValueError:
                self._house = self.DEFAULT_HOUSE

            try:
                self.street = street
            except TypeError:
                self._street = self.DEFAULT_STREET

            try:
                self.apt = apt
            except ValueError:
                self._apt = self.DEFAULT_APT

        @property
        def house(self):
            """ returns the house number"""
            return self._house

        @house.setter
        def house(self, house_num):
            """ allows user to set valid house number"""
            if house_num < self.MIN_HOUSE:
                raise ValueError
            self._house = house_num

        @property
        def street(self):
            """ returns the street"""
            return self._street

        @street.setter
        def street(self, street_name):
            """ allows user to set a valid street name"""
            if type(street_name) is str:
                self._street = street_name
            else:
                raise TypeError

        @property
        def apt(self):
            """ returns the apt number"""
            return self._apt

        @apt.setter
        def apt(self, apt_num):
            """ sets a valid value for apt number"""
            if apt_num < 1000:
                self._apt = apt_num
            else:
                raise ValueError

        def which_street_closer(self, other_address):
            """ distinguishes which street is closer alphabetically"""
            if self.street < other_address.street:
                return self.street
            else:
                return other_address.street

        def display(self):
            """displays the address"""
            print(self)

        def __str__(self):
            return f"{self._house} {self._street}, #{self._apt}\n"

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        date = new_date.split("/")
        assigned_month = date[0]
        assigned_day = date[1]
        assigned_year = date[2]
        self._date.day = assigned_day
        self._date.month = assigned_month
        self._date.year = assigned_year

    class Date:
        """class constants"""
        DEFAULT_MONTH = "1"
        DEFAULT_DAY = "1"
        DEFAULT_YEAR = "2000"
        DEFAULT_DATE = "1/1/2000"

        def __init__(self, assigned_month=DEFAULT_MONTH, assigned_day=DEFAULT_DAY, assigned_year=DEFAULT_YEAR):
            try:
                self.month = assigned_month
            except ValueError:
                self._month = self.DEFAULT_MONTH

            try:
                self.day = assigned_day
            except TypeError:
                self._day = self.DEFAULT_DAY

            try:
                self.year = assigned_year
            except ValueError:
                self._year = self.DEFAULT_YEAR

        @property
        def month(self):
            return self._month

        @month.setter
        def month(self, assigned_month):
            if 1 <= int(assigned_month) <= 12:
                self._month = assigned_month
            else:
                raise ValueError

        @property
        def day(self):
            return self._day

        @day.setter
        def day(self, assigned_day):
            if 1 <= int(assigned_day) <= 31:
                self._day = assigned_day
            else:
                raise ValueError

        @property
        def year(self):
            return self._year

        @year.setter
        def year(self, assigned_year):
            if 1990 <= int(assigned_year) <= 2020:
                self._year = assigned_year
            else:
                raise ValueError

        def display(self):
            """displays the birthday"""
            print(self)

        def __str__(self):
            return f"{self._month}/{self._day}/{self._year}"


class StudentListUtilities:
    """ class constants"""
    NOT_FOUND = "Not found"

    @staticmethod
    def to_string(students):
        all_results = ""
        for student in students:
            result = str(student)
            all_results += result
        return all_results

    @staticmethod
    def sort(students):
        for i in range(len(students) - 1):
            done = False
            for j in range(len(students) - i - 1):
                if students[j + 1] < students[j]:
                    students[j], students[j + 1] = students[j + 1], students[j]
                    done = True
            if not done:
                break
            else:
                pass
        return students

    @staticmethod
    def linear_search(students, name):
        for i in range(len(students)):
            if students[i].name == name:
                return i
        return StudentListUtilities.NOT_FOUND

    @staticmethod
    def binary_search(students, target):
        start = 0
        end = len(students) - 1
        return StudentListUtilities.binary_search_h(students, target, start, end)

    @staticmethod
    def binary_search_h(students, target, start, end):
        middle = (start + end) // 2
        middle_name = students[middle].name

        if middle_name == target:
            print("I have found it")
            return middle
        else:
            if middle_name > target:
                return StudentListUtilities.binary_search_h(students, target, start, middle - 1)
            if middle_name < target:
                return StudentListUtilities.binary_search_h(students, target, middle + 1, end)

    @staticmethod
    def selection_sort(students):
        length = len(students)
        for i in range(length):
            largest_index = StudentListUtilities.get_largest_index(students, length)
            length = length - 1
            sorted_end = students[largest_index]
            unsorted = students[length]
            students[largest_index] = unsorted
            students[length] = sorted_end

    @staticmethod
    def get_largest_index(students, length):
        max_name = students[0].name
        index = 0
        for i in range(length):
            if students[i].name > max_name:
                max_name = students[i].name
                index = i
        return index

    @staticmethod
    def insertion_sort(students):
        length = len(students)
        for i in range(1, length):
            unsorted = students[i]
            j = i - 1
            while unsorted < students[j] and j >= 0:
                students[j + 1] = students[j]
                j -= 1
            students[j + 1] = unsorted

    @classmethod
    def merge_sort(cls, students):
        length = len(students)
        if length > 1:
            mid = len(students) // 2
            first_half = students[:mid]
            second_half = students[mid:]
            cls.merge_sort(first_half)
            cls.merge_sort(second_half)
            first_half_index = 0
            second_half_index = 0
            student_index = 0
            while len(first_half) > first_half_index and len(second_half) > second_half_index:
                if second_half[second_half_index] > first_half[first_half_index]:
                    students[student_index] = first_half[first_half_index]
                    first_half_index += 1
                    student_index += 1
                else:
                    students[student_index] = second_half[second_half_index]
                    second_half_index += 1
                    student_index += 1
            while len(first_half) > first_half_index:
                students[student_index] = first_half[first_half_index]
                first_half_index += 1
                student_index += 1
            while len(second_half) > second_half_index:
                students[student_index] = second_half[second_half_index]
                second_half_index += 1
                student_index += 1
