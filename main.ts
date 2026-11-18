// news-image-20261118 — "The World in One Day"
// make.fun entry: one image summing up Wednesday 18 November 2026.
//
// The picture itself (entry.png, next to this file) is a newspaper front
// page drawn with Python/Pillow from live reporting of the day: US jets
// striking an IRGC missile site on Qeshm Island and five Iranian tankers
// sunk as Iran fired drones at a US radar base in Bahrain, Cyclone Akvan
// bearing down on Andhra Pradesh, Nvidia doubling its revenue, the Kerch
// Bridge hit for a second night, COP31 entering its final days, and Gaza
// facing winter without shelter. The drawing script (draw_news.py) is in
// this repo.
//
// This program only has one job: place that exact image at the output
// path the grader reads, /output/entry.png, byte for byte. It runs twice
// and must produce identical bytes both times, so it copies the file
// instead of redrawing it.
//
// Run locally:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

mkdirSync(outDir, { recursive: true });
const bytes = readFileSync(join(here, "entry.png"));

// The gate only accepts a whole PNG of at most 1 MiB and 1024x1024 px.
// Fail loudly here instead of shipping a bad file: the PNG signature
// must lead the file and the size must stay under the cap.
const PNG_SIGNATURE = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (!bytes.subarray(0, 8).equals(PNG_SIGNATURE)) {
  throw new Error("entry.png is not a PNG file");
}
if (bytes.length > 1048576) {
  throw new Error(`entry.png is ${bytes.length} bytes, over the 1 MiB cap`);
}
writeFileSync(target, bytes);
console.log(`wrote ${target} (${bytes.length} bytes)`);
