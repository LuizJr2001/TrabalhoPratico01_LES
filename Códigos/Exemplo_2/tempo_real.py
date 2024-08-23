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

