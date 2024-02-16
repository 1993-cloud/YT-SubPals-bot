from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def subscribe_to_channel(channel_url, num_subscriptions):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(executable_path='C:\path\to\chromedriver.exe')

    try:
        # Open the YouTube channel URL
        driver.get(channel_url)
        time.sleep(2)  # Wait for page to load

        # Locate the subscribe button and click it
        subscribe_btn = driver.find_element_by_xpath('//yt-formatted-string[contains(text(),"Subscribe")]')
        subscribe_btn.click()

        # Wait for the subscription to complete (you can adjust the time as needed)
        time.sleep(5)

        print(f"Subscribed successfully to {channel_url}!")
        print(f"Total subscriptions: {num_subscriptions}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    channel_url = input("Enter the YouTube channel URL: ")
    num_subscriptions = int(input("Enter the desired number of subscriptions: "))
    subscribe_to_channel(channel_url, num_subscriptions)
