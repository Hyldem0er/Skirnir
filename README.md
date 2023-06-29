<h1 align="center" >Skirnir</h1>


<p align="center">
  <img src="https://github.com/Hyldem0er/Skirnir/blob/master/data/Skirnir-transparent.png" alt="Profile Icon" width="300px">
</p>

#
## Table of contents

- [Setup](#installation)
- [Running the Program](#running-the-program)
- [Interface](#interface)
- [License](#licence)


Skirnir is a program specifically developed to scan popular social networks like Instagram, Facebook, Twitter, and LinkedIn in order to identify any remnants of your online presence or any lost accounts. It conducts searches using various combinations of your name, last name, birthdate, and pseudo. 

#

# Usage

<a id="installation"></a>
## Setup

To install the required dependencies, run the following command:

```shell
pip install -r requirements.txt
```
<a id="running-the-Program"></a>
## Running the Program

To launch the program, navigate to the project directory and run the following command: 
```shell
python main.py
```
<a id="interface"></a>
## Interface

- **Search Form**

    - **Firstname** : Enter your first name (no accented letters). If your first name is composed of multiple parts, you can separate them with a "-" or a space.
    - **Lastname** : Enter your last name (still no accented letters).
    - **Toggle Birthday** : By default, this option is enabled. You can disable it to decrease the number of generated nicknames.
    - **Search only the pseudo** : Enabling this option will reduce search time by focusing only on the provided pseudo.
    - **Pseudo** : Enter your desired pseudo. If you want to try different combinations with delimiters such as "-", "_", or ".", you can include spaces between parts of the pseudo.

- **Advanced settings**

    - **Surface Crawl Only** : If selected, the program will perform a surface crawl by searching Google and DuckDuckGo results with certain criteria to find the most relevant profiles. This method may sometimes uncover private accounts or deleted profiles. If this option is not selected, the program will perform a "deep crawl" search.
    
- **Social Networks**

    By default, all four social networks are selected. You can choose to search for your profile on specific social networks by selecting the corresponding checkboxes.

- **Deepcrawl**

    Deepcrawl is the default search method. It generates multiple nicknames based on the information provided in the search form fields and the size limit set using the horizontal scroll bar. Currently, only Instagram is deepcrawled. Given that Facebook is owned by Meta, it is possible that the pseudonyms validated during the Instagram deepcrawl also exist on Facebook. These URLs will appear in red, which means that the link will not necessarily work. For Twitter and LinkedIn, only the surface exploration results will be displayed. However, Skirnir crawl duckduckgo, some accounts that have existed or passed private can be found. To obtain more results, you can try running the program again with the "surface crawl only" option, which will complete in just a few seconds.

- **Filter search bar**

    A filter search bar will appear at the top of the result window. You can use it to refine the results if they are not as relevant as expected. The filter will only display results that exactly match your input. Please exercise caution when using this feature.

**Please remember that Skirnir is intended for educational purposes only.**

<a id="licence"></a>
## License

This project is distributed under the [GNU General Public License version 3(GNU GPLv3)](LICENSE).
