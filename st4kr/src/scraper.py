from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils import savelinks

def search_target(driver, target):
    driver.get("https://www.google.com")
    try:
        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Accept')]"))
        ).click()
    except:
        pass

    search_box = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys('"' + target + '"')
    search_box.send_keys(Keys.RETURN)
    print(f"Searching for '{target}' on Google...")

def scroll_and_collect(driver, target, output_file):
    all_links = []
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        page_links = savelinks(driver, output_file)
        all_links.extend(page_links)

        try:
            next_button = driver.find_element(By.ID, "pnnext")
            if next_button.is_displayed() and next_button.is_enabled():
                next_button.click()
                print("Navigating to the next page...")
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div#search"))
                )
            else:
                break
        except:
            break

    return list(set(all_links))
