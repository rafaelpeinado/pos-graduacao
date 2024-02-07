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


# Containers II (Kubernetes)
## Subindo uma aplicação utilizando containers...
### Possíveis problemas
* **Escalabilidade da aplicação:** será que funciona da mesma com 10, 100, 1000 ou um milhão de usuários mandando várias requisições?
* **Requisições de forma global:** podemos ter problemas de latência em outros países para acessar o servidor
*  **Variação nas requisições e picos de acessos:** épocas de muitas requisições e outras de poucas requisições. Por exemplo, e-commerce no final do mês vende menos, porém no começo do mês pode vender mais.


## Como tratar esses possíveis problemas?
### Orquestração de containers com Kubernetes
* **Kubernetes:** Kubernetes (k8s) é uma plataforma de orquestração de containers que automatiza a implantação, o dimensionamento e a gestão de aplicações que utilizam containers
  * Kubernetes é uma plataforma Open Source, lançada em junho de 2014 e foi escrita na linguagem GO por Joe Beda, Brendan Burns e Craig McLuckie


#### Benefícios da utilização de Kubernetes
* **Orquestração Automatizada**
  * Implantação
  * Escala
  * Operação
* **Escalabilidade**
  * Horizontal
  * Vertical
* **Desacoplamento da infraestrutura**
  * Portabilidade em ambiente on-premise ou nuvem
* **Abstração de recursos**
  * Automação do ciclo de vida da aplicação
* **Gerenciamento dinâmico de recursos**
  * Ambiente de Desenvolvimento Reproduzíveis
  * CI/CD
* **Plataforma Open Source**
  * Grátis


#### A arquitetura Kubernetes
* [Arquitetura Kubernetes](https://www.luizpessol.com.br/2020/09/03/o-que-e-kubernetes-por-que-usar-como-servico/)
* <img src="https://www.luizpessol.com.br/wp-content/uploads/2020/09/luiz_pessol_arquitetura_kubernetes-768x532.png">

Temos o Master node (onde se encontra o API Server, Scheduler, Controller - Manager, etcd), Worker node-1 e Worker node-2 (onde se encontram os pods, containers, kubelet, Container Runtime (Docker) e Kube-proxy)

* **Master node:** gerenciar e controlar os Worker node
  * **API Server:** regras de negócio e interage a partir do kubectl
  * **Scheduler:** gerencia toda a parte de planejamento e liberação dos pods e dizer onde cada um vai
  * **Controller - Manager:** manter o sistema consistente entre todos os nós
  * **etcd:** um banco de dados de configurações de chave e valor, que mantém as configurações de estado dos nós

* **Worker node:**
  * **Kubelet:** gerencia a criação dos pods (pod é o menor componente, e é onde se mantém os containers)
  * **Container Runtime (Docker):** é a plataforma de containers que estamos usando aqui dentro
  * **Kube-proxy:** todo o mapeamento de portas e redes dos pods e dos componentes

A arquitetura Kubernetes trabalha com **[Cluster](https://www.salesforce.com/br/blog/clusters/)** de computadores


#### Expondo aplicações escaláveis
[Understanding k8s Deployments](https://www.brazilclouds.com/blog/understanding-k8s-deployments)
<img src="https://assets-global.website-files.com/5e5a5c35a623e45f7f701878/5e994394e2013ba264e72b3a_dep.png">

* **Pod:** é onde está a aplicação ou alguma coisa que vai receber uma requisição
  * no exemplo temos 4 replicas da aplicação (4 pods)
* **ReplicaSet:** são as 4 réplicas
* **Deployment:** quando ele é alterado, automaticamente ele altera os pods
* **Service:** recebe o tráfego e faz o balanceamento para cada um dos pods
  * o tráfego chega pelo Ingress, passa pelo Service que tem uma porta que se comunica internamente com o Kubernetes e trafega os dados para cada um dos pods sem sobrecarregar cada um deles. 
* **Ingress:** faz a abertura de portas. Traz o tráfego externo para dentro do Kubernetes

## Escalando grandes aplicações com Kubernetes
### O arquivo YAML e as definições dos recursos
* O arquivo utilizado para definir as configurações dos recursos do Kubernetes, também chamados de manifestos:
  * Clusters
  * Pods
  * ReplicaSets
  * Deployments
  * Services
  * Ingress
  * AutoScalling (HPA e VPA)
  * ... e muitos outros recursos

### Criando um cluster
* **Clusters podem ser:**
  * On-premise
  * Cloud Provider
* **Provedores de Kubernetes na nuvem:**
  * Amazon Elastic Kubernetes Service (EKS)
  * Google Kubernetes Engine (GKE)
  * Microsoft Azure Kubernetes Service (AKS)
  * IMB Cloud Kubernetes Service
  * DigitalOcean Kubernetes (DOKS)


### Criando as imagens dos containers
Dockerfile --build--> Imagem --push--> Container Registry

### Criando um recurso
Cluster(master node e workers node) -> pod.yaml ---kubectl apply -f pod.yaml---> Pod criado

### Fluxo para deploy de grandes aplicações
Cluster --definir Deployment--> Deployment (ReplicaSet -> Pods) --definir Service--> Service --definir AutoScalling--> AutoScalling (HPA <-> VPA) --definir Ingress--> Ingress --Expor ao usuário-->


## Hands on
Kubernetes in Docker(kind)
[Kind](https://kind.sigs.k8s.io/): ferramenta para rodar clusters de Kubernetes local usando containers do Docker

* **kind create cluster:** cria um cluster, cria apenas um nó e esse nó vai ser o Control Pane
* **docker ps:** conseguiremos ver a imagem rodando

Queremos que o contexto que estamos usando é um cluster que criamos
Se criar um cluster sem nome, o nome dele automaticamente vai ser kind
* **kubectl cluster-info --context kind-kind:** estamos conectados com o Kubernetes
* **kubectl get nodes:** para ver os nós

**Obs.:** estamos simulando um cluster Kubernetes dentro do Docker, o container que está representando o nó. Tudo o que está dentro do nó, está dentro do container. Por isso, não é a forma ideal para se trabalhar em produção, pois temos uma camada a mais, que é a camada do Docker, o que gera perda de performance.

* **kind delete cluster --name=kind:** deletar um cluster com o nome kind

* **.yaml:**
  * **kind:** do tipo de recurso Cluster que tem nós como argumento
  * **nodes:** nós são definidos aqui
    * nesse caso temos 4 nodes (4 máquinas), sendo um control-pane e três workers. Se criássemos o recurso com 4 cores e 4 giga de RAM, teríamos 16 cores e 16 giga de RAM. Na prática são máquinas.

* **kind create cluster --config=cluster.yaml --name=k8s-cluster:** criar um cluster com o arquivo de configuração cluster.yaml com o nome k8s-cluster
* **kubectl cluster-info --context kind-k8s-cluster**
* **kubectl get nodes**

* **Obs.:** No [ENTRYPOINT do arquivo](./scripts-II/2.criar-pod/aplicacao/Dockerfile) estamos com apenas uma thread na porta 8000

* **Obs.:** O Kubernetes não tem a [imagem](./scripts-II/2.criar-pod/docker-compose.yaml) local, então ele precisa ir buscar no repositório registry do Docker Hub

* **docker build . -t rafaelpeinado/servidor-python:1.0**
* **kubectl get all:** listar todas as informações

Os Secrets do Kubernetes serve para guardar informações sensíveis
* **[secrets.yaml](./scripts-II/2.criar-pod/secrets.yaml)**
  * **type:** Opaque muito usado para variáveis de ambiente
* **kubectl apply -f secrets.yaml:** aplicar arquivos de configurações
* **kubectl get secrets:** pegar os secrets da cluster

* **[pod.yaml](./scripts-II/2.criar-pod/pod.yaml):**
  * **labels:** associar a alguma aplicação. No Kubernetes podemos criar alguns arquivos que estarão fazendo parte do mesmo label. Por exemplo, quando criarmos services, podemos ver os pods que tem os labels igual ao definido
  * **cpu:** 100m é 10% de um core, 1000m é 1 core inteiro.

* **kubectl apply -f pod.yaml:** criou o pod
* **kubectl logs -f servidor-python:** para verificar os logs do pod servidor-python
  * Ao tentar acessar a porta 8000, não carregou a aplicação, pois não temos acesso ao pod de forma externa
  * Temos que redirecionar uma porta da máquina para uma porta do Kubernetes
* **kubectl port-forward pod/servidor-python 8000:8000:** estamos acessando o pod servidor python a partir de uma porta para fazer um redirecionamento da porta 8000 para porta 8000
  * Após essa mudança a aplicação passou a funcionar
* **kubectl delete pod servidor-python:** para deletar um pod

* [ReplicaSet](./scripts-II/3.criar-replicaset/replicaset.yaml)
* **selector:**
  * **matchLabels:** selecionar todos os rótulos que dão match com o servidor-python
  * **replicas:** quantidade de pods

* **kubectl apply -f replicaset.yaml**
* **kubectl get replicaset**
* **kubectl delete pod servidor-python-4fntl**
* **kubectl get pods**

**Mensagem:** replicaset.apps/servidor-python configured, pois o pod não foi criado, foi apenas configurado

* **kubectl get pods:** os pods ainda estarão rodando do antigo
* **kubectl describe pod servidor-python-s4j4s:** para ver todas as informações do pod
  * caso o pod seja deletado, o novo virá com a nova imagem associada ao replicaset
* **kubectl delete replicaset servidor-python**


* O **Deployment** é exatamente igual ao **ReplicaSet**

* **kubectl apply -f deployment.yaml**
* **kubectl get all**
* SEMPRE QUE CRIAR UM DEPLOYMENT, CRIA TAMBÉM UM REPLICASET
  * A diferença é que no Deployment, sempre que configuramos o recurso, ele atualiza os pods 
* **kubectl apply -f deployment.yaml:** ao aplicar novamente a configuração com o deployment atualizado, ele irá derrubar os pods antigos e criar novos
* **kubectl get replicaset:** teremos dois replicaset, pois o antigo vai estar zerado e teremos o novo


**SERVICE**
* é para definir formas de fazer balanceamento de carga em um proxy reverso nos pods, ou seja, vamos dar um ponto interno de entrada para redirecionar o balanceamento de cargas para os pods internamente no cluster
* Existem três tipos de services:
  * **Cluster IP:** que é o default do Kubernetes
  * **Node Port:** quando queremos ter um acesso específico em uma porta específica em todos os nós do cluster, mas não é tão usado quanto o Cluster IP e o Load Balancer
  * **Load Balancer:** cria um IP externo para acessarmos ele para conseguirmos acessar o Kubernetes e acessar serviços internos dele e também trabalhando o balanceamento de carga da aplicação.

* **kubectl apply -f service-cluster-ip.yaml**
* **kubectl get services**
  * **kubectl get svc**
  * os IPs criado não temos acesso fora e precisaremos criar um **port forward** para o service
* **kubectl port-forward svc/servidor-python-service 8000:80**
  * vamos acessar a porta 8000 do localhost que será redirecionada para a porta 80 do service que irá redirecionar para a porta 8000 do Kubernetes, conforme parâmetro **[targetPort](./scripts-II/5.criar-service/service-cluster-ip.yaml)**
* **kubectl delete svc servidor-python-service**

* **kubectl apply -f service-node-port.yaml**
* **kubectl get svc:** foi criado a porta 80:30690/TCP, ou seja, quando acessar a porta 80 do service, ele será redirecionado para a porta 30690 do pod, que é fixa em cada nó dos clusters, ou seja, nos 4 nós
* **kubectl port-forward svc/servidor-python-service 30001:80**
* **kubectl delete svc servidor-python-service**

* **kubectl apply -f service-load-balancer.yaml**
* **kubectl get svc:** o EXTERNAL-IP fica pending, porque está criando a porta, porém aqui, como estamos usando o kind, ficará pending para sempre.
* **kubectl delete svc servidor-python-service**

Vamos usar o Cluster IP, porque é o padrão

* **kubectl describe svc servidor-python-service**
  * Endpoints


**INGRESS**
* Configurando o ingress-nginx com todos os seus componentes no cluster kubernetes
  * kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
  * Vai gerenciar tudo para a nossa aplicação
  * **http://localhost/:** vai cair no nginx

* aguardando os componentes do ingress-nginx ficarem ativos
  * kubectl wait --namespace ingress-nginx --for=condition=ready pod --selector=app.kubernetes.io/component=controller --timeout=90s

* **kubectl apply -f ingress.yaml**
  * temos um Deployment, que criou o ReplicaSet
  * service
  * pods
* o Ingress foi criado no service do nginx
  * **http://localhost/:** agora o localhost funciona
    * **por default, quando acessamos localhost, estamos acessando a porta 80 e quando é https, é a porta 443**
  * cada hora um pod diferente é acessado

* **for i in {1..10}; do curl http://localhost -w "\n"; done**
  * para fazer uma requisição no localhost 10 vezes
* **kubectl get pods**
* **kubectl logs -f servidor-python-546b64899b-6gcjd**

**[HPA](./scripts-II/7.criar-hpa/)**
* Vamos instalar o metric server, que é para termos um componente para ter a porcentagem de recursos usados no componente
* **kubectl apply -f teste-de-carga.yaml**
* **kubectl port-forward svc/teste-carga-svc 8089:80**
* **watch -n1 kubectl get hpa**
  * em formato **watch** é para acompanhar as mudanças em tempo real

* **kubectl delete hpa servidor-python**
* **kubectl delete deployment teste-carga-deployment**
* **kubectl delete svc teste-carga-svc**


**[PROBES](./scripts-II/8.adicionar-probes/)**
* **readinessProbe:** verifica se a aplicação está pronta para receber tráfego
  * a aplicação só vai rodar se este teste passar
* **livenessProbe:** verifica se a aplicação está em execução
  * e só vai continuar rodando se esse teste passar

Basicamente essas informações verificam se a aplicação está saudável, caso não esteja, será criado um novo pod

* **kubectl logs -f servidor-python-7bbf9f6c97-6ckm8:** terão várias requisições healthz

* **[Stats Studio](https://www.stats-studio.com/login):** Usa Kubernetes para funcionar
* [Docs](https://stats-studio-api.com/docs)


* **kubectl delete all --all:** vamos deletar tudo o que fizemos até agora
* **kind delete cluster --name=k8s-cluster**

## Observações
* [Terraform](https://www.terraform.io/)


