import saludos 

print (saludos.hola("Alex"))

nombres = ["Juan", "Pedro", "Carlos"]
saludos = saludos.holas(nombres)

for saludo in saludos.values():
    print(saludo)