# Using the openlibrary API
# https://openlibrary.org/dev/docs/api/authors

import requests

def get_author_works(author_id: str, num_works: int) -> dict:
    url = f"https://openlibrary.org/authors/{author_id}.json?limit={num_works}" 
    response = requests.get(url) 
    return response.json()

# Testing on JK Rowling 
author_data = get_author_works("OL23919A", 1)
print(author_data)
