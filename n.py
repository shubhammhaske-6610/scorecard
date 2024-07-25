def space(marks, subject):
    if marks > 75:
        grade="A+"
    elif marks > 70:
        grade="A"
    elif marks > 65:
        grade="B+"
    elif marks > 60:
        grade="B"
    elif marks > 55:
        grade="C+"
    elif marks > 50:
        grade="C"
    elif marks > 45:
        grade="D+"
    elif marks > 40:
        grade="D"     
    else:
        grade="fail"
    print("subject grade:",subject,grade)
    if grade == "fail":
        return
    else:
        return grade         
name = input("Enter your name: ")
std = input("Enter your standard: ")
a = int(input("Enter the marks obtained in English out of 100: ")) 
b = int(input("Enter the marks obtained in Marathi out of 100: "))
c = int(input("Enter the marks obtained in Hindi out of 100: ")) 
d = int(input("Enter the marks obtained in Science out of 100: "))
marks = a + b + c + d
percent = marks * 100/400
english = space(a,"English",) 
marathi = space(b, "Marathi") 
hindi   = space(c, "Hindi")
science = space(d, "Science")
if english and marathi and hindi and science:
 print("marks:",marks)
 print("percent:",percent)
else:
 print("marks:",marks) 
 