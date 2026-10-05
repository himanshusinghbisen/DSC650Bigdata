from pyspark.sql import SparkSession
import random

# Start Spark
spark = SparkSession.builder.appName("SentenceGenerator").getOrCreate()
sc = spark.sparkContext

# Word list
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

# Generate sentences on the driver
num_sentences = 1000
sentences = [
    " ".join(random.sample(words, random.randint(1, 6))) + "."
    for _ in range(num_sentences)
]

# Parallelize into RDD
sentences_rdd = sc.parallelize(sentences)

# Custom Transformation: Uppercase and tag
transformed = sentences_rdd.map(lambda s: f"{s.upper()} [PROCESSED]")

# Save to HDFS
output_path = "hdfs:///tmp/week4_output"
transformed.saveAsTextFile(output_path)

spark.stop()
