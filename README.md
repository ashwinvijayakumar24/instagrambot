# Instagram Bot

### What it does:

This bot logs in to your Instagram page (give it your username and password) and searches for posts with any tag of your liking. Then, the bot automatically
likes all of the posts associated with the tags. This bot can help you grow your followers and also just help support other creators' posts.

### How it works:

This bot was created using the Python programming language and uses Selenium, a set of libraries used to automate tasks and interact with browsers.
The program also uses Google Chrome as the browser needed to log in to Instagram

### Installations required:

You need to install 4 things prior to using this program:

- A Web browser (Google Chrome, Firefox, Microsoft Edge etc..)
- The lastest version of Python
- A driver to connect the program to the Web browser (I'll go more in depth on this later)
- Selenium (only after Python is downloaded as you need to use the integrated Python pip installer for selenium)

##### Web Browser:

    Easiest to install: type the browser of your choice into your search bar and install it if it's not already.
    I recommend Google Chrome, Firefox, Edge, Opera, or Safari if you are on a MacOS system

##### Python:

    Go to https://www.python.org and download the latest version available for your operating system. During the setup instructions,
    make sure to add Python to your PATH (it should be a checkbox during the setup installation).

##### Driver:

    This might get a bit complicated, so pay attention: A webdriver is used to connect your selenium program to the Web browser of your choice.
    This is how the program will be able to access the web browser. There are different drivers depending on what Web browser you installed. For
    all of these, install the version that supports your Web browser version and your operating system

    Google Chrome: https://chromedriver.chromium.org/downloads
    Microsoft Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
    Firefox: https://github.com/mozilla/geckodriver/releases
    Opera: https://github.com/operasoftware/operachromiumdriver/releases
    Safari: Enable webdriver extension on your macOS device (You can look more into this topic for more instructions)


    *Note: I did not work with macOS, so please disregard the next part as it only applies to Windows. Please search up more details on how this all works on macOS*


    After you have downloaded the necessary webdriver, unzip the file in your Downloads folder (or wherever you saved it) and extract the executable
    file from it (should be something like chromedriver.exe). Then go to your AppData folder (you can type in %appdata% in the Windows search bar to reach this
    folder) and then go to AppData > Local > Programs > Python > yourpythonversion and once you reach this folder, (copy and paste your driver into the folder.

    *If for some reason this doesn't work or you get lost, there are many articles and videos online to help you in this process

##### Selnium:

    Now after you have done all of this, you can then clone the instagram_bot.py file into a folder in your system or just copy and paste the contents. Then you can
    go to your command prompt or terminal, cd into the directory you are in, and type in "pip install selenium" and press enter. Remember to have Python installed
    before you do this. After the installation is complete, congratulations! You have everything you need to use this project.

### How to use the bot:

Now that you have installed everything, you can finally dabble with the code.

- First off: on line 9, you can change the webdriver.Chrome() to the Web browser that you have (ex. webdriver.FireFox(), webdriver.Edge() etc..)
- Secondly: on line 49 where a make a new instance of the InstaBot class, you can change the arguments of "yourusername" and "yourpassword" into the
  username and password of the account you want to use.
- Finally: on line 51, you can change the argument for the search_for_posts() method into any tag you want (ex. 'programming')

### Running the bot:

After you have modified the program to your needs, you can just run the file in your terminal and it should work. You can run it in the background and it will
work.

## Contact my email @24ashwinv@gmail.com or dm me at @thefamashwin on Instagram for any questions or to let me know if there is an error with the code
