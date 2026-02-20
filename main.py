www_dict = {
    "creepy": "aterrador o siniestro",
    "crack": "alguien profesional"
}
word = input("escribe palabra que no entiendas cpn mayusculas:")
if word in www_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(www_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("esta palabra no estaba en el diccionario")
