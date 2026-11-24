[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/rinoo9/u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/rinoo9/u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

# Say What Actually Broke

One line of software error copy for the [make.fun](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) bounty "Say What Actually Broke": a single line, at most 200 characters, that tells the user the brutal truth about what went wrong — and makes them laugh.

## The line

> Your file didn’t save — the disk is full. Your work now lives only in our thoughts and prayers. Free up some space and try again.

## Why it works

- **Names the real failure in plain words:** the save failed because the disk is full — no vague "something went wrong".
- **Funny on a single read:** "your work now lives only in our thoughts and prayers" is a twist a reader repeats out loud to a colleague.
- **Tells the user what to do next:** free up some space and try again.
- **Shippable in a real dialog:** blunt and honest, but polite enough that a team could paste it into a product without embarrassment.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` is fully deterministic — no network, no randomness, no environment reads — and writes the line to `/output/entry.txt`.
