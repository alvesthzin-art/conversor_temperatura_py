print("--- CONVERSOR DE TEMPERATURA ---")
celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius}°C equivalem a:")
print(f"-> {fahrenheit}°F")
print(f"-> {kelvin}K")
