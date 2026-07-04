# main.py

import argparse
import asyncio
import os

from models import CopyRequest
from generator import generate_copy
from async_runner import generate_many

from utils import (
    ensure_output_directory,
    save_json,
    save_csv,
    print_results,
    load_products_csv,
)

from config import (
    OUTPUT_DIRECTORY,
    JSON_OUTPUT,
    CSV_OUTPUT,
)


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="AI Marketing Copy Generator"
    )

    # Single Request
    parser.add_argument(
        "--product",
        type=str,
        help="Product name",
    )

    parser.add_argument(
        "--platform",
        type=str,
        choices=[
            "Instagram",
            "LinkedIn",
            "Email",
            "Twitter",
            "Facebook",
        ],
    )

    parser.add_argument(
        "--tone",
        type=str,
        choices=[
            "Professional",
            "Friendly",
            "Luxury",
            "Urgent",
            "Casual",
            "Witty",
        ],
    )

    parser.add_argument(
        "--char-limit",
        type=int,
        default=250,
    )

    # Bulk CSV
    parser.add_argument(
        "--csv",
        type=str,
        help="CSV containing requests",
    )

    # Batch API
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Use OpenAI Batch API",
    )

    return parser.parse_args()


def run_single(args):

    request = CopyRequest(
        product_name=args.product,
        platform=args.platform,
        tone=args.tone,
        char_limit=args.char_limit,
    )

    result = generate_copy(request)

    print_results([result])

    ensure_output_directory(OUTPUT_DIRECTORY)

    save_json(
        [result],
        os.path.join(
            OUTPUT_DIRECTORY,
            JSON_OUTPUT,
        ),
    )

    save_csv(
        [result],
        os.path.join(
            OUTPUT_DIRECTORY,
            CSV_OUTPUT,
        ),
    )


async def run_bulk_async(csv_path):

    requests = load_products_csv(csv_path)

    results = await generate_many(
        requests
    )

    print_results(results)

    ensure_output_directory(OUTPUT_DIRECTORY)

    save_json(
        results,
        os.path.join(
            OUTPUT_DIRECTORY,
            JSON_OUTPUT,
        ),
    )

    save_csv(
        results,
        os.path.join(
            OUTPUT_DIRECTORY,
            CSV_OUTPUT,
        ),
    )




def main():

    args = parse_arguments()

    # Async CSV Mode
    if args.csv:

        asyncio.run(
            run_bulk_async(
                args.csv
            )
        )

        return

    # Single Request Mode
    required = [
        args.product,
        args.platform,
        args.tone,
    ]

    if not all(required):

        raise ValueError(
            "Single mode requires "
            "--product --platform --tone"
        )

    run_single(args)


if __name__ == "__main__":
    main()