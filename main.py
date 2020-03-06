from download import download_articles_from
from get_titles import get_titles


def main():
    input("Save a .csv or .xlsx file in the Excel folder\nPress any key to continue when you're finished")
    titles = get_titles()
    download_articles_from(titles)
    print("Done...")


if __name__ == '__main__':
    main()
