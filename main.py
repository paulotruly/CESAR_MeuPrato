
# Cardápio 

# Função, CRUD, estrutura de dados, manipulação de arquivos e tratamento de erros e execeções

carne_vermelha = ["Picanha grelhada", "Filé mignon ao molho madeira", "Costela assada"]
aves = ["Frango grelhado com ervas", "Peru assado com farofa", "Magret de pato ao molho de laranja"]
frutos_mar = ["Camarão na moranga", "Salmão grelhado", "Lula à dorê"]
pratos_veganos = ["Lasanha de berinjela", "Grão-de-bico com legumes", "Estrogonofe de palmito"]
graos_massas = ["Arroz à grega", "Espaguete ao sugo", "Risoto de cogumelos"]
sobremesas = ["Pudim de leite", "Mousse de maracujá", "Torta de limão"]
bebidas = ["Suco natural", "Refrigerante", "Água com gás"]

print("1 - Carne vermelha")
print("2 - Aves")
print("3 - Frutos do mar")
print("4 - Pratos veganos")
print("5 - Grãos e massas")
print("6 - Sobremesas")
print("7 - Bebidas")
escolha_usuario = int(input("Qual categoria de alimento você deseja apreciar hoje?"))


# ------------------------------ CARNE VERMELHA ------------------------------

if (escolha_usuario == 1):
    
    print("1 - Com osso")
    print("2 - Sem osso")
    print("3 - Ambos")
    escolha1_carne = int(input("Você gosta de carne com osso ou sem osso?"))
    
    if (escolha1_carne == 1):
        print("O prato perfeito pra você hoje é: " + carne_vermelha[2])
        
    elif (escolha1_carne == 2):
        print("1 - Com molho")
        print("2 - Sem molho")
        print("3 - Ambos")
        escolha2_carne = int(input("Você prefere a carne ao molho sem molho?"))
        
        if (escolha2_carne == 1):
            print("A escolha perfeita pra você é: " + carne_vermelha[1])
        elif (escolha2_carne == 2):
            print("A escolha perfeita pra você é: " + carne_vermelha[0])
        elif (escolha2_carne == 3):
            print("Temos duas opções que cabem no seu gosto: " + carne_vermelha[1] + " e " + carne_vermelha[0])
        else: 
            print("ERRO: Selecione uma opção válida!")
            
    elif (escolha1_carne == 3):
        print("1 - Com molho")
        print("2 - Sem molho")
        print("3 - Ambos")
        escolha2_carne = int(input("Você prefere a carne ao molho ou sem molho?"))
        
        if (escolha2_carne == 1):
            print("A escolha perfeita pra você é: " + carne_vermelha[1])
        elif (escolha2_carne == 2):
            print("Temos duas opções que cabem no seu gosto: " + carne_vermelha[0] + " e " + carne_vermelha[2])
        elif (escolha2_carne == 3):
            print("Temos três opções que cabem no seu gosto: " + carne_vermelha[1] + ", " + carne_vermelha[0] + " e " + carne_vermelha[2])  
        else: 
            print("ERRO: Selecione uma opção válida!")    
    
    else:
        print("ERRO: Selecione uma opção válida!")
        
# ---------------------------------------------------------------------------
     
      
elif (escolha_usuario == 2):
    print(aves)
    
    
    
elif (escolha_usuario == 3):
    print(frutos_mar)
    
    
    
elif (escolha_usuario == 4):
    print(pratos_veganos)
    
    
    
elif (escolha_usuario == 5):
    print(graos_massas)
    
    
    
elif (escolha_usuario == 6):
    print(sobremesas)
    
    
    
elif (escolha_usuario == 7):
    print(bebidas)
    
       
else:
    print("ERRO: Selecione uma opção válida!")    

