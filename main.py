# Cardápio 

# Função, CRUD, estrutura de dados, manipulação de arquivos e tratamento de erros e execeções

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
escolha_usuario = int(input("Qual categoria de alimentos você deseja apreciar hoje?"))

# ------------------------------ CARNE VERMELHA ------------------------------

if (escolha_usuario == 1):    
    print("1 - Cotidiano/Casual")
    print("2 - Sofisticado/Formal")
    print("3 - Sem ocasião específica")
    escolha1_carne = int(input("Qual ocasião do encontro de hoje?"))
    
    if (escolha1_carne == 1):
        print("O prato perfeito pra você hoje é: " + carne_vermelha[0])
        
    elif (escolha1_carne == 2):
        print("1 - Com estrutura óssea")
        print("2 – Corte limpo/desossado")
        print("3 - Gostaria de ver ambas as opções")
        escolha2_carne = int(input("Você prefere a carne com qual estilo de corte?"))
        
        if (escolha2_carne == 1):
            print("A escolha perfeita pra você hoje é: " + carne_vermelha[2])
        elif (escolha2_carne == 2):
            print("A escolha perfeita pra você hoje é: " + carne_vermelha[1])
        elif (escolha2_carne == 3):
            print("Temos duas opções que podem atender ao seu paladar:  " + carne_vermelha[1] + " e " + carne_vermelha[2])
        else: 
            print("ERRO: Selecione uma opção válida!")
            
    elif (escolha1_carne == 3):
        print("1 - Com molho")
        print("2 - Sem molho")
        print("3 - Ambos")
        escolha2_carne = int(input("Você prefere a carne com preparo ao molho ou sem molho?"))
        
        if (escolha2_carne == 1):
            print("A escolha perfeita pra você hoje é: " + carne_vermelha[1])
        elif (escolha2_carne == 2):
            print("Temos duas opções que podem atender ao seu paladar: " + carne_vermelha[0] + " e " + carne_vermelha[2])
        elif (escolha2_carne == 3):
            print("Temos três opções que podem atender ao seu paladar: " + carne_vermelha[0] + ", " + carne_vermelha[1] + " e " + carne_vermelha[2])  
        else: 
            print("ERRO: Selecione uma opção válida!")    
    
    else:
        print("ERRO: Selecione uma opção válida!")

# -----------------------------------------------------------------------
# ------------------------------ AVES ------------------------------

if (escolha_usuario == 2):
    print("1 - Cotidiano/Casual")
    print("2 - Sofisticado/Formal")
    print("3 - Sem ocasião específica")
    escolha1_ave = int(input("Qual ocasião do encontro de hoje?"))
    
    if (escolha1_ave == 1):
        print("O prato perfeito pra você hoje é: " + aves[0])
        
    elif (escolha1_ave == 2):
        print("1 - Com estrutura óssea")
        print("2 – Corte limpo/desossado")
        print("3 - Gostaria de ver ambas as opções")
        escolha2_ave = int(input("Você prefere ave com qual estilo de corte?"))
        
        if (escolha2_ave == 1):
            print("A escolha perfeita pra você hoje é: " + aves[1])
        elif (escolha2_ave == 2):
            print("A escolha perfeita pra você hoje é: " + aves[2])
        elif (escolha2_ave == 3):
            print("Temos duas opções que podem atender ao seu paladar:  " + aves[1] + " e " + aves[2])
        else: 
            print("ERRO: Selecione uma opção válida!")
            
    elif (escolha1_ave == 3):
        print("1 - Com molho")
        print("2 - Sem molho")
        print("3 - Ambos")
        escolha3_ave = int(input("Você prefere ave com preparo ao molho ou sem molho?"))
        
        if (escolha3_ave == 1):
            print("A escolha perfeita pra você hoje é: " + aves[2])
        elif (escolha3_ave == 2):
            print("Temos duas opções que podem atender ao seu paladar:  " + aves[0] + " e " + aves[1])
        elif (escolha3_ave == 3):
            print("Temos três opções que podem atender ao seu paladar:  " + aves[0] + ", " + aves[1] + " e " + aves[2])  
        else: 
            print("ERRO: Selecione uma opção válida!")    
    
    else:
        print("ERRO: Selecione uma opção válida!")

# ------------------------------------------------------------------------------------------
# ------------------------------ FRUTOS DO MAR ------------------------------

elif (escolha_usuario == 3):  
    print("1 - Cotidiano/Casual")
    print("2 - Sofisticado/Formal")
    print("3 - Sem ocasião específica")
    escolha1_mar = int(input("Qual ocasião do encontro de hoje?"))
    
    if (escolha1_mar == 1):
        print("O prato perfeito pra você hoje é: " + frutos_mar[0])
        
    elif (escolha1_mar == 2):
        print("1 - Grelhado")
        print("2 - Frito")
        print("3 - Gostaria de ver as opções gerais")
        escolha2_mar = int(input("Você prefere frutos do mar com preparo grelhado ou frito?"))
        
        if (escolha2_mar == 1):
            print("A escolha perfeita pra você é: " + frutos_mar [1])
        elif (escolha2_mar == 2):
            print("A escolha perfeita pra você é: " + frutos_mar [2])
        elif (escolha2_mar == 3):
            print("Temos duas opções que podem atender ao seu paladar:  " + frutos_mar [1] + " e " + frutos_mar [2])
        else: 
            print("ERRO: Selecione uma opção válida!")
            
    elif (escolha1_mar == 3):
        print("1 - Com molho")
        print("2 - Sem molho")
        print("3 - Ambos")
        escolha2_mar = int(input("Você prefere ave com preparo ao molho ou sem molho?"))
        
        if (escolha2_mar == 1):
            print("A escolha perfeita pra você hoje é: " + frutos_mar [0])
        elif (escolha2_mar == 2):
            print("Temos duas opções que podem atender ao seu paladar: " + frutos_mar [1] + " e " + frutos_mar [2])
        elif (escolha2_mar == 3):
            print("Temos três opções que podem atender ao seu paladar: " + frutos_mar [0] + ", " + frutos_mar [1] + " e " + frutos_mar[2])  
        else: 
            print("ERRO: Selecione uma opção válida!")    
    
    else:
        print("ERRO: Selecione uma opção válida!")

# ------------------------------------------------------------------------------------
# ------------------------------ PRATOS VEGANOS -----------------------------

elif (escolha_usuario == 4):  
    print("1 - Cotidiano/Casual")
    print("2 - Sofisticado/Formal")
    print("3 - Sem ocasião específica")
    escolha1_veganos = int(input("Qual ocasião do encontro de hoje?"))
    
    if (escolha1_veganos == 1):
        print("1 - Cozido")
        print("2 - Refogado")
        print("3 - Gostaria de ver as opções gerais")
        escolha2_veganos = int(input("Você prefere pratos veganos com preparo cozido ou refogado?"))
        
        if (escolha2_veganos == 1):
            print("A escolha perfeita pra você hoje é: " + pratos_veganos [1])
        elif (escolha2_veganos == 2):
            print("A escolha perfeita pra você hoje é: " + pratos_veganos [2])
        elif (escolha2_veganos == 3):
            print("Temos três opções que podem atender ao seu paladar: " + pratos_veganos [1] + " e " + pratos_veganos [2])
        else: 
            print("ERRO: Selecione uma opção válida!")
        
    elif (escolha1_veganos == 2):
        print("O prato perfeito pra você hoje é: " + pratos_veganos [0])
            
    elif (escolha1_veganos == 3):
        print("1 - Encorpada")
        print("2 - Cremosa")
        print("3 – Leve")
        print("4 – Gostaria de ver as opções gerais")
        escolha3_veganos = int(input("Você prefere pratos veganos com qual tipo de textura?"))
        
        if (escolha3_veganos == 1):
            print("A escolha perfeita pra você hoje é: " + pratos_veganos [0])
        elif (escolha3_veganos == 2):
            print("A escolha perfeita pra você hoje é: " + pratos_veganos [2])
        elif (escolha3_veganos == 3):
             print("A escolha perfeita pra você hoje é: " + pratos_veganos [1])
        elif (escolha3_veganos == 4):
             print("Temos três opções que podem atender ao seu paladar: " + pratos_veganos [0] + " , " + pratos_veganos [1] + " e " + pratos_veganos [2])
        else: 
            print("ERRO: Selecione uma opção válida!")    
    
    else:
        print("ERRO: Selecione uma opção válida!")

# -----------------------------------------------------------------------------------
# ------------------------------ GRÃOS E MASSAS -----------------------------

elif escolha_usuario == 5:
    print("1 - Cotidiano/Casual")
    print("2 - Sofisticado/Formal")
    print("3 - Sem ocasião específica")
    escolha1_graos_massas = int(input("Qual ocasião do encontro de hoje? "))

    if escolha1_graos_massas == 1:
        print("1 - Grão")
        print("2 - Massa")
        print("3 - Gostaria de ver as opções gerais")
        escolha2_graos_massas = int(input("Você prefere qual base principal de preparo? "))

        if escolha2_graos_massas == 1:
            print("A escolha perfeita pra você hoje é: " + graos_massas[0])
        elif escolha2_graos_massas == 2:
            print("A escolha perfeita pra você hoje é: " + graos_massas[1])
        elif escolha2_graos_massas == 3:
            print("Temos duas opções que podem atender ao seu paladar: " + graos_massas[0] + " e " + graos_massas[1])
        else: 
            print("ERRO: Selecione uma opção válida!")

    elif escolha1_graos_massas == 2:
        print("O prato perfeito pra você hoje é: " + graos_massas[2])

    elif escolha1_graos_massas == 3:
        print("1 - Encorpada")
        print("2 - Cremosa")
        print("3 - Leve")
        print("4 - Gostaria de ver as opções gerais")
        escolha2_graos_massas = int(input("Você prefere pratos com qual tipo de textura? "))

        if escolha2_graos_massas == 1:
            print("A escolha perfeita pra você hoje é: " + graos_massas[1])
        elif escolha2_graos_massas == 2:
            print("A escolha perfeita pra você hoje é: " + graos_massas[2])
        elif escolha2_graos_massas == 3:
            print("A escolha perfeita pra você hoje é: " + graos_massas[0])
        elif escolha2_graos_massas == 4:
            print("Temos três opções que podem atender ao seu paladar: " +
                  graos_massas[0] + ", " + graos_massas[1] + " e " + graos_massas[2])
        else: 
            print("ERRO: Selecione uma opção válida!")    

    else:
        print("ERRO: Selecione uma opção válida!")

# ------------------------------------------------------------------------------
# ------------------------------ SOBREMESAS -----------------------------

elif escolha_usuario == 6:
    print("1 - Nostálgico")
    print("2 - Refrescante")
    print("3 - Cítrico")
    print("4 - Gostaria de ver as opções gerais")
    escolha1_sobremesas = int(input("Qual sensação você quer experimentar com nossas sobremesas? "))

    if escolha1_sobremesas == 1:
        print("A escolha perfeita para você hoje é: " + sobremesas[0])
    elif escolha1_sobremesas == 2:
        print("A escolha perfeita para você hoje é: " + sobremesas[1])
    elif escolha1_sobremesas == 3:
        print("A escolha perfeita para você hoje é: " + sobremesas[2])
    elif escolha1_sobremesas == 4:
        print("Temos três opções que podem atender ao seu paladar: " +
              sobremesas[0] + ", " + sobremesas[1] + " e " + sobremesas[2])
    else:
        print("ERRO: Selecione uma opção válida!")

# -----------------------------------------------------------------------
# ------------------------------ BEBIDAS -----------------------------

elif escolha_usuario == 7:
    print("1 - Natural")
    print("2 - Popular")
    print("3 - Essencial")
    print("4 - Gostaria de ver as opções gerais")
    escolha1_bebidas = int(input("Qual apelo gastronômico você quer fazer uso para escolher sua bebida hoje? "))

    if escolha1_bebidas == 1:
        print("A escolha perfeita para você hoje é: " + bebidas[0])
    elif escolha1_bebidas == 2:
        print("A escolha perfeita para você hoje é: " + bebidas[1])
    elif escolha1_bebidas == 3:
        print("A escolha perfeita para você hoje é: " + bebidas[2])
    elif escolha1_bebidas == 4:
        print("Temos três opções que podem atender ao seu paladar: " +
              bebidas[0] + ", " + bebidas[1] + " e " + bebidas[2])
    else:
        print("ERRO: Selecione uma opção válida!")

# ----------------------------------------------------------

else:
    print("ERRO: Selecione uma opção válida!")