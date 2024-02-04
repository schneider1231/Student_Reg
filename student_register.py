def write_register(reg_form):
    """
    Function to create a register in txt file format, getting input from the 
    user for number of students in the class and their student ID's
    """
    # Gets number of students
    
    student_amount = int(input("Enter number of students: "))
    # opens txt file to write in the name of the parameter 

    file = open(reg_form + '.txt', 'w')
    file.write("------Class Register------\n")

    # loops through number of students

    for student in range(student_amount):
        student_id = input("Enter student ID: ") # Enter student id's
        file.write(student_id + "\n") # writes id's onto "reg_form".txt
        file.write(".................................\n") # write dotted line       
    file.close() # close .txt file


write_register("reg_form")