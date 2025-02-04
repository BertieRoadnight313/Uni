#Task 1
name = input("Enter your name: ")
print("Hello, " + name + " .Good to meet you")

#Task 2
cent = int(input("Enter the temperature in Celsius: "))
fahr = cent * 9/5 + 32
print(cent, "C. Is equivalent to ", fahr,"F")

#Task 3
students = int(input("Enter the number of students: "))
group_size = int(input("Enter the size of the lab group: "))
left_over = students % group_size 
full_groups = students // group_size 
print("There are", full_groups, "full lab groups and", left_over, "students left over.")

#Task 4
pupils = int(input("Enter the number of students: "))  
total_sweets = int(input("Enter the total number of sweets: "))
sweets_per_pupil = total_sweets // pupils
sweets_left_over = total_sweets % pupils
print("Each student will get", sweets_per_pupil, "sweets and there will be", sweets_left_over, "sweets left over.")
