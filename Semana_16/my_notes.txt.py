# Escritura de Archivo de Texto
# Se crea y escribe en el archivo "my_notes.txt"
with open("my_notes.txt", "w") as file:
    file.write("Esta es la primera nota que realizo.\n")
    file.write("Aprendiendo a usar archivos en Python.\n")
    file.write("Es fundamental cerrar los archivos después de utilizarlos.\n")

# Lectura de Archivo de Texto
# Se abre el archivo en modo lectura y se leen las líneas una por una
with open("my_notes.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() elimina los saltos de línea adicionales

# El archivo se cierra automáticamente con "with open"
