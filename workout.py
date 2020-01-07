#Trey Orr
#Week Workout Planner
#1/6/2020
import math
import array
#Initializes all the lists as empty (N/A)
mexercise = ["N/A"]
msets = ["N/A"]
mreps = ["N/A"]
texercise = ["N/A"]
tsets = ["N/A"]
treps = ["N/A"]
wexercise = ["N/A"]
wsets = ["N/A"]
wreps = ["N/A"]
thexercise = ["N/A"]
thsets = ["N/A"]
threps = ["N/A"]
fexercise = ["N/A"]
fsets = ["N/A"]
freps = ["N/A"]
sexercise = ["N/A"]
ssets = ["N/A"]
sreps = ["N/A"]
suexercise = ["N/A"]
susets = ["N/A"]
sureps = ["N/A"]
loop = 0;
#Loop where workouts are inputted
while loop == 0:
    #User selects day of workout or to print the schedule
    print("----------------------------------------------------------------------")
    print("Welcome to Workout Planner: here are your selections of workout days")
    print("Quit and print- 'q'")
    print("Monday- 'm'")
    print("Tuesday- 't'")
    print("Wednesday- 'w'")
    print("Thurday- 'th'")
    print("Friday- 'f'")
    print("Saturday- 's'")
    print("Sunday- 'su': ")
    print("----------------------------------------------------------------------")
    day = input("Enter your choice: ")
    print("")
    if day == "q":
        loop = 1;
    #According to day chosen, the user inputs the workouts with their sets, reps, and weights
    if day == "m":
        mexercise.remove("N/A")
        msets.remove("N/A")
        mreps.remove("N/A")
        nMonday = int(input("Amount of workouts on Monday: "))
        for i in range(nMonday):
            exercise = input("Exercise: ")
            sets = input("Sets: ")
            reps = input("Reps(Weight) Ex: 10(135), 8(155), etc: ")
            print("Exercise added to Monday")
            mexercise.append(exercise)
            msets.append(sets)
            mreps.append(reps)
    elif day == "t":
        texercise.remove("N/A")
        tsets.remove("N/A")
        treps.remove("N/A")
        nTuesday = int(input("Amount of workouts on Tuesday: "))
        for i in range(nTuesday):
            exercise = input("Exercise: ")
            sets = input("Sets: ")
            reps = input("Reps(Weight) Ex: 10(135), 8(155), etc: ")
            print("Exercise added to Tuesday")
            texercise.append(exercise)
            tsets.append(sets)
            treps.append(reps)
    elif day == "w":
        wexercise.remove("N/A")
        wsets.remove("N/A")
        wreps.remove("N/A")
        nWednesday = int(input("Amount of workouts on Wednesday: "))
        for i in range(nWednesday):
            exercise = input("Exercise: ")
            sets = input("Sets: ")
            reps = input("Reps(Weight) Ex: 10(135), 8(155), etc: ")
            print("Exercise added to Wedneday")
            wexercise.append(exercise)
            wsets.append(sets)
            wreps.append(reps)
    elif day == "th":
        thexercise.remove("N/A")
        thsets.remove("N/A")
        threps.remove("N/A")
        nThursday = int(input("Amount of workouts on Thursday: "))
        for i in range(nThursday):
            exercise = input("Exercise: ")
            sets = input("Sets: ")
            reps = input("Reps(Weight) Ex: 10(135), 8(155), etc: ")
            print("Exercise added to Thursday")
            thexercise.append(exercise)
            thsets.append(sets)
            threps.append(reps)
    elif day == "f":
        fexercise.remove("N/A")
        fsets.remove("N/A")
        freps.remove("N/A")
        nFriday = int(input("Amount of workouts on Friday: "))
        for i in range(nFriday):
            exercise = input("Exercise: ")
            sets = input("Sets: ")
            reps = input("Reps(Weight) Ex: 10(135), 8(155), etc: ")
            print("Exercise added to Friday")
            fexercise.append(exercise)
            fsets.append(sets)
            freps.append(reps)
    elif day == "s":
        sexercise.remove("N/A")
        ssets.remove("N/A")
        sreps.remove("N/A")
        nSaturday = int(input("Amount of workouts on Saturday: "))
        for i in range(nSaturday):
            exercise = input("Exercise: ")
            sets = input("Sets: ")
            reps = input("Reps(Weight) Ex: 10(135), 8(155), etc: ")
            print("Exercise added to Saturday")
            sexercise.append(exercise)
            ssets.append(sets)
            sreps.append(reps)
    elif day == "su":
        suexercise.remove("N/A")
        susets.remove("N/A")
        sureps.remove("N/A")
        nSunday = int(input("Amount of workouts on Sunday: "))
        for i in range(nSunday):
            exercise = input("Exercise: ")
            sets = input("Sets: ")
            reps = input("Reps(Weight) Ex: 10(135), 8(155), etc: ")
            print("Exercise added to Sunday")
            suexercise.append(exercise)
            susets.append(sets)
            sureps.append(reps)
#Prints the workout schedule    
print("------------------------------------------")
print("------------------------------------------")
print("Monday:")
mlength = len(mreps) 
a = 0
while a < mlength:
    print("Excercise:", mexercise[a])
    print("Sets:", msets[a])
    print("Reps(Weights):", mreps[a])
    print("")
    a = a + 1
print("Tuesday:")
tlength = len(treps) 
b = 0
while b < tlength: 
    print("Excercise:", texercise[b])
    print("Sets:", tsets[b])
    print("Reps(Weights):", treps[b])
    print("")
    b = b + 1
print("Wedesday:")
wlength = len(wreps) 
c = 0
while c < wlength: 
    print("Excercise:", wexercise[c])
    print("Sets:", wsets[c])
    print("Reps(Weights):", wreps[c])
    print("")
    c = c + 1
print("Thursday:")
thlength = len(threps) 
d = 0
while d < thlength: 
    print("Excercise:", thexercise[d])
    print("Sets:", thsets[d])
    print("Reps(Weights):", threps[d])
    print("")
    d = d + 1
print("Friday:")
flength = len(freps) 
e = 0
while e < flength: 
    print("Excercise:", fexercise[e])
    print("Sets:", fsets[e])
    print("Reps(Weights):", freps[e])
    print("")
    e = e + 1
print("Saturday:")
slength = len(sreps) 
f = 0
while f < slength: 
    print("Excercise:", sexercise[f])
    print("Sets:", ssets[f])
    print("Reps(Weights):", sreps[f])
    print("")
    f = f + 1
print("Sunday:")
sulength = len(sureps) 
g = 0
while g < sulength: 
    print("Excercise:", suexercise[g])
    print("Sets:", susets[g])
    print("Reps(Weights):", sureps[g])
    print("")
    g = g + 1
print("------------------------------------------")
print("------------------------------------------")
#Writes to txt file
file = open("workout-schedule.txt", "w") 
file.write("Weekly Workout Schedule: \n")
file.write("\n")
file.write("Monday: \n")
fa = 0
while fa < mlength:
    file.write("Excercise: "+mexercise[fa]+"\n")
    file.write("Sets: "+msets[fa]+"\n")
    file.write("Reps(Weights): "+mreps[fa]+"\n")
    file.write("\n")
    fa = fa + 1
file.write("Tuesday: \n")
fb = 0
while fb < tlength:
    file.write("Excercise: "+texercise[fb]+"\n")
    file.write("Sets: "+tsets[fb]+"\n")
    file.write("Reps(Weights): "+treps[fb]+"\n")
    file.write("\n")
    fb = fb + 1
file.write("Wednesday: \n")
fc = 0
while fc < wlength:
    file.write("Excercise: "+wexercise[fc]+"\n")
    file.write("Sets: "+wsets[fc]+"\n")
    file.write("Reps(Weights): "+wreps[fc]+"\n")
    file.write("\n")
    fc = fc + 1
file.write("Thursday: \n")
fd = 0
while fd < thlength:
    file.write("Excercise: "+thexercise[fd]+"\n")
    file.write("Sets: "+thsets[fd]+"\n")
    file.write("Reps(Weights): "+threps[fd]+"\n")
    file.write("\n")
    fd = fd + 1
file.write("Friday: \n")
fe = 0
while fe < flength:
    file.write("Excercise: "+fexercise[fe]+"\n")
    file.write("Sets: "+fsets[fe]+"\n")
    file.write("Reps(Weights): "+freps[fe]+"\n")
    file.write("\n")
    fe = fe + 1
file.write("Saturday: \n")
ff = 0
while ff < slength:
    file.write("Excercise: "+sexercise[ff]+"\n")
    file.write("Sets: "+ssets[ff]+"\n")
    file.write("Reps(Weights): "+sreps[ff]+"\n")
    file.write("\n")
    ff = ff + 1
file.write("Sunday: \n")
fg = 0
while fg < sulength:
    file.write("Excercise: "+suexercise[fg]+"\n")
    file.write("Sets: "+susets[fg]+"\n")
    file.write("Reps(Weights): "+sureps[fg]+"\n")
    file.write("\n")
    fg = fg + 1
file.close() 
