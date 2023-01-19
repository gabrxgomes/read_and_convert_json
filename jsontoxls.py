import pandas
import json

arquivojson = pandas.DataFrame(json.load(open("testjson.json"))["employees"])


    #LEMBRE-SE SEMPRE DE PASSAR OS TITULOS E SUBTITULOS NOS ARGS

    # df = pd.DataFrame(json.load(open("test.json"))["TITULOS"]["SUBTITULOS"])


arquivojson.to_csv("test1.csv", index=False)






#df = (type(json_object))
#df == ('testxsv.csv')
#pandas.read_json("test2json.json").to_excel("output.xlsx")
#json_object.to_excel("output.xlsx")

#json_object = pandas.read_json('test2json.json').to_excel('output.xlsx')

