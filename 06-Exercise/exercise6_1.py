# Exercise 06

# Create a module containing a class with the following methods:
# import webget
import pandas as pd
from requests import get  # to make GET request
from concurrent.futures import ThreadPoolExecutor
import requests


class NotFoundException(ValueError):
    """Raised when the url returns value 404"""

    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)


class Exercise6_1:
    # 1. init(self, url_list)
    def __init__(self, url_list):
        self.url_list = url_list
        self.filenames = []

    # 4. iter() returns an iterator
    def __iter__(self):
        self.index = 0
        return self

    # 5. next() returns each of the downloaded files
    def __next__(self):
        index = self.index
        if index >= len(self.url_list):
            raise StopIteration

        self.index = index + 1
        return self.url_list[index]

    # 2. download(url, filename) raises NotFoundException when url returns 404
    # What is NotFoundException ???
    def download(self, url, filename):
        print("url", url)
        print("filename", filename)
        # open in binary mode
        with open(filename, "wb") as file:
            # get request
            try:
                r = requests.get(url)
                if r.status_code == 404:
                    raise NotFoundException("URL: ", url, " is not working. Status code 404")
                # write to file
                file.write(r.content)
                print("file downloaded")
            except ConnectionError as ex:
                print(ex)
            except NotFoundException as ex:
                print(ex)
            except Exception as ex:
                print(ex)

    # 3. multi_download(url_list) uses threads to download multiple urls as text and stores filenames as a property
    def multi_download(self, url_list):
        workers = 4
        with ThreadPoolExecutor(workers) as ex:
            urls = [url_list[x] for x in range(len(url_list))]
            filenames = [str(y)+".txt" for y in range(len(url_list))]
            ex.map(self.download, urls, filenames)
        return self.filenames

    # 6. filelist_generator(url_list) returns a generator to loop through the filenames
    def filelist_generator(self, ):
        pass

    # 7. avg_vowels(text) - a rough estimate on readability returns average number of vowels in the words of the text
    def avg_vowels(self, text):
        pass

    # 8. hardest_read() returns the filename of the text with the highest vowel score(use all the cpu cores on the computer for this work.
    def hardest_read(self):
        pass


if __name__ == '__main__':

    iterable = Exercise6_1(["url1", "Url2"])

    my_iterator = iter(iterable)
    while True:
        try:
            # get the next item
            element = next(my_iterator)
            print(element)
            # do something with element
        except StopIteration:
            # if StopIteration is raised, break from loop
            break

    filing = Exercise6_1([])

    url = "https://www.gutenberg.org/files/1342/1342-0.txt"
    url2 = "https://www.gutenberg.org/files/1343/1343-0.txt"
    url3 = "https://www.gutenberg.org/files/1344/1344-0.txt"

    url_list = [url, url2, url3]
    reslist = filing.multi_download(url_list)
    print("list of filenames: ", reslist)
    # filing.download(url, "1342-0.txt")
