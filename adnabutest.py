from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Create report file
report = open("test_report.txt", "w")

# Launch browser
driver = webdriver.Firefox()
driver.maximize_window()

# Open website
driver.get("https://adnabu-store-assignment1.myshopify.com/")

# Enter store password
password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "password"))
)

password_field.send_keys("AdNabuQA")

enter_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)

enter_button.click()

print("STEP 1: Website opened successfully")
report.write("STEP 1: Website opened successfully\n")

# Search for product
search_icon = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[contains(@class,'icon-search')]")
    )
)

search_icon.click()

search_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@type='search']")
    )
)

search_field.send_keys("Selling Plans Ski Wax")

print("STEP 2: Product searched successfully")
report.write("STEP 2: Product searched successfully\n")

# Select product from dropdown
dropdown_item = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//div[contains(@class,'predictive-search')]//a[contains(@href,'selling-plans-ski-wax')]"
        )
    )
)

dropdown_item.click()

# Add product to cart
add_to_cart = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "ProductSubmitButton-template--19850788667482__main")
    )
)

add_to_cart.click()

print("STEP 3: Product added to cart successfully")
report.write("STEP 3: Product added to cart successfully\n")

print("TEST PASSED")
report.write("TEST PASSED\n")

# Close report and browser
report.close()
driver.quit()
