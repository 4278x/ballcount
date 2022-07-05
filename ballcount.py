print('When did you start playing tennis? Answer in years')
from time import sleep
yearsplaying = input()
yearnow = 2022
days = int(yearnow) - int(yearsplaying)
print("You have being playing tennis for ",days ,"years")
sleep(2)
multiply_days = days * 365
print("That is equivalent to ", multiply_days,"days")
sleep(2)
print('How may balls do you estimate is in your container? Answer in numbers')
print('Reference: About 355 balls in a full cart')
print('About 75 balls in a full tennis basket')
print('About 25 balls in a full bag ')
amount_of_balls = input()
int(amount_of_balls)
print('How many times do you think that the container is emptied throughout your session? Answer in numbers')
empties = input()
balls_in_container = int(amount_of_balls)*int(empties)
sleep(1)
print('It is estimated that you shot roughly',balls_in_container,'balls on average during one session')
sleep(2)
print('On average, how many days in a week do you play tennis, consistently?')
how_many_days_in_a_week = input()
balls_in_a_week = int(how_many_days_in_a_week)*int(balls_in_container)
sleep(1)
print('You shot',balls_in_a_week,'balls throughout the week')
sleep(2)
how_many_weeks = int(multiply_days) / 7
rounded = round(how_many_weeks,0)
sleep(2)
print('There are',rounded,'weeks of you playing tennis during your career')

final_answer = int(balls_in_a_week)* int(rounded)
sleep(2)
print('You shot',final_answer,'balls in your career!, on estimate')


