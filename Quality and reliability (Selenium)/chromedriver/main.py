import csv

import Xpath
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

titles, ratings, urls, genres, descriptions, views, popularity,\
age, duration, u_reviews, c_reviews, original_titles, results = [], [], [], [], [], [], [], [], [], [], [], [], []

driver = webdriver.Chrome(
    executable_path="C:\\Users\\andre\\PycharmProjects\\Quality and reliability (Selenium)\\chromedriver\\chromedriver.exe")

try:
    driver.get(url=url)
    title_film = driver.find_elements(By.CLASS_NAME, 'titleColumn')
    for film in title_film:
        titles.append(film.text)

    rating_film = driver.find_elements(By.TAG_NAME, 'strong')
    for rate in rating_film:
        ratings.append(rate.text)

    url_film = driver.find_element(By.TAG_NAME, 'tbody')
    URL = url_film.find_elements(By.TAG_NAME, 'a')
    for url in URL:
        if url.get_attribute("href") not in urls:
            urls.append(url.get_attribute("href"))

    for u in range(len(urls)):
        driver.get(url=urls[u])

        if len(driver.find_elements(By.CSS_SELECTOR, Xpath.orig_path)) > 0:
            original_title = driver.find_element(By.CSS_SELECTOR, Xpath.orig_path)
            original_titles.append(
                original_title.text[16:].replace("\n", ''))
        else:
            original_titles.append("-")

        genre_film = driver.find_element(By.XPATH, Xpath.genre_path)
        genres.append(genre_film.text.replace("\n", '/'))

        description_film = driver.find_element(By.TAG_NAME, "p")

        descriptions.append(
            description_film.text)

        view_film = driver.find_element(By.CSS_SELECTOR, Xpath.view_path)

        views.append(view_film.text)

        if len(driver.find_elements(By.CSS_SELECTOR, Xpath.popularity_path)) > 0:
            popularity_film = driver.find_element(By.CSS_SELECTOR, Xpath.popularity_path)
            popularity.append(popularity_film.text)
        else:
            popularity.append('-')

        if len(driver.find_elements(By.XPATH, Xpath.li3)) > 0:
            age_film = driver.find_element(By.XPATH, Xpath.li2)
            age.append(age_film.text)

            duration_film = driver.find_element(By.XPATH, Xpath.li3)
            duration.append(duration_film.text)

        else:
            age.append("-")

            duration_film = driver.find_element(By.XPATH, Xpath.li2)
            duration.append(duration_film.text)

        u_review_film = driver.find_element(By.XPATH, Xpath.u_rev_path)
        u_reviews.append(u_review_film.text)

        c_review_film = driver.find_element(By.XPATH, Xpath.c_rev_path)
        c_reviews.append(c_review_film.text)

    print(
        f'???????????????????????? ????????????????: {original_titles}\n??????????: {genres}\n????????????????: {descriptions}\n????????????????????: {views}\n????????????????????????: {popularity}\n???????????????????? ??????????????????????: {age}\n?????????????????????????????????? ??????????????: {duration}\n???????????? ??????????????????????????: {u_reviews}\n???????????? ????????????????: {c_reviews}')

    for i in range(len(titles)):
        results.append({
            '????????????????': titles[i],
            '???????????????????????? ????????????????': original_titles[i],
            '??????????????': ratings[i],
            '????????': genres[i],
            '????????????????': descriptions[i],
            '???????????????????? ????????????????????': views[i],
            '????????????????????????': popularity[i],
            '???????????????????? ??????????????????????': age[i],
            '?????????????????????????????????? ????????????': duration[i],
            '?????????????? ??????????????????????????': u_reviews[i],
            '?????????????? ????????????????': c_reviews[i]
        })

    # print(results)

    # ???????????? ?? ??????????????
    with open("films.csv", 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(('???????????????? ????????????', '???????????????????????? ???????????????? ????????????', '??????????????', '????????', '????????????????',
                         '???????????????????? ????????????????????', '????????????????????????',
                         '???????????????????? ??????????????????????', '?????????????????????????????????? ????????????', '???????????????????? ?????????????? ??????????????????????????',
                         '???????????????????? ?????????????? ????????????????'))

        for res in results:
            writer.writerow(
                (res['????????????????'], res['???????????????????????? ????????????????'], res['??????????????'], res['????????'], res['????????????????'],
                 res['???????????????????? ????????????????????'],
                 res['????????????????????????'], res['???????????????????? ??????????????????????'], res['?????????????????????????????????? ????????????'],
                 res['?????????????? ??????????????????????????'], res['?????????????? ????????????????']))


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
