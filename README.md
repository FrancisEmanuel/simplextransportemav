# simplextransportemav
Neste trabalho foi desenvolvido um algoritmo simplex adaptado ao transporte, utilizando o método de aproximação de Vogel(MAV). Onde é possível encontrar o menor custo de transporte, minimizar Z, levando em consideração as demandas, fornecimentos e custos.

### Método de aproximação de Vogel (MAV)
É uma versão melhorada do método do menor custo, em geral, mas não sempre, produz soluções mehores.

#### Algoritmo desenvolvido
O Algoritmo foi desenvolvido de acordo com o método descrito no livro do Taha.
**A função mav:**
- Define as multas
- seleciona a maior multa e o menor custo unitário 
- Substitui a celula selecionada pela demanda ou fornecimento
