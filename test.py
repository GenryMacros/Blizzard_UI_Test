from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def test_warcraftPage():
    search_request = 'Warrior'
    url = 'https://www.blizzard.com/ru-ru/'


    #geckodriver
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(10)

    browser.get(url)
    browser.find_element_by_css_selector('[class="Navbar-item Navbar-modalToggle is-noSelect Navbar-games"]').click()
    browser.find_element_by_css_selector('[src="https://blznav.akamaized.net/img/games/logo-wow-3dd2cfe06df74407.png"]').click()
    browser.find_element_by_css_selector('[class="SiteNav-menuListItem SiteNav-menuListItem--search List-item"]').click()
    browser.find_element_by_css_selector('[id="searchInput"]').send_keys(search_request)
    browser.find_element_by_css_selector('[id="searchInput"]').send_keys(Keys.ENTER)
    
    actualResult = browser.find_element_by_css_selector('[href="/ru-ru/search/character?q=Warrior"]')

    
    assert actualResult.tag_name == "a"
    assert actualResult.text == "Посмотреть все результаты: 27"

def test_starcraftPage():
    url = 'https://www.blizzard.com/ru-ru/'

    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(10)

    browser.get(url)
    browser.find_element_by_css_selector('[aria-label="Подробнее StarCraft II"]').click()
    browser.find_element_by_css_selector('[class="Navigation-link Navigation-link--main" href="/ru-ru/game"]').click()
    
    actualResult = browser.find_element_by_class_name('PromoIntro-text')

    
    assert actualResult.tag_name == "a"
    assert actualResult.text == "Три расы, четыре режима и бесконечное множество игровых стилей. StarCraft&nbsp;II&nbsp;— венец развития стратегий в реальном времени. Сможете ли вы стать лучшим полководцем в галактике?"


