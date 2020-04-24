# Paper Trading Section


## THIS README IS A BIT OUT OF DATE:

I started shortly after first learning coding.  I have decided to revisit the project and make the program much better and have the repisotrty more optimized for debugging and adding features.

I am doing those first before editting this README, so take all the following text with a grain of salt.
 

## A few notes about the program:

1. I want to explain why the program asks if you want to add stocks that 'weren't previously in the portfolio.' I have it currently where each csv row is stock.  Once you have added a stock that row is there forever, even if you sell all yout stock.  

Soon I will have it so that the program adds the stock to the csv if it isn't already there, but for now it is a seperate seciton.

2. Shorting stocks is possible with the program (by having a negative quanitity), which isn't exactly how short positions work, but for the time being I am going to keep it that way to keep the program simple to use.


## FUTURE PLANS FOR IMPROVEMENT:

- As mentioned above, I will make the program a bit more user friendly by having the program add stocks autotically if they have never been in the csv, rather then. asking the user, which isn't really necessary.

- I may add a program that scrapes other financial information.  The idea was brought up to you about Quarter Reports.

- Efficiency improvement.  If you look at the code, I could speed things up (for example by only getting the live prices once) so I plan to do that to perfect my efficiency in coding.  


VERSION HISTORY:
```
1.2 ~ Finally combined the stock adding sections and organized the code!
 Combined the stock adding section with the buying/selling section.  
 (Now asked for stock once and if it isn't in CSV it is automatically grabbed and added)
 Added comments to explain the sections in the code
 Helped organize the code a bit more and fix some redundencies.
```

```
1.0.1 ~ Very minor improvements
 Fixed an additional rounding error that was not completely patched by last fix.
 Re-organized name to let version lead, just for less confusion.
```

```
1.0 ~ First Complete Version of Paper Trader
 Added and moved forward 'stock adding' part of code - Can now add stocks that have never been added before by abbreviation
 Program now starts with showing porfolio and live prices of stocks, then allows expanding portfolio, then buy/sell stocks
 Fixed minor rounding error bug
```

## ----

```
0.2 ~ Fixed bugs and some extra text
 Fixed the binary number calculation issues
 Added in text if you choose not to change profolio, so the program doesn't just terminate
```

```
0.1 ~ First attempt
 Built Paper Trader
```
