import json
 
# ABRINDO O ARQUIVO JSON
with open('test2json.json', 'r') as openfile:
 
    # LENDO O ARQUIVO JSON
    json_object = json.load(openfile)
# ESTAMOS LENDO UM JSON QUE FOI CONTRUIDO COMO UM ARRAY 
print(json_object)
print(type(json_object))

#SIMPLESMENTE ESSE CODIGO VAI LER O JSON EM QUE AS INFORMAÇÕES ESTÃO COLOCADAS EM UM ARRAY testjson e um json sem array test2json