# %%
from typing import Text
import requests
response = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1")
#print(response.json())
#print(response.json()["text"])
cat_fact = response.json()["text"]


# %%
