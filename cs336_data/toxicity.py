import fasttext

from typing import Any

def classify_nsfw(text: str) -> tuple[Any, float]:
  model = fasttext.load_model('/content/cs336-2025spring-assignment4-data/cs336_data/jigsaw_fasttext_bigrams_nsfw_final.bin')
  label, value = model.predict(text)
  return label[0][9:], value[0]


def classify_toxic_speech(text: str) -> tuple[Any, float]:
  model = fasttext.load_model('/content/cs336-2025spring-assignment4-data/cs336_data/jigsaw_fasttext_bigrams_hatespeech_final.bin')
  label, value = model.predict(text)
  return label[0][9:], value[0]