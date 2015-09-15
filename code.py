__author__ = 'Macbook'

# import the csv ibrary
# Ask the user to input his license number to check whether it is valid or invalid. If it is invalid, the reataurant should immeditialely renew license
#It shows the user the date the inspecton was carried out from the most recent one to the least recent one.
#The comparrison actually checks the number of Pass with the number of other values.
#If the number of pass is equal to the number of fail, then the licence number is invalid
counter_pass = 0
counter_fail = 0


import csv
test_file = 'food_inspections.csv'

csv_file = csv.DictReader(open(test_file, 'rb'), delimiter=',', quotechar='"')
print(" Welcome to My Python ")

# prompt the console to the user
license = raw_input("Enter A License Number :")

#a list that stores the date for the pass and fail
pass_list_date = []
fail_list_date =[]

#searches the licence
search = license

#The for loop to read the csv file
for line in csv_file:
    if ((line['License #']== search) & (line['Results'] == 'Pass')):
        counter_pass +=1
        pass_list_date.append(line ['Inspection Date'])
    elif ((line['License #']== search) & (line['Results'] == 'Fail')):
        fail_list_date.append(line ['Inspection Date'])
        counter_fail +=1

# display the number of pass for the license number
print("Number of Pass : " + " " + str(counter_pass)  + " And Date of Pass inspections : " + str(pass_list_date))

# display the number of fail for the license number
print("Number of Fail : " + " " + str(counter_fail) + " And Date of Fail inspections : " + str(fail_list_date))

# compare the number of pass with fail
if (counter_pass - counter_fail >= 1):
    print("Inspection for this license #") +"  " + search + "   " + "Valid"
else:
    print("Inspection for this license #") +"  " + search + "   " + "Invalid"
