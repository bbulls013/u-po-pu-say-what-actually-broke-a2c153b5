# Say What Actually Broke

One line of software error copy for the make.fun bounty
`u-po-pu-say-what-actually-broke-a2c153b5`.

## What it does

`main.py` (Python standard library only) writes a single line to
`/output/entry.txt` and prints it. The run is fully deterministic: no
randomness, no timestamps, no network, no input — the same line every
time.

## The entry line

> The disk is full, so your file is waiting outside in the rain with its suitcase. Free some space and let it back in.

## Why this line

It names the real failure in plain words — the disk is full — instead
of apologising in generalities, and it tells the user exactly what to
do next: free some space and try again. The joke is one image (a file
waiting outside in the rain with its suitcase) that a reader can repeat
to a colleague, and the wording is clean enough to paste into a real
product's error dialog.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py /tmp/out   # writes to a custom output directory
```

## License

MIT — see `LICENSE`.
