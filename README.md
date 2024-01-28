# Containers I (Kubernetes)


## Subindo uma aplicação localmente...
Banco       <--escrita---   http://localhost:8000    <--requisição--    http://localhost:3000  <--requisição--    http://meu-dominio.com.br   <--requisição--   Usuário
de Dados    --consulta-->         Back-end           ---resposta--->       Front-end           ---resposta--->        Proxy reverso           ---resposta--->

PostgreSQL

* **Proxy reverso:** redirecionamento de portas, ou seja, uma URL que compramos e a partir disso podemos expor na Internet 


### Possíveis problemas
* **Compartilhamento de recursos:** se rodarmos os componentes todos no mesmo SO e mesmo hardware, podemos ter recursos mais consumidos em um componente. Supondo que o backend está demandando muito recurso, poderíamos ter problemas de desempenho do frontend para apresentar as informações ao usuário.
* **Gestão das aplicações:** por algum motivo o componente pode cair e perder o contato com outros componentes. Por exemplo, o backend pode cair e como vamos levantá-lo novamente? É uma mudança simples?
* **Migração de ambientes:** por exemplo, estou rodando a aplicação em Windows e de repente, vou usar um servidor cloud que só disponibiliza Linux. Como vou instalar as dependências? Será que podemos usar os mesmos comandos?
* **Implantação do ambiente:** como ativar toda a aplicação. Por exemplo, aperto um botão e tudo sobe.


## Como tratar possíveis problemas
### Desenvolvimento usando containers
#### Docker
* Plataforma de virtualização de containers que simplifica o desenvolvimento, implantação e execução de aplicativos, proporcionando ambientes isolados e consistentes para suas operações
  * Docker é uma plataforma Open Source, lançada em março de 2013 e foi escrita na linguagem GO por Solomon Hykes
    * GO consegue criar threads muito pequenas

**Máquina virtual vs Container (Docker)**
* **Estrutura Máquina Virtual (VM)**
  * Sistema operacional convidado: não compartilha o kernel da máquina host. Além disso, precisa fazer boot e demora para subir.
  * Estrutura:
    * Infraestrutura
    * Sistema Operacional
    * Hypervisor
      * VM 1
        * Sistema Operacional Convidado
        * Binários e Bibliotecas
        * App1
      * VM 2
        * Sistema Operacional Convidado
        * Binários e Bibliotecas
        * App 2
      * VM 3
        * Sistema Operacional Convidado
        * Binários e Bibliotecas
        * App 3
* **Estrutura Container**
  * Estrutura:
    * Infraestrutura
    * Sistema Operacional
    * Docker Engine
      * Docker 1
        * Binários e Bibliotecas
        * App 1
      * Docker 2
        * Binários e Bibliotecas
        * App 2
      * Docker 3
        * Binários e Bibliotecas
        * App 3

**Benefícios da utilização de Containers**
* **Isolamento:**
  * Ambiente consistente
  * Isolamento de recursos
* **Portabilidade:**
  * Independência da plataforma
  * Fácil migração
* **Eficiência no uso de recursos:**
  * Overhead reduzido (recursos adicionais compartilhados são reduzidos, porém exemplo, tiramos o boot, etc)
  * Inicialização rápida
* **Gestão simplificada:**
  * Automação do ciclo de vida da aplicação
* **Desenvolvimento Ágil e DevOps:**
  * Ambiente de Desenvolvimento Reproduzíveis
  * CI/CD
* **Facilidade na manutenção:**
  * Atualizações simplificadas
  * Rollbacks

## A plataforma Docker e seus elementos
* Quando falamos de containers precisamos usar algum software para reproduzir containers

### A plataforma Docker
* **Client:**
  * docker build
  * docker run
  * docker pull
* **Docker Host:**
  * Docker Daemon (é uma API)
  * Imagens
  * Containers
* **Registry:**
  * Imagens
    * python
    * ubuntu
    * spark
    * postgresql
    * rediz
    * ... muitas outras

### Arquitetura cliente-servidor
Server docker daemon gerencia:
* Imagens
* Containers
* Volumes
* Networks
Client Docker CLI -> Rest API -> Server docker daemon


#### Docker Registry
* dockerhub: O Docker Hub é o registro padrão onde o Docker procura e armazena suas imagens.
  * Acesse: https://hub.docker.com/
  * Provavelmente já existe uma imagem para o que precisamos
    * Existem outros registros de contêineres que também podem ser explorados, sendo empregado na web ou em registros privados.


## Criando, puxando e rodando containers
### Fluxo para criação de um container
Dockerfile --build--> Imagem --run--> Container


#### O arquivo Dockerfile (A receita do bolo)
* Scripts com uma série de comandos em forma de camadas para criação de uma imagem docker utilizando a forma:
  * INSTRUÇÃO argumento
* Alguns comandos essenciais:
  * FROM node
  * WORKDIR /app
  * COPY package.json .
  * RUN npm install
  * EXPOSE . .
  * COPY 3000
  * CMD ["npm", "run", "dev"]


#### Puxando uma imagem do registro (Docker Hub)
* Para puxar uma imagem usamos o comando **docker pull** do **Client** que fará uma requisição no **Docker Daemon** do **Docker Host** e gravará no registro de imagens no **Registry** e em seguida teremos a imagem nas **Imagens** do **Docker Host**.


#### Criando uma imagem customizada
* Usamos o comando **docker build** a partir do arquivo **Dockerfile** que fará uma requisição no **Docker Daemon** no **Docker Host** e disponibilizará a imagem nas **Imagens** do **Docker Host**


#### Rodando um container
* Usamos o comando **docker run** que fará uma requisição no **Docker Daemon** no **Docker Host**, consultar a imagem nas **Imagens** do **Docker Host** e criar um container nos **Containers** do **Docker Host**.


## Hands On
* [Scripts](./scripts/README.md)
* **docker info:** traz informações da sessão que estamos usando ou também as informações mais básicas do Docker.
  * contexto, quantidades de containers rodando, entre outros
* **docker pull hello-world:** pegar uma imagem hello-world do Docker Registry
* **docker images:** lista as imagens disponíveis localmente
* **docker run hello-world:** roda a imagem hello-world
* **docker ps:** lista os containers ativos e suas informações básicas
* **docker build . -t imagem-script:**
  * **.:** local do arquivo Dockerfile
  * **-t imagem-script:** nome da tag da imagem
* **docker rm CONTAINER-ID:** para remover o container
* **docker run --rm imagem-script:** roda a imagem no container e depois de terminar a execução, deve excluir o container
* **docker build . -t imagem-ininterrupta:1.0**
  * **:1.0: versão da imagem**
* **docker run -d --name imagem-ininterrupta imagem-ininterrupta:1.0**
  * **-d:** não travar o terminal
  * **--name:** dar nome para o container
* **container ps -a**
* **docker exec -it imagem-ininterrupta bash**
  * **-it:** criar interação com o terminal
* **docker stop imagem-ininterrupta**

Podemos compartilhar arquivos entre o host e o container a partir de **volumes compartilhados**

* **docker run -d --name containers-e-volumes -v ${PWD}/volume:/app containers-e-volumes:1.0**
  * devemos informar que queremos fazer um bind(vincular) de volumes a partir da pasta volumes local para a pasta /app do container e vice-versa
* **docker inspect containers-e-volumes**
  * verificar a parte de **Mounts**

* **docker rm -f ID-CONTAINER**
  * **-f:** para forçar a remoção do container
* **docker start imagem-ininterrupta**
* **docker stop $(docker):** parar todos os containers
* **docker rm $(docker):** remover todos os containers

**4-container-api**
* **docker run -d -p 8000:8000 --name container-api -v ${PWD}/app:/api/app container-api:1.0**
  * **-p 8000:8000:** redirecionará a porta do localhost 8000 da máquina para o 8000 do container
* **docker run -d -p 9000:8000 --name container-api -v ${PWD}/app:/api/app container-api:1.0**
  * **-p 9000:8000:** redirecionará a porta do localhost 9000 da máquina para o 8000 do container
* * **docker run -d -p 8000:9000 --name container-api -v ${PWD}/app:/api/app container-api:1.0**
  * **-p 9000:8000:** redirecionará a porta do localhost 9000 da máquina para o 8000 do container, porém no exemplo dá erro, pois não tem nenhuma porta 9000 disponível do lado do container

**DOCKER COMPOSE**
Serve para criar vários containers ao mesmo tempo e subir vários ao mesmo tempo e podem se comunicar através de rede

Por padrão pega a variável de ambiente do .env

* **docker-compose build**
* **docker-compose up -d**
* http://localhost:8000/docs para ver todos as rotas da api

* Foi descomentado a [linha 24](./scripts/6-ambiente-docker-compose/docker-compose.yaml) para que restart: always passe a funcionar


* **docker push jogo-par-impar:1.0:** publicar no Docker Hub 
  * **docker build . -t rafaelpeinado/jogo-par-impar:1.0**
  * **docker push rafaelpeinado/jogo-par-impar:1.0**

## Observações
* **python:3.9-alpine:**
  * **python:** imagem do python
  * **3.9:** versão do python usado
  * **alpine:** é a menor versão de todas, que resulta na menor imagem possível, pois tem o mínimo de dependências

* **[Rancher](https://rancher.com/docs/rancher/v1.2/en/cattle/containers/):** o Rancher é uma ferramenta open source que serve para administrar uma infraestrutura de docker.

* **[Docker Docs](https://docs.docker.com/)**

* Grafana
* ElasticSearch


