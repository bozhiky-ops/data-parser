# utils.py
import os
import logging
import re
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Config:
    """Configuration dataclass."""
    input_file: str
    output_file: str
    log_level: int

def configure_logging(config: Config) -> None:
    """Configure logging based on the provided configuration."""
    logging.basicConfig(filename=config.output_file, level=config.log_level)

def read_text_file(file_path: str) -> str:
    """Read the content of a text file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"File {file_path} not found.")
        raise

def split_text_into_lines(text: str) -> List[str]:
    """Split text into individual lines."""
    return text.splitlines()

def extract_regex_pattern(pattern: str, text: str) -> List[str]:
    """Extract matches from the given text."""
    return re.findall(pattern, text)

def format_output(lines: List[str]) -> str:
    """Format the output."""
    return '\n'.join(lines)