# utils.py

import csv
import json
from pathlib import Path

from models import CopyRequest, CopyOutput


def ensure_output_directory(directory: str) -> None:
    """
    Create the output directory if it doesn't exist.
    """
    Path(directory).mkdir(parents=True, exist_ok=True)


def load_products_csv(filepath: str) -> list[CopyRequest]:
    """
    Load marketing copy requests from a CSV file.

    Expected columns:
    product_name, platform, tone, char_limit
    """
    requests = []

    with open(filepath, "r", encoding="utf-8", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            requests.append(
                CopyRequest(
                    product_name=row["product_name"],
                    platform=row["platform"],
                    tone=row["tone"],
                    char_limit=int(row["char_limit"]),
                )
            )

    return requests


def save_json(results: list[CopyOutput], filepath: str) -> None:
    """
    Save generated copy to a JSON file.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(
            [result.model_dump() for result in results],
            f,
            indent=4,
            ensure_ascii=False,
        )


def save_csv(results: list[CopyOutput], filepath: str) -> None:
    """
    Save generated copy to a CSV file.
    """
    with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([
            "Platform",
            "Tone",
            "Copy",
            "Word Count",
        ])

        for result in results:
            writer.writerow([
                result.platform,
                result.tone,
                result.copy_text,
                result.word_count,
            ])


def print_results(results: list[CopyOutput]) -> None:
    """
    Print generated marketing copy to the console.
    """
    for i, result in enumerate(results, start=1):
        print("=" * 80)
        print(f"Result #{i}")
        print(f"Platform : {result.platform}")
        print(f"Tone     : {result.tone}")
        print(f"Words    : {result.word_count}")
        print("-" * 80)
        print(result.copy_text)
        print()