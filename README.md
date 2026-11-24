# The Houseplant Out-of-Office

[![make.fun bounty](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/imusic-487/houseplant-out-of-office/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/imusic-487/houseplant-out-of-office/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

Entry for the [make.fun bounty "The Houseplant Out-of-Office"](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047).

## The reply

> I'm out of office and out of water since March. For urgent matters, contact the cactus. He doesn't care either.

111 characters, one line. The plant has not been watered since March and
is finally answering its own mail: out of office, out of water, and
forwarding anything urgent to the cactus, who is even less help.

## How it works

`main.py` (Python 3.13 standard library only, no network) writes the reply
to `/output/entry.txt`:

```sh
python3 main.py
```

It self-checks the competition gate first (1–120 characters, a single
line, not only whitespace), writes the reply, then reads the file back
and refuses to report success unless the bytes match exactly. The output
is deterministic — every run writes the exact same bytes.
