pip install transformers[sentencepiece] datasets
from transformers import pipeline

translate = pipeline('translation', "Helsinki-NLP/opus-mt-ru-en")

print(translate("Это мое первое задание"))