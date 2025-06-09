Great — here's how to **automate the CSV download from FanGraphs using Selenium** and make it usable as a **GitHub-hosted project**, so you can version control, share, or run it remotely (with tools like GitHub Actions or Codespaces).

---

## ✅ Step-by-Step: GitHub-Ready Project

---

### 🔧 1. **Project Structure**

```
fangraphs-csv-exporter/
│
├── README.md
├── requirements.txt
├── .gitignore
├── download_fangraphs_csv.py
```

---

### 📄 2. `requirements.txt`

```txt
selenium==4.15.2
```

> You can add `chromedriver-autoinstaller` if you want the script to auto-install ChromeDriver:

```txt
chromedriver-autoinstaller
```

---

### 🐍 3. `download_fangraphs_csv.py`

```python
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
```

---

### 📘 4. `README.md`

````markdown
# 📊 FanGraphs CSV Exporter

A Python script to automatically open the FanGraphs Leaderboard page, click the "Export Data" button, and download the CSV file to a local folder.

## ⚙️ Setup

1. Clone the repo:
```bash
git clone https://github.com/YOURUSERNAME/fangraphs-csv-exporter.git
cd fangraphs-csv-exporter
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python download_fangraphs_csv.py
```

## 📁 Output

The CSV will be saved in the `/downloads` folder created automatically in the project root.

````

---

### 🛡️ 5. `.gitignore`

```gitignore
__pycache__/
downloads/
````

---

### 🚀 Optional: GitHub Actions Integration

If you'd like to automate this on a schedule using **GitHub Actions**, I can provide a `workflow.yml` as well — just say the word.

---

### ✅ Next Steps

1. Ready for me to generate the GitHub repo and zip?
2. Want this connected to Google Drive or auto-pushed to another repo?
3. Want the output CSV uploaded somewhere or renamed?

Let me know and I’ll build that out for you.
