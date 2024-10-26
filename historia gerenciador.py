import random

# Função que gera a introcução da história
def gerar_introducao():
     introducoes = [ "Em um belo dia","Há muito tempo atrás","em uma cidade muito distante","em um lugar muito diferente" ]
     return random.choice (introducoes)

# Função que gera o desenvolvimento da história
def gerar_desenvolvimento ():
     desenvolvimentos = ["um duende " , "um burro " , "um principe" ,
                         "uma princesa " , "uma gorota"]
     return random.choice(desenvolvimentos)

# Função que gera o final da história
def gerar_final ():
     finais = ["um se aventurou por toda a floresta" , " desceu rolando de uma rampa"
               " não gostou do estilo da sua vida e virou um pirata." , " entrou em um portal mágico." ,
               "encontrou um amor verdadeiro."]
     return random.choice (finais)

# Função prinicipal que gera toda a história 
def gerar_historia ():
     introducao = gerar_introducao()
     desenvolvimento = gerar_desenvolvimento() 
     final = gerar_final () 

     historia = f"{introducao} {desenvolvimento} {final} "
     return historia 

# Exibe a história gerada 
if  __name__ == "__main__":
     print ( gerar_historia())