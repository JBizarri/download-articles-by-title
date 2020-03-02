import threading

from Crawler import Crawler


# TODO: Limit thread number
def create_download_thread(crawler, title):
    download_thread = threading.Thread(target=crawler.search, args=(title,))
    download_thread.start()


# This function will download all PDFs it can to Artigos directory
def download_articles_from(titles_list):
    crawler = Crawler()
    for title in titles_list:
        # download_thread(crawler, title)
        crawler.search(title)
