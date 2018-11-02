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
