# Health
# Patrick Kakungulu
# 9/27/2021
# Application to allow user to calculate their BMI.
# Calculate user heart rate for varying levels of exercise
# Intesity utilizing Karvonen formula.

# Introduce activity to user 
print('\t ****Kick start your health, know your Body Mass Index ', end = '')
print('and know your exercise needs.**** \n')
# user data input.
print('Please answer the following questions to get started! \n')

# function for user data input
def dataInput(promptCall):
    # repeat till we get a float input
    # float input
    userInput = input(promptCall)
    while not userInput.replace('.','',2).isdigit():
        userInput = input(promptCall)
    return int(userInput)
ageNum = dataInput('What is your age? ')
heightNum = dataInput('What is your Height in inches? ')
rheartNum = dataInput('Enter your Resting Heart Rate: ')
weightNum = dataInput('What is your weight in pounds? ')
print('\n')

# function for conversion of data
def bmiCal(heightNum, weightNum):
    heightMeters = heightNum*0.0254
    weightKgs = weightNum * 0.453592
    bmiNum = round(weightKgs /(heightMeters**2),2)
    return bmiNum
# call for bmi and bmi category function
def bmigroup(bmiNum):
    groupIn =''
    if (bmiNum <= 18.5):
        groupIn = 'Underweight'
    elif (bmiNum <= 24.9):
        groupIn = 'Normal'
    elif (bmiNum <= 29.9):
        groupIn = 'Overweight'
    elif (bmiNum >= 30):
        groupIn = 'obese'
    return groupIn
bmiNum = bmiCal(heightNum,weightNum)
groupIn = bmigroup(bmiNum)
print('Result . . .')
print('Your BMI is: ', bmiNum, '--',groupIn)
print('\n')

# function involving Karvonen heart rate
def karvInput(intensity, rheartNum, age):
    #calculation according to the formula
    mhr = 220 - ageNum
    hrr = mhr - rheartNum
    mtz = hrr * intensity
    ttz = mtz + rheartNum
    return int(ttz)

# User workout intensity suggestion and max
print('Exercise Intensity Heart Rates: ')
print('Intensity\t' + 'Max Heart Rate')
print()

# interval loop 50 percent and 95 percent included
for i in range(50, 96, 5):
    #lets for the function with Karv
    intensity = round(i/100, 2)
    maxHr = karvInput(intensity, rheartNum, ageNum)
    print(str("%.2f" % intensity),'\t       ', str(maxHr))

