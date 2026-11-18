# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/rajupramana370/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/rajupramana370/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image that sums up the world's news of **Wednesday, 18 November 2026** — a
newspaper front page drawn in code (Python + Pillow, see `draw_news.py`) from
that day's live reporting.

## The six stories

1. **War drums in the Strait (Middle East)** — US jets struck a Revolutionary
   Guards missile site on Qeshm Island, and Washington said it sank five
   Iranian tankers. Iran fired drones at a US radar base in Bahrain.
2. **Cyclone Akvan bears down (Asia)** — A cyclone strengthening over the Bay
   of Bengal is set to hit the Andhra Pradesh coast on Friday.
3. **Nvidia doubles its revenue (Business)** — Quarterly revenue of $115.8
   billion, up 103% on a year ago, as data-centre sales passed $107 billion.
4. **Kerch Bridge hit again (Europe)** — Ukraine struck the bridge to Crimea
   for a second night running, shutting it down; Russia hit bridges around
   Kyiv in reply.
5. **COP31 enters final days (World)** — Climate talks in Antalya enter their
   decisive phase, with 144 disputed items still on the table.
6. **Gaza faces a cold winter (Middle East)** — The UN warns more people will
   die of cold as winter sets in: 1.7 million remain displaced, most without
   adequate shelter.

Also today: Trump arrives in Manila for Quad talks; India and Japan hold 2+2
talks in Tokyo; Robert Pattinson named the new James Bond; Romania hit by a
5.3-magnitude quake.

Sources: The Daily Short, BBC, Al Jazeera, Reuters, Euronews.

## Run it

```sh
# Redraw the image (needs Python 3 + Pillow + DejaVu fonts)
python3 draw_news.py

# Produce the graded output
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# -> out/entry.png (1024x1024 PNG)
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=raju-pramana&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
