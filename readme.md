Apologies but i can only get to so far on this project within 2 hours
I didnt get chance to write code and do not have any tests


-----Setup of Virtual Environment for python
-----and required dependencies for scrapy -----

We can only use eclipsce when the virtual environment is active
c:\users\sachin
mkdir virtualenvs
cd virtualenvs
\Python27\python -m virtualenv sainsbury
sainsbury\Scripts\activate.bat

cd Scripts
easy_install C:\Users\sachin\downloads\pywin32-220.win-amd64-py2.7.exe
pip install urllib3[secure]
pip install /python27/3rdpartysource/lxml-3.4.4-cp27-none-win_amd64.whl
pip install /python27/3rdpartysource/Scrapy-1.0.4-py2-none-any.whl
scrapy
cd C:\Users\sachin\Sainsbury\Webscraper\desktop\py\scripts
scrapy pricelist
scrapy startproject pricelist
To get list of command history
doskey /history >C:\Users\sachin\Sainsbury\Webscraper\desktop\config\setup.txt

Also to use the project you need to go to scrapy project directory
cd "C:\Users\sachin\Sainsbury\Webscraper\desktop\py\scripts\pricelist\pricelist"

-------------End of setup ------------

---- Psuedo code for Extracting items---
Specify the fields in items
Create Spider
Using Crawling rules to filter out the urls based on the href value
Modify the pipeline

http://doc.scrapy.org/en/latest/intro/tutorial.html#defining-our-item
---- End of Psuedo code ---


Command on shell with logging 

scrapy crawl [spidername]