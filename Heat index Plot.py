def temp_humidity(celsius, h) :
    t = (celsius * 1.8) + 32
    if t <= 40:
        hi = t 
    else: 
        a = -10.3 + 1.1 * t + 0.047 * h
        if a < 79: 
            hi = a  
        else:
            b = -42.379 + 2.04901523 * t + 10.14333127 * h - 0.22475541 * t * h - 6.83783 * (10**-3) * (t**2) - 5.481717 * (10**-2) * (h**2) + 1.22874 * (10**-3) * (t**2) * h + 8.5282 * (10**-4) * t * (h**2) - 1.99 * (10**-6) * (t**2) * (h**2)
            if h <= 13 and 80 <= t <= 112:
                hi = b - ((13 - h)/4) * (((17 - abs(t - 95))/17)**0.5)
            elif h > 85 and 80 <= t <= 87:
                hi = b + 0.02 * (h - 85) * (87 - t) 
            else:
                hi = b
    hii = (hi - 32)/1.8
    print(f"Heat index is {hii}")
    return hii 
 

import pandas as pd 
from matplotlib import pyplot as plt 

axis = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
iso_bar1 = [temp_humidity(5, 35), temp_humidity(10, 35), temp_humidity(15, 35), temp_humidity(20, 35), temp_humidity(25, 35), temp_humidity(30, 35), temp_humidity(35, 35), temp_humidity(40, 35), temp_humidity(45, 35), temp_humidity(50, 35), temp_humidity(55, 35), temp_humidity(60, 35)]
iso_bar2 = [temp_humidity(5, 60), temp_humidity(10, 60), temp_humidity(15, 60), temp_humidity(20, 60), temp_humidity(25, 60), temp_humidity(30, 60), temp_humidity(35, 60), temp_humidity(40, 60), temp_humidity(45, 60), temp_humidity(50, 60), temp_humidity(55, 60), temp_humidity(60, 60)]
iso_bar3 = [temp_humidity(5, 40), temp_humidity(10, 40), temp_humidity(15, 40), temp_humidity(20, 40), temp_humidity(25, 40), temp_humidity(30, 40), temp_humidity(35, 40), temp_humidity(40, 40), temp_humidity(45, 40), temp_humidity(50, 40), temp_humidity(55, 40), temp_humidity(60, 40)]
plt.plot(axis, iso_bar1, iso_bar2, iso_bar3)
plt.show()


