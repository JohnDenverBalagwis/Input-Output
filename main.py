print("--------------------------------------------------")
print("             FILL UP THE FORM !                   ")
print("--------------------------------------------------")

name = input("Enter your name: ")
course = input("Enter your course: ")
year_and_section = input("Enter your Year and Section: ")
id_number = input("Enter your ID Number: ")
type_of_device = input("Enter the type of your device eg. Laptop/Smartphone: ")
brand = input("Enter the brand: ")
device_model = input("Enter device model: ")

print("--------------------------------------------------")
print("             M Y  P R O F I L E !                 ")
print("--------------------------------------------------")


def myfunc():
    print("Student Name: " + name)
    print("Course: " + course)
    print("Year and Section: " + year_and_section)
    print("ID Number: " + id_number)
    print("My device laptop is a " + type_of_device)
    print("It's brand is " + brand)
    print("It's model is " + device_model)


myfunc()

print("--------------------------------------------------")
print("              T H A N K  Y O U !                  ")
print("--------------------------------------------------")