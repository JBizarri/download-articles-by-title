import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Crawler:
    def __init__(self):
        # Set all the folder structure and variables
        self.root_directory = os.getcwd()
        self.download_directory_name = 'Articles'
        os.makedirs(self.download_directory_name, exist_ok=True)
        self.download_directory = os.path.join(self.root_directory, self.download_directory_name)

        # In case any article fail its title will be stored in this file
        self.fail_file_name = 'fails.txt'

        # Sets all the WebDriver parameters
        self.directory_chromedriver = os.path.join(self.root_directory, 'ChromeDriver', 'chromedriver.exe')
        self.options = Options()
        self.options.add_experimental_option('prefs', {
            "download.default_directory": self.download_directory,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True,
        }
                                             )
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--headless')

    def search(self, query):
        driver = webdriver.Chrome(self.directory_chromedriver, options=self.options)
        url = 'https://sci-hub.tw/'
        driver.get(url)
        search = driver.find_element_by_name('request')
        search.send_keys(query)
        search.send_keys(Keys.ENTER)

        # TODO: Find out why some files can't be downloaded and fix it
        try:
            download_button = driver.find_element_by_xpath('/html/body/div/div/ul/li/a')
            download_button.click()
        except NoSuchElementException:
            print(f"Error: Could not download '{query}'")
            self.write_fails(query)
            return False

        return True

    def write_fails(self, query):
        txt_path = os.path.join(self.download_directory, self.fail_file_name)
        with open(txt_path, 'a') as file:
            file.write(query + '\n')
