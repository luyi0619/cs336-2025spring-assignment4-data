import re

def mask_emails(text: str) -> tuple[str, int]:
  email_regex = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
  cleaned_text, count = re.subn(email_regex, '|||EMAIL_ADDRESS|||', text)
  return cleaned_text, count


def mask_phone_numbers(text: str) -> tuple[str, int]:
  phone_regex = r'(\(?\d{3}\)?[\s\-]?)?\d{3}[\s\-]?\d{4}'
  cleaned_text, count = re.subn(phone_regex, '|||PHONE_NUMBER|||', text)
  return cleaned_text, count


def mask_ips(text: str) -> tuple[str, int]:
  ipv4_regex = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
  cleaned_text, count = re.subn(ipv4_regex, '|||IP_ADDRESS|||', text)
  return cleaned_text, count  
