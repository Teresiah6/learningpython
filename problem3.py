#if age is 5 go to kindergaten
#ages 6 through 17 goes to grade 1 through 12
#if age is greater than 17 go to college
#complete in ten or less lines
age = eval(input("Enter an age: "))
if (age == 5):
    print("Go to Kindergaten")
elif (age >= 6) and (age <= 17):
    grade = age - 5
    print(f"Go to {grade} grade")
elif not(age < 17):
    print("Go to college or work")
else:
    print("Stay at home or daycare")