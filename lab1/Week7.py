"""
e_mail = input("What is the e-mail?: ")
mail = "ceng113@example.com"
e_mail = e_mail.lower()

a,b = e_mail.split("@")
a = a.replace(".", "")

last_mail = (a+"@"+b)

if last_mail == mail:
    print("You successfully logged in!!!")
else:
    print(":(")





email = input("Please enter an email address:")
ref_mail = "ceng113@example.com"
if "@" in email:

    email = email.lower()

    part_1 = email.split("@")[0]

    part_1 = part_1.replace(".", "")

    part_2 = email.split("@")[1]

    email = part_1 + "@" + part_2
    print(email)
if email == ref_mail:
    print("Equal")
else:
    print("Not equal")
else:
    print("Not equal")




student_grades = []
student_id = []

i_range = int(input("How many students are there?: "))
for i in range(i_range):
    student_id.append(input("what is the student's id: "))
    for n in range(3):
        student_grades.append([int(input("what are the grades?: "))])
print(student_grades,student_id)


"""






grade_list = []



n_st = int(input("Please enter number of students:"))



for i in range(n_st):

    print("Student ", str(i+1))

    mid_1 = int(input("Midterm 1:"))
    mid_2 = int(input("Midterm 2:"))
    f_grade = int(input("Final:"))
    grade_list.append([mid_1,mid_2,f_grade])



print(grade_list)



avg_grades = []



for sub_grades in grade_list:

    avg_grades.append(sub_grades[0]*0.3 + sub_grades[1]*0.3 + sub_grades[2]*0.4)



print(avg_grades)


