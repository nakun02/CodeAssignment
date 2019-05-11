Few configurations needed to do before running the Assignment:
    1. Download a chromeWebDriver and put this location in Path Variables and also change this line 
           driver = webdriver.Chrome('C:/Users/nakunl/Downloads/chromedriver.exe') in PLotShareHoldings .
     2.  Make sure Python Flask API is running on "http://127.0.0.1:5000" as i have hard-coded the Urls in angular.
     3. I didnt do message parsing and error handling in Angular side.

As part of this assignment i have created two GetAPIs in python where one  is returning me % change in holdings of a stock(passed as a parameter from Client as stockCode) for each Bank for a time period which is also being passed as parameters from the client and the another is returning me the list of Stocks which i load into a drop-down for the user to select.  .

once this is done user select a from and to Date and stock name from the given Drop-down and click on Plot Graph Button which in-turns starts a chromedriver to get the shareholdings using web scraping.

Once i get the above information i do Web scrapping on http://www.hkexnews.hk/sdw/search/searchsdw.aspx using selenium and get the shareHoldings for each and every ID of a bank.

the image in UI will take a bit of time to load as webScraping is time taking Process.it approx. takes around 1-2 miutes to load the image.
image.png


For RestAPI and all other purpose done above i have used FLASK and the filename is stored as  "PLotShareHoldings.py" in my project .

For Trading Strategy i observed few stocks  by taking yahoo finance API
 CodeAssignment.zip
and drew volume and price plot and the chunk of code is available in the same project inside "PlotSharingPrice.py" file.

And i observed that when price moved to a certain point and it need to take a correction after moving in that direction a good volume has been traded . 

Hence my observation is "Bounce Back strategy" is used over here when a stock tried to correct itself after a long run in specific direction.

i couldn't plot for multi stocks as i didn't have the symbol and couldn't find any.
