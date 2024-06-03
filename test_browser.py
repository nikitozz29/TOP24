from TopPages import *


def test_chrome_topnews(chrome):
    top_news_page = TopPages(chrome)
    top_news_page.go_to_site()
    top_news_page.click_on_close_button()


def test_firefox_topnews(firefox):
    top_news_page = TopPages(firefox)
    top_news_page.go_to_site()
    top_news_page.click_on_close_button()
