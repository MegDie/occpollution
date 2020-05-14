
How to install occpollution and make it work properly
===========================

.. role:: bash(code)
   :language: bash



How to install occpollution package 
-----------------------------------

.. _Wikipedia: https://www.wikipedia.org/

`__Wikipedia`

In order to install this package, you can simply put in a prompt:

.. code-block:: bash

    $ pip install git+https://github.com/Megdie/occpollution


ChromeDriver - Webdriver for Chrome
----------------------------

In most parts of our code, we use the module `selenium` allowing us to control the web through Python.
We chose Chrome so you need to install a very important file to manage to run this package. 
ChromeDriver is a separate executable that Selenium WebDriver uses to control Chrome. 
It is maintained by the Chromium team with help from WebDriver contributors. 
If you are unfamiliar with Selenium WebDriver, you should check out the Selenium site.
If you already have ChromeDriver, you should still read the following steps to make sure everything is okay:

- Ensure Chromium/Google Chrome is installed in a recognized location (identify carefully his PATH)
- Include the Chrome location in your PATH environment variable
- Then, check Google's version of your computer so you can know which version of chromedriver you must install
- Go to this website to find your own ChromeDriver file: https://chromedriver.chromium.org/downloads
- Help WebDriver find the downloaded ChromeDriver executable: 

Any of these steps should do the trick:
  - include the ChromeDriver location in your PATH environment variable
  - (Python only) include the path to ChromeDriver when instantiating webdriver.Chrome (see sample below)