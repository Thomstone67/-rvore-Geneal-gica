#pip install aima3
from aima3.logic import expr, FolKB, fol_fc_ask
clauses = []

clauses.append(expr("Progenitor(Pedro,Joao)"))
clauses.append(expr("Progenitor(Pedro,Clara)"))
clauses.append(expr("Progenitor(Pedro,Francisco)"))
clauses.append(expr("Progenitor(Pedro,Ana)"))
clauses.append(expr("Progenitor(Antonia,Joao)"))
clauses.append(expr("Progenitor(Antonia,Clara)"))
clauses.append(expr("Progenitor(Antonia,Francisco)"))
clauses.append(expr("Progenitor(Antonia,Ana)"))

clauses.append(expr("Progenitor(Ana,Helena)"))
clauses.append(expr("Progenitor(Ana,Joana)"))

clauses.append(expr("Progenitor(Joao,Mario)"))

clauses.append(expr("Progenitor(Helena,Carlos)"))
clauses.append(expr("Progenitor(Mario,Carlos)"))

clauses.append(expr("Progenitor(Clara,Pietro)"))
clauses.append(expr("Progenitor(Clara,Enzo)"))

clauses.append(expr("Progenitor(x,y) ==> Pessoa(x)"))
clauses.append(expr("Progenitor(x,y) ==> Pessoa(y)"))

clauses.append(expr("Sexo(Joao,Masculino)"))
clauses.append(expr("Sexo(Clara, Feminino)"))
clauses.append(expr("Sexo(Francisco,Masculino)"))
clauses.append(expr("Sexo(Ana,Feminino)"))
clauses.append(expr("Sexo(Pedro,Masculino)"))
clauses.append(expr("Sexo(Antonia,Feminino)"))

clauses.append(expr("Sexo(Pedro,Masculino)"))
clauses.append(expr("Sexo(Joao,Masculino)"))
clauses.append(expr("Sexo(Francisco,Masculino)"))
clauses.append(expr("Sexo(Mario,Masculino)"))
clauses.append(expr("Sexo(Carlos,Masculino)"))
clauses.append(expr("sexo(Pietro,Masculino)"))
clauses.append(expr("Sexo(Enzo,Masculino)"))

clauses.append(expr("Sexo(Antonia,Feminino)"))
clauses.append(expr("Sexo(Clara,Feminino)"))
clauses.append(expr("Sexo(Ana,Feminino)"))
clauses.append(expr("Sexo(Helena,Feminino)"))
clauses.append(expr("Sexo(Joana,Feminino)"))
clauses.append(expr("Sexo(Milene,Feminino)"))
clauses.append(expr("Sexo(Francisca,Feminino)"))
clauses.append(expr("Sexo(Antonia,Feminino)"))

clauses.append(expr("Progenitor(x,y) & Sexo(x,Feminino) ==> Mae(x,y)"))
clauses.append(expr("Progenitor(x,y) & Sexo(x,Masculino) ==> Pai(x,y)"))
clauses.append(expr("Progenitor(x,y) & Progenitor(x,z) & Sexo(y,Masculino) ==> Irmao(y, z)"))
clauses.append(expr("Progenitor(x,y) & Progenitor(x,z) & Sexo(y,Feminino) ==> Irma(y,z)"))
clauses.append(expr("Progenitor(x,a) & Progenitor(a, y) & Sexo(x, Masculino) ==> Avoh(x,y)"))
clauses.append(expr("Progenitor(x,a) & Progenitor(a, y) & Sexo(x, Feminino) ==> Avom(x,y)"))
clauses.append(expr("Progenitor(p,y) & Progenitor(x,z) & Sexo(y,Masculino) ==> Primo(y, z)"))
clauses.append(expr("Progenitor(p,y) & Progenitor(x,z) & Sexo(y,Feminino) ==> Prima(y, z)"))

Genealogica = FolKB(clauses)

perguntas = ["Sexo(x,Masculino)",
            "Progenitor(Ana,Milene)",
            "Irmao(Joao,Mario)"]

for i in perguntas:
    resposta = fol_fc_ask(Genealogica, expr(i))
    print("%s -> %s" %(i, (list(resposta))))
