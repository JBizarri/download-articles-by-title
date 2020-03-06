from concurrent.futures.thread import ThreadPoolExecutor

from Crawler import Crawler


# This function will download all PDFs it can to Articles directory
def download_articles_from(titles_list):
    crawler = Crawler()
    print("Starting download")
    pool = ThreadPoolExecutor(max_workers=5)
    for title in titles_list:
        pool.submit(crawler.search, title)

    pool.shutdown(wait=True)
    crawler.write_fails()
