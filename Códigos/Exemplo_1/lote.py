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


