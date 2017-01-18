
#Joe Bender
#This program is a hypothetical budget calculator. It welcomes the user, then presents the variables. 

price = int(68.549)

print (price)
#Asks user for name
name = input('What is your name?\n')

#displays name and describes program
print ("")
print ("Hi %s" % name);
print ("")
print ("This a program is a budget calculator. It can keep track of a persons income and expenditures.");
print ("")

#Assigning the variables values by asking the user for input

#hourly and overtime rate
hourlyRate = int(input('Please input the hourly rate:\n'))
overtimeRate = int(input('Please input the overtime rate:\n'))

#regular and overtime hours
regHours = int(input('Please input the number of regular hours worked:\n'))
otHours =int(input('Please input the number of overtime hours worked:\n'))

#rent due
rent = int(input('Please input the rent due:\n'))

#percent of bills
electricPercent = (float(input('Please input the percent of pay for the electric bill:\n')) /(100))
waterPercent = (float(input('Please input the percent of pay for the water bill:\n'))/(100))
sewagePercent = (float(input('Please input the percent of pay for the sewage bill:\n'))/(100))
gasPercent = (float(input('Please input the percent of pay for the gas bill:\n'))/(100))

#food car and entertainment
food = int(input('Please input amount of money for food:\n'))
entertainment = int(input('Please input amount of money for entertainment:\n'))
carPayment = int(input('Please input the amount of money for a car payment:\n'))
print ("")
print ("")



#Printing the variable names, their data, and their data types
print ("Here are your variables, the data they hold, and their data type:")
print ("")
print ("hourlyRate: " + str(hourlyRate) + " " + str(type(hourlyRate)))
print ("overtimeRate: " + str(overtimeRate) + " " + str(type(overtimeRate)))
print ("regHours: " + str(regHours) + " " + str(type(regHours)))
print ("otHours: " + str(otHours) + " " + str(type(otHours)))
print ("rent: " + str(rent) + " " + str(type(rent)))
print ("electricPercent: " + str(electricPercent) + " " + str(type(electricPercent)))
print ("waterPercent: " + str(waterPercent) + " " + str(type(waterPercent)))
print ("sewagePercent: " + str(sewagePercent) + " " + str(type(sewagePercent)))
print ("gasPercent: " + str(gasPercent) + " " + str(type(gasPercent)))
print ("food: " + str(food) + " " + str(type(food)))
print ("entertainment: " + str(entertainment) + " " + str(type(entertainment)))
print ("carPayment: " + str(carPayment) + " " + str(type(carPayment)))
print ("")

#calculating the grosspay you will receive
regPay = (hourlyRate * regHours)
otPay = (overtimeRate * otHours)
grossPay = (regPay + otPay)

#summing all of the expenses and storing it in deductions variable
deductions = rent + (grossPay * (electricPercent)) + (grossPay * waterPercent) + (grossPay * sewagePercent) + (grossPay * gasPercent) + food + entertainment + carPayment


#Printing out the calculations for GrossPay
print ("")
print ("Here is your monthly income:")
print ("")

print ("hourlyRate: $" + format(hourlyRate,'.2f'))
print ("regHours: " + str(regHours))
print ("Total Regular Pay: $" + format(regPay,'.2f'))
print ("")

print ("overtimeRate: $" + format(overtimeRate,'.2f'))
print ("otHours: " + str(otHours))
print ("Total Overtime Pay: $" + format(otPay,'.2f'))
print ("")

print ("Total Income: $" + format(otPay + regPay,'.2f'))
print ("")


#Showing the values for expenses and their summation
print ("")
print ("Here are your monthly expenses and their summation:")
print ("")

print ("rent: $" + format(rent,'.2f'))
print ("electricPercent: $" + format(grossPay * electricPercent,'.2f'))
print ("waterPercent: $" + format(grossPay * waterPercent,'.2f'))
print ("sewagePercent: $" + format(grossPay * sewagePercent,'.2f'))
print ("gasPercent: $" + format(grossPay * gasPercent,'.2f'))
print ("food: $" + format(food,'.2f'))
print ("entertainment: $" + format(entertainment,'.2f'))
print ("carPayment: $" + format(carPayment,'.2f'))
print ("")

print ("Total sum of expenses: $" + format(deductions,'.2f'))


#calculating netpay and storing it in a variable
netPay = (grossPay - deductions)

print ("")
print ("")

#printing the netPay variable
print ("Net Pay (Deductions subtracted from Gross Pay): $" + format(netPay,'.2f'))




