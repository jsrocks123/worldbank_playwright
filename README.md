# worldbank-playwright

![version](https://img.shields.io/badge/version-0.1.0-blue)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![pre_commit test](https://github.com/jsrocks123/worldbank_playwright/actions/workflows/github-ci.yml/badge.svg)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Demo for WorldBank to show various Playwright concepts using Python

![]()

**Table of Contents**

- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Execution / Usage](#-execution--usage)
- [Viewing Test Results](#-viewing-test-results)
- [Features](#features)

## 🛠️ Tech Stack

| Tool                                                                                                                                                                      | Description                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [Python](https://www.python.org/): ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)                                 | Python programming language                                                                 |
| [allure-pytest](https://pypi.org/project/allure-pytest/)                                                                                                                  | Allure reporting with your Pytest tests for better reporting                                |
| [playwright](https://pypi.org/project/playwright/): ![Playwright](https://img.shields.io/badge/-playwright-%232EAD33?style=for-the-badge&logo=playwright&logoColor=white) | Python library to automate the Chromium, WebKit, and Firefox browsers through a single API. |
| [pytest](https://pypi.org/project/pytest/): ![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3)                 | Popular testing framework for Python                                                        |
| [pytest-playwright](https://pypi.org/project/pytest-playwright/)                                                                                                          | Pytest plugin for Playwright integration for browser automation testing                     |
| [pandas](https://pypi.org/project/pandas/): ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)                  | Python library for data analysis and manipulation                                           |

## ⚙️ Installation

### Clone the project

```bash
git clone https://github.com/jsrocks123/worldbank_playwright
cd worldbank-playwright
```

### Install project dependencies

On macOS and Linux:

```sh
$ pip install poetry
$ poetry shell
$ poetry install
```

On Windows:

```sh
PS> python -m pip install worldbank-playwright
```

### Install playwright

```bash
playwright install
```

## 🏃‍♂️ Execution / Usage

To run worldbank-playwright, fire up a terminal window and run the following command:

```sh
$ pytest -v
```

When no browser was selected then chrome will be used.

## 📊 Viewing Test Results

### Install Allure Commandline To View Test results

#### For Windows:

Follow the instructions [here](https://scoop.sh/) to install Scoop.<br>
Run the following command to install Allure using Scoop:

```bash
scoop install allure
```

#### For Mac:

```bash
brew install allure
```

### View Results Locally:

```bash
allure serve allure-results
```

### View Results Online:

[View allure results via Github pages](https://github.com/jsrocks123/worldbank_playwright)

### View trace results:

1. Navigate to the [Playwright Trace Viewer](https://trace.playwright.dev/)
2. Locate the trace file stored under the test-results folder. This file is generated after running your tests. Click on
   the 'Upload' button in the Playwright Trace Viewer and select your trace file.
3. After uploading, the trace viewer will display a detailed timeline of events that occurred during your test. This
   includes network requests, JavaScript execution, and browser interactions. You can click on individual events for
   more details.

## Features

worldbank-playwright currently has the following set of features:

- Read data from line charts using web scraping
- Read data from table using web scraping
