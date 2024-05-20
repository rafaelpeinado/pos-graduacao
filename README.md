# Infra As Code (IAC) I
## Evolução da Infraestrutura
### Uma breve história sobre infraestrutura em nuvem
* **Anos 90:**
  * Servidores eram implantados dentro dos provedores de acesso à internet
  * Os servidores eram computadores comuns que não tinham mais potência para serem usados como desktops
  * Pagávamos pelo serviço e não pela solução
  * Não havia redundância de energia
  * Não havia redundância de link
  * Não havia redundância de dados
  * Não havia segurança de infraestrutura
  * E toda interação com o hardware era feita através de A.P.I. (Alguém que Pressiona Interruptor)
* **Anos 2000:**
  * Serviços como CPanel começam a ganhar mercado
  * Processadores multi-core se tornam mais populares
  * Os links ficam mais poderosos
  * Data centers de hospedagem mais bem estruturados surgem
  * Os serviços de hospedagem evoluem para ambientes compartilhados dentro de hardwares mais fortes
  * A interação com o hardware ainda é por de A.P.I. (Alguém que Pressiona Interruptor)
  * Ganha-se uma vantagem com máquinas virtualizadas, o reboot remoto do ambiente virtual
* **De 2003 a 2006:**
  * A Amazon (e-commerce) precisa de soluções que não existem no mercado
    * Alta escalabilidade para suportar picos de tráfego
    * Elasticidade para reduzir o custo operacional quando não tiver demanda
    * Flexibilidade para diferentes tipos de projetos
    * Extensibilidade para derivar serviços a partir de outros serviços
    * Redundância de dados, energia e link
    * Segurança
  * Surge o S3
  * Surge o SQS
  * Surge o EC2
  * Surgem diversos outros serviços derivados como SNS (Sistema de Mensageria Broker), RDS (Bancos de Dados), etc.

* **Diferenciais do hardware em nuvem:**
  * Hardware compartilhados com alto controle sobre o consumo
  * Redundância
    * Múltiplas placas de rede
    * Múltiplos links
    * Múltiplas fontes de alimentação
    * Múltiplas redes elétricas com alimentação de emergência
  * Segurança física e lógica
  * Controle e monitoramento remoto do hardware em nível granular
  

### Arquitetura Client/Server
* User <------> Server
  * Toda a aplicação ficava no mesmo hardware


### Arquitetura Cloud (conceito fundamental)
* User <------> Hedge <------> VPC (Virtual Private Cloud)
  * O servidor cloud é responsável por toda a segurança da infraestrutura (Hedge: infraestrutura de borda)
  * o VPC engloba:
    * **IAM (Identity Access Management):** podemos customizar partes do Hedge, ou seja, é uma camada de aplicação onde podemos inserir permissões de acesso daquela infraestrutura
    * Quando toda a requisição de controle de grupos, acessos e IAM, podemos acessar a infraestrutura, como o EC2. O EC2 também pode consultar o IAM para verificar as permissões para acessar por exemplo, um RDS, EBS (Disco Anexado), SQS
    * O **S3** por padrão não está dentro da VPC
    * **GraphDB** (muito comumente consumido pelo front-end)
* **Elastic Load Balancer:** providencia um SSL e faz parte da camada de borda (Hedge)

![Arquitetura Cloud (conceito fundamental)](./assets/arquitetura-cloud.png)


### Onion Architectural Vision
* O Cloud é capaz de ter múltiplos serviços que conseguem se consumir e até se gerenciar, pedindo permissões, por exemplo.
* **Controle e Telemetria:** responsável por fazer leitura em tempo real de todos os itens que estão dentro do hardware e funciona como operação remota, como, por exemplo, metade do processador pode ser desligado
* **Comutação e Provisionamento:** temos vários servidores e cada servidor tem seu próprio controle e telemetria interna, porém eles precisam ser disponibilizados
  * Por exemplo, temos um dado com 5 petabytes. O servidor não armazena tudo em um único disco. Na verdade ele usa comutação que é responsável por identificar quais hardwares ou serviços fazem parte de um único serviço/dado que será disponibilizado pelo usuários. Ele é capaz de comutar e trazer outros hardwares para dentro da solução desse serviço que vimos como uma coisa só.
* **API:** garante que todas as camadas sejam operadas. Algumas podemos operar e outras não
  * Console AWS
  * APPs

![Onion Architectural Vision](./assets/onion-architecutural-vision.png)


## Provedores
### Provedores Cloud
* Amazon Web Services
* Google Cloud
* Oracle Cloud
* Azure
* Hostinger
* locaweb
* uol host


### Serviços de Integração
* **Terraform:** é um serviço de Infra As Code que é compatível com diversas plataformas e ela consegue, através de um único template publicar a aplicação na AWS, Azure ou Google Cloud. Mas é bom lembrar que usar soluções como Terraform nos limita em relação a quantidade de serviços que conseguimos utilizar através do Terraform. E usar multi-cloud antes da hora, pode aumentar os custos de forma desnecessária
  * Infrastructure as Code
  * Multi-cloud provisioning
  * Manage Kubernetes
  * Manage network infrastructure
  * Manage virtual images
  * Integrate with existing workflows
  * Enforce policy as code
  * Inject secretes into Terraform
* **Containers:** um container é criado a partir de uma imagem
  * Docker
  * Kubernetes


## Isolamento
### Isolamento Físico
* **Restrições vantajosas:**
  * Não é necessário que operadores estejam presencialmente no data center
  * Não é necessário que operadores acessem fisicamente os servidores
* **Ganhos de Produtividade:**
  * Monitoramento remoto de cada elemento do ecossistema
  * Monitoramento automatizado
  * Análise de telemetria e desempenho do hardware
  * Migração remota de recursos lógicos
  * Identificação automatizada de degradação ou falhas de hardware
  * Manutenção programada
* **Melhoria de segurança:**
  * Acesso reduzido ao hardware
  * Redução de chances de vazamento ou comprometimento de dados
  * Redução de ocorrências de acidentes e erros humanos
  * Controle de danos e compartimentação de efeitos colaterais
* **Ganhos financeiros:**
  * Aumento da capacidade de escala de gestão dos recursos tecnológicos
  * Redução de incidentes
  * Redução de consumo de recursos energéticos
  * Preços mais competitivos e flexíveis


### Isolamento Lógico
* **Estabilidade:**
  * Redundância de recursos
  * Redução de pontos de falha
  * Balanceamento de recursos
  * Migração de recursos e aplicações sem interferência dos operadores do data center
* **Produtividade:**
  * Independência no controle de infraestrutura
  * Integração via código ou ferramentas de terceiros para gestão automatizada
  * Acesso às métricas de infraestrutura e aplicações para análise e otimização
  * Abstração de infraestrutura para consumo e desenvolvimento de serviços
  * Versionamento e controle de ambientes
* **Segurança:**
  * Dados transitórios criptografados
  * Dados estacionários criptografados
  * Alta granularidade nos níveis de permissões
  * Alta granularidade de rede em nível lógico
* **Controle:**
  * Autonomia de segurança
  * Autonomia de provisionamento
  * Autonomia de escalabilidade
  * Autonomia de controle de acesso
* **Custos:**
  * Consumo de recursos controlado pelo cliente em tempo real
  * Automação
  * Integração
  * Controle aberto e transparente dos custos


### Inovação
* Acesso a hardware e software de última geração sem imobilizar patrimônio
* Integração de APIs de terceiros que utilizam sua própria conta para executar aplicações e serviços de última geração
* A facilidade de qualquer um se tornar um provedor de serviços especializados
* A granularidade permite criar, validar e, evoluir ou encerrar projetos com rapidez e baixos custos
* Consumir serviços e softwares sob demanda sem a necessidade de aquisição de licenças e sem carência de uso


## Granularidade
### Fundamentos de Infraestrutura Cloud
* **Categorias de serviços AWS:**
  * Análises
  * Integração de aplicações
  * Blockchain
  * Aplicações empresariais
  * Gerenciamento financeiro na nuvem
  * Computação
  * Central de atendimento
  * Contêineres
  * Banco de dados
  * Ferramentas de desenvolvedor
  * Computação de usuário final
  * Web e plataforma móvel front-end
  * Jogos
  * Internet das Coisas
  * Machine learning
  * Gerenciamento e governança
  * Serviços de mídia
  * Migração e transferência
  * Redes e entrega de conteúdo
  * Tecnologias quânticas
  * Robótica
  * Satélite
  * Segurança, identidade e conformidade
  * Tecnologia sem servidor
  * Armazenamento
  * Cadeia de suprimentos

* A AWS tem aproximadamente 276 serviços diferentes

* Macro categorias de serviços em nuvem
  * **Computacionais:** loca um recurso computacional (CPU e memória) e coloca uma carga para ser rodada
    * EC2
    * Lambda
    * Machine Learning
    * ...
  * **Dados:** está pagando pela solução
    * S3
    * RDS
    * ...
  * **Rede:**
    * VPC
    * VPN
    * ...
  * **Borda**
    * Firewall: protege especificamente a rede
    * WAF (Web Applications Firewall): protege ataques em aplicações, linguagens, bancos de dados. São dinâmicos e inteligentes
    * CloudFront (CDN): armazenar e entregar conteúdo estático
    * ELB (Elastic Load Balancer)
    * ...

* **Abstração de serviços**
  * Quanto mais próximo da computação pura mais barato é o custo computacional CPU/Memória
  * Quanto mais abstraído maior é o custo/tempo
  * Quanto mais abstraído mais especializado
  * Processos de consumo constante custam mais barato em serviços computacionais como EC2
  * Processos de consumo esporádico e oscilante custam mais barato em serviços elásticos com Lambda, Fargate, Kubernetes e similares. O mesmo vale para bancos de dados.
  * Use a granularidade da nuvem a seu favor para ganhar escalabilidade a custos baixos


### Otimização de recursos computacionais

![Otimização de recursos computacionais](./assets/otimizacao-recursos-computacionais.png)
* Representação de como funciona uma aplicação em um servidor dedicado
* Tudo em um único servidor nos servidores dedicados


![Otimização de recursos computacionais Detalhado](./assets/otimizacao-recursos-computacionais-2.png)
* Aqui são separados em VMs e o tamanho da para cada aplicação
* o HyperV está alocado para cada VM
* O fato de ter um OS entre a VM e o Hardware, prejudica a performance do que está rodando ali dentro


![On Premises/Dedicado e Instância Cloud](./assets/on-premises-dedicado-instancia-cloud.png)
* O erro mais comum é migrar o que está no on premises com a mesma capacidade computacional para o Cloud, pois a instância virtual não temos acesso direto ao hardware
  * No on premises, ele sai do sistema operacional e vai diretamente para o hardware
  * enquanto na instância cloud, ele sai do serviço, passa pelo sistema operacional virtualizado, vai para o HyperV (que tem todas as camadas de segurança como criptografia, isolamento e tudo o que precisa para ter uma VM rodando) e depois para o host e para o hardware. Ou seja, temos a mesma capacidade de processamento de dados, mas tem um delay no transito dos dados


![Instância Virtualizada em Cloud](./assets/instancia-virtualizada-em-cloud.png)
* Além do sistema operacional da VM, temos o Sistema Operacional real
* Se os sistemas operacionais virtualizados precisam consumir hardware/recursos demais eles vão disputar o mesmo funil passando pelo HyperV. Quanto mais hardware eles precisarem, mais o HyperV vai consumir do hardware para tratar todas essas requisições.


![Instância Cloud Decomposta](./assets/instancia-cloud-decomposta.png)
* Decompõe a aplicação em serviços
* Menos tempo de configuração e tempo


* Comparação de uso de recursos computacionais
  * ![vCPU 8](./assets//vcpu-8.png)
  * ![vCPU 2](./assets//vcpu-2.png)


### Granularidade
* Instâncias menores
* Auto escalabilidade
* Ambientes enxutos
* Microsserviços
* Serviços distribuídos
* Gestão de dados independente

R: Automação


## Arquitetura
### Estrutura de Projetos em IaC
* **Well Architected Frameworks da AWS**
  * **Princípios:**
    * Pare de adivinhar suas necessidades de capacidade
    * Sistemas de teste em escala de produção
      * Usar logs de produção, para testar a aplicação na fase de testes
    * Automatize tendo em mente a experimentação arquitetônica
    * Considere arquiteturas evolucionárias
    * Impulsione arquiteturas usando dados
    * Melhore durante os dias de jogo
  * **Pilares:**
    * Excelência operacional
    * Segurança
    * Confiabilidade
    * Eficiência de desempenho
    * Otimização de custos
    * Sustentabilidade

* **Princípios da arquitetura eficiente**
  * Acoplamento fraco
    * ![Acoplamento fraco com assincronicidade](./assets/acoplamento-fraco-com-assincronicidade.png)
    * Podemos separar cada etapa em microsserviços e cada equipe responsável pode conhecer profundamente as regras de negócio desta etapa
  * Gestão de dados independente
    * **NoSQL**
      * Schemeless
      * Alta performance
      * Gestão compartilhada entre memória e disco
      * Persistência eventual*
      * Big Data
      * Redundância / Cluster
      * Backup difícil
    * **Key/Value**
      * Chave/Valor
      * Alta performance
      * Gestão compartilhada entre memória e disco
      * Persistência eventual e volátil*
      * Alto custo de escala
      * Alto custo de armazenamento
      * Redundância / Cluster
      * Sem Backup
    * **Objetos: S3, Google Storage**
      * Schemeless
      * Performance Média*
      * Persistência forte*
      * Baixo custo de escala
      * Baixo custo de armazenamento
      * Alto custo de recuperação de dados*
      * Redundância
      * Backup / Replicação
    * **SQL**
      * Schema
      * Performance baixa*
      * Persistência forte*
      * Alto custo de escala
      * Alto custo de armazenamento
      * Redundância e Cluster de alta complexidade
      * Backup / Replicação
  * Independência de camadas
  * Versionamento
  * Testes
  * Automação de deploys / pipelines
  * Monitoramento
  * Plano de contingência
  * Auto-reparação
  * Análise e evolução constante


## Observações e Referências
* [O que é o AWS CloudFormation?](https://docs.aws.amazon.com/pt_br/AWSCloudFormation/latest/UserGuide/Welcome.html)
* [Cloudflare](https://www.cloudflare.com/pt-br/)
* [Plataforma Solution](https://plataformasolution.com.br/)
* [AWS - Well Architected Framework](https://aws.amazon.com/architecture/well-architected)
* [Azure - Well Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)
* [Google - Well Architected Framework](https://cloud.google.com/architecture/framework)



# Infra As Code (IAC) II
## Arquitetura da Infraestrutura
### Rede Pública
* VPC pública com: 
  * Banco de dados -> 3 Máquinas EC2 -> Load Balancer que está conectado na Internet
* Intenção de expor a aplicação na Internet

### Rede Privada
* Objetivo de aproveitar as vantagens que a nuvem está oferecendo, mas o acesso precisa estar restrito e seguro


### Rede Híbrida
* VPC Privada ser intermediária, ou seja, temos a rede privada on-premises e a VPC privada e fazer a integração da VPC privada com a VPC pública, para integrar certas informações
  * Por exemplo, e-commerce: o e-commerce em si tem toda a aplicação independente e está em uma VPC pública, e todo o sistema ERP em uma VPC privada


### Sincronização Privado/Público
* Integração direta via API, pelo um middleware rodando dentro da VPC privada que faz a requisição para a aplicação online, porém a sincronização de dados só vai acontecer quando esse aplicativo for executado.
  * Ou seja, se executar demais podemos sobrecarregar a API e se executar de menos, podemos perder a sincronização da dados críticos

* Podemos usar o S3 e fazer essa sincronização em lote
* Podemos usar uma fila de eventos do SQS (fila de mensageria)
* Podemos usar uma fila de eventos do SNS (broker de mensageria)

* A fila de mensageria coloca as mensagens em uma fila de processamento e do outro lado um worker, que fica processando em background, esse worker vai pegar a tarefa que está na fila de tarefas e vai executar a tarefa
* O broker de mensagens a mensagem entra em uma fila de distribuição, ou seja, um hub de distribuição
  * Sendo assim, no SQS nós garantimos que um único processo vai executar aquela tarefa, reduzindo a duplicidade. Se o worker falhar, ele devolve na fila e o próximo worker pega
  * No caso do broker, SNS, ele vai jogar em um hub e ela vai ser distribuída para todo mundo que estiver ouvindo
* Quanto maior mensagem, mais é cobrado

* Como usar? 
  * Fizemos um pedido no e-commerce, esse pedido dispara uma mensagem no SQS informando o ERP que existe um batch relacionado a esse pedido no S3. O worker local pegou essa mensagem no SQS, executa a tarefa e pega o arquivo no S3 que tem todos os dados a respeito daquele pedido. Ou seja, o tamanho da mensagem é só o evento informando o worker, assim economizamos a cobrança. 


### Sincronização Público/Privado
* S3
* SQS
* Híbrido


## Arquitetura de software
### Domain Driven Design
* Um modelo de desenvolvimento de software
* Domínio: conjunto de regras de negócio que regem o funcionamento de determinado sistema
* Persistence: são dados, ou seja, o banco de dados fica fora da aplicação. A aplicação não pode ficar amarrada a esse banco de dados, caso seja necessário fazer uma migração


### Micro Serviços
* Escala sobre demanda cada parte da aplicação
* Equipes multidisciplinares garantindo que todos tenham visão da regra de negócio
* Criar cluster específicos diferentes
* É possível paralelizar os deploys por equipes

#### Por onde Começar?
* Monolithic architecture
* Microservice architecture
* Decompose by business capability
* Decompose by subdomain
* Self-contained Service
* Anti-corruption layer
* Database per Service
* Shared database
* Command-side replica
* API Composition
* CQRS
* Domain event
* Event sourcing
* Transactional outbox
* Transaction log tailing
* Consumer-driven contract test
* Consumer-side contract test
* Service component sest
* Multiple service instances per host
* Service instance per host
* Service instance per VM
* Service instance per Container
* Serverless deployment
* Service deployment platform
* Microservice chassis
* Externalized configuration
* Service Template
* Remote Procedure Invocation
* Messaging
* Domain-specific protocol
* Idempotent Consumer
* API gateway
* BAckend for front-end
* Client-side discovery
* Server-side discovery
* Service registry
* Self registration
* 3rd party registration
* Circuit Breaker
* Access Token
* Log aggregation
* Application metrics
* Audit logging
* Distributed tracing
* Exception tracking
* Health check API
* Server-side page fragment composition
* Client-side UI composition


## Ferramentas de IaC
### Gestão de infraestrutura como código
* **SDK**
  * Um kit para desenvolvedores de software, é uma biblioteca que contém wrappers que são facilitadores. Ou seja, podemos instalar esses SDKs na nossa aplicação e ele mesmo irá resolver diversos processos como, por exemplo, renovação de token
  * O objetivo principal é para interagir com a infraestrutura
    * Por exemplo, manipular a fila do SQS
* **CDK**
  * Gerenciar infraestrutura
  * Preparação para trabalhar com templates
  * Bloco de configurações separado do código
  * Desenvolvido em cima do SDK
* **CloudFormation**
  * Template de parametrizações
  * Desenvolvido em cima do CDK
* **Terraform**


### SDK (Software Development Kit)
* Bibliotecas em várias linguagens
* Documentação abrangente e detalhada
* Integração direta com a aplicação
* Gere a infraestrutura
* Interage com as funcionalidades dos serviços
* Compatibilidade com TODOS os serviços AWS
* Curva de aprendizagem e implantação alta


### CDK (Cloud Development Kit)
* Biblioteca em várias linguagens
* Documentação abrangente e detalhada
* Integração direta a aplicação
* Gere a infraestrutura
* NÃO Interage com as funcionalidades dos serviços
* Compatibilidade com TODOS os serviços AWS
* Curva de aprendizagem alta
* Curva de implantação média


### CloudFormation
* Independente de linguagem
* Baseado em templates JSON e YAML
* Documentação abrangente e detalhada
* Executado a partir de command line, IDE's e Console AWS
* Gere a infraestrutura
* NÃO Interage com as funcionalidades dos serviços
* Compatibilidade com a maioria dos serviços AWS
* Curva de aprendizagem média
* Curva de implantação muito baixa


### TerraForm
* Independente de linguagem
* Baseado em templates JSON e YAML
* Documentação abrangente e detalhada
* Executado a partir de command line, IDE's
* Gere a infraestrutura
* NÃO Interage com as funcionalidades dos serviços
* Compatibilidade limitada com serviços AWS
* Curva de aprendizagem média
* Curva de implantação muito baixa


### CloudFormation Designer
* [Visão geral da interface do AWS CloudFormation Designer](https://docs.aws.amazon.com/pt_br/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer-overview.html)


### Estrutura de Projetos com IaC
* **Versionamento (Código):**
  * Git
  * Controle de versão de código
  * Controle de versão de software
  * Rollback
  * Recuperação de catástrofe e mitigação de danos
  * Controle de qualidade (code review)
  * Recuperação point-in-time
  * Responsabilidade
  * Distribuição de Responsabilidades
  * Trabalho simultâneo/Timelines
  * Sub-modules
  * Comutação
  * Automação
  * Testes
  * Pipelines/Deploys
* **Versionamento (Infraestrutura):**
  * Tudo que código oferece
  * Versionamento de infraestrutura
  * Rollback junto com a aplicação
  * Pipelines/Deploys Automatizado
  * Teste e implantação com Zero Downtime (Blue/Green, Rolling, etc)
  * Garantia de integridade com a versão testada e produção
  * Autonomous Recovery
  * Auto-scaling em níveis de cluster, ambiente e região
  * Migração de região em um click
  * Multi-região com balanceamento DNS
  * *Multi-Plataforma
  * Versionamento de estrutura de dados
* **Testes:**
  * Teste Unitário
  * Teste Funcional
  * Teste Operacional
  * Teste de Stress: quando está além da capacidade, qual o comportamento irregular está apresentando e reagindo. Abre brechas de segurança, corrompe dados etc
  * Teste de Carga: avalia como a aplicação está se comportando, inclusive sobre a escalabilidade
  * *Homologação
  * Automação de Testes
* **Automação de deploys / pipelines:**
  * Testes
  * Flags
  * Procedimentos de sequenciamento, deploy e rollback
  * Governança e responsabilidade
  * Controle de qualidade
  * Integração com infraestrutura
* Version Control -> Build -> Unit Test -> Deploy to Test -> Auto Test -> Deploy to Production -> Measure/Validate -> Feedback -> Version Control...
* **Monitoramento:**
  * Coleta contínua de métricas da aplicação
  * Coleta contínua de métricas da infraestrutura
  * *Auditoria de dados
  * Coleta e Análise de dados temporais de APIs
  * Uso de machine learning para tomada de decisões automatizadas
  * ML para combate reativo de catástrofes
  * ML para combate reativo de ataques
  * ML para tomadas de ações inteligentes sobre escalabilidade
* **Plano de contingência:**
  * Governança estratégica, operacional, financeira e de crises
  * Conhecimentos profundos da aplicação e das regras de negócios
  * Documentação detalhada e atualizada
  * Entendimento profundo do funcionamento do ecossistema tecnológico
  * Integração íntima das equipes técnicas e de negócios
  * Integração íntima das equipes de desenvolvimento e infraestrutura (DevOps)
  * Planos de ação conjuntos
  * Automação de contingências
* **Autorreparação:**
  * Escalonamento automático para mitigação de danos
  * Redução de danos e prejuízos financeiros e reputacionais
  * Recuperação automática de desastres
  * Rollback automático
  * Detecção e reação automática a falhas operacionais
  * Detecção e reação automática a ataques
  * Redução dos custos de mão de obra
* **Análise e evolução constante:**
  * Mudanças constantes de tecnologia
  * Evolução e surgimento de novas soluções
  * Segurança
  * Estabilidade
  * Confiabilidade
  * Mudanças de escopos de projetos
  * Mudanças de paradigmas
  * Mudanças de equipes
  * *Motivação da equipe
  * *Constância e padronização


### Por onde começar com IaC?
* Passo a passo das necessidades:
  * Conheça, respeite, motive e prepare sua equipe
  * Conheça e documente profundamente as regras de negócios
  * Conheça, meça e documente seu Sistema
  * Conheça intimamente seu provedor Cloud
  * Teste TUDO
  * Otimize
  * Automatize
  * IaC
  * Evolua


### Dados vs Computação
* Dados precisam de backup
* Computação precisa de versionamento

* Dados precisam de sincronização
* Computação precisa de desacoplamento

* Dados precisam de persistência
* Computação precisa de independência

* Dados precisam de durabilidade
* Computação precisa de regeneração


### Para guardar na memória
* Seja granular
* Seja desacoplado e persistente
* Seja testável
* Seja automático
* Seja evolutivo
* E será Cloud IaC


## Observações
* [Martin Flower](https://martinfowler.com/)
* [What are microservices?](https://microservices.io/)

* Em Cloud substituímos sessão por access token, porque sessão é muito pesado, pois são vários dados que a maior parte do tempo não usamos que são armazenados ou consumidos durante a aplicação
  * A sessão guarda todos os acessos do usuário, porém isso dificultava a troca de sessão em múltiplos servidores
  * Access token faz uma consulta para verificar se o usuário tem acesso somente àquele método

