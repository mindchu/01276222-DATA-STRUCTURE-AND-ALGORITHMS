print(" *** Wind classification ***")
speed = float(input("Enter wind speed (km/h) : "))
if 0 <= speed <= 51.99:
    print("Wind classification is Breeze.")
elif 52.00 <= speed <= 55.99:
    print("Wind classification is Depression.")
elif 56.00 <= speed <= 101.99:
    print("Wind classification is Tropical Storm.")
elif 102.00 <= speed <= 208.99:
    print("Wind classification is Typhoon.")
else:
    print("Wind classification is Super Typhoon.")