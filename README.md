# Devops I
## Introdução ao DevOps
### O que é DevOps?
"O DevOps é a união de **pessoas, processos e produtos** que tem como objetivo gerar valor continuamente para os usuários finais." Donovan Brown
* Plan -> Code -> Build -> Test -> Release -> Deploy -> Operate -> Monitor -> Plan ...


### História do DevOps
* Origens e evolução
* A convergência de desenvolvimento e operações
* A influência do Agile


### A Cultura DevOps
* Mentalidade de colaboração
* Quebrando silos
* Cultura de aprendizado e experimentação
* Adaptação de processos


### Princípios Chave do DevOps
* Culture - People > Process > tools
* Automation - Infrastructure as Code
* Lean - Focus on value and customer
* Measurement - Measure everything
* Sharing - Collaboration/Feedback


### Benefícios do DevOps
* Entregas mais rápidas
* Soluções mais confiáveis
* Maior colaboração entre equipes
* Melhor satisfação do cliente
* Velocidade em se adaptar ao mercado


### Boas Práticas populares no DevOps
* Gestão Ágil
* Estratégias de Branch
* Estratégias de Release
* Continuous Integration
* Continuous Deployment
* Continuous Delivery
* Monitoring
* Feedback
* IaC
* SecOps 


### Explorar o percurso do DevOps
* **Integração Contínua:** A Integração Contínua impulsiona a mesclagem contínua e o teste de código, o que leva à descoberta precoce de defeitos.
* **Entrega Contínua:** A Entrega Contínua de soluções de software para ambientes de produção e teste ajuda as organizações a corrigir rapidamente bugs e responder a requisitos de negócio em constante mudança.
* **Controle de Versão:** O Controle de Versão, geralmente com um repositório baseado em Git, permite que as equipes localizadas em qualquer lugar do mundo se comuniquem efetivamente durante as atividades de desenvolvimento diário
* **Agile/Lean:**
  * Planeje e isole o trabalho em sprints.
  * Gerencie a capacidade de equipe e ajude as equipes a se adaptarem rapidamente às necessidades de negócios em constante mudança.
  * Uma Definição de Concluído do DevOps é um software de trabalho que coleta telemetria em relação às metas de negócios pretendidas.
* **Monitoramento e Registro em Log:** Monitoramento e Registro de Log de aplicativos em execução
* **Nuvem:** Nuvens públicas e híbridas facilitaram o impossível
* **IaC (Infraestrutura como Código):** Permite a automação e a validação da criação e da desinstalação de ambientes para fornecer plataformas de hospedagem de aplicativos seguras e estáveis.
* **Microsserviços:** Isole casos de uso empresarial em pequenos serviços reutilizáveis que se comunicam por meio de contratos de interface.
* **Contêineres:** Contêineres são a próxima evolução da virtualização.


### Ferramentas populares no DevOps
* Azure DevOps
* Github
* Gitlab
* CircleCI e CD
* Jenkins
* Cheff
* Puppet
* Octopus
* Etc...


### Explorar práticas de desenvolvimento Agile
* **Abordagem em cascata:**
  * Define, analisa, constrói, testa e entrega
  * Requisitos difíceis de definir com precisão, que podem mudar ao longo do tempo, inclusive durante o desenvolvimento
  * Requer solicitações de alteração e custo adicional após a entrega
* **Abordagem Agile:**
  * Destaca constantemente o planejamento adaptável e a entrega antecipada com melhoria contínua
  * Os métodos de desenvolvimento usam como base lançamentos e iterações
  * No final de cada iteração, deve haver um código em funcionamento testado
  * Foco em resultados de curto prazo


### Explorar os princípios do desenvolvimento Agile
1. Atender ao cliente por meio de entrega antecipada e contínua de um software valioso
2. Aceitar requisitos em mudança
3. Fornecer software funcional com frequência
4. Trabalhar em conjunto durante todo o projeto
5. Criar projetos com auxílio de indivíduos motivados
6. Usar conversas presenciais
7. Avaliar o progresso por meio do software de trabalho
8. Os processos do Agile promovem o desenvolvimento sustentável
9. Atenção contínua à excelência técnica e ao bom design
10. Simplicidade - A arte de maximizar a quantidade de trabalho não realizado
11. Usar equipes auto-organizáveis
12. Refletir sobre como aprimorar a eficácia


### Identificar equipes de transformação
* Existem vários desafios ao criar equipes:
  * Disponibilidade da equipe
  * Interrupção dos procedimentos e processos atuais
* Para superar os desafios, cria uma equipe que seja:
  * Focada na transformação
  * Bem respeitada em suas áreas
  * Interna e externa ao negócio
Um projeto de transformação pode entrar em conflito com as necessidades contínuas dos negócios


### Como começar a implementar a cultura DevOps?
* Dê um foco nas pessoas
* Entenda o negócio
* Converse muito
* Não seja arrogante ou qualquer outra expressão popular
* Alinhe os processos
* Teste as soluções

### Explorar metas compartilhadas e definir linhas do tempo
* Os projetos devem ter um conjunto claramente definido de resultados mensuráveis, como:
  * Reduzir o tempo gasto na correção de bugs em 60%
  * Reduzir o tempo gasto com trabalho não planejado em 70%
  * Reduzir a necessidade de horas extras da equipe para, no máximo, 10% do tempo de trabalho total
  * Remover todos os patches diretos de sistemas de produção
Um dos objetivos principais do DevOps é fornecer um valor maior para o cliente, portanto, os resultados devem ter foco no valor para o cliente.

* Metas mensuráveis devem ter prazos desafiadores, mas possíveis
* As linhas do tempo devem ser uma série constante de metas de curto prazo, cada uma clara e mensurável
* Linhas do tempo mais curtas têm vantagens:
  * Facilidade para alterar planos ou prioridades quando necessário
  * Redução do atraso entre a realização do trabalho e o recebimento de comentários
  * Facilidade para manter o suporte organizacional quando os resultados positivos são claros


### Desafio na Implementação
* Mudança de mentalidade
* Necessidade de treinamento
* Resistência à mudança


### Mitos sobre DevOps
* DevOps é Automação de Pipelines
* DevOps é resolver problema de Deploy
* DevOps é troubleshoot em produção
* DevOps é transportar toda a infraestrutura como código, vulgo IaC
* DevOps é contratar uma ferramenta top do mercado


## Escolhendo o projeto adequado
### Explorar projetos Greenfield e Brownfield
* Projetos de software Greenfield são desenvolvidos em um ambiente totalmente novo
* Os projetos de software Brownfield são desenvolvidos na presença imediata de aplicativos/sistemas de software já existentes


### Decidir quando usar projetos Greenfield e Brownfield
* **Projetos Greenfield:**
  * Parece ser um ponto de partida mais fácil
  * Uma tela em branco oferece a oportunidade de implementar tudo como você deseja
* **Projetos Brownfield:**
  * Vem com a bagagem de bases de código e equipes já existentes e, muitas vezes, uma grande quantidade de dívida técnica
  * O gasto de tempo com a manutenção de aplicativos Brownfield já existentes limita a capacidade de trabalhar em novos códigos
Há um equívoco comum de que o DevOps é melhor para projetos Greenfield do que projetos Brownfield. Esse não é o caso.


### Decidir quando usar sistemas de registro em relação a sistemas de envolvimento
* **Sistema de registro:**
  * Destaque na precisão e na segurança
  * Fornece a verdade sobre os elementos de dados
  * Historicamente evoluem de forma lenta e cuidadosa
* **Sistemas de participação:**
  * São mais exploratórios
  * Usam a experimentação para resolver novos problemas
  * São modificados regularmente
  * Priorizam alterações rápidas em relação a garantir que as alterações estejam corretas
Ambos os tipos de sistemas são importantes


### Identificar grupos para minimizar a resistência inicial
* **Diferentes tipos de membros da equipe:**
  * **Canários** testam voluntariamente características avançadas
  * **Os usuários pioneiros** avaliam voluntariamente as versões prévias
  * **Usuários** consomem produtos depois dos canário e dos usuário pioneiros
* **Metas de aprimoramentos ideias:**
  * Podem ser usadas para obter ganhos antecipados
  * São pequenas o suficiente para ser alcançadas em um prazo razoável
  * Trazem benefícios significativos o suficiente para serem evidentes para a organização


### Identificar métricas de projeto e KPIs (Indicadores Chave de Desempenho)
* **Resultados mais rápidos:** frequência, velocidade e tamanho da implantação, além do prazo de entrega
* **Eficiência:** proporção entre servidor e administrador, proporção de funcionários e clientes, uso e desempenho de aplicativos
* **Qualidade e segurança:** taxas de falha de implantação, taxas de falha de aplicativos, tempo médio de recuperação, taxas de relatórios de bugs, taxas de aprovação em testes, taxa de escape de defeitos, disponibilidade, cumprimento de SLA (Contrato de Nível de Serviço) e tempo médio de detecção
* **Cultura:** moral dos funcionário e taxas de retenção
As metas devem ser específicas, mensuráveis e com prazo determinado


## Estruturas de equipe
### Definir a estrutura da organização para práticas Agile
* As estruturas **horizontais** dividem as equipes com a arquitetura do software
* Equipes **verticais** abrangem a arquitetura e são alinhadas aos resultados do produto. É possível dimensioná-las adicionando equipes.
Ficou comprovado que as equipes verticais fornecem resultados melhores em projetos do Agile


### Explorar os membros ideias da equipe de DevOps
* Acreditam que é necessário fazer mudanças e demonstraram a capacidade de inovar
* São respeitados e têm um amplo conhecimento da organização e de suas operações
* O ideal é que eles já acreditem que as práticas de DevOps são necessárias
* Muitas equipes contratam instrutores ou mentores externos para Agile
* Instrutores do Agile têm habilidades de ensino e orientação
* Os instrutores do Agile devem ser orientadores e consultores
* Alguns instrutores são especialistas técnicos
* Alguns instrutores focam em processos do Agile
A expectativa é que os membros da equipe aprendam uns com os outros à medida que trabalham e adquirem habilidades 


### Habilitar a colaboração na equipe e entre equipes
* **Mudanças culturais:** espaços de trabalho mais abertos, etiqueta de reunião, terceirização e comunicação aprimorada
* **Equipes multifuncionais:** colaboração com outras pessoas, diversidade de opiniões, recompensas pelo comportamento coletivo
* **Ferramentas de colaboração:** Slack, Teams, Asana, Glip, JIRA


### Selecionar ferramentas e processos para práticas Agile
* Muitas vezes, as ferramentas podem melhorar os resultados alcançados
* Ferramentas físicas, como quadros brancos, catões de índice e notas adesivas
* Ferramentas de gerenciamento de projetos, como quadros Kanban para planejamento, monitoramento e visualização
* Ferramentas de gravação de tela para registrar bugs, criar instruções passo a passo e demonstrações


## Escolhendo ferramentas de DevOps
### O que é o Azure DevOps?
* **Azure Boards:** planejamento do Agile, acompanhamento de itens de trabalho, visualização e ferramenta de relatório
* **Azure Pipeline:** uma plataforma de CI/CD de linguagem, plataforma e nuvem agnóstica com suporte para contêineres ou Kubernetes
* **Azure Repos:** oferece repositório git privados hospedados em nuvem
* **Azure Artifacts:** oferece gerenciamento de pacotes integrados com suporte para os feeds de pacote Maven, npm, Python e NuGet de fontes públicas ou privadas
* **Azure Test Plans:** oferece uma solução integrada de testes planejados e exploratórios


### O que é o GitHub?
* **Codespaces:** fornece ambientes de desenvolvimento colaborativo hospedados em nuvem
* **Repos:** fornece repositórios git locais e hospedados em nuvem para projetos públicos e privados
* **Ações:** cria fluxos de trabalho de automação com variáveis de ambiente e scripts personalizados
* **Pacotes:** facilita a integração com vário pacotes já existente e repositórios de código aberto
* **Segurança:** analisa as vulnerabilidades de código e identificação no início do ciclo de desenvolvimento


## Planejamento ágil com projetos do GitHub e o Azure Boards
### Introdução aos painéis de projetos e projetos do GitHub
* Os quadros de projeto de **GitHub Projects** são compostos por problemas, solicitações de pull e anotações categorizadas como cartões que você pode arrastar e soltar nas colunas escolhidas
* Os GitHub Projects são uma versão nova, personalizável e flexível das ferramentas de projetos para planejar e acompanhar o trabalho no GitHub.


### Introdução ao Azure Boards
Processos do Agile, Scrum e Kanban por padrão
* Acompanhe o trabalho, os problemas e os defeitos de códigos associados ao projeto


### Vincular GitHub a Azure Boards
* O Aplicativo Azure Boards vincula itens de trabalho a commits, solicitações de pull e problemas
* Use Azure Boards para planejar e acompanhar seu trabalho e o GitHub como controle do código-fonte para desenvolvimento de software
* Autentique-se ao GitHub usando um nome de usuário/senha ou um PAT (token de acesso pessoal).


### Configurar projetos do GitHub
* Você pode usar um modelo de quadro de projeto para criar um quadro de projeto com automação já configurada
* Você também pode copiar um quadro de projeto para reutilizar as personalizações dele em projetos semelhantes
* Você pode vincular até 25 repositórios a um de sua organização ou pertencente ao usuário
* Depois de criar seu quadro de projeto, você pode adicionar problemas, solicitações pull e observações a ele


### Gerenciar o trabalho com quadros de projeto do GitHub
* Controle entregas de projetos
* Defina para qualquer período
* Inclua interrupções
* Datas de liberação
* Iterações para planejar os próximos trabalhos


### Personalizar exibições de projetos
Organize as informações alterando o layout, agrupando, classificando e filtrando seu trabalho
* Use paleta de comandos:
  * Troca de layout: Tabela
  * Mostrar: Marcos
  * Classificar por: Destinatários, asc
  * Agrupar por: Status
  * Campo coluna por: Status
  * Filtrar por: Status
  * Excluir exibição


### Colaborar usando discussões em equipe
* As discussões do GitHub podem ajudar a fazer sua equipe planejar em conjunto, atualizar umas às outras ou falar sobre qualquer tópico
* Conversas que abrangem projetos ou repositórios (problemas, solicitações de pull etc.)


## Introdução ao controle do código-fonte
### Explorar práticas fundamentais de DevOps
TODO: fases das práticas


### O que é controle de código-fonte?
* Um sistema de controle do código-fonte permite que os desenvolvedores colaborem no código e acompanhem as alterações. Use o controle de versão para salvar seu trabalho e coordenar as alterações de código em sua equipe
* O sistema de controle de versão salva um instantâneo de seus arquivos (histórico) para que você possa revisar e até mesmo reverter para qualquer versão do código com facilidade
* O controle do código-fonte protege o código-fonte não só contra catástrofes, mas também contra uma degradação casual provocada por erros humanos e consequências não intencionais


### Explorar os benefícios do controle do código-fonte
* Criar fluxos de trabalho
* Trabalhar com versões
* Colaboração
* Mantém o histórico de alterações
* Automatizar tarefas


### Explorar melhores práticas para o controle do código-fonte
* Faça alterações pequenas
* Não envie arquivos pessoais
* Atualize com frequência e logo antes do envio para evitar conflitos de mesclagem
* Verifique a alteração do código antes de enviá-la para um repositório. Garanta que a compilação e os testes sejam aprovados
* Preste muita atenção nas mensagens commit, pois elas informarão por que uma alteração foi feita
* Vincular alterações feitas no código a itens de trabalho
* Não importa seu histórico ou suas preferências, seja um bom parceiro de equipa e siga as convenções e os fluxo de trabalho acordados


## Sistemas de controle do código-fonte
### Entender o controle ds código-fonte centralizado
* Pontos fortes
  * Escalonamento facilitado para bases de código muito grandes
  * Controle de permissões granular
  * Permite o monitoramento do uso
  * Permitir o bloqueio de arquivo exclusivo
* Melhor usado para
  * Bases de código grandes integradas
  * Auditoria e controle de acesso até o nível de arquivo
  * Tipos de arquivo difíceis de mesclar
Há uma única cópia central do seu projeto, e os programadores confirmam as alterações na cópia central
Os sistemas de controle do código-fonte centralizados comuns são TFVC, CVS, Subversion (ou SVN) e Perforce


### Entender o controle ds código-fonte distribuído
* Pontos fortes
  * Suporte entre plataformas
  * Um modelo de revisão de código compatível com código aberto por meio de solicitação de pull
  * Suporte offline completo
  * Histórico portátil
  * Uma base de usuários motivada e em crescimento
* Melhor usado para
  * Tamanho menor (em bytes) e bases de código modulares
  * Evolução por meio de código aberto
  * Equipes altamente distribuídas
  * Equipes trabalhando em multiplataformas
  * Bases de código Greenfield
Cada desenvolvedor clona uma cópia de um repositório e tem o histórico completo do projeto
Os sistemas comuns de controle de código-fonte distribuídos são Mercurial, Git e Bazaar


### Explorar o Git e o Controle de Versão do Team Foundation
* GIT: sistema de controle de código-fonte distribuído. Cada desenvolvedor tem uma cópia do repositório do código-fonte em seu sistema de desenvolvimento
* TFVC: 
  * sistema centralizado de controle de código-fonte
  * os membros da equipe tem apenas uma versão de cada arquivo em seus computadores de desenvolvimento
  * no modelo **workspaces do servidor**, antes de fazer alterações, os membros da equipe fazem check-out publicamente dos arquivos
  * no modelo **workspaces locais**, cada membro da equipe usa uma cópia da versão mais recente da base de código para trabalhar offline conforme necessário


### Examinar e escolher o Git
* Branches de recursos
* Desenvolvimento distribuído
* Solicitações pull
* Comunidade
* Ciclo de lançamento


### Entender as objeções ao uso do Git
* **Substituindo o histórico:** se usado incorretamente, pode levar a conflitos
* **Arquivos grandes:** o Git funciona melhor com repositórios pequenos e que não contenham arquivos grandes (ou binários). Considere usar suporte do Git LFS
* **Curva de aprendizado:** algum treinamento e instrução serão necessários. Os desenvolvedores já existentes talvez precisem ser retreinados
* **Discussão:** quais objeções você tem?


## Azure Repos e GitHub
### Introdução ao Azure Repos
* **Conjunto de ferramentas de controle de versão para gerenciar seu código:**
  * Totalmente integrado com outros recursos do Azure DevOps
  * Pode se conectar a partir de ambientes de desenvolvimento comuns
  * Gerenciamento baseado em políticas para proteger branches
  * Oferece dois estilos de controle de versão:
    * **Git:** controle de versão distribuído
    * **TFVC (controle de versão do Team Foundation):** controle de versão centralizado


### Introdução ao GitHub
* Maior comunidade de código aberto
* Recursos do GitHub:
  * Automatize do código para a nuvem
  * Proteção do software em conjunto
  * Análise de código perfeita
  * Código e documentação em um só lugar
  * Coordenada
  * Gerenciar equipes


### Migrar do TFVC para Git
* Importação de ramificação única
  * Sincronização completa (git-tfs)

* Migração da dica:
  * somente a versão mais recente do código
  * o histórico permanece no servidor antigo
* Migração com histórico:
  * Tentar imitar o histórico do Git
* Recomendado migrar a dica porque:
  * O histórico é armazenado de modo diferente: o TFVC armazena conjuntos de alterações, o Git armazena instantâneos do repositório
  * As branches são armazenadas de modo diferente: pastas de branches TFVC, Git branches para todo o repositório


### Desenvolver online com GitHub Codespaces
Ambiente de desenvolvimento com base em nuvem hospedado pelo GitHub
* evita problemas com hardwares/softwares antigos
* altamente portátil
* proteção contra proliferação de propriedade intelectual
* com base no Visual Studio Code
* trabalhar usando PCs, tables e Chromebooks
* Conectar-se ao Codespaces no Visual Studio Code



## Observações
* [Visão geral do gerenciamento do ciclo de vida do aplicativo com a Microsoft Power Platform](https://learn.microsoft.com/pt-br/power-platform/alm/overview-alm)
* [Manual de DevOps: como obter agilidade, confiabilidade e segurança em organizações tecnológicas](https://a.co/d/8Cg6cRG)

