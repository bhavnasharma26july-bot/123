


# Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.
def totalcal():
     bill=int(input('enter the of amount bill you are going to pay:'))
     tip=int(input('kindly enter the percentage tip you are going to pay of the bill'))
     value=(bill/100*tip)+bill
     return(value)
print(totalcal())
