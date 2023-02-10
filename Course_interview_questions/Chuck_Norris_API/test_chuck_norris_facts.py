import json
import time

import requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestChuckNorrisRequests:
    @classmethod
    def setup_class(cls):
        global driver
        global url
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        url = "https://api.chucknorris.io/jokes/"

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_category_list(self):
        value = 'categories'
        response = requests.get(url + value)
        response_json = response.json()
        print(json.dumps(response_json, indent=1))

    def test_search_repository(self):
        search_size_bo = self.get_search_size('Barack Obama')
        search_size_cs = self.get_search_size('Charlie Sheen')
        if search_size_bo > search_size_cs:
            print(f"Bark Obama have more search results: {search_size_bo} then Charly Sheen: {search_size_cs}")
        elif search_size_cs > search_size_bo:
            print(f"Charly Sheen have more search results: {search_size_cs} then Bark Obama: {search_size_bo}")
        else:
            print(f"Charly Sheen and Bark Obama have the same number of search results : {search_size_bo}")

    def get_search_size(self, search_query):
        value = 'search'
        params = dict(query=search_query)
        response = requests.get(url + value, params)
        return response.json()['total']

    def test_random_chucknorris(self):
        file = open("chuck_norris_jokes.txt", "w")
        i = 0
        num = 1
        while 0 <= i <= 9:
            value = 'random'
            response = requests.get(url + value)
            # print(response.json()['value'])
            file.write(str(num) + ". ")
            file.write(response.json()['value'] + "\n")
            num += 1
            i += 1

    def test_random_by_category_chucknorris(self):
        value = 'random'
        params = dict(category='movie')
        response = requests.get(url + value, params)
        joke_url = response.json()['url']
        joke = response.json()['value']
        driver.get(joke_url)
        html_joke = driver.find_element(By.ID, "joke_value")
        assert joke == html_joke.text