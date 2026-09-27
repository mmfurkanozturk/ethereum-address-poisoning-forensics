#!/usr/bin/env python3
"""Estimate the brute-force search space for Ethereum vanity-address matching."""

from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prefix", type=int, help="number of hexadecimal prefix characters to match")
    parser.add_argument("suffix", type=int, help="number of hexadecimal suffix characters to match")
    args = parser.parse_args()

    n = args.prefix + args.suffix
    search_space = 16 ** n
    print(f"Matched hex characters: {n} ({args.prefix} prefix + {args.suffix} suffix)")
    print(f"Search space: {search_space:,} candidates")
    print(f"Expected attempts for a random search: ~{search_space:,}")


if __name__ == "__main__":
    main()
