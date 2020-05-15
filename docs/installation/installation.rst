
How to install occpollution and make it work properly
===========================

.. role:: bash(code)
   :language: bash


Install from github occpollution package
-----------------------------------

In order to install this package, you can simply put in a prompt:

.. code-block:: bash

    $ pip install git+https://github.com/Megdie/occpollution

I recommand to clone the entire folder, and then install it (git must be functionnal on your computer): 

.. code-block:: bash

    $ git clone https://github.com/Megdie/occpollution
    $ pip install /path/to/occpollution


ChromeDriver - Webdriver for Chrome
----------------------------

In most parts of our code, we use the module `selenium` allowing us to control the web through Python.
We chose Chrome so you need to install a very important file to manage to run this package. 
ChromeDriver is a separate executable that Selenium WebDriver uses to control Chrome. 
It is maintained by the Chromium team with help from WebDriver contributors. 
If you are unfamiliar with Selenium WebDriver, you should check out `the Selenium site`_.
If you already have ChromeDriver, you should still read the following steps to make sure everything is okay:

.. _ the Selenium site: https://www.selenium.dev/

- Ensure Chromium/Google Chrome is installed in a recognized location (identify carefully his PATH)
- Include the Chrome location in your PATH environment variable
- Then, check Google's version of your computer so you can know which version of chromedriver you must install
- Go to `this website`_ to find your own ChromeDriver file
- Help WebDriver find the downloaded ChromeDriver executable: 

.. _this website: https://chromedriver.chromium.org/downloads


Any of these steps should do the trick:
  - include the ChromeDriver location in your PATH environment variable
  - (Python only) include the path to ChromeDriver when instantiating webdriver.Chrome

Please find through `this link`_ a good explanation (by Tanguy Lefort) to include some executables in your PATH environment variable: 

.. _this link: https://github.com/bcharlier/HMMA238/blob/master/Vscode_windows.md