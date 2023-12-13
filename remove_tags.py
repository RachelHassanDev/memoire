from facebook_page_scraper import Facebook_scraper
import json

page_name = "RawbankSa"
posts_count = 10
browser = "firefox"
timeout = 600 #600 seconds
headless = True
meta_ai = Facebook_scraper(page_name, posts_count, browser, timeout=timeout, headless=headless)

json_data = meta_ai.scrap_to_json()
with open("./result.json", "w+", encoding="UTF-8") as myFile:
    myFile.write(json.dumps(json_data))