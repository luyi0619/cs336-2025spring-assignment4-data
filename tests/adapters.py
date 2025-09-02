from __future__ import annotations

import sys
import os

# Get the absolute path to the directory containing the module
# For example, if 'my_module.py' is in '../other_directory', use:
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'cs336_data'))

# Add the path to sys.path
sys.path.insert(0, module_path) # or sys.path.append(module_path)

from typing import Any
from extract import extract_text_from_html_bytes
from langid import identify_language
from pii import mask_emails, mask_phone_numbers, mask_ips
from toxicity import classify_nsfw, classify_toxic_speech
from quality import gopher_quality_filter
from deduplication import exact_line_deduplication


def run_extract_text_from_html_bytes(html_bytes: bytes) -> str | None:
    return extract_text_from_html_bytes(html_bytes)


def run_identify_language(text: str) -> tuple[Any, float]:
    return identify_language(text)


def run_mask_emails(text: str) -> tuple[str, int]:
    return mask_emails(text)


def run_mask_phone_numbers(text: str) -> tuple[str, int]:
    return mask_phone_numbers(text)


def run_mask_ips(text: str) -> tuple[str, int]:
    return mask_ips(text)


def run_classify_nsfw(text: str) -> tuple[Any, float]:
    return classify_nsfw(text)


def run_classify_toxic_speech(text: str) -> tuple[Any, float]:
    return classify_toxic_speech(text)


def run_classify_quality(text: str) -> tuple[Any, float]:
    raise NotImplementedError


def run_gopher_quality_filter(text: str) -> bool:
    return gopher_quality_filter(text)


def run_exact_line_deduplication(
    input_files: list[os.PathLike], output_directory: os.PathLike
):
    exact_line_deduplication(input_files, output_directory)


def run_minhash_deduplication(
    input_files: list[os.PathLike],
    num_hashes: int,
    num_bands: int,
    ngrams: int,
    jaccard_threshold: float,
    output_directory: os.PathLike,
):
    raise NotImplementedError
