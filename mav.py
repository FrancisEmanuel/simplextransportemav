"""
                        fRANCIS EMANUEL OLIVEIRA

    Desenvolvimento de algoritmo simplex adaptado ao transporte
    
"""
import numpy as np

def mav(aux, inicio, demanda,fornecimento,soma_id_linha, soma_id_coluna, demanda_nova,fornecimento_novo,z):
    multa_linha = np.array([])
    multa_coluna = np.array([])
    
    tam_coluna = aux[:,0].size
    tam_linha = aux[0,:].size
    
    li = 0
    while li<tam_coluna:
        multa = 0
        linha = np.sort(aux[li,:])
        multa = linha[1]-linha[0]
        multa_linha = np.append(multa_linha,multa)
        li=li+1
   
    
    col = 0
    while col<tam_linha:
        multa = 0
        coluna = np.sort(aux[:,col])
        multa = coluna[1]-coluna[0]
        multa_coluna = np.append(multa_coluna,multa)
        col=col+1
        
    
#========= Maior multa e a Celula com menor custo unitário ====================#

    if multa_linha.max()>multa_coluna.max():
        maior_multa = multa_linha.max()
        linha_celula = multa_linha.argmax()
        coluna_celula = np.argmin(aux[linha_celula,:]) 

    else:
        maior_multa = multa_coluna.max()
        coluna_celula = multa_coluna.argmax()
        linha_celula = np.argmin(aux[:,coluna_celula]) 
            
#======== Substitui a celula selecionada pela demanda ou fornecimento ========#   
      
    if multa_linha.max()>multa_coluna.max():
        # Soma os termos de Z, ex.: Z= 15*2+...
        z = z + inicio[linha_celula,coluna_celula+soma_id_linha] * demanda[coluna_celula] 
                                                                                          
        #Substitui   
        inicio[linha_celula,coluna_celula+soma_id_linha] = demanda[coluna_celula]          
        soma_id_linha = soma_id_linha+1
        aux = np.delete(aux,coluna_celula,1)
        #Novo fornecimento
        fornecimento_novo[linha_celula]=fornecimento[linha_celula]-demanda[coluna_celula] 
        #Cancela a Coluna
        demanda = np.delete(demanda,coluna_celula,0)                                      

    else:
        # Soma os termos de Z, ex.: Z= 15*2+...
        z = z + inicio[linha_celula+soma_id_coluna,coluna_celula] * fornecimento[linha_celula] 
                                                                                               
        inicio[linha_celula+soma_id_coluna,coluna_celula] = fornecimento[linha_celula]
        soma_id_coluna = soma_id_coluna+1
        aux = np.delete(aux,linha_celula,0)
        
        demanda_nova[coluna_celula]=demanda[linha_celula]-fornecimento[coluna_celula]
        fornecimento = np.delete(fornecimento,linha_celula,0)
        
    return aux, demanda, fornecimento,soma_id_linha, soma_id_coluna,demanda_nova, fornecimento_novo,z


# -------- START -------
    
inicio = np.array([[10,2,20,11],
                   [12,7,9,20],
                   [4,14,16,18]])

demanda_nova = demanda = np.array([5,15,15,15])

fornecimento_novo = fornecimento = np.array([15,25,10])
aux = inicio
z = 0
soma_id_linha = 0
soma_id_coluna = 0

while (len(demanda)>1)and(len(fornecimento)>1):    
    aux, demanda, fornecimento,soma_id_linha, soma_id_coluna,demanda_nova, fornecimento_novo, z = mav(aux, inicio, demanda,
                                                                                                   fornecimento,soma_id_linha, 
                                                                                                   soma_id_coluna, demanda_nova,
                                                                                                   fornecimento_novo,z)
    
i=0
while i<len(aux):
    z= z+ aux[i] * fornecimento_novo[i] 
    i=i+1 
    
print(z)
