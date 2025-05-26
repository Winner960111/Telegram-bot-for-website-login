from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

def login_to_website(email, password):
    
  # Set up Chrome options
  # options = Options()
  # options.add_argument("--headless=new")  # Ensure GUI is off
  # options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
  # options.add_argument("--no-sandbox")   # Bypass OS security model
  # options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems

  # Setup Chrome (make sure you have chromedriver installed)
  # driver = webdriver.Chrome(options=options)
  driver = webdriver.Chrome()

  # Open the login page
  driver.get("https://dash.billgang.com/auth/sign-in")
  print("Opened the login page.")
  # Wait for the page to load and the form to appear
  driver.implicitly_wait(10)  # seconds

  # Find the email and password fields (update selectors as needed)
  email_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter your email address']")
  password_input = driver.find_element(By.XPATH, "//input[@placeholder='*****************']")

  print("Found email and password fields.", email_input, password_input)

  # Enter your credentials
  email_input.send_keys(email)
  password_input.send_keys(password)

  # Submit the form (find the submit button and click it)
  submit_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[4]/button")
  print("\nFound submit button.", submit_button)
  submit_button.click()

  sleep(100)  # Wait for a few seconds to ensure the login is processed
  # Wait for the login to complete
  # # Wait for login to complete and get the page source
  # driver.implicitly_wait(10)
  # html = driver.get("https://dash.billgang.com/")

  # # Now you can use BeautifulSoup to parse `html`
  # from bs4 import BeautifulSoup
  # soup = BeautifulSoup(html, 'html.parser')
  # print(soup.prettify())

  # Don't forget to close the browser
  driver.quit()
  return True  # Simulate a successful login