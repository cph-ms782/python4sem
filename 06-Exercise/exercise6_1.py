# Exercise 06

# Create a module containing a class with the following methods:
# import webget
# import NotFoundException
import pandas as pd
from requests import get  # to make GET request


class Exercise6_1:
    # 1. init(self, url_list)
    def __init__(self, url_list):
        self.url_list = url_list

    # 5. urlist_iterator(url_list) returns an iterator to loop through the urls in the list
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        index = self.index
        if index >= len(self.url_list):
            raise StopIteration

        self.index = index + 1
        return self.url_list[index]

    # 2. download(url, filename) raises NotFoundException when url returns 404
    def download(self, url, filename):
        print("url", url)
        print("filename", filename)
        # open in binary mode
        with open(filename, "wb") as file:
            # get request
            try:
                response = get(url)
                # write to file
                file.write(response.content)
                print("file downloaded")
            except:
                print("NotFoundException")

    # 3. multi_download(url_list) uses threads to download multiple urls as text and stores filenames as a property
    def multi_download(self, url_list):
        with ThreadPoolExecutor(workers) as ex:
            res = ex.map(self.download(url, index), range(4), 4)
        return list(res)

    # # 4. urlist_generator(url_list) returns a generator to loop through the filenames
    # def urlist_generator(url_list):
    #     pass

    # 6. load_files() returns generator to yield each of the downloaded files
    def load_files(self):
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
    url = "https://www.gutenberg.org/files/1342/1342-0.txt"

    filing = Exercise6_1([])
    filing.download(url, "1342-0.txt")
