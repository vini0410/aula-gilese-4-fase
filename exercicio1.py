class classe_comparacao():
    def comparacao(self):
        pergunta = int(input("Digite o ano que voce nasceu;\n"
                             "Colocar (0) encerra o programa;\n"
                             ": "))
        if pergunta <= 2002:
            print("voce eh maior de 18 anos")
        elif pergunta > 2002:
            print("voce eh menor de 18 anos")

pessoa = classe_comparacao()
pessoa.comparacao()
