def temp_humidity(temp_celsius, humidity) :
    temp_fahrenheit = (temp_celsius * 1.8) + 32
    if temp_fahrenheit <= 40:
        heat_index1 = temp_fahrenheit 
    else: 
        a = -10.3 + 1.1 * temp_fahrenheit + 0.047 * humidity
        if a < 79: 
            heat_index1 = a  
        else:
            b = -42.379 + 2.04901523 * temp_fahrenheit + 10.14333127 * humidity - 0.22475541 * temp_fahrenheit * humidity - 6.83783 * (10**-3) * (temp_fahrenheit**2) - 5.481717 * (10**-2) * (humidity**2) + 1.22874 * (10**-3) * (temp_fahrenheit**2) * humidity + 8.5282 * (10**-4) * temp_fahrenheit * (humidity**2) - 1.99 * (10**-6) * (temp_fahrenheit**2) * (humidity**2)
            if humidity <= 13 and 80 <= temp_fahrenheit <= 112:
                heat_index1 = b - ((13 - humidity)/4) * (((17 - abs(temp_fahrenheit - 95))/17)**0.5)
            elif humidity > 85 and 80 <= temp_fahrenheit <= 87:
                heat_index1 = b + 0.02 * (humidity - 85) * (87 - temp_fahrenheit) 
            else:
                heat_index1 = b
    heat_index2 = (heat_index1 - 32)/1.8
    print(f"Heat index is {heat_index2}")
    return heat_index2 
 

import pandas as pd 
from matplotlib import pyplot as plt 

x_axis = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
y_axis = [temp_humidity(5, 50), temp_humidity(10, 50), temp_humidity(15, 50), temp_humidity(20, 50), temp_humidity(25, 50), temp_humidity(30, 50), temp_humidity(35, 50), temp_humidity(40, 50), temp_humidity(45, 50), temp_humidity(50, 50), temp_humidity(55, 50), temp_humidity(60, 50), temp_humidity(65, 50), temp_humidity(70, 50), temp_humidity(75, 50), temp_humidity(80, 50), temp_humidity(85, 50), temp_humidity(90, 50), temp_humidity(95, 50), temp_humidity(100, 50)]
plt.plot(x_axis, y_axis)
plt.show()


