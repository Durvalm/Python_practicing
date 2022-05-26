fahrenheit = float(input("\nWhat is the given temperature in degrees fahrenheit: "))

celsius = round((fahrenheit - 32) * 5 / 9, 4)
kelvin = round((fahrenheit - 32) * 5 / 9 + 273.15, 4)

print(f"\nDegrees Fahrenheit:\t{fahrenheit}"
      f"\nDegrees Celsius:\t{celsius}"
      f"\nDegrees Kelvin:\t\t{kelvin}")
