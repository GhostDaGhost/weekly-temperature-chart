# This is a program that will record temperatures of each day of the week as well as display the coldest and warmest day.

# GET MATH LIBRARY FOR THE math.floor FUNCTION
import math

# GET MATPLOTLIB LIBRARY
import matplotlib.pyplot as plt

# VARIABLE FOR TEMPERATURES WITHIN THE WEEK
temperaturesThisWeek = {
    'Monday': 0,
    'Tuesday': 0,
    'Wednesday': 0,
    'Thursday': 0,
    'Friday': 0,
    'Saturday': 0,
    'Sunday': 0
}

# WHEN TRIGGERED, START ASKING FOR TEMPERATURE OF EACH DAY OF THE WEEK
# No parameters.
# No return value.
def main():
    # AXIS OF X AND Y FOR THE CHART
    x_axis = []
    y_axis = []

    # ITERATE THROUGH EACH DAY OF THE WEEK
    for dayOfTheWeek in temperaturesThisWeek.keys():
        x_axis.append(dayOfTheWeek)

        temperatureInput = input('Enter the temperature for ' + dayOfTheWeek + ': ')
        if temperatureInput and temperatureInput != '':
            temperatureInput = int(temperatureInput)

            # ENSURE THAT THE TEMPERATURE INPUT IS CORRECT
            if temperatureInput and temperatureInput > 0:
                y_axis.append(temperatureInput)

                temperaturesThisWeek[dayOfTheWeek] = temperatureInput
                print('You entered the temperature of ' + str(temperatureInput) + ' for ' + dayOfTheWeek)
            else:
                temperaturesThisWeek[dayOfTheWeek] = 0
                print('You did not enter a correct temperature for ' + dayOfTheWeek + ' so it was set to a default of 0!')
        else:
            temperaturesThisWeek[dayOfTheWeek] = 0
            print('You did not enter a correct temperature for ' + dayOfTheWeek + ' so it was set to a default of 0!')

    # ONCE ALL WEEKDAYS HAVE TEMPERATURES RECORDED, GET THE COLDEST DAY
    coldestTemperature = min(temperaturesThisWeek.values())
    for dayOfTheWeek, weekdayTemperature in temperaturesThisWeek.items():
        if weekdayTemperature == coldestTemperature:
            print(dayOfTheWeek + ' was the coldest day with a temperature value of ' + str(weekdayTemperature) + '.')
            break

    # AFTER GETTING THE COLDEST DAY, GET THE WARMEST DAY
    warmestTemperature = max(temperaturesThisWeek.values())
    for dayOfTheWeek, weekdayTemperature in temperaturesThisWeek.items():
        if weekdayTemperature == warmestTemperature:
            print(dayOfTheWeek + ' was the warmest day with a temperature value of ' + str(weekdayTemperature) + '.')
            break

    # GET AVERAGE TEMPERATURE OF THE WEEK
    averageTemperature = sum(temperaturesThisWeek.values()) / float(len(temperaturesThisWeek))
    print('Average temperature of the week is:', math.floor(averageTemperature))

    # Build the bar chart.
    plt.bar(x_axis, y_axis)

    # Display the bar chart and set the title/labels.
    plt.title('Weekly Temperature Data')
    plt.xlabel('Days of the Week')
    plt.ylabel('Temperature Values')
    plt.show()

# TRIGGER MAIN FUNCTION ON INITIALIZATION
main()
