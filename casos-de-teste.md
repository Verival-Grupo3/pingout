# Caso de Teste 14 -  Acessar URL filter com intervalo de datas inválido
* Descrição do Caso de Teste
    * Fazer uma requisição GET no  URL /”yourUUID”/filter com UUID válido e intervalo de datas inválido
* Condição de Execução
    * Precondições
        * Exista pelo menos um UUID e datas (inicial e final) no banco
    * Inputs de Teste
        * UUID válida
        * Datas inválidas
    * Pontos de Observação
        * Não há
    * Pontos de Controle
        * Não há
    * Resultados Esperados
        * É esperado que retorne uma resposta de código 404
    * Pós-condições
		* Não há

# Caso de Teste 15 -  Criar requisição POST URL filter 
* Descrição do Caso de Teste
    * Fazer uma requisição POST no  URL /”UUID”/filter
* Condição de Execução
    * Precondições
        * Requisição POST com dados aleatórios
    * Inputs de Teste
        * URL
    * Pontos de Observação
        * Não há
    * Pontos de Controle
        * Não há
    * Resultados Esperados
        * É esperado que retorne uma resposta de código 405
    * Pós-condições
        * Não há

# Caso de Teste 16 - Validar UUID com UUID válido
* Descrição do Caso de Teste
    * Validar UUID recebendo UUID válido
* Condição de Execução
    * Precondições
        * O caso de teste pode ser rodado a qualquer momento, desde que o servidor esteja ligado
    * Inputs de Teste
	    * Não há
    * Pontos de Observação
        * Não há
    * Pontos de Controle
        * Não há
    * Resultados Esperados
        * É esperado que retorne true
    * Pós-condições
        * Não há

# Caso de Teste 17 - Validar UUID com UUID inválido
* Descrição do Caso de Teste
    * Validar UUID recebendo UUID inválido
* Condição de Execução
    * Precondições
        * O caso de teste pode ser rodado a qualquer momento, desde que o servidor esteja ligado
    * Inputs de Teste
	    * Não há
    * Pontos de Observação
        * Não há
    * Pontos de Controle
        * Não há
    * Resultados Esperados
        * É esperado que retorne false
    * Pós-condições
        * Não há

# Caso de Teste 18 - Filtrar para todos os pings

* Descrição do Caso dE Teste
    * Verificar se retorna todos os pings já realizados para aquele UUID específico
* Condição de Execução
    * Precondições
        * O caso de teste pode ser rodado a qualquer momento, desde que o servidor esteja ligado
    * Inputs de Teste
	    * Não há
    * Pontos de Observação
        * Não há
    * Pontos de Controle
        * Não há
    * Resultados Esperados
        * É esperada uma lista de todos os pings realizados no UUID em questão
    * Pós-condições
        * Não há

# Caso de Teste 19 -  Filtrar para uma data específica
* Descrição do Caso de Teste
	* Verificar se retorna os pings realizados para aquele UUID específico e para uma data específica
* Condição de Execução
    * Precondições
        Não há
    * Inputs de Teste
        Não há
    * Pontos de Observação
        Não há
    * Pontos de Controle
        Não há
    * Resultados Esperados
        É esperada uma lista dos pings realizados naquele UUID apenas na data em questão.   
    * Pós-condições
        Não há
