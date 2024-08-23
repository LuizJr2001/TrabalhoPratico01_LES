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


