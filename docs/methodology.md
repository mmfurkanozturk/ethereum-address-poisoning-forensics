# Methodology

## 1. Evidence sources

The investigation uses public Ethereum transaction, trace, contract-creation, token-transfer, and event-log data. Blockscout was used as the primary structured explorer during the investigation, with public explorer labels treated as supporting metadata rather than ground truth.

## 2. Asset verification

Token names and symbols are not trusted. A transfer is treated as genuine USDT or USDC only when the token contract exactly matches:

- USDT: `0xdAC17F958D2ee523a2206206994597C13D831ec7`
- USDC: `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

## 3. Successful-poisoning criteria

A case is classified as strongly consistent with successful address poisoning when the available evidence shows a sequence such as:

1. an address previously transacts with a legitimate counterparty;
2. a lookalike address appears in its history through dust or a zero-value/fabricated token event;
3. the address later sends material value to the lookalike;
4. the lookalike converts or forwards the proceeds;
5. the proceeds converge on infrastructure already linked to the same operator/treasury cluster.

No single heuristic is used in isolation.

## 4. Cluster attribution

Addresses are linked into the same operational cluster using observable actions such as:

- contract creation by the same operator;
- direct funding from the operator or treasury;
- repeated gas provisioning;
- proceeds consolidation into the same wallet;
- stablecoin/ETH recycling back into poisoning infrastructure;
- EIP-7702 implementation reuse;
- timing and transaction-pattern consistency.

## 5. Mixer boundary

A Tornado Cash withdrawal provides evidence that value entered an observable wallet from the mixer pool. It does not deterministically identify the deposit transaction or depositor. The analysis therefore stops at the anonymity boundary unless independent public evidence exists.

## 6. CEX boundary

A transfer to a publicly tagged centralized-exchange wallet would establish an on-chain endpoint controlled by the exchange. It would not, by itself, reveal the customer or account owner behind the deposit.
