def selecionar_prato():
    carne_vermelha = ["Picanha grelhada", "Filé mignon ao molho madeira", "Costela assada"]
    aves = ["Frango grelhado com ervas", "Peru assado com farofa", "Magret de pato ao molho de laranja"]
    frutos_mar = ["Camarão na moranga", "Salmão grelhado", "Lula à dorê"]
    pratos_veganos = ["Lasanha de berinjela", "Grão-de-bico com legumes", "Estrogonofe de palmito"]
    graos_massas = ["Arroz à grega", "Espaguete ao sugo", "Risoto de cogumelos"]
    sobremesas = ["Pudim de leite", "Mousse de maracujá", "Torta de limão"]
    bebidas = ["Suco natural", "Refrigerante", "Água"]

    print("1 - Carne vermelha")
    print("2 - Aves")
    print("3 - Frutos do mar")
    print("4 - Pratos veganos")
    print("5 - Grãos e massas")
    print("6 - Sobremesas")
    print("7 - Bebidas")
    try:
        escolha_usuario = int(input("Qual categoria de alimentos você deseja apreciar hoje? "))
    except ValueError:
        print("ERRO: Por favor, insira um número válido!")
        return None

    prato_escolhido = None  # Variável para guardar a escolha final

    # ------------------------------ CARNE VERMELHA ------------------------------
    if escolha_usuario == 1:
        print("1 - Cotidiano/Casual")
        print("2 - Sofisticado/Formal")
        print("3 - Sem ocasião específica")
        try:
            escolha1_carne = int(input("Qual ocasião do encontro de hoje? "))
        except ValueError:
            print("ERRO: Insira um número válido!")
            return None
        
        if escolha1_carne == 1:
            prato_escolhido = carne_vermelha[0]

        elif escolha1_carne == 2:
            print("1 - Com estrutura óssea")
            print("2 – Corte limpo/desossado")
            print("3 - Gostaria de ver ambas as opções")
            try:
                escolha2_carne = int(input("Você prefere a carne com qual estilo de corte? "))
            except ValueError:
                print("ERRO: Insira um número válido!")
                return None
            
            if escolha2_carne == 1:
                prato_escolhido = carne_vermelha[2]
            elif escolha2_carne == 2:
                prato_escolhido = carne_vermelha[1]
            elif escolha2_carne == 3:
                prato_escolhido = carne_vermelha[1] + " e " + carne_vermelha[2]
            else:
                print("ERRO: Selecione uma opção válida!")
                return None

        elif escolha1_carne == 3:
            print("1 - Com molho")
            print("2 - Sem molho")
            print("3 - Ambos")
            try:
                escolha2_carne = int(input("Você prefere a carne com preparo ao molho ou sem molho? "))
            except ValueError:
                print("ERRO: Insira um número válido!")
                return None
            
            if escolha2_carne == 1:
                prato_escolhido = carne_vermelha[1]
            elif escolha2_carne == 2:
                prato_escolhido = carne_vermelha[0] + " e " + carne_vermelha[2]
            elif escolha2_carne == 3:
                prato_escolhido = carne_vermelha[0] + ", " + carne_vermelha[1] + " e " + carne_vermelha[2]
            else:
                print("ERRO: Selecione uma opção válida!")
                return None
        
        else:
            print("ERRO: Selecione uma opção válida!")
            return None

    # ------------------------------ AVES ------------------------------
    elif escolha_usuario == 2:
        print("1 - Cotidiano/Casual")
        print("2 - Sofisticado/Formal")
        print("3 - Sem ocasião específica")
        try:
            escolha1_ave = int(input("Qual ocasião do encontro de hoje? "))
        except ValueError:
            print("ERRO: Insira um número válido!")
            return None
        
        if escolha1_ave == 1:
            prato_escolhido = aves[0]

        elif escolha1_ave == 2:
            print("1 - Com estrutura óssea")
            print("2 – Corte limpo/desossado")
            print("3 - Gostaria de ver ambas as opções")
            try:
                escolha2_ave = int(input("Você prefere ave com qual estilo de corte? "))
            except ValueError:
                print("ERRO: Insira um número válido!")
                return None
            
            if escolha2_ave == 1:
                prato_escolhido = aves[1]
            elif escolha2_ave == 2:
                prato_escolhido = aves[2]
            elif escolha2_ave == 3:
                prato_escolhido = aves[1] + " e " + aves[2]
            else:
                print("ERRO: Selecione uma opção válida!")
                return None

        elif escolha1_ave == 3:
            print("1 - Com molho")
            print("2 - Sem molho")
            print("3 - Ambos")
            try:
                escolha3_ave = int(input("Você prefere ave com preparo ao molho ou sem molho? "))
            except ValueError:
                print("ERRO: Insira um número válido!")
                return None
            
            if escolha3_ave == 1:
                prato_escolhido = aves[2]
            elif escolha3_ave == 2:
                prato_escolhido = aves[0] + " e " + aves[1]
            elif escolha3_ave == 3:
                prato_escolhido = aves[0] + ", " + aves[1] + " e " + aves[2]
            else:
                print("ERRO: Selecione uma opção válida!")
                return None

        else:
            print("ERRO: Selecione uma opção válida!")
            return None

    # ------------------------------ FRUTOS DO MAR ------------------------------
    elif escolha_usuario == 3:
        print("1 - Cotidiano/Casual")
        print("2 - Sofisticado/Formal")
        print("3 - Sem ocasião específica")
        try:
            escolha1_mar = int(input("Qual ocasião do encontro de hoje? "))
        except ValueError:
            print("ERRO: Insira um número válido!")
            return None

        if escolha1_mar == 1:
            prato_escolhido = frutos_mar[0]

        elif escolha1_mar == 2:
            print("1 - Grelhado")
            print("2 - Frito")
            print("3 - Gostaria de ver as opções gerais")
            try:
                escolha2_mar = int(input("Você prefere frutos do mar com preparo grelhado ou frito? "))
            except ValueError:
                print("ERRO: Insira um número válido!")
                return None
            
            if escolha2_mar == 1:
                prato_escolhido = frutos_mar[1]
            elif escolha2_mar == 2:
                prato_escolhido = frutos_mar[2]
            elif escolha2_mar == 3:
                prato_escolhido = frutos_mar[1] + " e " + frutos_mar[2]
            else:
                print("ERRO: Selecione uma opção válida!")
                return None

        elif escolha1_mar == 3:
            print("1 - Com molho")
            print("2 - Sem molho")
            print("3 - Ambos")
            try:
                escolha2_mar = int(input("Você prefere frutos do mar com preparo ao molho ou sem molho? "))
            except ValueError:
                print("ERRO: Insira um número válido!")
                return None

            if escolha2_mar == 1:
                prato_escolhido = frutos_mar[0]
            elif escolha2_mar == 2:
                prato_escolhido = frutos_mar[1] + " e " + frutos_mar[2]
            elif escolha2_mar == 3:
                prato_escolhido = frutos_mar[0] + ", " + frutos_mar[1] + " e " + frutos_mar[2]
            else:
                print("ERRO: Selecione uma opção válida!")
                return None
        
        else:
            print("ERRO: Selecione uma opção válida!")
            return None

    # ------------------------------ PRATOS VEGANOS ------------------------------
    elif escolha_usuario == 4:
        print("1 - Cotidiano/Casual")
        print("2 - Sofisticado/Formal")
        print("3 - Sem ocasião específica")
        try:
            escolha1_veganos = int(input("Qual ocasião do encontro de hoje? "))
        except ValueError:
            print("ERRO: Insira um número válido!")
            return None
        
        if escolha1_veganos == 1:
            print("1 - Cozido")
            print("2 - Refogado")
            print("3 - Gostaria de ver as opções gerais")
            try:
                escolha2_veganos = int(input("Você prefere pratos veganos com preparo cozido ou refogado? "))
            except ValueError:
                print("ERRO: Insira um número válido!")
                return None
            
            if escolha2_veganos == 1:
                prato_escolhido = pratos_veganos[1]
            elif escolha2_veganos == 2:
                prato_escolhido = pratos_veganos[2]
            elif escolha2_veganos == 3:
                prato_escolhido = pratos_veganos[1] + " e " + pratos_veganos[2]
            else:
                print("ERRO: Selecione uma opção válida!")
                return None

        elif escolha1_veganos == 2:
            prato_escolhido = pratos_veganos[0]

        elif escolha1_veganos == 3:
            print("1 - Encorpada")
            print("2 - Cremosa")
            print("3 – Leve")
            print("4 – Gostaria de ver as opções gerais")
            try:
                escolha3_veganos = int(input("Você prefere pratos veganos com qual tipo de textura? "))
            except ValueError:
                print("ERRO: Insira um número válido!")
                return None
            
            if escolha3_veganos == 1:
                prato_escolhido = pratos_veganos[0]
            elif escolha3_veganos == 2:
                prato_escolhido = pratos_veganos[2]
            elif escolha3_veganos == 3:
                prato_escolhido = pratos_veganos[1]
            elif escolha3_veganos == 4:
                prato_escolhido = pratos_veganos[0] + ", " + pratos_veganos[1] + " e " + pratos_veganos[2]
            else:
                print("ERRO: Selecione uma opção válida!")
                return None

        else:
            print("ERRO: Selecione uma opção válida!")
            return None

    # ------------------------------ GRÃOS E MASSAS ------------------------------
    elif escolha_usuario == 5:
        print("1 - Cotidiano/Casual")
        print("2 - Sofisticado/Formal")
        print("3 - Sem ocasião específica")
        try:
            escolha1_graos_massas = int(input("Qual ocasião do encontro de hoje? "))
        except ValueError:
            print("ERRO: Insira um número válido!")
            return None
        
        if escolha1_graos_massas == 1:
            print("1 - Grão")
            print("2 - Massa")
            print("3 - Gostaria de ver as opções gerais")
            try:
                escolha2_graos_massas = int(input("Você prefere qual base principal de preparo? "))
            except ValueError:
                return None
            
            if escolha2_graos_massas == 1:
                prato_escolhido = graos_massas[0]
            elif escolha2_graos_massas == 2:
                prato_escolhido = graos_massas[1]
            elif escolha2_graos_massas == 3:
                prato_escolhido = graos_massas[0] + " e " + graos_massas[1]
            else:
                print("ERRO: Selecione uma opção válida!")
                return None

        elif escolha1_graos_massas == 2:
            prato_escolhido = graos_massas[2]

        elif escolha1_graos_massas == 3:
            prato_escolhido = graos_massas[0] + ", " + graos_massas[1] + " e " + graos_massas[2]

        else:
            print("ERRO: Selecione uma opção válida!")
            return None

    # ------------------------------ SOBREMESAS ------------------------------
    elif escolha_usuario == 6:
        print("1 - Leve")
        print("2 - Doce")
        print("3 - Cremoso")
        try:
            escolha_sobremesa = int(input("Qual tipo de sobremesa você prefere? "))
        except ValueError:
            print("ERRO: Insira um número válido!")
            return None
        
        if escolha_sobremesa == 1:
            prato_escolhido = sobremesas[1]
        elif escolha_sobremesa == 2:
            prato_escolhido = sobremesas[0]
        elif escolha_sobremesa == 3:
            prato_escolhido = sobremesas[2]
        else:
            print("ERRO: Selecione uma opção válida!")
            return None

    # ------------------------------ BEBIDAS ------------------------------
    elif escolha_usuario == 7:
        print("1 - Natural")
        print("2 - Gasosa")
        print("3 - Sem gás")
        try:
            escolha_bebida = int(input("Qual tipo de bebida prefere? "))
        except ValueError:
            print("ERRO: Insira um número válido!")
            return None
        
        if escolha_bebida == 1:
            prato_escolhido = bebidas[0]
        elif escolha_bebida == 2:
            prato_escolhido = bebidas[1]
        elif escolha_bebida == 3:
            prato_escolhido = bebidas[2]
        else:
            print("ERRO: Selecione uma opção válida!")
            return None

    else:
        print("ERRO: Categoria inválida!")
        return None

    # Retorna o prato escolhido ao main
    return prato_escolhido