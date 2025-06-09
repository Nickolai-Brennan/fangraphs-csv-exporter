import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# ------------------------------
# CONFIG
# ------------------------------
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
URL = 'https://www.fangraphs.com/leaders/major-league?pos=all&stats=bat&lg=all&qual=y&season=2025&season1=2025&ind=0&team=0&type=1&month=0'

# ------------------------------
# Ensure download folder exists
# ------------------------------
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# ------------------------------
# Auto-install ChromeDriver
# ------------------------------
chromedriver_autoinstaller.install()

# ------------------------------
# Set Chrome download preferences
# ------------------------------
options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": DOWNLOAD_FOLDER,
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True
})
options.add_argument("--headless")  # Optional

# ------------------------------
# Launch browser and download
# ------------------------------
driver = webdriver.Chrome(options=options)
driver.get(URL)

time.sleep(5)  # Let page load

try:
    button = driver.find_element(By.XPATH, "//a[contains(text(), 'Export Data')]")
    button.click()
    print("Clicked Export Data")
except Exception as e:
    print("Could not click export:", e)
    driver.quit()
    exit()

# ------------------------------
# Wait for download
# ------------------------------
time.sleep(10)  # Increase if needed

# ------------------------------
# Confirm CSV
# ------------------------------
csv_files = [f for f in os.listdir(DOWNLOAD_FOLDER) if f.endswith(".csv")]
if csv_files:
    print(f"✅ Downloaded: {csv_files[-1]}")
else:
    print("❌ CSV not found.")

driver.quit()
