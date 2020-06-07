def conv_perc(perc):
    '''
    This function converts a grade on the percentage scale to BSD's 4 pt. Proficiency scale.
    Parameters: Percentage Grade
    Returns: Technically nothing, but prints out the Letter grade, the BSD scale grade, and the percentage scale grade.
    '''
    if perc >= 90.0:
        bsd = 0.06*(perc - 90) + 3.40
        print("\nLetter grade: A\nBSD grade:", round(bsd, 2), "\nPercentage grade:", perc, "%")
    else:
        if perc >= 80.0:
            bsd = 0.07*(perc - 80) + 2.7
            print("\nLetter grade: B\nBSD grade:", round(bsd, 2), "\nPercentage grade:", perc, "%")
        else:
            if perc >= 70.0:
                bsd = 0.07*(perc - 70) + 2.0
                print("\nLetter grade: C \nBSD grade:", round(bsd, 2), "\nPercentage grade:", perc, "%")
            else:
                if perc >= 60.0:
                    bsd = 0.07*(perc - 60) + 1.6
                    print("\nLetter grade: D\nBSD grade:", round(bsd, 2), "\nPercentage grade:", perc, "%")
                else:
                    bsd = (0.8 / 30)*(perc - 0) + 0
                    print("\nLetter grade: F\nBSD grade:", round(bsd, 2), "\nPercentage grade:", perc, "%")
                    
def conv_bsd(bsd):
    '''
    This function converts a grade on BSD's 4 pt. Proficiency scale to the percentage scale.
    
    Parameters: BSD Scale Grade
    Returns: Technically nothing, but prints out the Letter grade, the BSD scale grade, and the percentage scale grade.
    '''
    if bsd >= 3.4: #If the grade is in BSD's A range.
        perc = (bsd - 3.4)/0.06 + 90
        print("\nLetter grade: A\nBSD grade:", bsd, "\nPercentage grade:", round(perc, 2), "%")
    else:
        if bsd >= 2.7: #If the grade is in BSD's B range.
            perc = (bsd - 2.7)/0.07 + 80
            print("\nLetter grade: B\nBSD grade:", bsd, "\nPercentage grade:", round(perc, 2), "%")
        else:
            if bsd >= 2.0: #If the grade is in BSD's C range.
                perc = (bsd - 2.0)/0.07 + 70
                print("\nLetter grade: C\nBSD grade:", bsd, "\nPercentage grade:", round(perc, 2), "%")
            else:
                if bsd >= 1.6: #If the grade is in BSD's D range.
                    perc = (bsd - 1.6)/0.04 + 60
                    print("\nLetter grade: D\nBSD grade:", bsd, "\nPercentage grade:", round(perc, 2), "%")
                else:
                    #If the grade is in BSD's F range. Note: This allows a 0 on the BSD scale, which a student could theoretically get if they only got N's, and if N's are equivalent to 0, which I'm not sure of.
                    perc = (bsd - 0)/(0.8/30) + 0
                    print("\nLetter grade: F\nBSD grade:", bsd, "\nPercentage grade:", round(perc, 2), "%")

'''
def gpa_calc():
    A = 4
    B = 3
    C = 2
    D = 1
    F = 0
    
    i = 1
    num_classes = 0
    
    while i <= sem_total:
        print("How many for-credit classes did you take during Semester", i, "?")
        num_classes = num_classes + int(input("Please enter an integer value\t"))
        i = i + 1
    
    print("You have taken", num_classes, "classes")
    
    i = 1
    while i <= num_classes:
        
        some_grades = "You didn't enter anything"
        
        print("What was your grade in Class Number", i, "?")
        some_grades[i] = input("Please enter the letter grade in CAPS\t")
        
        i = i + 1
'''
    
    
    
    
    
    