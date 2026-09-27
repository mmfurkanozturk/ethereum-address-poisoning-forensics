# Privacy Design

The triggering event involved the researcher's own wallet. This repository intentionally excludes all identifiers that would allow readers to recover that wallet from the initial incident.

Specifically omitted:

- the researcher's Ethereum address;
- the legitimate recipient involved in the researcher's original transfer;
- the lookalike address generated specifically for the researcher;
- the original poisoning transaction hash;
- screenshots containing recoverable wallet identifiers.

Why omit the transaction hash? Because a public transaction hash is enough to inspect the logs and recover the addresses involved, defeating the purpose of redacting the wallet address in prose.

The public addresses retained in the repository belong to the independently investigated attack infrastructure, public protocol contracts, or unrelated on-chain counterparties in the four case studies.
