# Palestra: Blockchain e Criptomoedas - Jó Ueyama
Surgiu em 2008

## O que é blockchain?
* Blockchain é uma base de dados.
* É tirar uma entidade centralizadora, isto é, **descentralizadora** e **autônoma**, ou seja, eu posso comprar e vender criptomoeda em qualquer momento. Não há alguém definindo horário de funcionamento ou operando alguma função para seu fucnionamento.
* Exemplo: para fazer um pix ou uma transferência é necessário um entidade central que é o banco. Já com a blockchain, tiramos o elemento central e as bases são replicadas (P2P). Sendo assim, as informações são:
  * distribuídas para várias mineiradoras e entidades.
  * atualizadas de uma base para outra, mantendo a mesma versão para todas as bases da rede. Desta forma, é difícil fazer uma operação fraudulenta, pois isso irá refletir em todas as bases de dados.
* A descentralização existe, pois não existe uma terceira parte confiável.
  
Em resumo:
* é uma base de dados
* armazena dados usando uma estrutura chamada blocos
* BD armazaena dados em tabelas

### Demo da Blockchain
[Blockchain](https://andersbrownworth.com/blockchain)
Na demo, se ficar vermelha, significa que ela foi alterada, ou seja, o bloco ficou sujo e, para evitar isso, precisa fazer o processo de **mineração**. A mineração é o tempo gasto para identificar um hash que corresponda a cadeia.
    **Block:** número do bloco
    **Nonce:** A quantidade de tentativas para encontrar um hash com o padrão dos quatro primeiro algarismos. Ou seja, se eu fizer uma modificação no bloco, o padrão é perdido e suja a cadeia. Toda alteração gera um novo padrão de hash.
    **Data:** dados gravados no bloco
    **Prev:** identificação do bloco anterior
    **Hash:** identificação do bloco atual

## Por que blockchain?
CBDC: Real Digital - está sendo criada em cima da blockchain
Metaverso
NFT

### Custo
* Serviços de transferência de valores
* Impostos envolvidos

### Tempo
Exemplo dado é que o Bitcoin também é lento, porém a blockchain do Bitcoin não foi feito para pequenas transações. Por exemplo, processar um bitcoin pode levar 10 minutos e isso é incoerente ao realizar o pagamento de uma pizza ou em um supermercado. A blockchain de Bitcoin foi feita para investimentos.

Agora com as moedas reais:
* Alto tempo de processamento
* Transferência internacionais levam dias
* Lentidão

### Segurança
* Todos os participantes seguem um padrão de segurança

* Unimed, Lojas Americanas, Submarino sofreram ataques
* Enquanto outra mais seguras não
* Falta um padrão de segurança

* Segurança não fica atrelada a um servidor centralizado

* Mecanismos de comunicação segura

### Tolerância a falhas
* A base de dados é replicada, isto é, "espelhada"
* Atualização constante
* A replicação protege o ledger das(os):
  * Falhas
  * Ataques
* Seria muito útil para sistemas de saúde como o Connect SUS
  * Ficou inoperante por um período em virtude de falhas
  * Dados da vacina atualizados e disponíveis "world-wide"

## Tipos de implementação
* Público - **Qualquer um pode entrar** e contruibuir na rede: Airbnb, Uber
  * Exemplo: Bitcoin, Ethereum
* Privado - **Participantes devem ser convidados** para ser membro da rede
  * Exemplo: Blockchain de uma organização (cadeia de suprimentos), Enterprise Ethereum
* Permissionado - **Uma mistura das duas:** o participante pode ingressar na rede após a verificação e podem contribuir para certas atividades posteriormente
  * Exemplo: [Ripple](https://ripple.com/)

### Distributed Ledger Technology (DLT) e Blockchain
[DLT e blockchain: entenda a diferença](https://conteudo.beegin.com.br/dlt-e-blockchain/)
* Analogia com a classe e o objeto

DLT é como se fosse a classe
* DLT é simplesmente uma **base descentralizada** que é gerenciada por **vários participantes** em vários **nodos**
  * Exemplo: Blockchain do Bitcoin, Blockchain do Ethereum, Tangle

É como se fosse um objeto
* Blockchain é uma implementação de DLT
  * Estrutura do bloco
  * Sequência do bloco
  * Protocolo de consenso

Outra analogia: o Gol é uma implementação de Carro.
DLT é o conceito

### Blockchain é descentralizado
Obs: no distribuído há um controlador que controla vários nodos
O descentralizado os nodos compartilham e atualizam uma a outra.

## Primeira aplicação da blockchain: criptomoeda
[Moeda Solana](https://coinmarketcap.com/pt-br/currencies/solana/): a Google tem investido nessa criptomoeda.

* Uma discussão sobre o futuro: 
  * Life after Google: The Fall of Big Data and the Rise of the Blockchain Economy
    * Quer dizer que o centralizado vai acabar

## Principais componentes:
### Funções Hash

Input             Process             Output
Cat.jpg       ->  Cryptographic   ->  dee6a5d375827436ee4b47a...
1.21 MB           hash function       a hash 32 bytes

#### O que é uma função hash?
* Funciona como uma **impressão digital**
* **Difícil** haver **duas pessoas com a mesma digital**
* Assim como uma pessoa, um documento pode ter uma impressão
  * um vídeo, uma transação e assim por diante

Arbitrary Length Input -> Hash Function -> Fixed Length Output (n-bit)

Não importa o tamanho do objeto, o hash é o parâmetro de identificação
Podemos ter um arquivo gigante e ter uma hash desse arquivo. Se o arquivo for modificado a hash terá um efeito avalanche e que ficará visível que ocorreu essa mudança.

#### Estrutura do bloco blockchain com Hash
* Markie root contém o hash do bloco
* O hash é quem **assegura a imutabilidade** do bloco
* **Efeito avalanche**
* Exemplo:
  * Rafael Peinado: d19a034d0c08bb3d592edb10c5a85260f261e848d6a5f3803404a9dd85db1dc7
  * Rafa Peinado: f885824ae71abec45a5252a3435c04a527af7a0a051e96b151c7b5bd0e57567d

#### Demo da Função Hash
[SHA256 online hash function](https://emn178.github.io/online-tools/sha256.html)

### Livro-contábil imutável
**Ledger tradicional**
Comprar uma casa -> escritura do imóvel -> registrado no cartório
Se a escritura for hackeada, não terá como provar que a casa é da pessoa

Por outro lado, pelo blockchain, se o livro for hackeado, terá que gerar todos os hashes para que a alteração possa funcionar

* No cenário real: mudança de títulos residenciais acima de GBP40K
* Algo em torno de 100 transações por hora
* Suscetível a erros e fraudes

### Mineração
* É como cadeados com segredo
  * É difícil de adivinhar
  * Toma bastante tempo para testar
  * 10.000 tentativas com segredo de 4 dígitos
  * Ganha quem tem maior poder computacional
    * O mesmo ocorre com a mineração
  
  * Mas por outro lado é fácil de testar o segredo desde que ele tenha sido fornecido
    * Trabalho de nodos pares na blockchain

#### Mining systems
Começou com processadores normais
  * Quatro plataformas de hardware: CPU, GPU, FPGA e um ASIC

### Protocolo de consenso
* É fácil atingir um acordo em cliente/servidor
  * O servidor "manda" e detém as regras
  * O cliente confia no servidor
  * P.ex., o cliente confia no Banco do Brasil
* Mas em ambiente sem um intermediário confiável?
* Ambiente com nodos que podem estar defeituosos
* Ambiente carece de regras para se chegar a um consenso

* **Protocolo que dita o acordo entre os nodos não-confiáveis sobre os dados na blockchain**
* P.ex., quem vai criar o novo bloco?

#### Por que é difícil atacar o Bitcoin?
[ICAI CONCEPT PAPER ON BLOCKCHAIN TECHNOLOGY ADOPTION TRENDS AND IMPLICATIONS](https://taxguru.in/chartered-accountant/blockchain-technology-adoption-trends-implications-accountancy-profession.html)
[Why You Can't Cheat at Bitcoin](https://taxguru.in/wp-content/uploads/2018/09/Why-you-cant-Cheat.png)

#### Blockchain é para todos os sistemas?
Ver imagem 52:38
* Do you need a Blockchain?
  * **Database** needed?
  * There are multiple writers
  * Writers are **unknown** or untrusted or have conflicting interests
  * **Can't rely** on trusted **3rd party**
You might need a blockchain
  * Access control not needed
  * **Immutability** over efficiency
  * **Public transactions** ok

  * Suitable blockchain type:
    * Public
    * Consortium
    * Private
      * Multiple-party consensus

