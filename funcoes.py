def verificaarquivo(estrelas):
    try:
        arquivo = open("pontossalvos.txt","r",encoding="utf-8")
        estrelasatualizado = eval(arquivo.read())        
        arquivo.close()

    except:
        estrelasatualizado = {}

    estrelasatualizado.update(estrelas)
    arquivo = open("pontossalvos.txt","w",encoding="utf-8")
    arquivo.write(str(estrelasatualizado))
    arquivo.close()

    