#!/usr/bin/env python3
"""Read-only verification of selected evidence transactions via Blockscout."""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request

BASE = "https://eth.blockscout.com/api/v2/transactions/"

TX_HASHES = [
    "0xdf411d528000928fe0657df956886a8b01069ff16d0c836f9d9e4e1e09acd337",
    "0x9312cd31d993d93fcf9b26426f95bb8e623b662026db537dd6e415d5d6ad97ff",
    "0x7bfc382551791d2eac3459d57b3a15d6cf665763a635c4af50a1930c9ccc1b00",
    "0x02de7483e4cefb158f9307d9bc8b134c4cf00c6b25548380646c4dfee36f1570",
    "0x07c914ea84d0c341c2fd05e02165c55065e2f83f51972152996b48f4b0e53dc8",
    "0xa791ecb5b7e967c1b398c1b9a98ce1db5ac986acbd2a87b800d1ff46a60fd152",
    "0xcd43125fc92e5ac9620019a3bc8227886bac132cfa33112ded02e45a173524eb",
    "0xb562aa33762ac5109aec26fcb18d90d96ed98024feb3cec8eee49d8510c049d5",
    "0x255c7a0d145670ae3d040ed7afacbec86f196259643257a15892dd84a7b31e96",
    "0xb2c28a01268110ecb7f224a260a26a410e30e7bbcf5f2a4f1e10fae019735e27",
    "0xe567cc5ea13c61628c162f6821b438a06ab6292410335b6ca19aef0c2c3f9b83",
]


def fetch(tx_hash: str) -> dict:
    req = urllib.request.Request(
        BASE + tx_hash,
        headers={"User-Agent": "address-poisoning-forensics/1.0"},
    )
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.load(response)


def eth_from_wei(value: str | int | None) -> str:
    if value in (None, ""):
        return "0"
    return f"{int(value) / 10**18:.18f}".rstrip("0").rstrip(".")


def main() -> int:
    for tx_hash in TX_HASHES:
        print("=" * 100)
        print(tx_hash)
        try:
            tx = fetch(tx_hash)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            print(f"ERROR: {exc}")
            continue

        print("timestamp:", tx.get("timestamp"))
        print("status:   ", tx.get("status"))
        print("from:     ", tx.get("from", {}).get("hash") if isinstance(tx.get("from"), dict) else tx.get("from"))
        print("to:       ", tx.get("to", {}).get("hash") if isinstance(tx.get("to"), dict) else tx.get("to"))
        print("ETH value:", eth_from_wei(tx.get("value")))

        transfers = tx.get("token_transfers") or []
        if transfers:
            print("token transfers:")
            for t in transfers:
                token = t.get("token") or {}
                total = t.get("total") or {}
                decimals = int(total.get("decimals") or token.get("decimals") or 0)
                raw = int(total.get("value") or 0)
                amount = raw / (10 ** decimals) if decimals else raw
                print(
                    f"  {amount} {token.get('symbol')} | "
                    f"{t.get('from', {}).get('hash') if isinstance(t.get('from'), dict) else t.get('from')} -> "
                    f"{t.get('to', {}).get('hash') if isinstance(t.get('to'), dict) else t.get('to')} | "
                    f"contract={token.get('address_hash')}"
                )

    return 0


if __name__ == "__main__":
    sys.exit(main())
