from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.headless = True
DRIVER_PATH = r"C:\Users\lfbia\Documents\GitHub\pythonWs\mandosBot\geckodriver.exe"

def scrappePrices(de, ate, dayMonthYear1, dayMonthYear2 = None):
    if dayMonthYear2:
        ida = getPrice(dayMonthYear1, de, ate)
        volta = getPrice(dayMonthYear2, ate, de)
        return ida, volta, ida + volta
    else:
        return getPrice(dayMonthYear1, de, ate)

def getPrice(dayMonthYear, de, ate):             #expects input in the dd/mm/yyyy format
    day, month, year = dayMonthYear.split('/')
    driver = webdriver.Firefox(options= options, executable_path=DRIVER_PATH)
    url = 'https://www.latam.com/pt_br/apps/personas/booking?fecha1_dia=%s&fecha1_anomes=%s-%s&fecha2_dia=&fecha2_anomes=&from_city1=%s&to_city1=%s&from_city2=%s&to_city2=%s&ida_vuelta=ida&cabina=Y&nadults=1&nchildren=0&ninfants=0&application=lanpass#/'

    driver.get(url % (day, year, month, de, ate, ate, de))
    time.sleep(5)

    p1Raw = driver.find_element_by_xpath("//button[@class='price-button']").text.split('\n')[1][:-3]
    driver.close()
    return int(p1Raw[:2] + p1Raw[3:])

if __name__ == "__main__":
    print(scrappePrices('LON', 'SAO', '10/10/2021'))
    print(scrappePrices('LON', 'SAO', '10/02/2021'))
    print(scrappePrices('LON', 'SAO', '10/02/2021', '25/02/2021'))
