''' s '''
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://reference.medscape.com/drug-interactionchecker")

alphabets = list("abcdefghijklmnopqrstuvwxyz")

driver.find_element(
    By.XPATH, "/html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/button[1]").send_keys(Keys.ENTER)

for alphabet in alphabets:
    while True:
        try:
            search_input = driver.find_element(By.ID, "MDICtextbox")
            search_input.send_keys(alphabet)
            time.sleep(10)
            ul = driver.find_element(By.ID, "MDICdrugs")
            li_lst = ul.find_elements(By.XPATH, "./li")
            res = []
            for li in li_lst:
                source = li.find_element(By.XPATH, "./a").get_attribute("href")
                parts = source.split("submdic('")

                key = parts[1].split("'")[0]
                abbreviation = parts[1].split("'")[2]
                name = parts[1].split("'")[4]
                link = f"https://reference.medscape.com/drug/{key}"

                print(source)
                print(key)
                print(abbreviation)
                print(name)
                print(link)

                temp = {
                    "source": source,
                    "key": key,
                    "abbreviation": abbreviation,
                    "name": name,
                    "link": link
                }
                res.append(temp)

            #
            json_object = json.dumps(res, indent=4)
            with open(f"./data/{alphabet}.json", "w", encoding="utf-8") as outfile:
                outfile.write(json_object)

            search_input.clear()
            break
        except Exception as error:
            print(error)
            continue
