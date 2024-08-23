# Trabalho 1 – Laboratório de Engenharia de Software I (2024/01) - CEFET-MG
Neste projeto da matéria de Laboratório de Engenharia de Software I, ministrada pela professor Eduardo Costa, nosso grupo desenvolveu um relatório prático no GitHub com o tema " Exemplo prático de uso do framework open source Apache Spark". Dentre os usos do Spark, como processamento de dados em grande escala com módulos integrados para SQL, streaming, machine learning e processamento de gráficos, foi escolhido como foco o tópico "Processamento de Dados com Apache Spark". 

## Integrantes do Grupo 3
**Arthur Soares Higino / 20213012893** 

**Luiz Carlos dos Santos Júnior / 20213008611**

**Vitório Marcos Abreu Rodrigues / 20193023089**

# Processamento de Dados com Apache Spark

Este repositório contém recursos e exemplos relacionados ao processamento de dados com o Apache Spark. O Apache Spark é uma poderosa estrutura de código aberto para processamento de dados em grande escala e é amplamente utilizado para análise de big data, aprendizado de máquina e processamento em tempo real.

## Conteúdo

- [Visão Geral do Apache Spark](#visão-geral-do-apache-spark)
- [Processo de Instalação](#instalação)
- [Exemplos](#exemplos)
- [Referências](#referências)
- [Conclusão](#conclusão)

## Visão Geral do Apache Spark

O Apache Spark é uma notável estrutura de processamento de dados distribuída, altamente valorizada por sua eficiência no tratamento de conjuntos de dados de grande escala de maneira simultânea. Sua flexibilidade é um dos principais atrativos, uma vez que oferece suporte a diversas linguagens de programação, incluindo Scala, Java, Python e R. Essa diversidade de linguagens torna o Apache Spark uma escolha amplamente preferida entre cientistas de dados, engenheiros de big data e profissionais de análise, pois permite que eles utilizem a linguagem que melhor se adequa às suas necessidades e competências individuais. 

A capacidade do Apache Spark de processar dados em paralelo em uma arquitetura distribuída é crucial para lidar com as crescentes demandas de dados da era moderna. Isso significa que ele pode dividir tarefas de processamento em várias unidades independentes, executando-as em vários nós ou máquinas, acelerando significativamente a análise e o processamento de conjuntos de dados massivos. 

Além disso, o Apache Spark oferece uma ampla gama de bibliotecas e ferramentas integradas que permitem a análise de dados, o aprendizado de máquina, o processamento em tempo real e a integração perfeita com outras tecnologias, como Hadoop e sistemas de armazenamento distribuído. Essas características tornam o Apache Spark uma escolha poderosa para empresas e organizações que desejam extrair insights valiosos de seus dados em um ambiente escalável e eficiente. Sua popularidade contínua e sua comunidade ativa de desenvolvedores contribuem para a evolução e aprimoramento constantes dessa estrutura.

## Instalação

A instalação do Apache Spark pode ser realizada em várias plataformas. Abaixo, fornecemos instruções básicas para a instalação em sistemas operacionais, como Windows e Linux. Certifique-se de verificar a [documentação oficial do Apache Spark](https://spark.apache.org/documentation.html) para obter instruções detalhadas e informações atualizadas.

### Pré-requisitos

Antes de instalar o Apache Spark, certifique-se de que você tenha o seguinte instalado em seu sistema:

1. **Java**: O Apache Spark requer o Java 8 ou superior. Você pode verificar a versão Java instalada com o seguinte comando:

   ```
   java -version

Se o Java não estiver instalado ou estiver em uma versão anterior, siga as etapas abaixo para instalá-lo no seu sistema operacional.

### Windows

1. Acesse o site oficial da Oracle Java em [Oracle Java Downloads](https://www.oracle.com/java/technologies/javase-downloads.html).
2. Faça o download do instalador Java adequado para o seu sistema (32 bits ou 64 bits).
3. Execute o instalador baixado e siga as instruções na tela para concluir a instalação.

### Linux

Abra um terminal e execute os seguintes comandos:

```
sudo apt update
sudo apt install default-jre
sudo apt install default-jdk
```

### Download JDK

Além do Java, você precisrá realizar o download do JDK (Java Development Kit) 

#### Windows:

1. Acesse o site oficial da Oracle Java em [Oracle Java Downloads](https://www.oracle.com/java/technologies/javase-downloads.html).
2. Procure a seção "Oracle JDK" e clique no botão "Download" para o JDK correspondente à sua arquitetura (32 bits ou 64 bits).
3. Você será redirecionado para a página de termos e condições. Aceite os termos e clique em "Download" novamente.
4. O download do instalador do JDK será iniciado. Execute o instalador baixado e siga as instruções na tela para concluir a instalação.

#### Linux (Ubuntu):

No Ubuntu, você pode instalar o OpenJDK, que é uma implementação de código aberto do Java. Para instalar o OpenJDK 8, siga as etapas abaixo:

1. Abra um terminal e execute o seguinte comando para instalar o OpenJDK 8:

```shell
sudo apt update
sudo apt install openjdk-8-jdk
```

2. Após a instalação, você pode verificar a versão do Java com o seguinte comando:

Agora, com o JDK devidamente instalado em seu sistema, você pode prosseguir com a instalação e configuração do Apache Spark e seguir as etapas do README anteriormente fornecido para instalar o Python com o Jupyter Notebook e a biblioteca pyshark. Certifique-se de configurar as variáveis de ambiente necessárias para o JDK, como a variável `JAVA_HOME`.

### Instalação do Python com Jupyter Notebook

2. Após a instalação do Apache Spark, será necessário baixar o python para conseguir utilizar a biblioteca pyshark no seu computador. Certifique-se de que você tenha o Python instalado em seu sistema. Você pode verificar se o Python está instalado executando o seguinte comando no seu terminal:

```shell
python --version
```

Se o Python não estiver instalado, siga as etapas apropriadas para o seu sistema operacional:

#### Windows

1. Baixe o instalador Python mais recente para Windows em [python.org/downloads](https://www.python.org/downloads/windows/).

2. Execute o instalador baixado e siga as instruções na tela. Certifique-se de marcar a opção "Add Python to PATH" durante a instalação.

#### Linux (Ubuntu)

O Python é pré-instalado na maioria das distribuições Linux. No entanto, você pode instalar o Python 3 com o seguinte comando:

```shell
sudo apt update
sudo apt install python3
```

#### Linux (Fedora)

Para instalar o Python 3 no Fedora, use o seguinte comando:

```shell
sudo dnf install python3
```

Após a instalação do Python, você pode instalar o Jupyter Notebook:

1. Abra um terminal e execute o seguinte comando para instalar o Jupyter Notebook:

```shell
pip install jupyter
```

2. Depois que o Jupyter Notebook estiver instalado, você pode iniciar o servidor do Jupyter Notebook executando o seguinte comando:

```shell
jupyter notebook
```

Isso abrirá o Jupyter Notebook em seu navegador padrão. Você pode criar um novo notebook Python e executar comandos Python nele.

### Instalação do pyshark

Agora que você tem o Python e o Jupyter Notebook instalados, você pode instalar o pyshark, que é uma biblioteca Python para análise de tráfego de rede.

1. Abra um terminal ou o prompt de comando.

2. Execute o seguinte comando para instalar o pyshark usando o pip:

```shell
pip install pyshark
```

Após a conclusão da instalação, você pode usar o pyshark em seu ambiente Jupyter Notebook para analisar dados de tráfego de rede.

Lembre-se de que você deve ter o Apache Spark e o arquivo CSV "dados.csv" configurados e prontos, como mencionado no início do README, para executar o código original com sucesso.

### Instalação do numpy
Para manipular arrays multidimensionais e funções matemáticas de alto desempenho para trabalhar com esses arrays, os quais armazenam os dados a manipular, é comum o uso da biblioteca numpy.
   ```
   pip install numpy
   ```

### Download do Apache Spark

1. Acesse a [página de downloads do Apache Spark](https://spark.apache.org/downloads.html).
2. Selecione a versão desejada e o tipo de pacote. Geralmente, você pode escolher entre um arquivo `.tgz` ou `.zip`.
3. Baixe o arquivo para o seu sistema local.

### Instalação do Apache Spark
   
1. Extraia o arquivo baixado em um diretório de sua escolha. Você pode usar um comando como este:

   ```
   tar -xzf spark-3.2.0-bin-hadoop3.2.tgz
   ```
Certifique-se de substituir "spark-3.2.0-bin-hadoop3.2.tgz" pelo nome do arquivo que você baixou.  

2. Defina a variável de ambiente `SPARK_HOME` apontando para o diretório do Spark e adicione o diretório `bin` ao seu `PATH`. Você pode fazer isso adicionando as seguintes linhas ao seu arquivo `.bashrc`, `.bash_profile` ou `.zshrc`, dependendo do seu shell:

   ```
   export SPARK_HOME=/caminho/para/o/diretório/spark-3.2.0
   export PATH=$SPARK_HOME/bin:$PATH
   ```
Lembre-se de substituir "/caminho/para/o/diretório" pelo caminho real para o diretório onde o Spark foi extraído.

3. Após salvar as alterações no seu arquivo de perfil, atualize as variáveis de ambiente com o comando:

   ```
   source ~/.bashrc  # ou source ~/.bash_profile, dependendo do seu arquivo de perfil
   ```
4. O Apache Spark agora deve estar instalado e configurado em seu sistema. Para verificar a instalação, você pode executar o seguinte comando para iniciar o shell interativo do Spark:

   ```
   spark-shell
    ```
Isso iniciará o shell interativo do Spark e indicará que a instalação foi bem-sucedida.


## Exemplos

### Exemplo 1: Processamento de Lote de Dados

1. **Criar arquivo de dados:**
Faça um arquivo chamado exemplo.txt com algumas linhas de dados. Exemplo:

   ```
   1,Arthur
   2,Luiz
   3,Vitorio
   4,Eduardo
   ```
2. **Criar código Spark:**
Crie um arquivo Python (por exemplo, `lote.py`) com o seguinte código para processar o arquivo de dados:

   ```python
   from pyspark.sql import SparkSession
   
   # Criando uma sessão Spark
   sessao_spark = SparkSession.builder.appName("ProcessamentoEmLote").getOrCreate()
   
   # Carregando o arquivo previamente criado
   dados = sessao_spark.read.csv("exemplo.txt", header=False, inferSchema=True)
   
   # Realizando uma operação simples, como contar o número de linhas
   numero_linhas = dados.count()
   print(f"Quantidade total de linhas: {numero_linhas}")
   
   # Finalizando a sessão Spark
   sessao_spark.stop()

   
   ```
3. **Executar o Código:**
Abra um terminal e execute o código Python:

   ```
   $ spark-submit lote.py
   <output> - Quantidade total de linhas: 4
   ```
OBS: exemplo.txt precisa estar no mesmo diretório de lote.py.

### Exemplo 2: Processamento em Tempo Real de Dados

1. **Escrever o código Spark Streaming:**
Crie um arquivo Python (por exemplo, `tempo_real.py`) com o seguinte código para processar dados em tempo real:

   ```python
   from pyspark.streaming import StreamingContext
   
   # Configurando o StreamingContext com um intervalo de 1 segundo
   contexto_streaming = StreamingContext(sparkContext, 1)
   
   # Criando um DStream a partir de uma fonte de dados em tempo real, como Kafka ou sockets
   # Para este exemplo, utilizamos uma fonte de teste
   fluxo_dados = contexto_streaming.socketTextStream("localhost", 9999)
   
   # Realizando uma operação simples, como contagem de palavras
   contagem_palavras = fluxo_dados.flatMap(lambda linha: linha.split(" ")).countByValue()
   
   # Exibindo os resultados em tempo real
   contagem_palavras.pprint()
   
   # Iniciando o contexto de streaming
   contexto_streaming.start()
   
   # Mantendo a aplicação em execução até que seja interrompida (Ctrl+C para parar)
   contexto_streaming.awaitTermination()

   ```
2. **Iniciar a Fonte de Dados em Tempo Real:**
Execute em outro terminar uma fonte de dados em tempo real, através do comando `nc` (Netcat):

   ```
   $ nc -lk 9999
   ```
   
4. **Executar o Código Spark Streaming:**
No terminal onde você escreveu o código Spark Streaming, execute o código:

   ```
   $ spark-submit tempo_real.py

   ```
Com isso o texto digitado com `nc` será processado em tempo real pelo Spark.

### Exemplo 3: Integração com Spark SQL e Spark MLlib

1. **Escrever o código Spark SQL e MLlib:**
Crie um arquivo Python (ex: `sql_mllib.py`) com o código para realizar uma tarefa de análise de dados utilizando Spark SQL em conjunto com MLlib:

   ```python
   from pyspark.sql import SparkSession
   from pyspark.ml.feature import VectorAssembler
   from pyspark.ml.regression import LinearRegression
   
   # Iniciando uma sessão Spark
   sessao_spark = SparkSession.builder.appName("SparkMLlib").getOrCreate()
   
   # Carregando um arquivo CSV como DataFrame utilizando Spark SQL
   dados = sessao_spark.read.csv("dados.csv", header=True, inferSchema=True)
   
   # Preparando os dados para treinar o modelo de regressão linear
   colunas_caracteristicas = dados.columns[:-1]
   montador_vetores = VectorAssembler(inputCols=colunas_caracteristicas, outputCol="caracteristicas")
   dados = montador_vetores.transform(dados)
   
   # Dividindo os dados em conjuntos de treino e teste
   dados_treino, dados_teste = dados.randomSplit([0.7, 0.3])
   
   # Criando e treinando um modelo de regressão linear
   modelo_lr = LinearRegression(featuresCol="caracteristicas", labelCol="label")
   modelo_treinado = modelo_lr.fit(dados_treino)
   
   # Avaliando o modelo nos dados de teste
   resultados_teste = modelo_treinado.evaluate(dados_teste)
   print("Raiz do Erro Quadrático Médio (RMSE):", resultados_teste.rootMeanSquaredError)
   
   # Finalizando a sessão Spark
   sessao_spark.stop()

   
   ```
3. **Executar o Código:**
No terminal, execute o código Python:

   ```
   $ spark-submit sql_mllib.py
   <output> - Raiz do Erro Quadrático Médio (RMSE): 1.7763568394002505e-15
   ```
OBS: `dados.csv` precisa estar no mesmo diretório que seu código.

## Conclusão

O **Apache Spark** é uma ferramenta de código aberto útil para o processamento de dados em grande escala, muito utilizada em análise de big data, aprendizado de máquina e processamento em tempo real. Ele suporta várias linguagens de programação, incluindo Scala, Java, Python e R.

Na seção de Instalação, são fornecidas instruções de instalação do Apache Spark em sistemas operacionais como Windows e Linux, juntamente com os pré-requisitos.

Na seção Exemplos é mostrado a aplicação da em cenários comuns:

1. Processamento de Lote de Dados: Como criar um arquivo de dados e processá-lo em lote.
2. Processamento em Tempo Real de Dados: Como usar o Spark Streaming para processar dados em tempo real.
3. Integração com Spark SQL e Spark MLlib: Como usar o Spark SQL e o Spark MLlib para análise de dados e aprendizado de máquin.

## Referências

Estas são algumas das referências utilizadas na criação deste roteiro:

- [Enunciado do Projeto](https://eduardocunha11.github.io/firstblog/aulas/lab-programacao/Roteiro-Trabalho1.pdf)
- [Site oficial do Apache Spark](https://spark.apache.org/)
- [Documentação do Apache Spark](https://spark.apache.org/documentation.html)
- [ [Spark] Structured Streaming - Processamento de dados perto do tempo real com Spark](https://www.youtube.com/watch?v=0IuMhbgj2ng)
- [Processamento em lote](https://www.ibm.com/docs/pt-br/cloud-paks/cp-data/4.0?topic=openscale-batch-processing-overview).
