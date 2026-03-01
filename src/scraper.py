from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def scrape_movies():

    # Setup browser
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")  # enable later if needed

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    base_url = "https://www.imdb.com/search/title/?title_type=feature&release_date=2024-01-01,2024-12-31"
    driver.get(base_url)
    time.sleep(5)

    # 🔥 Click "50 more" multiple times
    load_clicks = 5  # 5 clicks ≈ 300 movies

    for i in range(load_clicks):
        try:
            print(f"Clicking 50 more {i+1}")

            # Scroll to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            # Locate the "50 more" span
            load_more = driver.find_element(By.XPATH, "//span[contains(text(),'50 more')]")

            # Click via JS
            driver.execute_script("arguments[0].click();", load_more)

            time.sleep(4)

        except Exception as e:
            print("No more '50 more' button found.")
            break

    # Collect all movie links
    movie_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/title/tt')]")

    all_movies = []
    seen_links = set()

    for element in movie_elements:
        link = element.get_attribute("href")
        title = element.text

        if link and title and link not in seen_links:
            seen_links.add(link)
            all_movies.append((title, link))

    print("\nTotal movies collected:", len(all_movies))

    # 🔥 Now scrape storyline for each movie
    scraped_data = []

    for idx, (title, link) in enumerate(all_movies):
        print(f"Scraping {idx+1}/{len(all_movies)}: {title}")

        driver.get(link)
        time.sleep(2)

        storyline = "Not Found"

        try:
            storyline_element = driver.find_element(By.XPATH, "//span[@data-testid='plot-xl']")
            storyline = storyline_element.text.strip()
        except:
            storyline = "Not Found"

        scraped_data.append({
            "Movie Name": title,
            "Storyline": storyline
        })

    driver.quit()

    df = pd.DataFrame(scraped_data)
    df.to_csv("data/imdb_2024_movies.csv", index=False)

    print("\nCSV saved successfully as imdb_2024_movies.csv")


if __name__ == "__main__":
    scrape_movies()