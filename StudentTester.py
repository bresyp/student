import random
import string


from Student import Student
from Student import StudentListUtilities
from array import Array


def main():
    s1 = Student("Jacob", 12)
    try:
        s1.phone = create_number()
    except ValueError:
        print("s1 phone invalid")
    try:
        s1.address = random_address()
    except ValueError:
        print(f"s1  address invalid")

    s2 = Student("JP", 10)
    try:
        s2.phone = create_number()
    except ValueError:
        print("s2 phone number invalid")
    try:
        s2.address = random_address()
    except ValueError:
        print(f"s2 address invalid")

    students = [s1, s2]

    classes = ["Bio", "Math Analysis", "AP Gov", "Econ", "AP Lang",
               "AP Spanish Lit", "Writing for College", "US History",
               "World History", "CS"]

    for i in range(Array.DEFAULT_SIZE):
        rand_class = random.choice(classes)
        classes.remove(rand_class)
        try:
            students[i].add_class(i, rand_class)
        except (IndexError, ValueError, TypeError):
            print("Your class name or period num were invalid")

    print(StudentListUtilities.to_string(students))


def create_number():
    """ makes a random phone number"""
    phone_num = [random.randint(0, 9) for _ in range(10)]
    for i in range(10):
        phone_num[i] = f"{phone_num[i]}"
    phone_num = "".join(phone_num)
    return phone_num


def random_address():
    """ create random address"""
    house = "".join([str((random.randint(0, 9)) for _ in range(4))])
    street = "".join([str(random.choice(string.ascii_lowercase)) for _ in range(random.randint(4, 9))])
    street_letter = f"{random.choice(string.ascii_uppercase)}"
    street = street_letter + street
    apt_num = "".join([str((random.randint(1, 9)) for _ in range(random.randint(1, 3)))])
    return int(house), street, apt_num


main()


