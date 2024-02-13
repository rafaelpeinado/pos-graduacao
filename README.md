# Microsserviços I
## Fundamentos
### Histórico
* **Mainframe Monolithic (1980s)**
  * Input / Output
  * Processing
  * Data Storage
  * Reporting
  * Time Division Multiplexing
* **Client-Server (1990s)**
  * GUI
  * Main Computing on Server
  * I/O at Client
  * LAN
* **Web Application (2000s)**
  * GUI - Browser
  * Main Computing on Web Server
  * Layered Components
  * Internet Based
* **Service Oriented Architecture (2010s)**
  * Layered Services
  * SOAP WebServices
  * Binary Communication 
  * Internet Based
* **Microservices (Present)**
  * Granular Services
  * REST / Message Queue
  * Based Upon Subdomains
  * Internet Based

**Histórico de Tecnologias**
* 1999: Continuous Integration via XP
* 2001: 
  * Feb: Agile Manifesto
* 2006: AWS EC2
* 2009:
  * DevOps
  * Java EE6
* 2010: NETFLIX to AWS
* 2011:
  * May: DropWizard
  * June: Vert.x
* 2012:
  * March
    * Ribbon
    * Hystrix
    * Microservices Assess - Thoughtworks Radar
  * July: 
    * Eureka
* 2013:
  * March: Docker
  * Sept: Spring Boot
* 2014:
  * March: Microservices Defined - Thoughtworks Fowler, Lewis
  * June: Kubernetes


### Pessoas e ideias
* Fred George - ThoughtWorks - Bayesian Principles - 2004
* Peter Rodgers - Micro-Web-Services - 2005
* Alistair Cockburn - Hexagonal Architecture - 2005
* James Lewis - ThoughtWorks - Microservices - 2011
* Martin Fowler - ThoughtWorks - Microservices - 2011

### O Termo Microsserviços
[Microservices: a definition of this new architectural term](https://martinfowler.com/articles/microservices.html)
"Microservices" - yet another new term on the crowded streets of software architecture. Although our natural inclination is to pass such things by with a contemptuous glance, this bit of terminology describes a style of software systems that we are finding more and more appealing. We've seen many projects use this style in the last few years, and results so far have been positive, so much so that for many of our colleagues this is becoming the default style for building enterprise applications. Sadly, however, there's not much information that outlines what the microservice style is and how to do it.

In short, the microservice architectural style [1] is an approach to developing a single application as a suite of small services, each running in its own process and communicating with lightweight mechanisms, often an HTTP resource API. These services are built around business capabilities and independently deployable by fully automated deployment machinery. There is a bare minimum of centralized management of these services, which may be written in different programming languages and use different data storage technologies.

[1] The term "microservice" was discussed at a workshop of software architects near Venice in May, 2011 to describe what the participants saw as a common architectural style that many of them had been recently exploring. In May 2012, the same group decided on "microservices" as the most appropriate name. James presented some of these ideas as a case study in March 2012 at 33rd Degree in Krakow in Microservices - Java, the Unix Way as did Fred George about the same time. Adrian Cockcroft at Netflix, describing this approach as "fine grained SOA" was pioneering the style at web scale as were many of the others mentioned in this article - Joe Walnes, Daniel Terhorst-North, Evan Botcher and Graham Tackley.


É um estilo arquitetural, ou seja, uma forma de trabalhar, criar e consolidar tecnologias que vai indicar uma direção


### Empresas e Ideias
* Amazon
* [AWS](https://queue.acm.org/detail.cfm?id=1142065)
* [ThoughtWorks](https://www.thoughtworks.com/insights/topic/microservices)
* [Netflix](https://netflixtechblog.com/redesigning-the-netflix-api-db5a7221fcff)
* [Google](https://cloudplatform.googleblog.com/2015/01/in-coming-weeks-we-will-be-publishing.html)


### Preparação para Microsserviços *
[Implementing Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html)
Arquiteturas de microsserviços combinam vários conceitos, tecnologias e padrões:
* Desenvolvimento de Software Ágil
* Arquiteturas Orientadas à Serviço: Service Oriented Architecture (SOA)
* API-first Design
* CI/CD
* Design Patterns Twelve-Factor App


### O que são Serviços Web?
Um **serviço web** é qualquer software disponibilizado pela Internet que usa um **formato padronizado**, como eXtensible Markup Language (XML) ou JavaScript Object Notation (JSON), para a solicitação e resposta de uma interação através de **Application Programming Interface (API)**.

Cliente --- mensagem de solicitação --> Internet --- mensagem de solicitação --> Serviço Web
        <---- mensagem de resposta ----          <---- mensagem de resposta ---- 


### O que significa API? *
* API significa Application Programming Interface (Interface de Programação de Aplicação). No contexto de APIs, a palavra Aplicação refere-se a qualquer software com uma função distinta.
* A interface pode ser pensada como um contrato de serviço entre duas aplicações. Esse contrato define como as duas se comunicam usando solicitações e respostas.
* A documentação de suas respectivas APIs contém informações sobre como os desenvolvedores devem estruturar essas solicitações e respostas.


### O que é uma API?
* APIs são mecanismos que permitem que dois componentes de software se comuniquem usando um conjunto de definições e protocolos.
* Por exemplo, o sistema de software do instituto meteorológico contém dados meteorológicos diários.
* A aplicação para previsão do tempo em seu telefone "fala" com esse sistema por meio de APIs e mostra atualizações meteorológicas diárias no telefone.


### Como as APIs funcionam?
* A arquitetura da API geralmente é explicada em termos de cliente e servidor.
* A aplicação que envia a solicitação é chamada de cliente e a aplicação que envia a resposta é chamada de servidor.
* As operações podem ser síncronas ou assíncronas.
* Então, no exemplo do clima, o banco de dados meteorológico do instituto é o servidor e o aplicativo móvel é o cliente.


### O que é API Web?
* Uma API Web ou API de serviço da Web é uma interface de processamento de aplicações entre um servidor da Web e um navegador da Web.
* A API REST é um tipo especial de API Web que usa o estilo de arquitetura padrão explicado acima.
* Os diferentes termos que abrangem as APIs, como API Java ou APIs de serviço, existem porque, historicamente, as APIs foram criadas antes da World Wide Web. As APIs Web modernas são APIs REST e os termos podem ser usados de forma intercambiável.

**Obs: A maioria dos serviços Web são APIs, mas nem todas as APIs são serviços Web**


### O que são integrações de API?
* As integrações de API são componentes de software que atualizam automaticamente os dados entre clientes e servidores.
* Alguns exemplos de integrações de API são quando os dados automáticos são sincronizados com a nuvem por meio da galeria de imagens do seu telefone ou a data e a hora são sincronizadas automaticamente no seu laptop quando você viaja para um local com outro fuso horário.


### Acessibilidade de APIs?
* **APIs privadas:** elas são internas a uma empresa e são usadas apenas para conectar sistemas e dados dentro da empresa.
* **APIs públicas:** estas são abertas ao público e podem ser usadas por qualquer pessoa. Pode ou não haver alguma autorização e custo associado a esses tipos de APIs.
* **APIs de parceiros:** estas são acessíveis apenas por desenvolvedores externos autorizados para auxiliar as parcerias entre empresas.
* **APIs compostas:** estas combinam duas ou mais APIs distintas para atender a requisitos ou comportamentos complexos do sistema.


### O que é um endpoint de API e por que ele é importante?
* Os endpoint da API são os pontos de contato finais no sistema de comunicação da API. Estes incluem URLs de servidores, serviços e outros locais digitais específicos de onde as informações são enviadas e recebidas entre sistemas. Os endpoints da API são fundamentais para as empresas por dois motivos principais:
  1. **Segurança:** Os endpoint da API tornam o sistema vulnerável a ataques. O monitoramento da API é crucial para impedir o uso indevido.
  2. **Performance:** Os endpoints da API, especialmente os de alto tráfego, podem causar gargalos e afetar a performance do sistema.


### Como criar uma API?
1. **Planejar a API:**
   * As especificações da API, como OpenAPI, fornecem o esquema para o design da sua API
   * É melhor pensar em diferentes casos de uso com antecedência e garantir que a API esteja de acordo com os padrões atuais de desenvolvimento de API.
2. **Criar a API:**
   * Os designers de API fazem a prototipagem APIs usando código boilerplate.
   * Depois que o protótipo é testado, os desenvolvedores podem personalizá-lo de acordo com as especificações internas.
3. **Testar a API:**
   * O teste de API é o mesmo que o teste de software e deve ser feito para evitar bugs e defeitos.
   * As ferramentas de teste de API podem ser usadas para testar a resistência da API contra ataques cibernéticos.
4. **Documentar a API:**
   * Embora as APIs sejam autoexplicativas, a documentação da API funciona como um guia para melhorar a usabilidade.
   * APIs bem documentadas que oferecem uma série de funções e casos de uso tendem a ser mais populares em uma arquitetura orientadas a serviços.
5. **Comercializar a API:**
   * Existem marketplaces de API para desenvolvedores comprarem e venderem outras APIs.
   * Catalogar sua API pode permitir que você ganhe dinheiro com ela.


### Exercício: API
* [US National Weather Service](https://www.weather.gov/)
* [API](https://api.weather.gov/)
* [Documentação](https://www.weather.gov/documentation/services-web-api)
* Exemplos de chamadas das APIs:
  * https://api.weather.gov/gridpoints/TOP/31,80/forecast
  * https://api.weather.gov/points/39.7456,-97.0892
  * https://api.weather.gov/alerts/active?area=NY


### Principais tipos de APIs *
* Principais tipos de APIs e seu funcionamento, dependendo de quando e por que elas foram criadas:
  * **APIs REST**
    * Essas são as APIs mais populares e flexíveis encontradas na Web atualmente.
    * O cliente envia solicitações ao servidor como dados.
    * O servidor usa essa entrada do cliente para iniciar funções internas e retorna os dados de saída ao cliente.
  * **APIs RPC**
    * Essas APIs são conhecidas como Remote Procedure Calls (Chamadas de Procedimento Remoto)
    * O cliente conclui uma função (ou um procedimento) no servidor e o servidor envia a saída de volta ao cliente.
  * **APIs SOAP**
    * Essas APIs usam o SOAP - Simple Object Access Protocol (Protocolo de Acesso a Objetos Simples).
    * Cliente e servidor trocam mensagens usando XML.
    * Esta é uma API menos flexível que era mais popular no passado.
  * **GraphQL**
    * GraphQL é uma especificação, uma linguagem de consulta de API e um conjunto de ferramentas. GraphQL opera em um único endpoint usando HTTP.
    * Ela prioriza fornecer aos clientes exatamente os dados que eles solicitam e nada mais.
    * Foi projetada para tornar as APIs rápidas, flexíveis e amigáveis ao desenvolvedor.
    * Como alternativa ao REST, o GraphQL oferece aos desenvolvedores de frontend a capacidade de consultar vários bancos de dados, microsserviços e APIs com um único endpoint de GraphQL.
**Obs.:** Websocket, entre outros

### Comparação entre os principais tipos de APIs *
#### REST
* **Fundamento:** API design pattern
* **Características:** 
  * Orientado a recursos
  * Baseado em dados
  * Flexível
* **Formato de Dados:** JSON/XML/YAML/HTML/plain text
* **Curva de Aprendizado:** Fácil
* **Comunidade:** Grande
* **Casos de Uso:**
  * Todos os tipos de apps web
  * Apps Cloud
  * Serviços de computação em nuvem


#### RPC
* **Fundamento:** API design pattern
* **Características:** 
  * Orientado a ação
  * Alto desempenho
* **Formato de Dados:** JSON/XML/Thrift/Protobuf/FlatBuffers
* **Curva de Aprendizado:** Fácil
* **Comunidade:** Grande
* **Casos de Uso:**
  * Sistemas de microsserviços complexos
  * Aplicações IoT


#### SOAP
* **Fundamento:** Protocolo para criação de APIs
* **Características:** 
  * Padronizado
  * Altamente seguro
  * Foco em aplicações corporativas
* **Formato de Dados:** XML
* **Curva de Aprendizado:** Desafiadora
* **Comunidade:** Pequena
* **Casos de Uso:**
  * Serviços financeiros
  * CRM
  * Gerenciamento de Identidade
  * Integração de sistemas legado


#### GraphQL
* **Fundamento:** Linguagem de consulta e runtime server-side para APIs
* **Características:** 
  * Endpoint único
  * Requisições fortemente típadas
  * Buscas enxutas
  * Auto-documentável
* **Formato de Dados:** JSON
* **Curva de Aprendizado:** Média
* **Comunidade:** Em crescimento
* **Casos de Uso:**
  * Apps móveis de alto desempenho
  * Sistemas complexos
  * Arquiteturas baseadas em microsserviços


### REST
* O modelo REST (REpresentational State Transfer) representa uma das possibilidades para a criação de web services, com utilização semântica dos métodos HTTP (GET, POST, PUT e DELETE)
* O criador do modelo REST foi [Roy Fielding](https://roy.gbiv.com/), um dos principais autores de especificação HTTP e cofundador do projeto Apache HTTP Server
* O termo REST foi apresentado pela primeira vez em 2000 na tese de doutorado de Roy Fielding [Architectural Styles and the Design of Network-based Software Architectures](https://ics.uci.edu/~fielding/pubs/dissertation/top.htm)
* Uma requisição HTTP é equivalente a uma chamada de um método (operação) em um objeto (recurso) residente no servidor.
* Principais características de uma requisição REST:
  * <img src="https://d1.awsstatic.com/whatisimg/New-API-GW-Diagram.c9fc9835d2a9aa00ef90d0ddc4c6402a2536de0d%20(1).67a41a2ef9823282fe672434ddd56dd22c13d5a5.png">


### O que são APIs REST?
* A principal característica da API REST é a ausência de estado. A ausência de estado significa que os servidores não salvam dados do cliente entre as solicitações.
  * **Por isso temos que ter técnicas de cache e de sessão**
* As solicitações do cliente ao servidor são semelhantes aos URLs que você digita no navegador para visitar um site. A resposta do servidor corresponde a dados simples, sem renderização gráfica típica de uma página da Web.


### Quais são so benefícios da APIs REST?
#### Integração
*  As APIs são usadas para integrar novas aplicações com sistemas de software existentes. Isso aumenta a velocidade de desenvolvimento porque cada funcionalidade não precisa ser escrita do zero.
*  Você pode usar APIs para aproveitar o código existente.

#### Inovação
* Setores inteiros podem mudar a chegada de uma nova aplicação. As empresas precisam responder rapidamente e oferecer suporte à rápida implantação de serviços inovadores.
* Elas podem fazer isso fazendo alterações no nível da API sem precisar reescrever todo o código.

#### Expansão
* As APIs apresentam uma oportunidade única para as empresas atenderem às necessidades de seus cliente em diferentes plataformas.
* Por exemplo, a API de mapas permite a integração de informações de mapas por meio de sites, Android, iOS etc.
* Qualquer empresa pode fornecer acesso semelhante ao seus respectivos bancos de dados internos usando APIs gratuitas ou pagas.

#### Facilidade de manutenção
* A API atua como um gateway entre dois sistemas
* CAda sistema é obrigado a fazer alterações internas para que a API não seja afetada
* Dessa forma, qualquer alteração futura de código feita por uma parte não afetará a outra parte.


### Como proteger uma API REST?
* Todas as APIs devem ser protegidas por meio de autenticação e monitoramento adequados. As duas principais maneiras de proteger APIs REST incluem:

#### Tokens de autenticação
**Eles são usados para autorizar os usuários a fazer a chamada de API.** Os tokens de autenticação verificam se os usuários são quem afirmam ser e têm direitos de acesso aquela chamada de API específica. Por exemplo, quando você faz login em seu servidor de e-mail, seu cliente de e-mail usa tokens de autenticação para acesso seguro.


#### Chaves de API
**As chaves de API verificam o programa ou a aplicação que faz a chamada de API.** Elas identificam a aplicação e garantem que ela tenha os direitos de acesso necessários para fazer a chamada de API específica. As chaves de API não são tão seguras quanto os tokens, mas permitem o monitoramento da API para coletar dados sobre o uso. Você pode ter notado uma longa sequência de caracteres e números no URL do seu navegador ao visitar diferentes sites. Essa string é uma chave API que o site usa para fazer chamadas de API internas.


### APIs REST vs. RESTful
* Uma API RESTful segue ou implementa todas as exigências e restrições do estilo de arquitetura definido pelo criado do modelo REST (Roy Fielding) no processo de construção de uma aplicação.
* **As exigências para um API ser RESTful são:**
  1. Arquitetura cliente-servidor
  2. Comunicação stateless
  3. Cache
  4. Interface uniforme
  5. Sistema de camadas


### Exercício
#### cUrl
* cUrl é uma ferramenta de linha de comando utilizada para obter ou enviar dados, incluindo arquivos, usando a sintaxe URL
* Disponível para Sistemas Operacionais em UNIX/LINUX, Windows, MacOS
* Mais informações: [https://curl.se/](https://curl.se/)

##### Instalação cUrl
* GNU/Linux, distribuições em Debian (como o Ubuntu), execute: sudo apt install curl
* Windows: pré-instalado, mas caso não estiver, acesse: [https://curl.se/windows/](https://curl.se/windows/)
* Distribuições baseados em Arch Linux, execute: sudo pacman -S curl
* MacOS: pré-instalado, mas caso naõ estiver, execute: brew install curl (necessita instalar Brew brevemente)


#### Métodos HTTP
| Método HTTP | Descrição                               |
| :---------- | :-------------------------------------- |
| GET         | Lê/Consulta um recurso                  |
| POST        | Cria um recurso                         |
| PUT         | Atualiza/Altera um recurso              |
| PATCH       | Atualiza/Altera um recurso parcialmente |
| DELETE      | Remove um recurso                       |

O método de requisição **[HTTP PUT](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods/PUT)** cria um novo recurso ou substitui uma representação do recurso de destino com os novos dados.
A diferença entre **PUT** e **POST** é que PUT é idempotente: chamá-lo uma ou várias vezes sucessivamente terá o mesmo efeito (não é um efeito colateral), enquanto usar o POST repetidamente pode ter efeitos adicionais, como executar uma ação várias vezes.


#### Comandos cUrl relacionados com REST
| Comando cUrl    | Descrição                                                                                                                                                                                                                                                     | Exemplo                                                     |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------- |
| -i ou --include | Inclui os cabeçalhos de resposta na resposta                                                                                                                                                                                                                  | curl -i http://www.exemplo.com                              |
| -d ou --data    | Inclui dados para postar na URL. Os dados precisam ser codificados por url                                                                                                                                                                                    | curl -d "data-to-post" http://www.exemplo.com               |
| -H ou --header  | Envia o cabeçalho da solicitação para o recurso Os cabeçalhos são comuns com solicitações de API REST                                                                                                                                                         | curl -H "key:12345" http://www.exemplo.com                  |
| -X POST         | Especifica o método HTTP a ser usado com a solicitação (neste exemplo, POST). Se você usar o -d na solicitação, curl especificará automaticamente um método POST. Com solicitações GET, incluir o método HTTP é opcional, porque GET é o método padrão usado. | curl -X POST -d "resource-to-update" http://www.exemplo.com |


#### JSON Server
* JSON Server é uma aplicação que simula REST APIs com base em arquivos JSON simples
* https://github.com/typicode/json-server
* https://www.npmjs.com/package/json-server


#### Praticando
* docker build -t jsonserver .
* docker run -d --rm -it --name jsonserver-container -p 8080:8080 jsonserver
* curl -X GET http://localhost:8080/carros ou curl http://localhost:8080/carros ou http://0.0.0.0:8080/carros

* Vamos copiar o arquivo [carros.json](./aula-1/app1/carros.json) e sobrescrever dentro do container
* ls -l carros.json
* docker cp carros.json jsonserver-container:tmp/base.json
* docker ps
* docker restart jsonserver-container 
* curl -i -H "Accept: application/json" -H "Content-type: application/json" -X POST http://0.0.0.0:8080/carros -d '{"id":"9","marca":"audi","modelo":"q7"}'
* curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X PUT http://0.0.0.0:8080/carros/9 -d '{"id":"9","marca":"bmw","modelo":"x1"}'
* curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X PATCH http://0.0.0.0:8080/carros/9 -d '{"id":"9","modelo":"x2"}'
* curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X DELETE http://0.0.0.0:8080/carros/9


## Microsserviços
### O que são microsserviços? *
São uma combinação de abordagens arquitetônicas e organizacionais apra o desenvolvimento de software em que as aplicações são compostas por serviços independentes que se comunicam por meio de APIs bem definidas.
As arquiteturas de microsserviços facilitam a escalabilidade e agilizam o desenvolvimento de aplicativos, habilitando a inovação e acelerando o tempo de introdução de novos recursos e os ciclos de implantação no mercado.

* [Microsserviços em poucas palavras](https://www.thoughtworks.com/pt-br/insights/blog/microservices-nutshell)
* [Microservices - a definition of this new architectural term](https://martinfowler.com/articles/microservices.html)


### Microsserviços, uma definição desse novo termo arquitetural
"O termo 'Arquitetura de microsserviços" surgiu nos últimos ano para descrever uma maneira específica de projetar aplicativos de software como conjuntos de serviços implementáveis independentemente. Embora não exista uma definição precisa desse estilo arquitetônico, existem certas características comuns em torno da organização, em relação à capacidade de negócios, implantação automatizada, inteligência nos terminais e controle descentralizado de linguagens e dados." Martin Fowler


### O que são microsserviços?
* [Azure](https://azure.microsoft.com/pt-br/solutions/microservice-applications) 
* [Google Cloud](https://cloud.google.com/learn/what-is-microservices-architecture?hl=pt-br)
* [IBM](https://www.ibm.com/br-pt/topics/microservices)
* [vmware](https://www.vmware.com/br/topics/glossary/content/microservices.html)
* [aws](https://aws.amazon.com/pt/microservices/)
* [Red Hat](https://www.redhat.com/pt-br/topics/microservices/what-are-microservices)


### Aplicações monolíticas vs. microsserviços
<img src="https://lh3.googleusercontent.com/o06PFnIMiTC8ek3_yVCb8kY02yZ-AinFakQ_LITcFUjpCOmqJIl1sPfVR3-xxUHQwzmnhefvdKRltcFYerK0z_NgTrwiFOqHWxYTJvHUl3s1mHIOR5WYTpQhNCKDJzzEaEROLsSZfl50bDaR7-1S8eI">

<img src="https://d1.awsstatic.com/Developer%20Marketing/containers/monolith_1-monolith-microservices.70b547e30e30b013051d58a93a6e35e77408a2a8.png">


#### Aplicação monolítica
* Para entender os benefícios dos microsserviços, considere primeiro uma aplicação monolítica.
* Os três processos (usuários, tópicos e mensagens) de uma aplicação monolítica estão altamente acoplados. Eles funcionam como um único serviços.
* Se um processo da aplicação apresentar um pico de demanda, toda a arquitetura deverá ser dimensionada. Adicionar ou melhorar recursos torna-se mais complexo à medida que a base de código cresce, o que limita a experimentação e dificulta a implementação de novas ideias.
* A disponibilidade de aplicações monolíticas também fica em risco, porque muitos processos dependentes e altamente acoplados aumentam o impacto da falha de um único processo.


#### Aplicação microsserviços
* Agora suponha que a mesma aplicação seja executada em uma arquitetura de microsserviços
* Cada processo da aplicação é criado como um componente independente que é executado como um serviço. Os serviços se comunicam usando operações de API leves.
* Cada serviço executa uma única função que pode oferecer suporte a várias aplicações. Como os serviços são executados de maneira independente, eles podem ser atualizados, implantado e dimensionados para atender à demanda por funções específicas de uma aplicação.
* Uma arquitetura de microsserviços permite iteração, automação e agilidade geral muito mais rápidas. Inicie, falhe e recupere: tudo rapidamente.


### Arquitetura monolítica
Um sistema monolítico está codificado em uma forma legada e que a complexidade está oculta dentro do monolítico, base de código. E as vezes ele cresceu em um ponto em que é muito difícil evoluir esse sistema ou criar um novo sistema. Além do fato, de termos um modelo de armazenamento que não levam as boas práticas modernas de implementação. O banco de dados tinha uma visão generalista.

Geralmente uma aplicação monolítica tinha um banco de dados que tentava resolver tudo e isso gerava problemas de escalas e de tamanho de banco de dados.


### Arquitetura microsserviços
* **Load balancer:** vai nos ajudar a balancear a carga que está sendo consumida nessa aplicação

**Obs.:** Monolito é mais fácil antes que seja mais difícil
Enquanto, microsserviços é mais difícil antes de ser mais fácil


### Aplicações monolíticas vs. microsserviços *
#### Monolítico v1 (toda funcionalidade em um aplicativo)
* **Prós:**
  * Inicialmente simples
  * Baixas latências entre processos
  * Base de código única, uma unidade de implementação
  * Eficiente quanto a recursos em pequenas escalas
* **Contras:**
  * A sobrecarga de coordenação aumenta à medida que a equipe cresce
  * Fraca imposição de modularidade
  * Escalonamento fraco
  * Implementação tudo ou nada (paralisação)
  * Longos tempos de build

#### Monolítico v2 (conjunto de camadas físicas monolíticas: front-end, servidor de aplicativos, camada de banco de dados)
* **Prós:**
  * Inicialmente simples
  * Fáceis consultas de união
  * Esquema único de implementação
  * Eficiente quanto a recursos em pequenas escalas
* **Contras:**
  * Tendência de maior acoplamento no decorrer do tempo
  * Escalonamento e redundância fracos (Tudo ou nada, somente vertical)
  * Difícil de ajustar
  * Gerenciamento de esquema tudo ou nada

#### Microsserviços (Modular, independente, relação gráficas vs. Camadas físicas, persistência isolada)
* **Prós:**
  * Cada unidade é simples
  * Escalonamento e desempenho independentes
  * Teste e implementação independentes
  * Pode ajustar o desempenho com perfeição (cache, replicação etc)
* **Contras:**
  * Muitas unidades cooperando
  * Muitas recompras pequenas
  * Exige ferramentas mais sofisticadas e gerenciamento de dependências
  * Latências de rede

* **Fonte:** [Manual de DevOps: como obter agilidade, confiabilidade e segurança em organizações tecnológicas, Capítulo 13](https://a.co/d/dCZ5Xha)


### Caso Prime Video
* [Scaling up the Prime Video audio/video monitoring service and reducing costs by 90%](https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90)
Nesse caso o Prime Video saiu de microsserviços para monolito.


### Características dos microsserviços
* **Descentralizados:** os microsserviços são descentralizados na forma como são desenvolvidos, implantados, gerenciados e operados
* **Poliglotas:** as arquiteturas de microsserviços adotam uma abordagem heterogênea para sistemas operacionais, linguagens de programação, armazenamentos de dados e ferramentas.
* **Independentes:** cada serviço do componente de uma arquitetura de microsserviços pode ser desenvolvido, implantado, operado e dimensionado sem afetar a função de outros serviços
* **Caixas pretas:** os detalhes da complexidade dos componentes de microsserviços ficam escondidos de outros componentes
* **Especializados:** cada serviço de componente é projetado para um conjunto de recursos e se concentra em resolver um problema específico
* **Você cria, você executa:** o DevOps é um princípio organizacional fundamental para microsserviços


### Checkpoint *
As aplicações de microsserviços são compostas por **serviços independentes que se comunicam por APIs bem definidas**
Os microsserviços compartilham as seguintes características:
* Descentralizados
* Independentes
* Especializados
* Poliglotas
* Caixas pretas
* Você cria, você executa


### Os principais desafios para implementar entrega contínua (Continuous Delivery)
Principais desafios segundo o State of DevOps Report 2020 apresentado pela **[Puppet](https://www.puppet.com/)** e **[CircleCI](https://circleci.com/)**:
* **Cobertura de teste incompleta:** escrever bons testes que cubram todos os cenários possíveis é quase impossível, especialmente em ambientes complexos onde há um número infinito de comportamentos de usuário, dependências, arquiteturas dinâmicas e muito mais
* **Mentalidade organizacional:** não é nenhuma surpresa que a mentalidade organizacional seja um desafio comum em cada grupo. Ouvimos muito isso em nosso trabalho com empresas, e é a única coisa com a qual os líderes seniores e profissionais estão de acordo
* **Arquitetura de aplicação fortemente acoplada:** a arquitetura de aplicação fortemente acoplada é uma das principais restrições para as equipes de entrega. Atualizar sua aplicação ou serviço requer coordenação com outras equipes, retardando a entrega de cada equipe devido às dependência complexas. O acoplamento fraco significa que os aplicativos são mais modulares =, para que as equipes possam entregar em seu próprio ritmo, usando seus próprios fluxos de trabalho.


### Arquiteturas levemente acopladas
"As organizações com esses tipos de arquiteturas orientadas a serviços, como o Google e a Amazon, têm flexibilidade e escalabilidade incríveis. Elas têm dezenas de milhares de desenvolvedores, em que pequenas equipes ainda podem ser incrivelmente produtivas." Randy Shoup, ex-diretor de engenharia do eBay, Stitch Fix, Google, WeWork
[Loosely coupled architecture](https://dora.dev/devops-capabilities/process/loosely-coupled-architecture/)


### Não existe uma solução arquitetural definitiva
Randy Shoup, também observou:
"Nâo há uma arquitetura perfeita para todos os produtos e todas as escalas. Qualquer arquitetura atende a um conjunto específico de metas ou intervalo de requisitos e restrições, como tempo de lançamento, facilidade de desenvolvimento de funcionalidades, dimensionamento etc. A funcionalidade de qualquer produto ou serviço quase certamente crescerá ao longo do tempo e nossas necessidades na arquitetura também mudarão. O que funciona na escala 1:X raramente funciona na escala 10:X ou 100:X.


## Arquitetura de Microsserviços
### Evolução da arquitetura
Monolithic (Single unit) -> SOA (Coarse-grained) -> Microservices (Fine-grained)


### Diferentes formas de implementar microsserviços
* Model/View/Controller (MVC)
* Pub-sub
* CQRS (Command Query Responsibility Segregation)


Physical (Bare metal) -> Virtualization (Virtual machines) -> Containerization (Docker) -> Serverless


**Bare metal:** uma máquina dedicada

### Arquitetura e padrões
<img src="https://microservices.io/i/MicroservicePatternLanguage.jpg">

* [A pattern language for microservices](https://microservices.io/patterns/index.html)


N-tier -> Service-oriented architecture (SOA) -> Microservices


### Teorema CAP
* O teorema CAP afirma que um sistema distribuído, composto por vários nós que armazenam dados, não pode fornecer simultaneamente mais de duas das três garantias a seguir:
  * **Consistência:** cada solicitação de leitura recebe a gravação mais recente ou um erro quando a consistência não pode ser garantida.
  * **Disponibilidade:** cada solicitação recebe um resposta sem erros, mesmo quando os nós estão inativos ou indisponíveis.
  * **Tolerância à partição:** o sistema continua operando apesar da perda de um número arbitrário de mensagens entre os nós.


### [Arquitetura Hexagonal](https://github.com/rafaelpeinado/fullcycle/tree/feature/arquitetura-hexagonal)
* Definida por Alistair Cockburn, em meados dos anos 90
* **Ideia central:** usar adaptadores para mediar a comunicação entre domínio e o restante do sistema
* **Adaptadores:** mesma ideia de padrões de projeto (GoF)
* Nome deriva do diagrama usado para ilustrar a arquitetura, formado por dois hexágonos concêntricos.

#### Objetivos
* Estabelecer uma separação clara entre:
  * Domínio limpo de tecnologia (classes do negócio)
  * Restante do sistema

**Domínio limpo de tecnologia**
* Camada de domínio não conhece:
  * Banco de dados usados pelo sistema
  * Frontend usados pelo sistema
  * Gateways de pagamentos usados pelo sistema
  * Serviços externos com os quais os sistema interage
Restante do sistema
* Interface com o usuário (Web, mobile, etc)
* Persistência e BDs
* Integrações com outros sistemas

[Engenharia de Software Moderna](https://engsoftmoderna.info/artigos/arquitetura-hexagonal.html)


#### Vantagens *
* Permite que desenvolvedores se concentrem no domínio:
  * Representa o propósito do sistema
  * Responsável pela geração de valor
* Testabilidade (mais fácil de testar domínio limpo de tecnologia)
* Maior facilidade de troca de bibliotecas, frameworks, BDs, etc.


#### Adaptadores
[Hexagonal architecture](https://alistair.cockburn.us/hexagonal-architecture/)
* Domínio "limpo" de tecnologia
  * as regras de negócios
* Adaptadores
* Restante do Sistema (tudo relacionado a tecnologia):
  * Front-end
  * Banco de dados
  * Sistemas Externos
  * Gateways de Pagamento
  * Cache
  * Bibliotecas Log
  * Pub/Sub


#### Exemplo Netflix
**A Netflix foi pioneira em implementação com sucesso em escala global nos conceitos da aula de hoje**
[Ready for changes with Hexagonal Architecture](https://netflixtechblog.com/ready-for-changes-with-hexagonal-architecture-b315ec967749)
<img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*NfFzI7Z-E3ypn8ahESbDzw.png">



### The Twelve-Factor App
[The Twelve-Factor App](https://12factor.net/)

#### Objetivos
* Minimize o esforço de configuração do novo desenvolvedor.
* Maximize a portabilidade do aplicativo.
* Implante aplicativos facilmente em plataformas de nuvem modernas.
* Manter a paridade do ambiente entre o desenvolvimento e a produção.
  * Codebase
  * Dependencies
  * Config
  * Backing services
  * Build, release, run
  * Processes
  * Port-binding
  * Concurrency
  * Disposability
  * Dev/prod parity
  * Logs
  * Administrative processes


### Domain Driven Design *
* O Domain Driven Design (DDD) é uma abordagem para o desenvolvimento de software para necessidades complexas, conectando a implementação a um modelo em evolução
* Coloca o foco principal do projeto no domínio central e na lógica do domínio
* Baseia projetos complexos em um modelo de domínio
* Inicia a colaboração criativa (usando uma linguagem ubíqua, ou UL) entre especialistas técnicos e de domínio para refinar iterativamente um modelo conceitual que trata de problemas de domínio específicos


#### DDD e Bounded Context (Contexto Limitado)
* Os Microsserviços devem ter um contexto limitado bem definido e executar apenas uma tarefa.
* Um contexto limitado encapsula um único domínio
* Um design orientado a domínio
  * Define os pontos de integração com outros domínios
  * Alinha-se bem com as características do Microsserviços
* Cuidado ao criar Microsserviços Monolíticos! 

* Vários fatores traçam limites entre os contextos, sendo a cultura humano dominante
* Contextos limitados têm conceitos não relacionados (por exemplo, tíquetes de suporte em um contexto de suporte ao cliente)
* Eles também compartilham conceitos (ex. Produtos e cliente)

[Bounded Context](https://www.martinfowler.com/bliki/BoundedContext.html)


##### Exemplo: Google Cloud Datastore
* Uma arquitetura **altamente acoplada** pode impedir a **produtividade de todos** e a capacidade de fazer mudanças com segurança.
* Por outro lado, uma **arquitetura levemente acoplada** promove produtividade e segurança com interfaces bem definidas que impõem como os módulos se conectam uns com os outros.
* Uma **arquitetura levemente acoplada** permite que equipes pequenas **e produtivas façam mudanças que possam ser implantadas de forma segura e independente.**
* Além disso, como cada serviço também tem uma API bem definida, ele facilita o teste de serviços e a criação de contratos de nível de serviço (SLAs) e de outros tipos entre equipes.


### Lei de Conway
* [Conway's Law](https://martinfowler.com/bliki/ConwaysLaw.html)
Sistemas computacionais vão espelhar a estrutura organizacional da empresa, isto é, se a empresa tem um organização monolítica, a aplicação vai ser monolítica
"Organizações que projetam sistemas (no sentido amplo usado aqui) são obrigadas
(compelidas) a produzir projetos que sejam cópias das estruturas de comunicação dessas
organizações."

**Organizational structure** reflete em **Application architecture**

### Exercício
* Uber, por exemplo

## Observações e Referências
* **[Criando Microsserviços - Sam Newman](https://a.co/d/92bwaKP)**
* **[Microsserviços Prontos Para a Produção - Susan J. Fowler](https://a.co/d/1sAwFar)**
* **[Domain-driven design - Eric Evans](https://a.co/d/eGZMvoC)**
* **[Microservices Patterns: With Examples in Java - Chris Richardson](https://a.co/d/5pT9Cxm)**
* **[Microservices in Action - Morgan Bruce/Paulo A Pereira](https://a.co/d/dh462RF)**


* **[RabbitMQ](https://rabbitmq.com/)**
* **[Qual é a função de um gateway de API?](https://www.redhat.com/pt-br/topics/api/what-does-an-api-gateway-do)**


### Exemplos de padrões de microsserviços
**AWS - Implementação de microsserviços**
* https://docs.aws.amazon.com/pt_br/whitepapers/latest/microservices-on-aws/microservices-onaws.html
* https://docs.aws.amazon.com/pt_br/whitepapers/latest/microservices-on-aws/microservices-onaws.pdf

**Microsoft Azure - Microsserviços do .NET**
* https://learn.microsoft.com/pt-br/dotnet/architecture/microservices/

**Google Cloud - Introdução a microsserviços**
* https://cloud.google.com/architecture/microservices-architecture-introduction?hl=pt-br80


### Exemplo: Cielo
[Cielo Developers](https://developercielo.github.io/)

### Exemplo: Embrapa
[AgroAPI](https://www.agroapi.cnptia.embrapa.br/portal/)

### Artigo
[Microservices: The Journey So Far and Challenges Ahead](https://ieeexplore.ieee.org/document/8354433)



# Microsserviços II
## Fundamentos
### O que sabemos até agora
* **Microsserviços:**
  * O padrão de desenvolvimento de software de microsserviços fornece um método para criar um serviço unificado a partir de uma coleção de serviços menores.
  * Cada componente de microsserviço se concentra em um conjunto de ações fracamente acopladas em um conjunto de dados pequeno e bem definido.
  * Cada microsserviço inclui um sistema de armazenamento independente para que todos os seus dados estejam localizados em um único local.
* **Linguagens:**
  * Os microsserviços podem ser escritos em qualquer linguagem de programação e podem usar qualquer ambiente de banco de dados, hardware e software que faça mais sentido para a organização.
  * Uma interface de programação de aplicativos (API) fornece os únicos meios para os  usuários e outros serviços acessarem os dados do microsserviço.
* **REST API:**
  * A API não precisa estar em nenhum formato específico, mas a transferência de estado representacional (REST) é popular, em parte porque sua legibilidade humana e natureza sem estado a tornam útil para interfaces da Web.
  * Outros formatos de API comuns incluem gRPC e GraphQL, cada um com abordagens e compensações diferentes para como os dados são acessados.


**Monolithic - Service-Oriented Architecture - Microservice**
<a href="https://www.researchgate.net/figure/The-Evolution-of-Software-Architectures_fig1_346675531"><img src="https://www.researchgate.net/profile/Davide-Taibi/publication/346675531/figure/fig1/AS:966041417043970@1607333630062/The-Evolution-of-Software-Architectures.png" alt="The Evolution of Software Architectures"/></a>


* Os princípios usados para projetar Microsserviços são os seguintes:
  1. Serviços Autônomos Independentes
  2. Escalabilidade
  3. Descentralização
  4. Serviços resilientes
  5. Balanceamento de carga em tempo real
  6. Disponibilidade
  7. Entrega contínua por meio da integração de DevOps
  8. Integração de API e monitoramento contínuo
  9. Isolamento de falhas
  10. Auto-Provisionamento


## Quando usar microsserviços
### Monolith First
[Monolith First](https://martinfowler.com/bliki/MonolithFirst.html)


### Microservice Prerequisites
[Microservice Prerequisites](https://martinfowler.com/bliki/MicroservicePrerequisites.html)
1. Rapid provisioning
   1. Cloud
   2. Automation
2. Basic Monitoring (algum nível de monitoramento)
3. Rapid application deployment (por exemplo, frameworks etc)
4. Development Pipeline (CI/CD)
5. DevOps Culture


#### Antipadrões (Antipatterns)
O que não deveria fazer ou deveria evitar
* **Magic pixie dust (pó mágico):** acreditar que uma pitada de microsserviços resolverá todos os problemas de desenvolvimento
* **Microservices as the goal (microsserviços como meta):** tornar a adoção de microsserviços a meta e medir o sucesso em termos do número de serviços escrito.
* **Scattershot adoption (ADoção dispersa):** tentar adotar a arquitetura de microsserviços sem qualquer coordenação e por várias equipes de desenvolvimento
* **Trying to fly before you can walk (tentar voar antes de andar):** tentar adotar a arquitetura de microsserviços sem praticar técnicas básicas de desenvolvimento, como código limpo, bom design e testes automatizados
* **Focussing on technology (foco em tecnologia):** concentrar nos microsserviços, mais comumente na infraestrutura de implantação, e negligenciar questões-chave, como a decomposição do serviço
* **The more the merrier (quanto mais, melhor):** criar intencionalmente uma arquitetura de microsserviços muito refinada (over architecting)
* **Red flag law (lei da bandeira vermelha):** manter o mesmo processo de desenvolvimento e estrutura organizacional que foram usados no desenvolvimento de aplicativos monolíticos.


[Microservices adoption antipatterns](https://microservices.io/microservices/antipatterns/-/the/series/2019/06/18/microservices-adoption-antipatterns.html)


#### Quando microsserviços é uma má ideia
[When Microservices Are a Bad Idea](https://semaphoreci.com/blog/bad-microservices)


#### Como responder a essas perguntas?
* Como lidar com operações que são de longa duração, processadas em diversos microsserviços diferentes, em inúmeras bases de dados diferentes e ainda assim, garantir integridade?
* Se os microsserviços possuem cada um a sua própria base de dados, como manter a integridade referencial? Como manter os relacionamentos?
* Se o processamento das atividades ocorrerá em inúmeros microsserviços de maneira distribuída, como informar ao usuário que o processamento ocorreu com sucesso ou falha?
* O que acontece quando um microsserviço está fora do ar? Todos os demais também ficarão? Se não, como se dará uma transação quando um microsserviço do ecossistema estiver indisponível?
* Quando um microsserviço for publicado, quais outros deverão ser atualizados? Ou não deveria haver essa dependência?
* Sendo as bases de dados distribuídas, como manter os dados atualizados entre todas elas?
* Posso ter uma base de dados para cada microsserviço, no mesmo servidor e dados?
* Como faria para publicar 20 microsserviços?

[Microsserviços, você precisa mesmo?](https://www.linkedin.com/pulse/microsservi%C3%A7os-voc%C3%AA-precisa-mesmo-lucas-massena/?originalSubdomain=pt)


## Padrões de Arquitetura / Design Patterns
### Padrões de projetos (Design Patterns) *
* São similares a esboços para uma construção, que podem ser ajustados para resolver um problema, baseado em microsserviços.
* Não é código, mas um conceito que irá influenciar em uma solução.
* Para implementar um padrão de projeto, é necessário escolher e seguir o conceito do padrão escolhido e adapta-lo ao problema a ser resolvido.


#### Referência de livro e site
* Chris Richardson
* Site https://microservices.io/
* Livro [Microservices Patterns](https://a.co/d/4UmJOYd)


### Padrões de projetos (Design Patterns)
[Pattern: Microservice Architecture](https://microservices.io/patterns/microservices.html)
<img src="https://microservices.io/i/Microservice_Architecture.png">


### Categorias de Padrões de Projetos para Microsserviços *
* **Padrões de decomposição:** 
  * Esses padrões nos dizem como decompor aplicações, por exemplo uma aplicação monolítica para microsserviços
* **Padrões de integração:**
  * Cobrem principalmente aspectos de comunicação de microsserviços
  * Recomendam como os microsserviços podem se comunicar entre si e com outros sistemas e como agregar resultados de vários serviços antes de enviá-los de volta ao usuário
* **Padrões de banco de dados:**
  * Recomendam estratégias de armazenamento de dados para microsserviços
  * Ajudam a resolver problemas de dados como sincronização de dados, atomicidade, ACID e compartilhamento de dados
  * Endereçam a integridade dos dados, como lidar com transações entre microsserviços e transações distribuídas
* **Padrões de observabilidade:**
  * Tem objetivo de rastrear e monitorar a integridade e o desempenho de microsserviços
  * Um exemplo é enviar uma notificação se houver uma falha no microsserviço
* **Padrões de preocupações transversais (Cross-Cutting Concerns):** 
  * Esses padrões são outras preocupações que auxiliam na manutenção dos microsserviços
  * Não são ou fazem partes da lógica de negócios, mas orientam práticas recomendadas para criar, manter e proteger microsserviços

[Microservice Architecture and Design Patterns for Microservices](https://medium.com/@madhukaudantha/microservice-architecture-and-design-patterns-for-microservices-e0e5013fd58a)

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*CKSVv4WkS8Okx572rX45HA.png">

**Vamos ver na aula:**
* Strangler
* API Gateway
* CQRS
* SAGA
* Circuit Breaker

### Design Patterns em Nuvem pública
#### AWS
* [Habilitar a persistência de dados em microsserviços](https://docs.aws.amazon.com/pt_br/prescriptive-guidance/latest/modernization-data-persistence/welcome.html)
* [Decompor monólitos em microsserviços](https://docs.aws.amazon.com/pt_br/prescriptive-guidance/latest/modernization-decomposing-monoliths/welcome.html)
* [Integração de microsserviços usando serviços da AWS com tecnologia sem servidor](https://docs.aws.amazon.com/pt_br/prescriptive-guidance/latest/modernization-integrating-microservices/welcome.html)
* [Padrões, arquiteturas e implementações de design de nuvem](https://docs.aws.amazon.com/pt_br/prescriptive-guidance/latest/cloud-design-patterns/introduction.html)


#### Azure
* [Cloud Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/)


#### Conteúdo sobre Design Patterns
* [Microservice Architecture and Design Patterns for Microservices](https://medium.com/@madhukaudantha/microservice-architecture-and-design-patterns-for-microservices-e0e5013fd58a)
* [Mind-mapping Microservices Design Patterns](https://medium.com/@mail.ruchitayal/mind-mapping-microservices-design-patterns-dd1cfdba8dae)


### Padrão de Decomposição: Strangler *
* Esse padrão é comumente usado para transformar incrementalmente um aplicativo monolítico
em microsserviços, substituindo uma funcionalidade específica por um novo serviço.
* O objetivo é que o legado e as versões novas e modernizadas coexistam
* O novo sistema é inicialmente suportado e encapsulado pelo sistema existente. Esse suporte dá ao novo sistema tempo para crescer e potencialmente substituir totalmente o sistema antigo.
* O padrão possui 3 etapas: transformar, coexistir e eliminar:
  * Transformar (transform): Crie uma nova aplicação paralela com abordagens modernas
  * Coexistir (coexist): Deixe a aplicação existente onde está por um tempo. Redirecione partes da a aplicação existente para a nova aplicação e implemente novas funcionalidades incrementalmente.
  * Eliminar (eliminate): Remova as funcionalidades antigas aplicação existente.

<img src="https://static-assets.amplication.com/blog/monoliths-to-microservices-using-the-strangler-pattern/2.png">


<img src="https://docs.aws.amazon.com/pt_br/prescriptive-guidance/latest/modernization-decomposing-monoliths/images/strangler-fig.png">


| Vantagens                                                                                             | Desvantagens                                                                                                                                               |
| :---------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Permite uma migração de um serviço para um ou mais serviços                                           | Não é adequado para sistemas pequenos em que a complexidade é baixa e o tamanho é pequeno                                                                  |
| Mantém os serviços antigos em funcionamento enquanto refatora para versões atualizadas                | Não pode ser usado em sistemas em que as solicitações para o sistema back-end não podem ser interceptadas e roteadas                                       |
| Oferece a capacidade de adicionar novos serviços e funcionalidades enquanto refatora serviços antigos | A camada de proxy ou fachada (façade) pode se tornar um ponto único de falha ou um gargalo de desempenho se não for projetada adequadamente                |
| O padrão pode ser usado para controle de versão de APIs                                               | Requer um plano de reversão para cada serviço refatorado para voltar à maneira antiga de fazer as coisas com rapidez e segurança se as coisas derem errado |
| O padrão pode ser usado para interações antigas para soluções que não são ou não serão atualizadas    |                                                                                                                                                            |

* [How to break a Monolith into Microservices](https://martinfowler.com/articles/break-monolith-into-microservices.html)


### Padrão de Integração: API Gateway *
* O padrão de gateway de API é recomendado para projetar e criar aplicativos complexos ou grandes baseados em microsserviços com vários aplicativos clientes. O padrão é semelhante ao [padrão de fachada](https://aws.amazon.com/pt/blogs/architecture/unlocking-data-from-existing-systems-with-serverless-api-facade/) (façade) do design orientado a objetos, mas faz parte de um proxy reverso de sistema distribuído ou roteamento de
gateway e usa um modelo de comunicação síncrona.
* O padrão fornece um proxy reverso para redirecionar ou rotear solicitações para seus endpoints de microsserviços internos. Um gateway de API fornece um único endpoint ou URL para os aplicativos cliente e mapeia internamente as solicitações para microsserviços internos. Uma camada de abstração é fornecida ocultando certos detalhes da implementação e funcionalidades adicionais também podem ser incluídas ao serviço de back-end, como transformações de resposta e solicitação, autorização de acesso ao endpoint ou rastreamento.
* Você deve considerar o uso do padrão de gateway da API se:
  * O número de dependências de um microsserviço é gerenciável e não cresce com o tempo
  * O sistema de chamada exige uma resposta síncrona do microsserviço
  * Existe o requisito de baixa latência
  * É preciso expor uma API para coletar dados de vários microsserviços

#### Caso de Uso
* Um cliente faz pagamentos mensais regulares em um sistema de seguro que consiste em quatro
microsserviços (“Cliente”, “Comunicação”, “Pagamentos” e “Vendas”). O microsserviço “Cliente” atualiza o banco de dados do cliente com os detalhes do pagamento mensal. O microsserviço “Vendas” atualiza o banco de dados de vendas com informações relevantes que ajudam a equipe de vendas a acompanhar o cliente em busca de oportunidades de venda cruzada. O microsserviço “Comunicação” envia um e-mail de confirmação ao cliente após o pagamento ser processado com sucesso. Finalmente, o microsserviço “Pagamentos” é o sistema geral que o cliente usa para fazer seu pagamento mensal. O padrão usa serviços da web para integrar os subsistemas “Cliente”, “Vendas” e “Comunicação” com o microsserviço “Pagamentos”.
* Há três desafios em usar esse padrão para esse caso de uso:
  1. As chamadas síncronas são feitas para sistemas downstream, o que significa que qualquer latência causada por esses subsistemas afeta o tempo geral de resposta.
  2. Os custos operacionais são mais altos porque o sistema de “Pagamentos” aguarda as respostas dos outros microsserviços antes de responder ao sistema de chamadas. O tempo total de execução é, portanto, relativamente maior em comparação com um sistema assíncrono.
  3. O tratamento de erros e a repetição são tratados separadamente para cada microsserviço dentro do sistema de “Pagamentos”, não pelos microsserviços individuais.


* **Cenário 1:** Cenário 1: Cada microsserviço tem seu próprio gateway de API. O microsserviço “Pagamentos” chama sistemas individuais e implementa o padrão de gateway da API.
<img src="https://docs.aws.amazon.com/pt_br/prescriptive-guidance/latest/modernization-integrating-microservices/images/integrating-diagram1.png">


* **Cenário 2:** Cada microsserviço é implantado como uma função (Serverless), mas todos os
microsserviços são conectados pelo mesmo gateway de API.
<img src="https://docs.aws.amazon.com/pt_br/prescriptive-guidance/latest/modernization-integrating-microservices/images/integrating-diagram2.png">


### Padrão de Banco de Dados: CQRS *
* O padrão de segmentação de responsabilidade de consulta de comando (CQRS - Command Query Responsibility Segregation) separa a mutação de dados, ou a parte do comando de um sistema, da parte de consulta.
* Você pode usar o padrão CQRS para separar atualizações e consultas se elas tiverem requisitos diferentes de taxa de throughput, latência ou consistência.
* O padrão CQRS divide o aplicativo em duas partes: o lado do comando e o lado da consulta.
  * O lado do comando trata das solicitações **create, update e delete**
  * O lado da consulta executa a parte query usando as réplicas de leitura.

<img src="https://docs.aws.amazon.com/images/prescriptive-guidance/latest/modernization-data-persistence/images/cqrs.png">

**O diagrama mostra o seguinte processo:**
1. A empresa interage com o aplicativo enviando comandos por meio de uma API.
2. Comandos são ações como criar, atualizar ou excluir dados.
3. O aplicativo processa o comando de entrada no lado do comando. Isso envolve validar, autorizar e executar a operação.
4. O aplicativo persiste os dados do comando no banco de dados de gravação (comando).
5. Depois que o comando é armazenado no banco de dados de gravação, os eventos são disparados para atualizar os dados no banco de dados de leitura (consulta).
6. O banco de dados de leitura (consulta) processa e persiste os dados. Os bancos de dados de leitura são projetados para serem otimizados para requisitos de consulta específicos.
7. A empresa interage com APIs de leitura para enviar consultas para o lado da consulta do aplicativo.
8. O aplicativo processa a consulta de entrada no lado da consulta e recupera os dados do banco de dados lido.


**Obs.:** fazer leitura é muito mais rápido, por isso a latência é bem pequena. Hoje as aplicações são mais rápidas, pois não precisam concorrer com operações de escrita, são feitos somente para leitura.


### Padrão de Banco de Dados: SAGA *
* O padrão saga é um padrão de gerenciamento de falhas que ajuda a estabelecer a consistência em aplicativos distribuídos e coordena as transações entre vários microsserviços para manter a consistência de dados.
* Um microsserviço publica um evento para cada transação e a próxima transação é iniciada com base no resultado do evento. Ele pode seguir dois caminhos diferentes, dependendo do êxito ou da falha das transações.

<img src="https://docs.aws.amazon.com/pt_br/prescriptive-guidance/latest/modernization-data-persistence/images/enabling-diagram6.png">

A ilustração a seguir mostra como o padrão SAGA implementa um sistema de processamento de pedidos em um provedor de nuvem pública:
1. Cada etapa (por exemplo, “ProcessPayment”) tem etapas separadas para lidar com o sucesso ou
Falha do processo
2. Sucesso “UpdateCustomerAccount”
3. Falha “SetOrderFailure”


### Padrão de preocupações transversais: Disjuntor ou Circuit Breaker
* O padrão Disjuntor ou Circuit Breaker ajuda a evitar a ocorrência de falhas em cascata, quando microsserviços estiverem indisponíveis ou com alta latência.
* O padrão do disjuntor pode impedir que um microsserviço repita uma chamada para outro microsserviço quando a chamada já causou interrupções ou falhas repetidas.
* O padrão também é usado para detectar quando o serviço de chamada está funcionando novamente.

* No exemplo a seguir, temos dois microsserviços:
1. O microsserviço “Order” (Pedidos) que inicia a chamada
2. O microsserviço “Payment” (Pagamentos) que recebe a chamada
* Quando não há falhas, o serviço de Pedidos encaminha todas as chamadas para o serviço de Pagamentos pelo Circuit Breaker (Disjuntor), como mostra o diagrama a seguir:
<img src="https://docs.aws.amazon.com/images/prescriptive-guidance/latest/cloud-design-patterns/images/circuit-breaker-1.png">

* Se o serviço de pagamento atingir o tempo limite, o Disjuntor poderá detectar o tempo limite e rastrear a falha:
<img src="https://docs.aws.amazon.com/images/prescriptive-guidance/latest/cloud-design-patterns/images/circuit-breaker-2.png">

* Se os tempos limite excederem um limite especificado, o aplicativo abrirá o circuito. Quando o circuito está aberto, o Disjuntor não encaminha as chamadas para o microsserviço de Pagamentos. Ele retorna uma falha imediata quando o microsserviço de Pedidos liga para o serviço de
pagamento
<img src="https://docs.aws.amazon.com/images/prescriptive-guidance/latest/cloud-design-patterns/images/circuit-breaker-3.png">


* O objeto disjuntor tenta verificar periodicamente se as chamadas para o serviço de pagamento foram bem-sucedidas:
<img src="https://docs.aws.amazon.com/images/prescriptive-guidance/latest/cloud-design-patterns/images/circuit-breaker-4.png">

* Quando a chamada para o serviço de pagamento é bem-sucedida, o circuito é fechado e todas as outras chamadas são encaminhadas para o serviço de pagamento novamente:
<img src="https://docs.aws.amazon.com/images/prescriptive-guidance/latest/cloud-design-patterns/images/circuit-breaker-5.png">


### Um exemplo de etapas para construção de uma aplicação baseada em microsserviços *
1. **Definição e Planejamento**
  * Identifique as funcionalidades do seu aplicativo para dividi-las em microsserviços
  * Defina as interfaces e a forma de comunicação (APIs REST, mensagens em fila, eventos assíncronos etc.)
  * Planeje a estrutura de cada microsserviço
2. **Desenvolvimento Individual dos Microsserviços**
  * Desenvolva cada microsserviço como um projeto independente
  * Use um framework para criar APIs
3. **Comunicação entre Microsserviços**
  * Configure a forma como os microsserviços irão se comunicar
  * Use bibliotecas para implementar a comunicação
4. **Gerenciamento de Dados**
  * Decida como os microsserviços irão armazenar e acessar dados
  * Pode-se compartilhar um banco de dados centralizado ou usar banco de dados separados para cada microsserviço
  * Lide com consistência de dados entre os microsserviços
5. **Teste e Integração**
  * Teste cada microsserviço de forma independente
  * Implemente testes de integração para garantir que os microsserviços interajam corretamente.
6. **Implantação**
  * Use contêineres Docker para empacotar cada microsserviço com suas dependências
  * Use ferramentas como Kubernetes ou Docker Compose para implantar e, também, orquestrar os microsserviços.
7. **Monitoramento e Observabilidade**
  * Implemente monitoramento para cada microsserviço e para a comunicação entre eles
  * Use ferramentas como Prometheus, Grafana, ELK (Elasticsearch, Logstash, Kibana) para monitorar a saúde e o desempenho
8. **Escalabilidade**
  * Implemente escalabilidade automática para lidar com picos de tráfego
  * Use ferramentas de orquestração para adicionar ou remover instâncias de microsserviços conforme necessário
9. **Segurança**
  * Proteja as APIs com autenticação e autorização adequadas
  * Mantenha as dependências atualizadas para evitar vulnerabilidades conhecidas
10. **Documentação**
  * Documente cada microsserviço, suas APIs e como eles se comunicam
  * Forneça uma documentação clara para ajudar no desenvolvimento, manutenção e integração com outros sistemas


### Identificando limites de microsserviços
* Cada serviço tem uma única responsabilidade.
* *Não há nenhuma chamada de conversa entre os serviços. Se a divisão da funcionalidade em dois serviços gerar excesso de conversas, isso poderá ser um sintoma de que essas funções pertencem ao mesmo serviço.
* Cada serviço é pequeno o suficiente para ser criado por uma pequena equipe trabalhando de forma independente.
* Não há nenhuma interdependência que exige que dois ou mais serviços sejam implantados em sincronia. Deve ser sempre possível implantar um serviço sem redistribuir outros serviços.
* Os serviços não estão acoplados de forma firme e podem evoluir de forma independente.
* Os limites do serviço não criarão problemas de consistência ou integridade de dados. Às vezes, é importante manter a consistência dos dados colocando a funcionalidade em um único microsserviço. Dito isto, considere se você realmente precisa de consistência forte. Existem estratégias para abordar a eventual consistência em um sistema distribuído, e os benefícios dos serviços de decomposição geralmente superam os desafios de gerenciar a consistência eventual.

* "Right Size" Microservices
* https://www.softplan.com.br/en/tech-writers/microsservicos-dotamanho-certo-parte-i/


### Exemplo
* **EC2:** máquina virtual
* **S3:** armazenar objetos na nuvem, e uma das funcionalidades é, por exemplo, armazenar páginas estáticas
* **Refactor Spaces (Accelerate incremental app refactor):** 


## Métodos Ágeis DevOps
### Métodos Ágeis
* Lean
* Scrum
* Kanban
* Extreme Programming (XP)
* Design Sprint


### O que é DevOps?
[Definição do modelo do DevOps](https://aws.amazon.com/pt/devops/what-is-devops/)
* Plan
* Code
* Build
* Test
* Release
* Deploy
* Operate
* Monitor

* O DevOps é a combinação de filosofias culturais, práticas e ferramentas que aumentam a capacidade de uma empresa de distribuir aplicativos e serviços em alta velocidade: otimizando e aperfeiçoando produtos em um ritmo mais rápido do que o das empresas que usam processos tradicionais de desenvolvimento de software e gerenciamento de infraestrutura.
* Essa velocidade permite que as empresas atendam melhor aos seus clientes e consigam competir de modo mais eficaz no mercado.


#### Prática de DevOps
* Integração Contínua (CI: Continuous Integration)
* Entrega Contínua (CD: Continuous Delivery)
* Infraestrutura como Código (IaC: Infrastructure as a Code)
* Microsserviços
* Monitoramento e Logs
* Comunicação e colaboração


### Continuous Delivery + Continuous Deployment
[Continuous Delivery vs Continuous Deployment](https://blog.crisp.se/2013/02/05/yassalsundman/continuous-delivery-vs-continuous-deployment)
<img src="https://blog.crisp.se/wp-content/uploads/2013/02/continuous-delivery-deployment-sm.jpg">


### Continuous Integration & Continuous Delivery (CI/CD) *
* **Código:**
  * Controle de versão
  * Ramificação (branching)
  * Revisão de código
* **Build:**
  * Compilação
  * Testes unitários
  * Análise estática
  * Empacotamento
* **Testes:**
  * Testes de integração
  * Testes de carga
  * Testes de segurança
  * Testes de aceitação
* **Deploy:**
  * Implantação
  * Validação
* **Monitorar:**
  * Monitorização
  * Medição


## Ferramentas, Linguagens, Frameworks
### Cloud Native Landscape
[Cloud Native Landscape](https://landscape.cncf.io/)


### Algumas Ferramentas
* **Containerization:**
  * Docker & Docker Compose
  * Kubernetes
* **Service mesh:**
  * Istio
  * Linkerd
  * Consult Connect
* **API gateway:**
  * Ambassador
  * Kong
  * Apiman
  * WSO2 API Manager
  * Apigee
* **Monitoring tools:**
  * New Relic
  * CloudWatch
  * Datadog
  * Prometheus
  * Grafana
* **Log consolidation tools:**
  * Fluentd
  * Graylog
  * Splunk
  * ELK (Elasticsearch, Logstash, Kibana)
* **Tracing tools:**
  * Zipkin
  * Jaeger
  * New Relic
  * Splunk
* **CI/CD tools:**
  * Jenkins
  * GitLab CI/CD
  * CircleCI
* **API Documentation:**
  * OpenAPI

### Algumas linguagens
* Java
* Python
* Node.js
* Golang
* .NET Core
* TypeScript (TS)


### Algumas frameworks
* Spring Framework
* Vert.x
* Express.js
* Django
* Flask
* Go kit
* FastAPI

### The State of Developer Ecosystem 2023
[The State of Developer Ecosystem 2023](https://www.jetbrains.com/lp/devecosystem-2023/)


## Modelos de Maturidade
### Microservices 2022
[Microservices](https://www.jetbrains.com/lp/devecosystem-2022/microservices/)


### Richardson Maturity Model
* Um modelo, desenvolvido por Leonard Richardson, que divide os principais elementos de uma abordagem REST em três etapas. Eles introduzem recursos, verbos http e controles de hipermídia.


#### Exemplo de Modelo de Maturidade para Microsserviços
* **Stage 0:** Monolithic or Pre-Cloud
* **Stage 1:** Cloud-Native
* **Stage 2:** Service Mesh
* **Stage 3:** Application Networking


[The Microservices Maturity Model](https://www.greymatter.io/blog/the-microservices-maturity-model/)
<img src="https://www.greymatter.io/wp-content/uploads/2023/01/greymatter-Microservices-Maturity-Model-2023-1.jpg">



### Exemplo: Azure Microservices assessment and readiness
| Critério                                               | Critério                                                 |
| :----------------------------------------------------- | :------------------------------------------------------- |
| Entender as prioridades de negócios                    | Avaliar o tratamento de transações                       |
| Registrar decisões de arquitetura                      | Avalie seu modelo de desenvolvimento de serviços         |
| Avaliar a composição da equipe                         | Avaliar sua abordagem de implantação                     |
| Utilizar a metodologia dos Doze Fatores                | Avalie sua plataforma de hospedagem                      |
| Entenda a abordagem de decomposição                    | Avaliar o monitoramento de serviços                      |
| Avaliar a prontidão do DevOps                          | Avaliar a atribuição de token de correlação              |
| Identificar áreas de negócios que mudam com frequência | Avaliar a necessidade de uma estrutura de microsserviços |
| Avaliar a prontidão da infraestrutura                  | Avalie sua abordagem ao teste de aplicativos             |
| Avaliar os ciclos de lançamento                        | Avaliar a segurança dos microsserviços                   |
| Avaliar a comunicação entre serviços                   | Avaliar como os serviços são expostos aos clientes       |



## EXEMPLO: Especificação REST API



## Observações e Referências
* **[Manual de DevOps - Vários Autores](https://a.co/d/djmMuTZ)**
* **[Team Topologies - Matthew Skelton/Manuel Pais](https://a.co/d/51d9Ljz)**
* **[Jornada Microsserviços - Vários Autores](https://a.co/d/9vCrYlx)**
* **[Padrão de Projeto Facade em Java](https://www.devmedia.com.br/padrao-de-projeto-facade-em-java/26476)**

* IoT geralmente estamos trafegando em cima do protocolo MQTT ou AMQP
