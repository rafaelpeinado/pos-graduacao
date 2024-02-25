# Serverless I
Links para o início da aula:
* [AWS Budgets](https://aws.amazon.com/pt/aws-cost-management/aws-budgets/)
* [Como configurar o VSCode local para funcionar com a AWS](https://docs.aws.amazon.com/pt_br/toolkit-for-vscode/latest/userguide/setup-credentials.html)


## Como será o futuro?
* Todo o código que escrevemos é lógica de negócios

## O que é serverless?
* Sem provisionamento de infraestrutura, sem gerenciamento
* Dimensionamento automático
* Pague pelo valor
* Altamente disponível e seguro

## Os aplicativos sem servidor abrangem muitas categorias diferentes de serviços
* **Computação:**
  * AWS Lambda
  * AWS Fargate
* **Armazenamento de dados:**
  * Amazon Simple storage service (S3)
  * Amazon Aurora Serverless
  * Amazon DynamoDB
  * Proxy
* **Integração:**
  * Gateway de API
  * Amazon Simple queue Service (Amazon SQS)
  * Amazon Simple Notification Service (Amazon SNS)
  * Step Functions
  * AWS AppSync
  * Amazon EventBridge

## O que é Amazon API Gateway?
### Interface de programação de aplicativos (API)
"Na construção de aplicativos, uma API simplifica a programação, abstraindo a implementação subjacente e expondo apenas objetos ou ações que o desenvolvedor precisa."

Cliente     --- solicitar -->   API     <->     Servidor Web    <->     Base de dados
            <-- resposta  ---   

Empresas e serviços baseados na Web oferecem APIs para uso dos desenvolvedores, como:
* Redes sociais: Facebook, Twitter, etc
* Processamento de pagamento: Amazon Pay, PayPal, etc

**Obs.:** geralmente REST ou WebSocket

### Amazon API Gateway
O Amazon API Gateway é um serviço totalmente gerenciado (sem servidor) que facilita aos desenvolvedores criar, publicar, manter, monitorar e proteger API em qualquer escala.

* **API Gateway é uma porta de entrada que lida com preocupações comuns, permitindo que os desenvolvedores se concentrem na lógica de negócios**
  * Client -> Amazon API Gateway -> AWS Lambda -> Amazon DynamoDB
  * **Estrangulamento:** ajuda a limitar a quantidade de chamadas em paralelo está acontecendo com a API
  * **Cache**
  * **Autorização**
  * **Chaves de API**
  * **Planos de uso**
  * **Mapeamento de solicitação/resposta**


#### Tipos de endpoint
Isso é uma parte muito importante da escolha, pois quando falamos de serviços serverless não precisamos ficar cuidando dos servidores que estão por baixo, qual zona de disponibilidade. Então a configuração correta desse serviço é muito importante e para isso precisamos ter clareza da necessidade do problema que estamos resolvendo

* **Otimizado para bordas**
  * Utiliza o CloudFront para reduzir a sobrecarga da conexão TLS (reduz o tempo de ida e volta)
    * utiliza CDN
    * isso deixa a aplicação mais próxima do cliente
    * após fazer alterações nessa API, existe um tempo de propagação
  * Projetado para um conjuntos de clientes distribuídos globalmente
* **Regional**
  * Tipo de API recomendado para casos de uso geral
  * Projetado para construir APIs para clientes na mesma região
* **Privado**
  * Acessível apenas na VP (e em redes conectadas à VPC)
  * Projetado para construir APIs usadas internamente ou por microsserviços privados


### Tipos de API
#### Protocolos Suportados

Cliente   ---->   Gateway de API    ---->   Cliente
          <----                     <----
        APIs RESTful              APIs WebSocket


Dentro do API Gateway temos dois protocolos:
* **APIs RESTful**
  * Solicitação/Resposta
  * Métodos HTTP como GET, POST, etc.
  * Comunicação de curta duração
  * Apátrida

* **APIs WebSocket**
  * WebSocket sem servidor
  * Canal de comunicação de duas vias
  * Comunicação de longa duração
  * Com estado


#### APIs RESTful
* **Dois sabores: API REST e API HTTP**
* **API REST é mais rica em recursos**
* **A API HTTP é construída desde o início:**
  * Mas rápido - até 60% mais rápido
  * Custo mais baixo - até 71% mais barato
  * Mais fácil de usar


### Integrações
Pode se conectar a, praticamente, qualquer coisa

API Gateway:
* Funções Lambda
* Terminais HTTP públicos
* Qualquer outro serviço AWS
* Pontos finais em VPC (Virtual Private Cloud)
* AWS Direto Conectar

Caso público de arquitetura do Itaú
* [Itaú Unibanco acelera desenvolvimento do Pix na nuvem AWS](https://aws.amazon.com/pt/solutions/case-studies/itau-pix/)
  * É interessante ter Gateway de API como serviço, seja API Gateway, Apigee ou o Kong, um que não precise ficar cuidando de servidores e de fato usar como serviços para ter menos overhead operacional, ou seja, ficar pensando muito tempo no operacional e menos no negócio

### O Ciclo de solicitação
Essa implementação é pensando muito em segurança, o que é o mínimo para uma API, mesmo sendo privada.
WAF -> Autenticar -> Autorizador -> Autorizar -> Integração

Na [Camada OSI](https://www.alura.com.br/artigos/conhecendo-o-modelo-osi), quando estamos falando de VPN, estamos falando da camada 4 e quando estamos falando dos ataques mais comuns, estamos falando da camada 7

* **WAF (Web Application Firewall):** aparece apenas quando uma lista de controle de acesso à web (ACL) do AWS WAF está configurada para maior segurança. Durante esta fase, as regras do AWS WAF são avaliadas e é tomada uma decisão sobre continuar ou cancelar a solicitação
  * Verifica se não é um tipo de ataque DDoS, se esse usuário não está mandando muitas requisições mais do que deveria e assim por diante
* **Autenticar:** presente apenas quando autorizadores do AWS Identity and Access Management (IAM) são usados. Durante essa fase, as credenciais da solicitação assinada são verificadas. O acesso é concedido ou negado com base no direito do cliente de assumir a função de acesso.
* **Autorizador:** presente apenas quando um autorizador Lambda, JWT ou Amazon Cognito é usado. Durante esta fase, a lógica do autorizador é processada para verificar o direito do usuário de acessar o recurso.
  * não fazer no backend, pois isso é falha de segurança
  * tudo tem que ser feito pré backend
* **Autorizar:** presente apenas quando um autorizador Lambda ou IAM é usado. Durante esta fase, os resultados da fase de **autenticação** e **autorização** são avaliados e aplicados.


## Prática
### [01 - Primeira API](./aula-01/02-API-Gateway/01-Primeira-API/)

[Passo a passo](./aula-01/02-API-Gateway/01-Primeira-API/README.md) para executar as tarefas

* Usar o Norte Virgínia:
  * é a região com menores preços
  * está no melhor level de disponibilidade
* [swagger-api.json](./aula-01/02-API-Gateway/01-Primeira-API/swagger-api.json)
  * é uma maneira de fazer as definições da API, através dele identificamos os paths, os endpoints, os verbos HTTP, a versão, as respostas etc

A principal diferença do GET e do POST, é que o GET os parâmetros são enviados na URL, o que o torna menos seguro. Enquanto o POST, é enviado no corpo da requisição e ele é empacotado e criptografado junto, na ida e na volta.

* **Etapas:**
  * Solicitação de método
  * Solicitação de integração
  * Integração HTTP
  * Resposta de integração
  * Resposta do método

* Cloud9 é uma IDE que sobe na EC2 (uma VM)


## O que é FAAS (Function as a Service)?
### Visão de alto nível

Evento -> Função Lambda -> Serviços AWS ou Bancos de dados ou etc.

* **Função Lambda:**
  * Python
  * Javascript
  * Java
  * Golang
  * C#
  * BYOL
  * Imagens do contêiner

* Cada função tem que resolver um pequeno problema
  * Por exemplo, em um e-commerce o fazer pagamento temos que consultar o número de crédito do cliente, ver se tem saldo, ver se não é uma transação fraudulenta e se temos o item no estoque. Podemos fazer tudo em uma única função? Sim, porém não é recomendado, visto que vai ficar muito grande. Se der erro em algum passo, por exemplo, no segundo, não conseguimos seguir para o terceiro.  
  * Além disso, o Lambda é cobrado pelo tempo, vamos supor que as requisições levam 10 ms, 100ms e 20ms, vamos ter um Lambda que vai ser cobrado por usar 140ms, ou seja, se rodar um Lambda ou três em paralelo, o valor final será o mesmo.
  * Ou seja, se der algum erro, nós podemos retentar apenas uma parte, a que deu erro e depois juntar as respostas (eventos) para seguir com a transação

### A visão de preços
Informações extremamente importantes
* Dois componentes de preços:
  * Número de solicitações
  * Duração (em GB-s)
* A duração é medida em incrementos de 1ms, com base na configuração da memória de função
  * 100ms com 2GB de RAM
    * custa o mesmo que
  * 200ms com 1GB de RAM

* A configuração mais comum de se encontrar é:
  * Por exemplo, uma lista de 100 mil posições e precisamos achar um item nesta lista e correr a lista até achar o item informado. No pior cenário, vamos passar por todos os pontos da lista e achar no último e isso demora. A melhor solução a se usar nesse caso é usar o [HashMap](https://www.geeksforgeeks.org/internal-working-of-hashmap-java/).


### Código de embalagem
* Arquivos compactados (ficam no S3, que é o serviço de Storage)
  * Código de função (/var/tarefa)
  * Camada de função (/opt)
  * Camada de função (/opt)
  * Sistema operacional (AL ou AL2)
* Imagens de contêiner
  * Imagem do contêiner de função

Em arquivos compactados vamos supor que temos uma aplicação node e ao usar o npm ele cria uma pasta node_modules com todas as dependências. Ao empacotar tudo, a aplicação pode ficar com, por exemplo, 200MB e compactado com 50MB, o que é muita coisa. O ideal é que o **Código da Função** seja de 1MB. Então o código da função fica todo o código criado e as camadas é colocado as dependências daquele código.

Por exemplo, vamos supor que temos uma aplicação com 10 endpoints, ou seja, deveríamos ter 10 funções Lambda. E supondo que esses 10 Lambdas estão conectados no mesmo banco de dados o MySQL. Ou seja, todos têm a mesma dependência. Ou seja, podemos usar a mesma layer (Camada da Função) para todos eles e ainda podemos versionar as layers.
Com isso, podemos ganhar velocidade na hora que o Lambda vai ficar pronto.

### AWS Lambda nos bastidores
Tem workers com microVM que fazem cold start

## Modos de invocação do Lambda
* Mapeamentos de origem de eventos
* Front-end
* Fila interna

### Três modos de invocação
É importante entender a diferença, pois o tratamento de erro é diferente para cada um
* **Síncrono:** quando o chamador espera uma resposta da função
  * o tratamento é feito do lado do cliente
* **Assíncrono:** quando o chamador não espera uma resposta da função
  * chama via S3, SNS
  * Quando o Lambda falha, ele tem um fila de eventos
* **Mapeamento de origem de eventos:** integração com fontes de eventos específicos. Synchronous under the hood.
  * streaming de dados
  * comportamento igual oo síncrono

**Diferença entre Síncrono e Mapeamento de origem de eventos**
* Na chamada síncrona, recebemos um evento e tratamos ele. 
* Em um streaming de dados geralmente olhamos para janela de tempo como, por exemplo, 200ms. Todos os eventos dentro de 200ms serão enviados de uma vez.


#### Modo de invocação síncrona
* Útil quando você precisa de uma **resposta imediata** da função.
* Os erros são retornados ao chamador.
* Retorna aceleradores quando você atinge o limite de simultaneidade.
  * vamos supor que temos 1000 requisições em paralelo na API, só que posso permitir que na hora que chegue 1000, ele permita a chegar em 1500 por 10 segundos e depois abaixar.

**Obs.:** **nunca** retornar o stack trace do erro para quem chamou. Pegar o stack trace, que é os detalhes do erro que mostram a linha, as dependências e etc, é uma falha de segurança crítica, pois estamos expondo muitos detalhes da aplicação.


#### Modo de invocação assíncrona
* O chamador obtém apenas uma **confirmação** da função Lambda.
* Fila interna que pode persistir mensagens por até 6 horas
* Suporta novas tentativas (até 2 tentativas ou 3 invocações no total), destinos e DLQ (Dead-Letter Queue).


#### Mapeamento de origem de eventos
* O Mapeamento da Fonte de Eventos **extrai** mensagens na origem e, em seguida, faz invocações síncronas.
* Pode fazer lotes, tratamentos de erros e muito mais. Os recursos exatos diferem de acordo com a origem do evento.


### Arquiteturas de amostra
* **Síncrono:**
  * Gateway de API da Amazon -> AWS Lambda
  * AWS AppSync (GraphQL) -> AWS Lambda
  * Funções de etapas da AWS (Máquinas de Estados) -> AWS Lambda

* **Assíncrono:**
  * Amazon SNS -> AWS Lambda
  * Amazon Event Bridge -> AWS Lambda
  * Configuração AWS -> AWS Lambda

* **Mapeamento de origem de eventos:**
  * Amazon DynamoDB -> AWS Lambda
  * Amazon SQS -> AWS Lambda
  * Amazon MQ -> AWS Lambda


### Ambientes de execução Lambda
* **Ambientes de Execução (EE):** onde seu código realmente é executado. Um EE lida com uma solicitação por vez.
* **Simultaneidade:** número de EEs servindo ativamente o tráfego para uma determinada Função/Versão/Alias.

Simultaneidade aproximadamente RPS x Duração
Simultaneidade <= número de EEs


### Ciclo de vida do ambiente de execução
Inicialização, invocar, invocar, invocar, desligar
* São pagos apenas Inicialização e invocação
* O máximo que um ambiente fica de pé são 6h, mas o Lambda aprende a necessidade e tempo de manter esse ambiente rodando


## Prática
### [03-Lambda](./aula-01/03-Lambda/)
Foi usado uma Lambda simples usando serverless framework, que é um modelo de infraestrutura como código para desenvolver serverless e pode ser usado AWS, Azure etc.

[03-Lambda Intro](./aula-01/03-Lambda/01-intro/README.md)
* **timeout:** cada execução de Lambda pode durar até 15 minutos, porém o importante de setar o timeout é que caso o serviço dê algum erro, ele não fique executando por muito tempo. Então, se temos um serviço que a execução demora em média 180ms, é muito seguro um timeout de 300ms, levando em consideração que de vez em quando ela vai demorar mais.

* **sls deploy --verbose:** para fazer deploy da função
* **sls invoke -f hello**: para chamar a função hello que foi criada
* **sls invoke local -f hello:** para chamar a função localmente
* **sls remove:** remove tudo do cloud

Não é recomendado usar o serverless para S3, Dynamo. Para esses casos usamos o CDK ou Terraform e conecta o serverless com o CDK


[03-Lambda Layers](./aula-01/03-Lambda/02-Layers/README.md)
* **sls create --template "aws-python3":** vai criar o serverless.yaml e o handler.py
* **requirements.txt:** para criar dependências do python
* **boto3:** é o SDK do AWS para Python

**Obs.:** **podemos ter até cinco layers por Lambda** e a soma do código com todas as layers zipadas não podem passar de 50MB e descompactada não pode passar de 250MB.
* É possível fazer controle de versão na camada de dependências.


## Observabilidade
### Métricas
* **Construídas em**
  * **REST:** contagem de chamadas de API, latência, 4XXs, 5XXs, latência de integração, contagem de ocorrências de cache, contagem de falhas de cache
  * **HTTP:** contagem de chamadas de API, latência, 4XXs, 5XXs, latência de integração, dados processados
  * **WebSocket:** contagem de conexões, contagem de mensagens, erro de integração, erro de cliente, erro de execução, latência de integração
* **Personalizado**
  * Crie métricas personalizadas por meio do filtro de métricas a partir de registros

### Exploração de Logs
* **Registros de execução**
  * dois níveis de registro, ERROR e INFO
  * opcionalmente, registre a solicitação do método/conteúdo do corpo
  * definir globalmente no cenário ou substituir por método
* **Registros de acesso**
  * formato personalizável para logs analisáveis por máquina
  * logs do CloudWatch ou Kinesis Firehose

### Rastreamento - [X-Ray](https://aws.amazon.com/pt/xray/)
O caminho que foi percorrido para acessar o serviço.
* tempo de ida e de volta
* se deu erro em algum ponto
* qual foi a query no banco de dados

## Prática
Fazer conexões HTTP API com Lambda function e DynamoDB
[02-HTTP-API](./aula-01/02-API-Gateway/02-HTTP-API/README.md)

**Obs..:** O DynamoDB funciona melhor trazendo um milhão de requisições em paralelo e trazer uma linha do que trazer um milhão de linha em uma requisição. Ele é chave-valor muito rápido. Inclusive, ele é tão rápido que estão deixando de usar o Redis para usar o Dynamo


[03-Validacao-Autenticacao](./aula-01/02-API-Gateway/03-Validacao-Autenticacao/README.md)
* [JSON Schema](https://json-schema.org/): importante estudar, porque através dele podemos criar um JSON que faz validação dos dados antes de chegar no backend.
* [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
* [OWASP Top Ten API](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)

Quando pensamos muito em custo, temos dois tipos de arquitetura:
* **x86_64:** arquitetura da Intel (i3, i5, i7, i9)
* **arm64:** funciona diferente do x86_64 e gasta menos energia. Essa arquitetura ficou muito conhecida com as placas de automação residencial
  * caso decidir usar arm, o código precisa ser compilado e as dependências instaladas precisam ser para arm64.

A principal diferença entre API REST e API HTTP, está no plano de ação, por exemplo. Essa função só está disponível no API REST.


## Observações e Referências
* [Itaú Unibanco acelera desenvolvimento do Pix na nuvem AWS](https://aws.amazon.com/pt/solutions/case-studies/itau-pix/)
* O serverless não é recomendado quando, por exemplo, usar o API Gateway ele vai ter uma cobrança específica por milhão de mensagem que vai diminuindo até bilhão, teremos tanta mensagem isso desde o estágio inicial da empresa, que o preço vai inviabilizar
* [Conheça as diferenças entre HTTP/1.1 e HTTP/2](https://www.neomind.com.br/blog/diferencas-entre-http1-1-e-http2/)

* **Diferença entre microVM, VM e contêineres**
  * microVM é um conceito de como vamos rodar o serviço
  * A diferença de VM e contêiner é que a VM tem um SO inteiro para rodar a aplicação em cima, enquanto o contêiner tem uma abstração do sistema operacional com Runtime do Container no meio.
  * Uma microVM se aproxima muito dos contêineres, porém a diferença é que a microVM tem que ser mais rápida que o contêiner, porque um contêiner pode subir para receber milhares de requisições ao mesmo tempo. E cada microVM responde a uma requisição por vez.
  * [Firecracker](https://firecracker-microvm.github.io/)


