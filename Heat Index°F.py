t = float(input("Enter the air temperature (in Fahrenheit): "))
h = float(input("Enter the relative humidity: "))
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
print(f"the heat index is {hi}°F ")

if hi < 80: 
    print("Safe exposure") 
elif 80 <= hi <= 90:
    print("Caution")
elif 90 <= hi <= 105:
    print("Extereme Caution")
elif 105 <= hi <= 130:
    print("Danger! ")
else: 
    print("Extermely Dangerous!! ")

