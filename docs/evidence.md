# Evidence Registry

The entries below are selected transactions that establish the core relationships in the case study.

## Case 1 — ETH

**Source → poison**  
`0xdf411d528000928fe0657df956886a8b01069ff16d0c836f9d9e4e1e09acd337`

- From: `0x680D559852643aC72383C232589e2799080e2c4F`
- To: `0x284336EF3282B012bd1518Fe3D38042DFe87116a`
- Value: `4.984970314501777 ETH`
- Timestamp: 2026-05-28 16:49:11 UTC

**Poison → treasury**  
`0x9312cd31d993d93fcf9b26426f95bb8e623b662026db537dd6e415d5d6ad97ff`

- Value: `4.984891681206054340 ETH`
- To: `0xBD114DD6A8a8260fCf9632e537E69b9C0b83F9EB`

## Case 2 — USDT

**Source → poison**  
`0x7bfc382551791d2eac3459d57b3a15d6cf665763a635c4af50a1930c9ccc1b00`

- Genuine token contract: `0xdAC17F958D2ee523a2206206994597C13D831ec7`
- Amount: `2,959.486930 USDT`
- To: `0xD2b665c4Ea3239224Fd5389e6baB6031829005C3`

**Swap**  
`0x02de7483e4cefb158f9307d9bc8b134c4cf00c6b25548380646c4dfee36f1570`

- Input: `2,959.486930 USDT`
- Internal ETH received: `1.547562681148039936 ETH`

**Poison → treasury**  
`0x07c914ea84d0c341c2fd05e02165c55065e2f83f51972152996b48f4b0e53dc8`

- Value: `1.547872133793657120 ETH`

## Case 3 — USDC

**Source → poison**  
`0xa791ecb5b7e967c1b398c1b9a98ce1db5ac986acbd2a87b800d1ff46a60fd152`

- Genuine token contract: `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`
- Amount: `1,390 USDC`
- To: `0x51D3a8FA041aCfBFc5f425ee7265A9D83e33e390`

**Swap**  
`0x1c2420fc69251d398e2150d7cea5035ec1afff9e66f43ae4faace6d633084078`

- Input: `1,390 USDC`
- Internal ETH received: `0.798604186915133103 ETH`

**Poison → treasury**  
`0xcd43125fc92e5ac9620019a3bc8227886bac132cfa33112ded02e45a173524eb`

- Value: `0.799282871251762423 ETH`

## Case 4 — USDT

**Source → poison**  
`0xb562aa33762ac5109aec26fcb18d90d96ed98024feb3cec8eee49d8510c049d5`

- Genuine token contract: `0xdAC17F958D2ee523a2206206994597C13D831ec7`
- Amount: `1,450 USDT`
- From: `0x6730418f0D76824Cd4BE0B7CDDD8E3722334bd6d`
- To: `0x3428AB1cDb2a578B0685957AED9C29fd17AEB170`

**Swap**  
`0x255c7a0d145670ae3d040ed7afacbec86f196259643257a15892dd84a7b31e96`

- Input: `1,450 USDT`
- Internal ETH received: `0.848200569328803179 ETH`

**Poison → treasury**  
`0xb2c28a01268110ecb7f224a260a26a410e30e7bbcf5f2a4f1e10fae019735e27`

- Value: `0.849054504802400352 ETH`

## Tornado Cash withdrawal branch

`0xe567cc5ea13c61628c162f6821b438a06ab6292410335b6ca19aef0c2c3f9b83`

Decoded withdrawal parameters include:

- Tornado pool: `0x12D66f87A04A9E220743712cE6d9bB1B5616B8Fc`
- Recipient: `0x53BB6CA3997261073A73C8830Ca21522b4786c37`
- Relayer: `0xda0b76cc92e94a6f972Ed29C104BBe8d73c2f753`
- Fee: `0.0017208394461 ETH`

The recipient receives approximately `0.0982791605539 ETH` from the 0.1 ETH pool after the relayer fee.

The relayer is a protocol participant and must not be treated as the attacker without independent evidence.
