# Gerenciamento e Estruturas de Fila I
## Introdução
- **O que é gerenciamento de filas?**
  - Um mecanismo para comunicação assíncrona entre sistemas e serviços
  - Garante processamento ordenado e confiável de mensagens
  - Reduz acoplamento entre componentes
- **Exemplos de uso:**
  - Notificações assíncronas (exemplo: envio de e-mails em segundo plano)
  - Processamento de pagamentos
  - Coleta e análise de logs


## Conceitos Fundamentais
- **O que é uma Message Queue (MQ)?**
  - Um intermediário entre **produtores** e **consumidores** de mensagens
  - Permite **desacoplamento** e melhora a escalabilidade
- **Modelos de Mensageria:**
  - **Fila Tradicional (RabbitMQ):** as mensagens são consumidas e removidas
  - **Log Distribuído (Kafka):** as mensagens são persistidas para múltiplos consumidores
- **Componentes principais:**
  - **Produtor:** envia mensagens
  - **Broker:** gerencia e roteia mensagens
  - **Consumidor:** processa mensagens


## Arquitetura de Mensageria
- **Comunicação síncrona versus comunicação assíncrona**
- **Padrões de entrega de mensagens:**
  - **Point-to-Point (Fila Tradicional):** um único consumidor por mensagem
  - **Publish/Subscribe (Tópicos):** mensagens entregues para vários consumidores
- **Benefícios do uso de mensageria:**
  - Melhor **escalabilidade**
  - **Tolerância** a falhas
  - Processamento **distribuído**


## Visão Geral do RabbitMQ
- **O que é?**
  - Broker de mensagens baseado no protocolo AMQP (Advanced Message Queuing Protocol)
  - Projetado para **processamento confiável e ordenado** de mensagens
- **Principais Características**
  - Baixa latência e alta confiabilidade
  - Suporte a múltiplas estratégias de roteamento
  - Confirmação de entrega e filas mortas (Dead Letter Queues)
- **Casos de Uso:**
  - Sistemas que precisam garantir ordem e entrega de mensagens
  - Comunicação assíncrona entre microsserviços
  - Balanceamento de carga para workers
- **Componentes:**
  - **Exchange:** roteia mensagens para as filas
  - **Queue:** armazena as mensagens até serem consumidas
  - **Bindings:** ligação entre exchange e filas
- **Tipos de Exchanges:**
  - **Direct:** mensagem vai para uma fila específica
  - **Fanout:** mensagem enviada para todas as filas vinculadas
  - **Topic:** roteamento baseado em padrões (exemplo: logs.error)
  - **Headers:** roteamento baseado em cabeçalhos da mensagem


### Breve Histórico do RabbitMQ
- Criado em **2007** pela empresa **Rabbit Technologies Ltd.**
- Baseado no protocolo **AMQP (Advanced Message Queuing Protocol)**
- Em **2010**, foi adquirido pela **VMware** e depois passou para a **Pivotal**
- Atualmente, é um dos **brokers de mensagens mais utilizados** no mundo


## Visão Geral do Kafka
- **O que é?**
  - Uma plataforma de streaming distribuído
  - Projetado para processar eventos em tempo real
  - Baseado no conceito de **logs distribuídos** e **persistência de mensagem**
- Principais Características:
  - **Alta taxa** de throughput
  - Mensagens armazenadas para **reprocessamento**
  - Capacidade de **escalar horizontalmente**
- **Casos de Uso:**
  - Processamento de logs e eventos em tempo real
  - Integração em tempo real de dados entre sistemas
  - Sistemas que precisam de replay de mensagens
  - Análise de grandes volumes de dados


### Breve Histórico do Kafka
- Criado no **LinkedIn em 2011** para processar grandes volumes de dados em tempo real
- Em **2012**, foi doado para a **Apache Software Foundation** e se tornou um projeto open-source
- Criado para suportar **alto throughput**, sendo amplamente usado em **Big Data e streaming de eventos**
- Hoje, é mantido pela **Confluent** e uma grande comunidade open-source


### Arquitetura do Kafka
- **Componentes:**
  - **Produtor:** envia eventos para um **Tópico**
  - **Broker:** gerencia o armazenamento e distribuição de mensagens
  - **Partições:** dividem os eventos para escalabilidade
  - **Consumidores:** processam as mensagens armazenadas
- **Diferencial do Kafka:**
  - Mensagens **persistem** por tempo configurável
  - Possibilidade de **múltiplos consumidores** lerem a mesma mensagem


## Comparação entre Frameworks

| Característica        | RabbitMQ                               | Kafka                                                   |
| :-------------------- | :------------------------------------- | :------------------------------------------------------ |
| Modelo                | Fila Tradicional                       | Log distribuído                                         |
| Entrega de mensagens  | Apenas uma vez por consumidor          | Múltiplos consumidores podem processar a mesma mensagem |
| Retenção de mensagens | Até ser consumida                      | Definida pelo tempo de retenção                         |
| Escalabilidade        | Limitada à arquitetura de filas        | Horizontal, baseada em partições                        |
| Casos de uso          | Mensageria tradicional, microsserviços | Processamento de eventos em tempo real, Big Data        |


## Boas Práticas do cotidiano
- **RabbitMQ:**
  - Configurar **Dead Letter Queues** para evitar perda de mensagens
  - Usar **Prefetch** para evitar sobrecarga nos consumidores
- **Kafka:**
  - Definir **tempo de retenção** corretamente para evitar o consumo excessivo de armazenamento
  - Equilibrar **número de partições** para melhorar a performance


## Exemplos de problemas reais em cenários sem mensageria
- **E-commerce:** lentidão no checkout devido à geração de notas ficais e envio de e-mails
- **Processamento de pagamentos:** pagamentos podem falhar se o serviço de terceiros estiver indisponível
- **Aplicação de alto tráfego:** servidores sobrecarregados em momentos de pico


## Desafios Encontrados
- Aplicações fazem **chamadas diretas** a outros serviços (REST APIs)
- Dependência da **disponibilidade** do serviço externo
- **Alta latência** em chamadas síncronas
- **Dificuldade de escalar** horizontalmente


## Observações
- [Try RabbitMQ](https://tryrabbitmq.com/)




