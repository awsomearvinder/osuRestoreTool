import json
import time
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = input("Input your osu username.")
password = input("Input your osu password.")
user = input("Input your osu user id. (I'm too lazy to automate this)")
count = input("How many of your most played maps do you want to download?")
resp = requests.get(f"https://osu.ppy.sh/users/{user}/beatmapsets/most_played?limit={count}")
json_value = json.loads(resp.text)
driver = webdriver.Firefox()
driver.get("https://osu.ppy.sh/home")
sign_in = driver.find_element_by_class_name("js-user-login--menu")
sign_in.click()
username = driver.find_element_by_name("username")
username.send_keys(username)
password = driver.find_element_by_name("password")
password.send_keys(password)
password.send_keys(Keys.RETURN)
time.sleep(1)

for beatmap in json_value[20:]:
    id = f"{beatmap['beatmapset']['id']}"
    page = driver.get(f"https://osu.ppy.sh/beatmapsets/{id}#osu/{beatmap['beatmap_id']}")
    time.sleep(1)
    btn = driver.find_element_by_class_name("btn-osu-big--beatmapset-header")
    btn.click()