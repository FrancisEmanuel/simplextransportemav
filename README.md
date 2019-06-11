# simplextransportemav
Neste trabalho foi desenvolvido um algoritmo simplex adaptado ao transporte, utilizando o método de aproximação de Vogel(MAV). Onde é possível encontrar o menor custo de transporte, minimizar Z, levando em consideração as demandas, fornecimentos e custos.

### Método de aproximação de Vogel (MAV)
É uma versão melhorada do método do menor custo, em geral, mas não sempre, produz soluções mehores.

#### Algoritmo desenvolvido
O Algoritmo foi desenvolvido de acordo com o método descrito no livro do Taha.
<p>**A função mav:**
     - Define as multas
     - seleciona a maior multa e o menor custo unitário 
     - Substitui a celula selecionada pela demanda ou fornecimento
  
  ```
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
  ```
