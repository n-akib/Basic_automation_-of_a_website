# 🤖 Basic Automation of a Website

This project demonstrates **UI test automation** using **Python** and **Selenium WebDriver**. It simulates common user actions such as logging in and registering on a website, making it a great base for automated testing practice or real-world use.

---

## 🚀 Features

- 🔹 Automates login and registration workflows  
- 🔹 Uses Selenium WebDriver for browser interaction  
- 🔹 Targets elements using XPath, ID, or CSS selectors  
- 🔹 Supports Chrome browser testing  
- 🔹 Easy-to-understand Python scripts  

---

## 🛠 Tech Stack

- **Python 3.x**  
- **Selenium**  
- **ChromeDriver**  
- *(Optional)* **Pytest**  
- *(Optional)* **virtualenv**

---

## 📁 Project Structure

```
Basic_automation_-of_a_website/
├── login_test.py             # Script to automate login testing
├── registration_test.py      # Script to automate registration flow
└── README.md                 # Project documentation (this file)
```

---

## ✅ Prerequisites

Before running the tests, ensure the following are installed:

- Python 3.x  
- Google Chrome browser  
- ChromeDriver (must be in your system PATH)  

You can download ChromeDriver from:  
https://sites.google.com/a/chromium.org/chromedriver/

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/n-akib/Basic_automation_-of_a_website.git
cd Basic_automation_-of_a_website
```

2. **Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/macOS
source venv/bin/activate
```

3. **Install Required Packages**
```bash
pip install selenium
```

---

## ▶️ How to Run the Scripts

After setup, simply run the scripts with:

```bash
python login_test.py
```

```bash
python registration_test.py
```

Make sure to update the **URL** and form field selectors as needed, based on the site you're testing.

---

## 🔧 Customization

You can adapt this project for other websites by:

- Changing the `url` in each script  
- Updating element locators (XPath, CSS selectors)  
- Adding assertions or validations  
- Incorporating frameworks like `pytest` for structured testing

---

## 💡 Future Improvements

- [ ] Add Pytest support  
- [ ] Add `waits` using `WebDriverWait` for more reliable execution  
- [ ] Integrate logging and screenshots for test reporting

---

## 🧑‍💻 Author

**Nagib Mahfuze Akib**  
💼 [LinkedIn](https://www.linkedin.com/in/nagib-mahfuze-akib)  
📬 n.mahfuze@gmail.com

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).
