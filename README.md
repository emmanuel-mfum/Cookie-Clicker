# Cookie-Clicker
Python bot that plays the online game Cookie clicker in an automated way

The cookie-clicker game is an online game where the player has to click a cookie as much as he can in order to increase his cookie count.
As the cookie count increases,the player can buy up items on the right of the screen, that will allow him to produce more cookies (and therefore increase his
cookie count).

This program will first go to the website of the game (http://orteil.dashnet.org/experiments/cookie/) via the Selenium webdriver for Chrome. We find the cookie on the page
as well as all the ids for the options on the right. We also set two time markers, one for 5 seconds after current time and one for 5 minutes after current time.

We then enter inside the main loop ( a while loop), where click on the cookie on the screen and  check to see if the five seconds set earlier  have passed.
After the five seconds mark, we stop clicking on the cookie for a short while and we get all the prices for the items listed on the right by using again Selenium.
The prices found are then converted into integers and added into a dictionary (the key is the price and the value is the name of the option).

The next step is to get from the website our current cookie count, convert it into an integer.

Following that, we make a dictionary of all the options which we can currently afford and for every item iside our dictionary of prices, we compare the price
of each item to our current cookie avount and if that price is lower than our count, we store the name of the corresponding option's name into a dictionary where 
the key is the price and the value is the name of the option.

Of that new dictionary we find the item with the highest key (price) an retrieve its value (the name of the most expensive, but affordable option).
We can therefore search across the game page for the element whose id attribut is the same as the name we have just retrieved. We then click on what is 
the most expensive and affordable option.

Afterwards, we add another 5 seconds to our time marker in order to click again on the cookie on the website.

The while will therefore continue running until we reach the five-minute time marker. When that happens, we get the our final score (the cookie count) from the web page
and we print it inside the Pycharm console.

