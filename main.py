import csv
from playwright.sync_api import sync_playwright


def extractStats(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # Set headless=False to watch the browser actions
        page = browser.new_page()
        page.goto(url)
        # Wait for dynamic content to load if necessary
        # page.wait_for_selector('some_selector_that_loads_last')
        try:
            likes = page.locator('[data-e2e="like-count"]').first.text_content()
        except Exception:
            likes = '0'
        print('likes', likes)
        try:
            comments = page.locator('[data-e2e="comment-count"]').first.text_content()
        except Exception:
            comments = '0'
        print('comments', comments)
        try:
            shares = page.locator('[data-e2e="share-count"]').first.text_content()
        except Exception:
            shares = '0'
        print('shares', shares)
        try:
            others = page.locator('[data-e2e="undefined-count"]').first.text_content()
        except Exception:
            others = '0'
        print('others', others)
        browser.close()
        return {'likes': likes, 'comments': comments, 'shares': shares, 'others': others}


def main():
    with open('user.csv', newline='', encoding='utf-8') as infile, \
         open('output.csv', 'w', newline='', encoding='utf-8') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = ['name', 'link', 'likes', 'comments', 'shares', 'others']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        cnt = 0
        for row in reader:
            cnt += 1
            print(f'Processing {cnt}: {row}')
            #if cnt > 4:
            #    break
            name = row['name']
            link = row['link'].strip()
            if not link:
                print(f'Skipping {name}: no link')
                writer.writerow({'name': name, 'link': '', 'likes': '', 'comments': '', 'shares': '', 'others': ''})
                continue
            print(f'Processing {name}: {link}')
            try:
                stats = extractStats(link)
                writer.writerow({'name': name, 'link': link, **stats})
            except Exception as e:
                print(f'Error processing {name}: {e}')
                print('===============\n\n')
                writer.writerow({'name': name, 'link': link, 'likes': 'ERROR', 'comments': 'ERROR', 'shares': 'ERROR', 'others': 'ERROR'})


if __name__ == '__main__':
    main()
