from TopPages import SearchHelper


def chrome_test_topnews(chrome):
    top_news_page = SearchHelper(chrome)
    top_news_page.go_to_site()
    top_news_page.click_on_close_button()


def firefox_test_topnews(firefox):
    top_news_page = SearchHelper(firefox)
    top_news_page.go_to_site()
    top_news_page.click_on_close_button()
