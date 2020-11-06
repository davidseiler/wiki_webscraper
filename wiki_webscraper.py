from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import os


# ###### GLOBALS #######
DIR_NAME = os.getcwd()
BASE_URL = "https://ageofempires.fandom.com/wiki/Units_(Age_of_Empires_III)"


# Setup firefox webdriver
def start_webdriver():
    options = Options()
    # options.headless = True   # headless just for testing purposes
    driver = webdriver.Firefox(options=options)
    return driver


# Setup output file
def get_output_file():
    curr_time = datetime.now()
    output_file_name = curr_time.strftime("%d/%m/%Y-%H:%M:%S Unit Stats.csv")
    output_file = os.path.join(DIR_NAME, output_file_name)
    return output_file


# Get unit/building stats
def get_unit_stats(url, driver):
    stats = ""
    # TODO implement
    return stats


# Write to output file
def write_output(output_file, data):
    # TODO measure the performance impact of using this function instead of just keeping the file open while webscraping
    file = open(output_file, encoding='utf-8', mode='a')
    file.write(data)
    file.close()


# Start scraping
def start_scraping():
    # TODO implement
    pass




# TESTS
get_output_file()
start_webdriver()





