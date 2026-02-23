# TikTok Crawl

A simple TikTok video stats scraper using [Playwright](https://playwright.dev/python/).

## What it does

Reads a list of TikTok usernames and video URLs from `user.csv`, fetches engagement stats (likes, comments, shares, others) for each video, and writes the results to `output.csv`.

## Requirements

- Python 3.8+
- [Playwright](https://playwright.dev/python/)

## Installation

```bash
pip install playwright
playwright install chromium
```

## Usage

1. Prepare `user.csv` with two columns: `name` and `link`.

```csv
name,link
username1,https://www.tiktok.com/@username1/video/...
username2,https://www.tiktok.com/@username2/video/...
```

2. Run the script:

```bash
python main.py
```

3. Results will be saved to `output.csv` with columns: `name, link, likes, comments, shares, others`.

## Output Example

`output.csv`:

```csv
name,link,likes,comments,shares,others
mongmer.26,https://www.tiktok.com/@mongmer.26/video/7602194617433328917,12.3K,845,1.2K,0
su.den.roi.day,https://www.tiktok.com/@su.den.roi.day/video/7607841631600905490,8.7K,312,560,0
ghetanpatee,https://vt.tiktok.com/ZSaQbbFbt/,ERROR,ERROR,ERROR,ERROR
nguoi6_thiclamdep,,,,, 
```

| Column | Description |
|--------|-------------|
| `name` | TikTok username from `user.csv` |
| `link` | Video URL from `user.csv` |
| `likes` | Number of likes on the video |
| `comments` | Number of comments |
| `shares` | Number of shares |
| `others` | Other engagement count (e.g. saves) |

> - Empty stats = row had no link in `user.csv`
> - `ERROR` = page failed to load or an unexpected error occurred
> - `0` = page loaded but the stat selector was not found

## Notes

- Rows with an empty `link` are skipped (written with empty stats).
- If fetching stats for a row fails, it is written with `ERROR` in the stats columns.
- Individual stat fields fall back to `0` if the selector is not found on the page.
