# Import the necessary modules from Selenium
from selenium import webdriver  # Allows you to launch/initialize a browser.
from selenium.webdriver.common.keys import Keys  # Provides keys in the keyboard like RETURN, F1, ALT, etc.
from selenium.webdriver.common.by import By  # Enables locating elements by their attributes.
import time  # Import the 'time' library for time-related tasks.
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL of the page with the form
form_url = 'https://qavalidation.com/demo-form/'  # The URL of the web form you want to fill out.

# Form data
first_name = 'William'  # The name to be filled in the form.
last_name = 'Odumah'
full_name = 'William Odumah'
email = 'williamodumah@gmail.com'  # The email to be filled in the form.
gender = 'Male'
phone_number = '2046982982'
street = '2815 Pembina Highway'
city = 'Winnipeg'
state = 'Manitoba'
country = 'Canada'
postal_code = 'R3T4Y8'
your_message = 'This is a test message.'  # The message to be filled in the form.

# Initialize WebDriver
driver = webdriver.Chrome()  # Initialize a Chrome browser session using Selenium WebDriver.


def fill_form():
    # Function to fill out the form
    driver.get(form_url)  # WebDriver navigates to the form URL.
    
    # # Wait for the element to be loaded and visible
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "u_Ddc_4607"))
    # )

    # Locate form fields by their name, ID, or other attributes
    
    # firstname_field = driver.find_element(By.ID, 'u_Ddc_4607')  # Find the name input field by its ID.
    # lastname_field = driver.find_element(By.ID, 'u_Ddc_338354')
    
    fullname_field = driver.find_element(By.ID, 'g4072-fullname')
    email_field = driver.find_element(By.ID, 'g4072-email')  # Find the email input field by its ID.
    phone_field = driver.find_element(By.ID, 'g4072-phonenumber')
    
    # gender = Select(driver.find_element(By.ID, 'g4072-gender-button'))
    # QA_tools = Select(driver.find_element(By.ID, 'g4072-qatools-button'))
    
    message_field = driver.find_element(By.ID, 'contact-form-comment-g4072-otherdetails')  # Find the message textarea by its ID.
    # submit_button = driver.find_element(By.ID, 'submit_button_id')  # Find the form's submit button by its ID.
    submit_button = driver.find_element(By.CLASS_NAME, 'wp-block-button__link')
    
    # Fill out the form
    # firstname_field.send_keys(first_name)  # Enter 'your_name' into the name field.
    # lastname_field.send_keys(last_name)  # Enter 'your_name' into the name field.
    fullname_field.send_keys(full_name)
    email_field.send_keys(email)  # Enter 'your_email' into the email field.
    phone_field.send_keys(phone_number)
    
    # gender.select_by_visible_text('Male')
    # QA_tools.select_by_visible_text('Selenium')
    
    message_field.send_keys(your_message)  # Enter 'your_message' into the message field.
    
    # Submit the form
    submit_button.click()   # Click the submit button to send the form.


def main():
    # Main function to execute the script
    fill_form()  # Call the function to fill the form.
    time.sleep(5)  # Pause the execution for 5 seconds so you can observe the results.
    driver.quit()  # Close the browser window and end the WebDriver session.

if __name__ == "__main__":
    main()  # Execute the main function when the script is run.
