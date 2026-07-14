celsius = [0, 20, 30, 40, 50]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
above_100 = list(filter(lambda f: f > 100, fahrenheit))
print("Temperatures in Fahrenheit:")
print(fahrenheit)

print("\nTemperatures above 100°F:")
print(above_100)