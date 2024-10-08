<h1 align="center" >Skirnir</h1>


<p align="center">
  <img src="https://github.com/Hyldem0er/Skirnir/blob/master/data/Skirnir-logo-semi-transparent.png" alt="Profile Icon" width="300px">
</p>

## Introduction

Welcome to Skirnir, a sophisticated Open Source Intelligence (OSINT) tool designed to empower your online presence discovery. In the digital era, maintaining awareness of your footprint across popular social networks is crucial. Skirnir is specialized in scraping platforms like Instagram, Facebook, Twitter, and LinkedIn to uncover any trace of your online identity or lost accounts.

### Key Features

* **Surface crawl**: Utilize various queries of firstname, lastname, diminutives, nicknames and keyword  to crawl Google.
* **Deepcrawl**: Perform in-depth searches to reveal private or deleted profiles using thousands of generated nicknames. 
* **Customizable Settings**: Customize your search with advanced options, including deepcrawl preferences, network selection and length of generated nicknames.
* **Intuitive Interface**: Skirnir's user-friendly interface simplifies the process of refining and filtering search results.
* **CLI**:  Command Line Interface is also available for nerds experienced users.
* **Proxy Handling**: Import your own proxies (public/private) in Skirnir.


**Please remember that Skirnir is intended for educational purposes only.**

## Screenshot
<p align="center">
  <img src="https://github.com/Hyldem0er/Skirnir/blob/905af69f5fbe94bdadb1e706fcb4b09a988fd90e/data/skirnir.png" alt="Skirnir UI" width="500px">
</p>



## Getting Started

### Create a Python Environment

```bash
python3 -m venv env
```

### Activate the Python Environment

#### Linux/MacOS

```bash
source env/bin/activate
```

#### Windows

```powershell
.\env\Scripts\activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Launch the Skirnir Program (User Interface)

#### Linux/MacOS

```bash
python3 main.py --ui
```

#### Windows

```powershell
.\env\Scripts\python.exe main.py --ui
```

## Documentation
You can have a look at the documentation here: [Wiki](https://hyldem0er.gitbook.io/skirnir/)
## License
<a id="licence"></a>
This project is distributed under the [GNU General Public License version 3(GNU GPLv3)](LICENSE).
