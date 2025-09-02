import fasttext
import os

from typing import Any


def identify_language(text: str) -> tuple[Any, float]:
  model = fasttext.load_model('/content/cs336-2025spring-assignment4-data/cs336_data/lid.176.bin')
  text = text.replace('\n', '')
  lang, value = model.predict(text)
  return (lang[0][-2:], value[0])