from selenium.webdriver.common.by import By

def savelinks(driver, output_file):
    links = []
    for a in driver.find_elements(By.XPATH, './/a'):
        href = a.get_attribute('href')
        if href and "google.com" not in href:
            links.append(href)
    links = list(set(links))
    with open(output_file, "a") as file:
        for link in links:
            file.write(link + "\n")
    print(f"{len(links)} valid links appended to '{output_file}'")
    return links
