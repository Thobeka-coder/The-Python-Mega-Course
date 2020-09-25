def weather_condition(temperature):
    if temperature > 7:
        return "warm"
    else:
        return "cold"

user_input = int(input("Enter temperature: "))
#print(weather_condition(user_input))
print("The temperature is {} and it is {}" .format(user_input, weather_condition(user_input)))
