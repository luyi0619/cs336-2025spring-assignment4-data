from resiliparse.parse.encoding import detect_encoding
from resiliparse.extract.html2text import extract_plain_text


def extract_text_from_html_bytes(html_bytes: bytes) -> str | None:
  detected_encoding = detect_encoding(html_bytes)
  decoded_html_bytes = html_bytes.decode(detected_encoding)
  return extract_plain_text(decoded_html_bytes)