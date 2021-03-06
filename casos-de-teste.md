# Caso de Teste 1  - Criar pingout

* Descrição do Caso de Teste
  * Testar a criação do pingout ao realizar um POST na url /create-pingout, afim de receber o código 201 e um UUID como resposta.
* Condição de Execução
  * Descreve uma condição a ser experimentada durante este teste.
  * Precondições
    * O caso de teste pode ser rodado a qualquer momento, desde que o servidor esteja ligado.
  * Inputs de Teste
    * O 'client', ele é responsável pela requisição no sistema.
  * Pontos de Observação
    * Não há.
  * Pontos de Controle
    * Não há.
  * Resultados Esperados
    * É esperado que retorne uma resposta de código 201 e um JSON contendo o UUID.
  * Pós-condições
    * Ele não precisa desfazer nenhuma configuração nada, pois ele não faz nenhuma configuração importante que pode impactar em outros casos de teste.

# Caso de Teste 2 - Bloquear requisições GET no create-pingout

* Descrição do Caso de Teste
  * Testar o bloqueio de requisições GET na url /create-pingout, afim de receber o código 405 como resposta
* Condição de Execução
  * Descreve uma condição a ser experimentada durante este teste.
  * Precondições
    * O caso de teste pode ser rodado a qualquer momento, desde que o servidor esteja ligado.
  * Inputs de Teste
   * O 'client', ele é responsável pela requisição no sistema.
  * Pontos de Observação
    * Não há.
  * Pontos de Controle
    * Não há.
  * Resultados Esperados
    * É esperado que retorne uma resposta de código 405.
  * Pós-condições
    * Ele não precisa desfazer nenhuma configuração nada, pois ele não faz nenhuma configuração importante que pode impactar em outros casos de teste.

# Caso de Teste 3 - Armazenar Ping

* Descrição do Caso de Teste
  * Realizar uma requisição POST na URL “valid_uuid”/ping .
* Condição de Execução
  * Descreve uma condição a ser experimentada durante este teste.
  * Precondições
    * Exista um pingout criado no banco
  * Inputs de Teste
    * UUID do pingout
  * Pontos de Observação
    * Não há
  * Pontos de Controle
    * Não há
  * Resultados Esperados
    * É esperado que retorne uma resposta de código 201 e que o ping.
  * Pós-condições
    * O ping é salvo no banco

# Caso de Teste 4 - Realizar ping com UUID inexistente

* Descrição do Caso de Teste
  * Realizar uma requisição POST na URL “nonexistent_uuid”/ping co, uuid inexistente.
* Condição de Execução
  * Descreve uma condição a ser experimentada durante este teste.
  * Precondições
    * O caso de teste pode ser rodado a qualquer momento, desde que o servidor esteja ligado.
  * Inputs de Teste
    * UUID válido porém não salvo no banco
  * Pontos de Observação
    * Não há
  * Pontos de Controle
    * Não há
  * Resultados Esperados
    * É esperado que retorne uma resposta de código 404.
  * Pós-condições
    * O ambiente não sofre nenhuma alteração devido ao processo do teste.

# Caso de Teste 5 - Realizar ping com UUID inválido

* Descrição do Caso de Teste
  * Realizar uma requisição POST na URL “nonexistent_uuid”/ping co, uuid inválido.
* Condição de Execução
  * Descreve uma condição a ser experimentada durante este teste.
  * Precondições
  * O caso de teste pode ser rodado a qualquer momento, desde que o servidor esteja ligado.
    * Inputs de Teste
    * UUID inválido.
  * Pontos de Observação
    * Não há.
  * Pontos de Controle
    * Não há.
  * Resultados Esperados
    * É esperado que retorne uma resposta de código 400.
  * Pós-condições
    * O ambiente não sofre nenhuma alteração devido ao processo do teste.

# Caso de Teste 6 - Bloquear Requisições GET no ping

* Descrição do Caso de Teste
  * Testar o bloqueio de requisições GET na URL /ping
* Condição de Execução
  * Descreve uma condição a ser experimentada durante este teste.
    * Precondições
  * O caso de teste pode ser rodado a qualquer momento, desde que o servidor esteja ligado.
    * Inputs de Teste
    * UUID válido
  * Pontos de Observação
    * Não há.
  * Pontos de Controle
    * Não há.
  * Resultados Esperados
    * É esperado que retorne uma resposta de código 405.
  * Pós-condições
    * O ambiente não sofre nenhuma alteração devido ao processo do teste


# Caso de Teste 7 -  Acessar o URL de UUID

* Descrição do Caso de Teste
  * Fazer uma requisição GET no  URL /”yourUUID”
  * Testar o armazenamento do ping e data.
* Condição de Execução
  * Descreve uma condição a ser experimentada durante este teste.
  * Precondições
    * Existir uma UUID valida para uso.
  * Inputs de Teste
    * UUID do pingout
  * Pontos de Observação
    * Não há
  * Pontos de Controle
    * Não há
  * Resultados Esperados
    * É esperado que retorne uma resposta de código 200 e um JSON com todos os pings realizados no UUID.
  * Pós-condições
    * Nenhuma.

# Caso de Teste 8 -  Acessar o URL de UUID inválido

* Descrição do Caso de Teste
  * Fazer uma requisição GET no  URL /”invalidUUID” inválido  
  * Testar o armazenamento do ping e data.
* Condição de Execução
  * Descreve uma condição a ser experimentada durante este teste.
  * Precondições
    * Usar um UUID inválido.
  * Inputs de Teste
  * UUID inválido do pingout
    * Pontos de Observação
  * Não há.
    * Pontos de Controle
  * Não há.
    * Resultados Esperados
  * É esperado que retorne uma resposta de código 400.
    * Pós-condições
Nenhuma

# Caso de Teste 9 -  Acessar o URL de UUID inexistente

* Descrição do Caso de Teste
  * Fazer uma requisição GET no  URL /”validUUID” válido, porém inexistente.
  * Testar o armazenamento do ping e data.
* Condição de Execução
    * Descreve uma condição a ser experimentada durante este teste.
  * Precondições
    * Usar um UUID inexistente.
  * Inputs de Teste
    * UUID inexistente do pingout.
  * Pontos de Observação
    * Não há.
  * Pontos de Controle
    * Não há.
  * Resultados Esperados
    * É esperado que retorne uma resposta de código 404.
  * Pós-condições
    * Não há.

# Caso de Teste 10 -  Bloquear requisição POST no URL do UUID

* Descrição do Caso de Teste
  * Fazer uma requisição POST no  URL /”yourUUID” .
* Condição de Execução
  * Descreve uma condição a ser experimentada durante este teste.
    * Precondições
  * Um UUID válido para uso no banco de dados.
    * Inputs de Teste
    * O UUID que será usado para requisição POST.
  * Pontos de Observação
    * Não há.
  * Pontos de Controle
    * Não há.
  * Resultados Esperados
    * É esperado que retorne uma resposta de código 405.
  * Pós-condições
    * Não há.


# Caso de Teste 11 -  Acessar URL filter com dados válidos

* Descrição do Caso de Teste
  * Fazer uma requisição GET no  URL /”yourUUID”/filter/ passando UUID válido e datas válidas
* Condição de Execução
  * Precondições
    * Exista um UUID e datas no banco
  * Inputs de Teste
    * UUID válido
    * Datas válidas
  * Pontos de Observação
    * Não há
  * Pontos de Controle
    * Não há
  * Resultados Esperados
    * É esperado que retorne uma resposta de código 200 e um JSON que contém todos os pings e as datas realizados no range definido.
  * Pós-condições
    * É mostrado os dados de ping filtrados por data

# Caso de Teste 12 -  Acessar URL filter com UUID inválido e datas válidas

* Descrição do Caso de Teste
  * Fazer uma requisição GET no  URL /”invalidUUID”/filter com UUID inválido e datas válidas.
* Condição de Execução
  * Precondições
    * Exista pelo menos um UUID e datas (inicial e final) no banco
  * Inputs de Teste
    * UUID inválida
    * Datas válidas
  * Pontos de Observação
    * Não há
  * Pontos de Controle
    * Não há
  * Resultados Esperados
    * É esperado que retorne uma resposta de código 404.
  * Pós-condições
    * Não há

# Caso de Teste 13 -  Acessar URL do filter com datas com formato inválido

* Descrição do Caso de Teste
  * Fazer uma requisição GET no  URL /”yourUUID”/filter com UUID válido e  o formato das datas inválidas.
* Condição de Execução
  * Precondições
    * Exista pelo menos um UUID e datas (inicial e final) no banco
  * Inputs de Teste
    * UUID válida
    * Datas com formato inválido
  * Pontos de Observação
    * Não há
  * Pontos de Controle
    * Não há
  * Resultados Esperados
    * É esperado que retorne uma resposta 404
  * Pós-condições
    * Não Há

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

# Caso de Teste 20 -  Filtrar para um intervalo de tempo

* Descrição do Caso de Teste
  * Verificar se retorna os pings realizados para aquele UUID específico e para um período entre as datas inicial e final fornecidas.
* Condição de Execução
  * Descreve uma condição a ser experimentada durante este teste.
  * Precondições
  * Inputs de Teste
  * Pontos de Observação
  * Pontos de Controle
  * Resultados Esperados
    * É esperada uma lista dos pings realizados naquele UUID apenas entre as datas em questão.
  * Pós-condições

# Caso de Teste 21 -  Validar formato das datas de entrada para o filtro de intervalo de tempo

* Descrição do Caso de Teste
  * Verificar se a função de filtro de intervalo de tempo lança exceção quando as datas inicial e final não estão no formato esperado (datetime).
* Condição de Execução
  * Descreve uma condição a ser experimentada durante este teste.
  * Precondições
  * Inputs de Teste
  * Pontos de Observação
  * Pontos de Controle
  * Resultados Esperados
    * Que seja lançada a exceção no caso de formato incorreto.
  * Pós-condições

# Caso de Teste 22 -  Filtrar ocorrências em cada dia para um intervalo de tempo

* Descrição do Caso de Teste
  * Verificar se retorna os pings realizados a cada dia para aquele UUID específico e para um período entre as datas inicial e final fornecidas.
* Condição de Execução
  * Descreve uma condição a ser experimentada durante este teste.
  * Precondições
  * Inputs de Teste
  * Pontos de Observação
  * Pontos de Controle
  * Resultados Esperados
    * É esperada uma lista dos dias e dos pings realizados a cada dia naquele UUID apenas entre as datas em questão.
  * Pós-condições

# Caso de Teste 23 -  Validar formato das datas de entrada para o filtro de ocorrências em um intervalo de tempo

* Descrição do Caso de Teste
  * Verificar se a função de filtro de ocorrências em um intervalo de tempo lança exceção quando as datas inicial e final não estão no formato esperado (datetime).
* Condição de Execução
  * Descreve uma condição a ser experimentada durante este teste.
  * Precondições
  * Inputs de Teste
  * Pontos de Observação
  * Pontos de Controle
  * Resultados Esperados
    * Que seja lançada a exceção no caso de formato incorreto.
  * Pós-condições

# Caso de Teste 24 -  Validar conexão para a coleção

* Descrição do Caso de Teste
  * Validar conexão do mongo db e retornar a database principal
* Condição de Execução
  * Descreve uma condição a ser experimentada durante este teste.
  * Precondições
  * Inputs de Teste
  * Pontos de Observação
  * Pontos de Controle
  * Resultados Esperados
    * É esperado que retorne o cliente do pingout.
  * Pós-condições

# Caso de Teste 25 -  Validar conexão com a database

* Descrição do Caso de Teste
  * Validar conexão com a coleção principal do app
* Condição de Execução
  * Descreve uma condição a ser experimentada durante este teste.
  * Precondições
  * Inputs de Teste
  * Pontos de Observação
  * Pontos de Controle
  * Resultados Esperados
    * É esperado que retorne a história de pings do pingout.
  * Pós-condições
