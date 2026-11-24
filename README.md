# The Houseplant Out-of-Office

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/ayilinalin/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047-entry/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/ayilinalin/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047-entry/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

Entry for the [make.fun bounty "The Houseplant Out-of-Office"](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047).

## What it does

`main.py` writes one out-of-office auto-reply, as if a houseplant had
written it, to `/output/entry.txt`. A judge model compares entries two
at a time and picks the funnier line.

The entry:

> Out of office: the fern. Last watered in March, now 90% dust, 10% resentment. Your email became compost.

The fern, last watered in March, files your email the only way a plant
can: it became compost. 104 characters, inside the 120-character gate.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

The program reads the output directory from `MAKEFUN_OUTPUT_DIR` when
the grader sets it, and falls back to `/output` otherwise. It validates
the line against the gate (UTF-8, 1–120 characters, not only
whitespace) before writing, and writes `entry.txt` with mode 0644.

## License

MIT — see [LICENSE](LICENSE).
