from transformers import pipeline

# Load sentiment-analysis pipeline
classifier = pipeline('sentiment-analysis')

# Analyze sentiment
sentence = "I love using Hugging Face Transformers!"
result = classifier(sentence)

print(result)
