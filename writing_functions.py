def saludar(nombre,momento):
    momento = momento.lower()
    if (momento == "mañana"):
        saludo = "Buenos dias"
    elif (momento == "tarde"):
        saludo = "Buenas tardes"
    elif (momento == "noche"):
        saludo = "Buenas noches"
    else:
        saludo = "Hola"
    print(f"{saludo} {nombre}!")
saludar("Ana","mañana")
saludar("Luis","Tarde")
saludar("Marta","noche")
saludar("Susana","lunes")