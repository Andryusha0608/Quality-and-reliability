import csv
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

import Xpath

driver = webdriver.Chrome(
    executable_path="C:\\Users\\andre\\PycharmProjects\\Quality and reliability (Selenium)\\chromedriver\\chromedriver.exe")

assert_titles, assert_ratings, assert_genres, assert_descriptions, assert_views, assert_popularity, assert_age, \
assert_duration, assert_u_reviews, assert_c_reviews, assert_original_titles = [], [], [], [], [], [], [], [], [], [], []
with open("films.csv", 'r', newline='', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        assert_titles.append(row['Название фильма'])
        assert_original_titles.append(row['Оригинальное название фильма'])
        assert_ratings.append(row['Рейтинг'])
        assert_genres.append(row['Жанр'])
        assert_descriptions.append(row['Описание'])
        assert_views.append(row['Количество просмотров'])
        assert_popularity.append(row['Популярность'])
        assert_age.append(row['Возрастное ограничение'])
        assert_duration.append(row['Продолжительность фильма'])
        assert_u_reviews.append(row['Количество отзывов пользователей'])
        assert_c_reviews.append(row['Количество отзывов критиков'])
    # print(
    #     f'Названия: {assert_titles}\nОригинальные названия: {assert_original_titles}\nРейтинг: {assert_ratings}\nЖанры: {assert_genres}\nОписания: {assert_descriptions}\nПросмотров:'
    #     f' {assert_views}\nПопулярность: {assert_popularity}\nВозрастные ограничения: {assert_age}\nПродолжительность фильмов: '
    #     f'{assert_duration}\nОтзывы пользователей: {assert_u_reviews}\nОтзывы критиков: {assert_c_reviews}')


class TestIMBD(unittest.TestCase):

    def test_home_page(self):
        driver.get(url="https://www.imdb.com/chart/top/?ref_=nv_mv_250")
        for i in range(len(assert_titles)):
            self.assertEqual(driver.find_element(By.XPATH,
                                                 f"/html/body/div[2]/div/div[2]/div[3]/div/div[1]/div/"
                                                 f"span/div/div/div[3]/table/tbody/tr[{i + 1}]/td[2]").text,
                             assert_titles[i])
            self.assertEqual(driver.find_element(By.XPATH,
                                                 f'/html/body/div[2]/div/div[2]/div[3]/div/div[1]/div/'
                                                 f'span/div/div/div[3]/table/tbody/tr[{i + 1}]/td[3]/strong').text,
                             assert_ratings[i])

    def test_secondary_page(self):
        driver.get(
            url="https://www.imdb.com/title/tt0892769/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=7EMAJ2J2SE4PJS0AD8CD&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_202")

        self.assertEqual(driver.find_element(By.CSS_SELECTOR, Xpath.orig_path).text[16:].replace("\n", ''),
                         assert_original_titles[201])
        self.assertEqual(driver.find_element(By.XPATH, Xpath.genre_path).text.replace("\n", "/"), assert_genres[201])

        self.assertEqual(driver.find_element(By.TAG_NAME, "p").text, assert_descriptions[201])

        self.assertEqual(driver.find_element(By.CSS_SELECTOR, Xpath.view_path).text, assert_views[201])

        self.assertEqual(driver.find_element(By.CSS_SELECTOR, Xpath.popularity_path).text, assert_popularity[201])

        self.assertEqual(driver.find_element(By.XPATH, Xpath.li2).text, assert_age[201])

        self.assertEqual(driver.find_element(By.XPATH, Xpath.li3).text, assert_duration[201])

        self.assertEqual(driver.find_element(By.XPATH, Xpath.u_rev_path).text, assert_u_reviews[201])

        self.assertEqual(driver.find_element(By.XPATH, Xpath.c_rev_path).text, assert_c_reviews[201])


if __name__ == '__main__':
    unittest.main()
