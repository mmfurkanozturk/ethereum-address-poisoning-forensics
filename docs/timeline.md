# Timeline

## March 2026 — Early observable bootstrap branch

- `0x53BB6CA3997261073A73C8830Ca21522b4786c37` receives repeated internal ETH transfers originating from the Tornado Cash Classic 0.1 ETH pool.
- One fully decoded example is transaction `0xe567cc5ea13c61628c162f6821b438a06ab6292410335b6ca19aef0c2c3f9b83`, where the Tornado withdrawal recipient is `0x53BB...6c37`.
- `0x53BB...6c37` later funds older attack-generation infrastructure, including `0x2c398E...e26b` and `0x7a4991...DDdE`.

This establishes an observable funding branch into the cluster. It does not identify the Tornado deposit-side sender.

## April 2026 — Operator appears

- `0x61077f362c0FA529f60729AAc4611A34206D7129` funds operator/gas wallet `0x09CfEe647fA339133380191C8DB6b44F24500c9D`.
- The operator later creates and funds multiple poisoning-related contracts and EIP-7702 accounts.

## May 2026 — Consolidation wallet appears

- `0xBD114DD6A8a8260fCf9632e537E69b9C0b83F9EB` receives its first observed material inflow from a poison address on 28 May.
- The same wallet later funds the operator and poisoning infrastructure and swaps ETH into real stablecoins used for dust campaigns.

## May–July 2026 — Four verified successful cases

See [cases.csv](../data/cases.csv) and [evidence.md](evidence.md).

## August–September 2026 — Infrastructure rotation

- EIP-7702 and batch-transfer infrastructure changes over time.
- `0x0Ca8E8d976dF3321F6ff0A8CCa96536a51565c81` and implementation `0x6D362D2F7f7e8ed494B0eeeB473Abb3728D12c17` are part of the later campaign infrastructure.

## 26 September 2026 — Campaign still active

- The operator continues repeated zero-value calls into current poisoning infrastructure.
- No verified cash-out to a clearly tagged centralized-exchange endpoint had been established at the research cutoff.
