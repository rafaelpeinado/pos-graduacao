# Cloud Computing (IaaS, Paas, SaaS) I
## Introdução
### O que é Computação em Nuvem?
* A computação em nuvem é um modelo de entrega de serviços de computação pela Internet
* Permite acesso on-demand a recursos compartilhados como servidores, armazenamento, aplicativos, redes e muito mais
* É um modelo de pagamento por uso que ajuda a reduzir significativamente os custos de infraestrutura


### História e Evolução da Computação em Nuvem
É um conceito que veio da década de 50
* A ideia de compartilhar recursos de computação remota ao início da era da computação
* A tecnologia de virtualização e o aumento da banda larga foram os principais impulsionadores para a adoção generalizada da computação em nuvem
* Hoje, a computação em nuvem é uma tendência importante no mundo da tecnologia

* [A Brief History of Cloud Computing](https://www.dataversity.net/brief-history-cloud-computing/)
* [Internet Solutions Division Strategy for Cloud Computing](https://s3.amazonaws.com/files.technologyreview.com/p/pub/legacy/compaq_cst_1996_0.pdf)


### Benefícios e Desafio da Computação em Nuvem
* Benefícios incluem escalabilidade, flexibilidade, disponibilidade e redução de custos
* Desafios incluem segurança, privacidade, conformidade e migração de dados
  * Há criptografia ativa para manter os dados privados

O primeiro serviço de Cloud da AWS foi em 2006 e a cloud se popularizou por volta de 2010


### Modelos de Serviço em Nuvem
* O modelo de Infraestrutura como Serviço (IaaS) fornece infraestrutura básica de computação, armazenamento e rede
  * requer mais administração
* O modelo de Plataforma como Serviço (PaaS) fornece ambiente de desenvolvimento e implantação completo para aplicativos
* O modelo de Software como Serviço (SaaS) fornece aplicativos prontos para uso pela Internet
  * Microsoft Office 365


* Por exemplo, uma nuvem privada é a VMware, que é um virtualizador de servidores que podemos pegar 3 ou 4 máquinas e criar um conceito de IaaS, porém não é totalmente IaaS, já que temos que administrar o hardware também e os serviços que estão dentro dos servidores 


#### Modelo de responsabilidade compartilhada

<img src="https://learn.microsoft.com/pt-br/azure/security/fundamentals/media/shared-responsibility/shared-responsibility.svg">

* [Divisão de responsabilidade](https://learn.microsoft.com/pt-br/azure/security/fundamentals/shared-responsibility)

A AWS usa serviços de Microsoft Office 365

### Tipos de Implantação em Nuvem
* A implantação de nuvem pública é quando os recursos de computação são fornecidos por um provedor de nuvem público
* A implantação de nuvem privada é quando os recursos de computação são fornecidos em um ambiente de nuvem privada
* A implantação de nuvem híbrida é quando os recursos de computação são fornecidos em um ambiente que combina nuvem pública e privada
  * em geral as empresas que possuem servidores fazem uso de nuvem híbrida


#### Provedores de Cloud Populares
* **Amazon Web Services (AWS)** é o provedor de nuvem mais popular e líder do mercado
* **Microsoft Azure** é uma solução de nuvem completa da Microsoft
* O **Google Cloud** oferece uma variedade de serviços de nuvem escaláveis e seguros


## IaaS
Alguns provedores:
* Locaweb Cloud
* Alibaba Cloud
* IBM Cloud

### O que é IaaS?
* IaaS significa Infraestrutura como Serviço
* O modelo IaaS fornece infraestrutura básica de computação, armazenamento e rede
* Os usuários podem acessar esses recursos por meio da Internet, pagando apenas pelo que usam

* Migrações Lift and Shift, que é migrar o servidor local para a cloud


### Componentes de IaaS
* Os componentes principais do modelo IaaS incluem servidores, hypervisors, máquinas virtuais e contêineres
* Servidores são computadores físicos que fornecem recursos de computação, armazenamento e rede 
* Hypervisors são programas que permitem que vários sistemas operacionais sejam executados em um único servidor. Estes permitem virtualizar o hardware e sua capacidade
* Máquinas virtuais são sistemas operacionais que são executados em um ambiente virtualizado.
* Os contêineres são ambientes de tempo de execução isolados que permitem a execução de aplicativos em um sistema operacional hospedeiro compartilhado


### Casos de uso de IaaS
* O IaaS é amplamente utilizado para hospedagem de sites, migração de aplicações legadas para a nuvem, armazenamento de arquivos e backup de dados
* Também podemos usar o IaaS para desenvolvimento e teste de aplicativos
* O IaaS é uma solução econômica para empresas que precisam de recursos de computação sob demanda


### Vantagens e Desvantagens do Uso de IaaS
* As vantagens do modelo IaaS incluem escalabilidade, flexibilidade e redução de custos
* Os desafios do modelo IaaS incluem segurança, privacidade e conformidade
* Os usuários precisam ter um conhecimento técnico mínimo para configurar e gerenciar o ambiente de nuvem



## Redes
### Arquitetura de Rede em Nuvem
* A arquitetura de rede em nuvem refere-se à forma como os recursos de rede são organizados na nuvem
* Leaf-spine e hub-spoke são topologias de redes comumente usadas na nuvem
* VLANs e VxLAN são tecnologias usadas para separar o tráfego de rede em diferentes redes virtuais


### Conceitos de Segurança em Redes em Nuvem
Não é uma boa prática criar conexões de VPN para ter conexões com a nuvem. Geralmente essas conexões são feitas via [VNet](https://learn.microsoft.com/pt-br/data-integration/vnet/overview) na própria nuvem.
* A segurança da nuvem envolve proteção de dados, aplicativos e infraestrutura
* As medidas de segurança incluem autenticação de usuários, criptografia e monitoramento de rede
* Os provedores de nuvem geralmente oferecem recursos de segurança integrados em seus serviços


## Tipos de Armazenamento em Nuvem
* Existem vários tipos de armazenamento em nuvem, incluindo SAN, NAS e armazenamento de objetos
* SAN é um sistema de armazenamento em rede que fornece acesso a dados em alta velocidade
* NAS é um sistema de armazenamento de arquivos que permite o compartilhamento de arquivos em diferentes plataformas
* O armazenamento de objetos é uma forma escalável e econômica de armazenar grandes quantidades de dados não estruturados (mais utilizado). São utilizados não apenas para documentos, mas para construção de Data Lakes e outros usos de armazenamento especializado


### Estratégias de Armazenamento em Nuvem
* As estratégias de armazenamento em nuvem incluem backup, arquivamento e recuperação de desastres
* O backup é a cópia dos dados para proteção contra perda de dados
* O arquivamento é o armazenamento a longo prazo de dados que não são mais frequentemente acessados
* A recuperação de desastres envolve a restauração de dados após uma interrupção do serviço


### Exemplo Práticos de Configuração de Redes e Armazenamento
* Existem ofertas de sistemas gerenciadores de bancos de dados (SGBDs) PaaS, IaaS e SaaS
* Bancos de dados para controles transacionais (operações CRUD, OLTP) e analíticos (Big Data, DataWarehouse, OLAP), em formatos SQL e NoSQL
* Outros tipos de bancos de dados especializados são muito utilizados em Cloud - CacheDB, GrafoDB, VectorDB, entre outros
  * [VectorDB](https://www.cloudflare.com/pt-br/learning/ai/what-is-vector-database/)


## Orquestração
### O que é orquestração na computação na nuvem?
* Orquestração é a automação de implantação, provisionamento, coordenação e gerenciamento de aplicativos em ambientes distribuídos em nuvem
* A orquestração de contêineres é um método popular de orquestração que utiliza ferramentas como Kubernetes e Docker Swarm
* A orquestração ajuda a aumentar a eficiência, reduzir erros humanos e melhorar a escalabilidade
  

### Ferramentas de Orquestração
* Kubernetes é uma plataforma de orquestração de contêineres que permite gerenciar e automatizar o deployment, o scaling e a operação de aplicativos em contêineres
* Docker Swarm é uma ferramenta de orquestração de contêineres que permite a criação, gestão, e escalonamento de aplicativos com base em contêineres Docker.


### Paralelismo e Escalabilidade na Nuvem
* O paralelismo é a capacidade de dividir um trabalho em partes menores que possam ser executadas simultaneamente para acelerar o processo
* A escalabilidade é a capacidade de aumentar ou diminuir a capacidade de processamento ou armazenamento de um sistema de acordo com a demanda
* Os recursos da nuvem podem ser facilmente escalados e dimensionados horizontalmente para lidar com picos de demanda

#### Estudos de Caso de Orquestração e Paralelismo
* Spotify usa o Kubernetes para gerenciar aplicativos em contêineres em sua plataforma de streaming de música
* Capital One usou o Docker Swarm para reduzir o tempo de desenvolvimento e deployment de aplicativos em contêineres em sua plataforma bancária
* Outros exemplos incluem a aplicação de ferramentas de orquestração em empresas como Microsoft, IBM, Cisco, e muitas outras
* [Estudo de Caso da WebMotors](https://aws.amazon.com/pt/solutions/case-studies/webmotors/)
* [Estudo de Caso da WebMotors](https://aws.amazon.com/pt/solutions/case-studies/Webmotors/)


## PaaS
### PaaS - Plataforma como Serviço
* PaaS é um modelo de serviço em nuvem que fornece um ambiente de desenvolvimento e implantação completo para aplicativos
* Permite que as empresas foquem no desenvolvimento de aplicativos enquanto o provedor de nuvem gerencia a infraestrutura subjacente
* A escalabilidade, flexibilidade e redução de custos são as principais vantagens do modelo PaaS
  

### Exemplos de Serviços de PaaS
* AWS RDS Databases é um serviço de gerenciamento de banco de dados relacional da Amazon Web Services
* Azure SQL Database é um serviço de banco de dados relacional totalmente gerenciado do Microsoft Azure
* Heroku é uma plataforma de desenvolvimento de aplicativos em nuvem que suporta várias linguagens de programação, incluindo Ruby, Node.js e Java


### Desenvolvimento e implantação de aplicativos em PaaS
* A PaaS oferece um ambiente completo de desenvolvimento e implantação de aplicativos
* Os desenvolvedores podem se concentrar apenas no desenvolvimento do aplicativo, enquanto a plataforma gerencia a infraestrutura subjacente
* O PaaS oferece suporte a várias linguagens de programação e ferramentas de desenvolvimento


## SaaS
### SaaS - Software como Serviço
* SaaS é um modelo de serviço em nuvem que fornece aplicativos prontos para uso pela internet
* As empresas podem reduzir custos ao evitar a necessidade de instalar aplicativos em computadores locais
* Os desafios do modelo SaaS incluem segurança, privacidade e conformidade


### Exemplos populares de aplicativos SaaS
* Microsoft 365 é uma suíte de aplicativos em nuvem que inclui Word, Excel, PowerPoint, Outlook e outros aplicativos
* Salesforce é uma plataforma de gerenciamento de relacionamento com o cliente (CRM) que é amplamente utilizada por empresas de todas as áreas


### Vantagens e desafios do uso de SaaS
* Vantagens do uso de SaaS incluem escalabilidade, flexibilidade e redução de custos
* Desafios do uso de SaaS incluem segurança, privacidade e conformidade regulatória


### Modelos de negócios em SaaS
* O modelo de assinatura é o mais comum em SaaS, onde os usuários pagam uma taxa mensal ou anual pelo acesso ao software
* Outros modelos de negócios em SaaS incluem freemium, onde o software é gratuito, mas recursos adicionais são pagos, e o modelo pay-per-use


### Segurança e conformidade em ambiente SaaS
* As empresas precisam garantir que seus dados sejam seguros ao usar aplicativos SaaS, pois eles são armazenado em nuvem
* Os provedores de SaaS geralmente oferecem recursos de segurança, como criptografia de dados, autenticação de usuários e acesso baseado em função, para garantir um ambiente seguro e confiável


## Estudos de caso
### Estratégias de escolha entre IaaS, PaaS e SaaS
* Compreender as diferenças entre IaaS, PaaS e SaaS
* Avaliar as necessidades de negócios e o custo-benefício de cada modelo
* Considerar as habilidades de TI da organização
* Analisar a escalabilidade e flexibilidade oferecidas por cada modelo
* Identificar os recursos de segurança e conformidade oferecidos por cada modelo


### Estudos de casos de empresas que utilizam diferentes modelos
* Netflix adota a nuvem pública e utiliza uma estratégia mista entre IaaS e PaaS
* Salesforce é uma exemplo de uso SaaS
* AWS EC2 é um exemplo de uso de IaaS
* A General Electric implementou uma estratégia de nuvem híbrida
* A aplicação do modelo de nuvem varia de acordo com as necessidades de negócios de cada organização


### Cenários típicos de uso para cada modelo
* IaaS é adequado para empresas que precisam de infraestrutura flexível e escalável
* PaaS é adequado para desenvolvedores que desejam criar aplicativos sem se preocupar com a infraestrutura
* SaaS é adequado para empresas que desejam usar software sem se preocupar com a infraestrutura ou manutenção
* Cada modelo tem suas vantagens e desvantagens, e a escolha depende das necessidades específicas de cada organização


### Consideração de custo e desempenho
* IaaS pode ser menso caro em comparação com outros modelos, mas pode exigir mais habilidades técnicas
* Paas pode oferecer economia de custos devido à automação da infraestrutura, mas pode ter menos flexibilidade do que IaaS
* SaaS pode oferecer economia de custos e flexibilidade, mas pode ser limitado em termos de personalização e integração
* A escolha do modelo de nuvem deve ser baseada em uma avaliação cuidadosa dos requisitos de custo e desempenho da organização


### Estudos de caso reais de empresas que migraram 100% para a nuvem
* A Nubank migrou seus serviços para a nuvem para acompanhar o rápido crescimento da empresa
* A Dow Jones usou a nuvem da AWS para reduzir o tempo de entrega de infraestrutura de semanas para minutos
* O Bank of America fechou uma parceria de modernização para a nuvem Microsoft, incluindo Office 365 SaaS e Azure IaaS e PaaS para modernização de datacenters.


### Desafios enfrentados e lições aprendidas
* A segurança e privacidade dos dados foram os principais desafios enfrentados pelas empresas que migraram para a nuvem
* A migração de aplicativos existentes é outro desafio, pois muitos aplicativos não foram projetados para serem executados em nuvem
* As empresas também precisaram investir em treinamento e desenvolvimento para garantir que seus funcionários tivessem as habilidades necessárias para trabalhar em um ambiente de nuvem


### Tendências futuras na computação em nuvem
* A inteligência artificial e a automação devem desempenhar um papel cada vez mais importante na computação em nuvem no futuro
* A nuvem híbrida, que combina nuvem pública e privada, deve se tornar cada vez mais popular à medida que as empresas buscam flexibilidade da nuvem pública e a segurança da nuvem privada
* A segurança da nuvem continuará a ser um foco importante para as empresas à medida que mais dados são armazenados na nuvem


## Conclusão
* A computação em nuvem é uma tendência importante no mundo da tecnologia e deve continuar a crescer nos próximos anos
* As empresas que desejam se manter competitivas devem considerar a migração para a nuvem para aproveitar seus benefícios em termos de escalabilidade, flexibilidade e redução de custos
* Existem muitos recursos disponíveis para empresas que desejam aprender mais sobre a computação em nuvem, incluindo cursos, certificações e consultores especializados
  

## Observações
* [Magalu Cloud](https://magalu.cloud/)
* [O que é PCI e quais são as normas dos cartões de crédito na internet?](https://www.ecommercebrasil.com.br/artigos/o-que-e-pci-e-quais-sao-as-normas-dos-cartoes-de-credito-na-internet)
* [Microsoft revela tour virtual em um de seus datacenters](https://news.microsoft.com/pt-br/microsoft-revela-tour-virtual-em-um-de-seus-datacenters/)


# Cloud Computing (IaaS, Paas, SaaS) II
* [Infraestrutura global do Azure](https://azure.microsoft.com/pt-br/explore/global-infrastructure)
* [Lógica do aplicativo e interface do usuário habilitada para IA](https://azure.microsoft.com/pt-br/solutions/modern-application-development#tabx53d2a906181c44c3956df6ff1960dfbf)


## Observações
* Flexible Server Azure
* [Qual é a diferença entre GPUs e CPUs?](https://aws.amazon.com/pt/compare/the-difference-between-gpus-cpus/)
