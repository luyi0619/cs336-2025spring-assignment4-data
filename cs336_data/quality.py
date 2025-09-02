

def gopher_quality_filter(text: str) -> bool:
  words = text.split()
  
  # Contain less than 50 or more than 100,000 words.
  if len(words) < 50 or len(words) > 100000:
    return False

  # Have a mean word length outside the range of 3 to 10 characters.
  word_total_length = 0
  for w in words:
    word_total_length += len(w)
  word_avg_length = word_total_length / len(words)
  if word_avg_length < 3 or word_avg_length > 10:
    return False
  
  # Have more than 30% of lines ending with an ellipsis (“...”).
  lines = text.split('\n')
  ellipsis_line_cnt = 0
  for line in lines:
    if line.endswith('...'):
      ellipsis_line_cnt += 1
  if ellipsis_line_cnt / len(lines) > 0.3:
    return False
  
  # Contain less than 80% of words with at least one alphabetic character.
  alphabetic_words_cnt = 0
  for w in words:
    if any(c.isalpha() for c in w):
      alphabetic_words_cnt += 1
  if alphabetic_words_cnt / len(words) < 0.8:
    return False

  return True