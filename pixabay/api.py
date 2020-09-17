import os
import requests
import time
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


def get_api():
    api_key = '18254741-ce7f3e60a43d460c4e262ec4f'
    url = "https://pixabay.com/api/"
    query = 'cat'
    PER_PAGE = 200
    image_type = 'dog'

    PARAMS = {'q': query, 'per_page': PER_PAGE, 'page': 1, 'image_type': image_type}
    end_point = url + "?key=" + api_key

    header = {
        'Content-Type': 'application/json',
        'Cache-control': 'no-cache',
    }
    req = requests.get(url=end_point, params=PARAMS, headers=header)
    data = req.json()
    # return data
    print(req.text)
