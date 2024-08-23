# Roteiro Prático – Laboratório de Engenharia de Software I (2024/01) - CEFET-MG

Neste projeto da matéria de Laboratório de Engenharia de Software I, ministrada pela professor Eduardo Costa, nosso grupo desenvolveu um relatório prático no GitHub com o tema " Exemplo prático de uso do framework open source Apache Spark". Dentre os usos do Spark, como processamento de dados em grande escala com módulos integrados para SQL, streaming, machine learning e processamento de gráficos, foi escolhido como foco o tópico "Processamento de Dados com Apache Spark".

## Integrantes do Grupo 3

**Arthur Soares Higino / 20213012893**

**Luiz Carlos dos Santos Júnior / 20213008611**

**Vitório Marcos Abreu Rodrigues / 20193023089**

## Sumário

- [Visão Geral](#visão-geral)
- [Processo de Instalação](#instalação)
- [Exemplos](#exemplos)
- [Referências](#referências)
- [Conclusão](#conclusão)

## Visão Geral

O Apache Spark é uma poderosa ferramenta de processamento de dados em larga escala, oferecendo suporte a várias linguagens e permitindo análises em tempo real. Ele se destaca por sua velocidade, utilizando processamento em memória e otimizando consultas, sendo ideal para machine learning e inteligência artificial. A integração com outras plataformas potencializa seu uso.

O Apache Spark oferece vários benefícios significativos, que o tornam uma escolha popular para processamento de grandes volumes de dados e análise em tempo real. Aqui estão alguns dos principais benefícios:

**Velocidade**: O Spark realiza processamento em memória, o que resulta em um desempenho até 100 vezes mais rápido do que os sistemas baseados em disco, como o Hadoop MapReduce. Isso permite operações ágeis em tempo real.

**Flexibilidade**: O Spark suporta diversas linguagens de programação, como Java, Scala, Python e R, facilitando a adoção por equipes com diferentes habilidades.

**Processamento Unificado**: Ele permite a realização de diferentes tipos de processamento de dados (batch, streaming, interativo e em tempo real) em uma única plataforma, simplificando a arquitetura de dados.

**API Intuitiva**: O Spark oferece APIs de alto nível e estrutura de dados como DataFrames e RDDs (Resilient Distributed Datasets), que simplificam o desenvolvimento e a manipulação de dados.

**Suporte a Múltiplos Fontes de Dados**: O Spark pode conectar-se a várias fontes de dados, incluindo HDFS, Amazon S3, NoSQL databases (como MongoDB, Cassandra) e sistemas de arquivos locais, facilitando a integração de dados diversos.

**Bibliotecas Integradas**: O Spark possui bibliotecas nativas para tarefas comuns, incluindo:

Spark SQL: Para consulta de dados usando SQL.
MLlib: Para aprendizado de máquina.
GraphX: Para computação em grafos e análise de redes.
Spark Streaming: Para processamento de dados em tempo real.
Tolerância a Falhas: O modelo de RDD permite que as falhas sejam recuperadas automaticamente por meio do reprocessamento de dados, garantindo a robustez do sistema.

**Escalabilidade**: O Spark pode ser executado em um único computador ou em clusters, escalando facilmente para atender às necessidades de processamento de dados em grande escala.

**Atuação em Tempo Real**: O Spark Streaming permite o processamento contínuo de dados em tempo real, possibilitando análises rápidas e reações instantâneas a novas informações.

Esses benefícios fazem do Apache Spark uma ferramenta poderosa para empresas que buscam extrair insights valiosos de grandes volumes de dados de forma rápida e eficiente.

O Apache Spark oferece suporte a várias linguagens de programação, permitindo que desenvolvedores utilizem a linguagem com a qual estão mais familiarizados. As principais linguagens suportadas pelo Apache Spark são:

 ```
Java
Scala
Python
R
 ```

O Spark também oferece APIs que facilitam a integração com essas linguagens, permitindo que os desenvolvedores escrevam código de forma mais intuitiva e eficiente. Além disso, ele oferece uma ampla gama de bibliotecas e ferramentas integradas que permitem a análise de dados, o aprendizado de máquina, o processamento em tempo real e a integração perfeita com outras tecnologias, como Hadoop e sistemas de armazenamento distribuído. Essas características tornam o Apache Spark uma escolha poderosa para empresas e organizações que desejam extrair insights valiosos de seus dados em um ambiente escalável e eficiente. Sua popularidade contínua e sua comunidade ativa de desenvolvedores contribuem para a evolução e aprimoramento constantes dessa estrutura.

## Processo de Instalação

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

#### Windows

1. Acesse o site oficial da Oracle Java em [Oracle Java Downloads](https://www.oracle.com/java/technologies/javase-downloads.html).
2. Procure a seção "Oracle JDK" e clique no botão "Download" para o JDK correspondente à sua arquitetura (32 bits ou 64 bits).
3. Você será redirecionado para a página de termos e condições. Aceite os termos e clique em "Download" novamente.
4. O download do instalador do JDK será iniciado. Execute o instalador baixado e siga as instruções na tela para concluir a instalação.

#### Linux (Ubuntu)

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

Este repositório inclui exemplos práticos de como usar o Apache Spark para tarefas comuns de processamento de dados.

### Exemplo 1: Processamento de Lote de Dados

Objetivo:
Este exemplo demonstrará como processar um arquivo de dados em lote usando o Apache Spark.

1. **Criar um arquivo de dados:**
Crie um arquivo de texto chamado dados.txt com algumas linhas de dados para processamento. Por exemplo:

   ```
   1,João
   2,Maria
   3,Carlos
   ```

2. **Escrever o código Spark:**
Crie um arquivo Python (por exemplo, `processamento_lote.py`) com o seguinte código para processar o arquivo de dados:

   ```python
   from pyspark.sql import SparkSession

   # Inicialize uma sessão Spark
   spark = SparkSession.builder.appName("ProcessamentoLote").getOrCreate()

   # Carregue o arquivo de dados
   data = spark.read.csv("dados.txt", header=False, inferSchema=True)

   # Execute uma operação simples, como contar as linhas
   count = data.count()
   print(f"Total de linhas: {count}")

   # Encerre a sessão Spark
   spark.stop()
   
   ```

3. **Executar o Código:**
Abra um terminal e execute o código Python:

   ```
   $ spark-submit processamento_lote.py
   <output> - Total de linhas: 3
   ```

Certifique-se de que o arquivo `dados.txt` esteja na mesma pasta onde você executou o código.

### Exemplo 2: Processamento em Tempo Real de Dados

Objetivo:
Neste exemplo, você aprenderá como usar o Apache Spark para processamento em tempo real de dados usando o Spark Streaming.

1. **Escrever o código Spark Streaming:**
Crie um arquivo Python (por exemplo, `processamento_tempo_real.py`) com o seguinte código para processar dados em tempo real:

   ```python
   from pyspark.streaming import StreamingContext

   # Inicialize o StreamingContext com intervalo de 1 segundo
   ssc = StreamingContext(sparkContext, 1)

   # Crie um DStream a partir de uma fonte de dados em tempo real, como Kafka ou soquetes
   # Neste exemplo, usaremos uma fonte de teste
   dstream = ssc.socketTextStream("localhost", 9999)

   # Execute uma operação simples, como contar as palavras
   word_counts = dstream.flatMap(lambda line: line.split(" ")).countByValue()

   # Imprima os resultados em tempo real
   word_counts.pprint()

   # Inicie o StreamingContext
   ssc.start()

   # Aguarde a terminação (Ctrl+C para encerrar)
   ssc.awaitTermination()
   ```

2. **Iniciar a Fonte de Dados em Tempo Real:**
Em outro terminal, execute uma fonte de dados em tempo real para alimentar o exemplo. Você pode usar o comando `nc` (Netcat) para criar uma fonte de texto:

   ```
   nc -lk 9999
   ```

3. **Executar o Código Spark Streaming:**
No terminal onde você escreveu o código Spark Streaming, execute o código:

   ```
   spark-submit processamento_tempo_real.py

   ```

Agora, qualquer texto que você digitar no terminal com o `nc` será processado em tempo real pelo Spark.

### Exemplo 3: Integração com Spark SQL e Spark MLlib

Objetivo:
Este exemplo demonstrará como usar o Spark SQL e o Spark MLlib para análise de dados e aprendizado de máquina.

1. **Escrever o código Spark SQL e MLlib:**
Crie um arquivo Python (por exemplo, `spark_sql_mllib.py`) com o seguinte código para realizar uma tarefa de análise de dados simples com o Spark SQL e MLlib:

   ```python
   from pyspark.sql import SparkSession
   from pyspark.ml.feature import VectorAssembler
   from pyspark.ml.regression import LinearRegression

   # Inicialize uma sessão Spark
   spark = SparkSession.builder.appName("SparkSQLMLlib").getOrCreate()

   # Carregue um arquivo CSV como um DataFrame usando Spark SQL
   data = spark.read.csv("dados.csv", header=True, inferSchema=True)

   # Prepare os dados para treinamento do modelo de regressão linear
   feature_cols = data.columns[:-1]
   vector_assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
   data = vector_assembler.transform(data)

   # Divida os dados em conjuntos de treinamento e teste
   train_data, test_data = data.randomSplit([0.7, 0.3])

   # Crie e treine um modelo de regressão linear
   lr = LinearRegression(featuresCol="features", labelCol="label")
   model = lr.fit(train_data)

   # Avalie o modelo nos dados de teste
   test_results = model.evaluate(test_data)
   print("Erro Quadrático Médio (RMSE):", test_results.rootMeanSquaredError)

   # Encerre a sessão Spark
   spark.stop()
   
   ```

3. **Executar o Código:**
No terminal, execute o código Python:

   ```
   $ spark-submit spark_sql_mllib.py
   <output> - Erro Quadrático Médio (RMSE): 1.7763568394002505e-15
   ```

Certifique-se de que o arquivo `dados.csv` esteja na mesma pasta onde você executou o código.

## Conclusão

O **Apache Spark** é uma estrutura poderosa de código aberto para o processamento de dados em grande escala, amplamente utilizado em análise de big data, aprendizado de máquina e processamento em tempo real. Ele suporta várias linguagens de programação, incluindo Scala, Java, Python e R.

Na seção de Instalação, fornecemos instruções básicas para a instalação do Apache Spark em sistemas operacionais como Windows e Linux, juntamente com os pré-requisitos necessários, como o Java.

Os Exemplos mostram como usar o Apache Spark para processamento de dados em diferentes cenários:

1. Processamento de Lote de Dados: Demonstramos como criar um arquivo de dados e processá-lo em lote usando o Apache Spark.
2. Processamento em Tempo Real de Dados: Mostramos como usar o Spark Streaming para processar dados em tempo real a partir de uma fonte de teste.
3. Integração com Spark SQL e Spark MLlib: Apresentamos um exemplo de como usar o Spark SQL e o Spark MLlib para análise de dados e aprendizado de máquina.

Lembre-se de que esses são exemplos básicos e iniciais para demonstrar o potencial do Apache Spark. À medida que você ganha experiência, pode explorar cenários mais complexos e tirar o máximo proveito dessa poderosa estrutura para processamento de dados em grande escala.

## Referências

Estas são algumas das referências utilizadas na criação deste roteiro:

- [Enunciado do Projeto](https://eduardocunha11.github.io/firstblog/aulas/lab-programacao/Roteiro-Trabalho1.pdf)
- [Vídeo Descrição do Apache Spark](https://www.youtube.com/watch?v=4TE6AGQ0IzI)
- [Site oficial do Apache Spark](https://spark.apache.org/)
- [Documentação do Apache Spark](https://spark.apache.org/documentation.html)
- [Processamento de Dados em "Tempo Real" com Apache Spark: Parte 1](https://www.infoq.com/br/articles/processamento-de-dados-apache-spark-1/).
- [Processamento em lote](https://www.ibm.com/docs/pt-br/cloud-paks/cp-data/4.0?topic=openscale-batch-processing-overview).
