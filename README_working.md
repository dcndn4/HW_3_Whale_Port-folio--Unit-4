#  Behind-the-Scenes: Whale Portfolio

Having been in theater when I was younger, I always found the activities behind the curtain as fun and interesting as the show itself.

And in life.

So to make the most progress possible, I'm going to write out my process in this space - exploring the topics, putting the info together in my own way. 

This assignment is all about quantitative analysis = presenting reality in terms of a numerical value.

The first step in the process is to look at portfolio returns over time. Returns are the change in ending value from one day to the next, or one week or month to the next. It is compared to a benchmark for that sector or type of instrument. 

Here is the "Returns analysis example" text:

> Example - returns analysis (3.2 exercise)

> What are the average daily returns over each date range?
> 
>   []  1 Year = 0.04538 or 4.53%
>   []  3 Year = 0.03455 or 3.45%
>   []  5 Year = 0.02304 or 2.30%
>   []  10 Year = 0.01488 or 1.49%

>   What insights could this provide in regards to wanting to trade AMD stock in the long-term vs. short-term?

>   The data shows that AMD had an average daily return over the last 1-year time frame of 0.004538, or 4.53%. This compares with long-term average daily returns of, for example, 3.45% for a 3 year horizon, and 1.49% for a 10 year horizon. By contrasting the short-run (1 year) trend against the long run trend (10 years), it’s apparent that AMD has had much stronger performance only recently.

>   As to what this foretells for an investor looking to buy AMD stock now, however, is less clear: it’s possible that this 1-year performance signals a dramatic    change in AMD’s business model, and that this strong performance will continue. On the other hand, the most recent year’s could just be an anomaly, and that performance for AMD will revert to its long run trend.

>   A third and entirely alternative explanation is that the equity market overall experienced a boom over this last year, and that AMD—like all stocks in the    market—rose in value. In the next unit, you will learn how to adjust for these market effects, so that you can evaluate stock performance from year-to-year on a more even measure.
  
>   And so deconstructing those concepts:
  
>   Returns over price changes -- returns are looked at instead of price changes because they are kind of boiled down to the informational nugget. Raw price itself can be very volatile, returns data moves over a much smaller range and each amount change is more meaningful.
        
>   Possible explanations for the improved performance over the last year are discussed - and they are very different. Returns data alone is not sufficient by itself - it needs to be seen within the context of the overall market. 

### Boiled down, returns are a pure numerical value about the benefits received from owning a certain stock or portfolio. Although not cash benefits, since investors don't sell every day.. it is the unrealized gains/losses over time. It doesn't include any contextual information at all, it's simply a statement about the results achieved by that specific investment. 
        
## Standard Deviation (std in pandas)

Standard deviation measures the distance between a set of values, and their center gravity basically (mathematically, by center gravity we mean average) (class mtls)

Daily standard deviation is a parametric statistical measure (wikipedia), meaning it describes the data set within certain assumptions (such as mean distribution/ bell curve).  When a data set pattern is outside that usual distribution, a box plot can be utilized. Box plots contain information about the standard distribution of results, but also provide more meaningful information about all the rest of the data points. 
        
>   From investopedia: measures the dispersion of a dataset relative to its mean (i.e. average). It is calculated as the square root of variance: each data point's deviation from the mean. The greater that distance, the greater the standard deviation. 
        


### Standard Deviation Example 


  |                 Portfolio A        |            Portfolio B             |

  | Value  |Return % |Final Value | Value | Return % | Final Value |
  | :-----:|:-------:| :--------:  | :-----:| :-------:| :---------:|
  |  1,000 |   .75   |   1,008     |  1,000 |   1.50  |   1,015     |
  |  1,008 |  1.00   |   1,018     |  1,015 |  5.00   |   1,066     |
  |  1,018 |   3.00   |   1,048     |  1,066 |  12.00   |   1,194   |
  |  1,048 |  -1.50   |   1,032     |  1,194 |  -9.00   |   1,086   |
  |  1,032 |   .50   |   1,038     |  1,086 |  -4.00   |   1,043   |
  |  1,038 |  2.00   |   1,058     |  1,043 |   1.50   |   1,058   |
  
       (David M. Lane website)[davidmlane.com/yhyperstat/A40397.html]
       
This example shows the utility of standard deviation. 

Although both portfolios started at $ 1,000 and ended at $ 1,058, the volatility of the two was very different. Volatility could be described as how much the returns jump around over time.

Portfolio A has returns ranging from -1.5% to 3%, while Portfolio B's returns ranged from -9% to 12%. So that range of volatility for B is a much larger range than for A - the distance between the highest and lowest returns amounts. While that range amount is dramatic, a more useful way to look at volatility is standard deviation, because it takes into account all the values during the period, and incorporates that info into a statistic. 

The standard deviation for portfolio A is 1.52, while for portfolio B it is 7.24. 

Variance itself is an ingredient within standard deviation.. is usually not part of the analysis itself because it doesn't graph out in a way that is helpful (investopedia). Also, variance may end up being in a different unit of measurement than the data itself, which adds to the confusion.

An asset's volatility is "an annualized measure of dispersion in the stochastic process that is used to model the log returns." Most commonly modeled using          standard deviation (sigma). (~Carol Alexander, Practical Financial Econometrics, 90)

Volatility is mainly captured within the annualized standard deviation, which multiplies the internal standard deviation (daily, weekly or monthly) by the square root of the number of intervals in the year (250, 52 or 12). That annualized standard deviation is usually in the range of 10% to 30%. Nasdaq's volatility (annualized standard deviation) is 28.8%, while the S&P 500's volatility is 18.1%. 


    
  ### Benchmarks for standard deviation: 
  > Volatile stocks have high standard deviation
  
  > 'Blue chip' stocks tend to have lower standard deviation
  
  > Index funds are built in such a way as to have low volatility (lower standard deviation) in relation to their benchmark index - intended to replicate the results of the index.
  
  > Standard deviation (std dev) is widely reported for any stock or investment instrument, by analysts, portfolio managers and advisors (and investors). 
  
  > Standard deviation can be compared to stocks/funds in a specific asset class or market sector. Mostly, those instruments would be expected to be similar - as they're  affected by overall market conditions similarly. Stocks/funds within that group with higher volatility have something else going on (investopedia video).
          
### Standard deviation usefulness:
is shown in the same unit of measurement as the underlying data, which helps make it understandable
graphical results are clear and easy to discuss
          
### Curve of standard deviation
normal curve - then 68% of results fall w/n 1 std dev, or mean, data point. 
shape with more volatility - fewer than 68% are within the 1 std dev, and more of the data points are outside of those bounds. 
          
### Standard deviation downside: 
Standard deviation analysis doesn't supply a reason for the deviation.. could be the company experiences positive growth. That would be variance from the mean, so std dev is higher, so risk/reward are higher.. Kind of circuitious.. when reward is higher, risk is assumed to also be higher. Outliers and extreme values skew the shape of the curve, and may reduce the informational value of this calculation. When there are outliers, the normal distribution isn't applicable, but there isn't a different model to use instead basically, so talking about the results is more difficult. Past results don't predict the future, of course.
         
Standard deviation was explored using python prior to pandas section, as pandas has built-in formula. It's included in investopedia of course.. not explored further here. Input to the .std method in pandas is a DF with date-time column as index, and monetary values (close) as the one related column. (so is that a series? or a dataframe still?)
                
## Primary relationship between standard deviation (1 vs. 2 etc..) and risk/reward. 
        
>   []  1 std dev may equate to being in the group of 70% of the total population of values
>   
>   []  2 std dev for instance might be within 95% of total population of the group
>   
>   []  3 std dev = 100% basically
>   
>   []  bell curve
>   
>   []  little greek o symbol
>   
>   []  is denominator for Sharpe Ratio
        
### Standard deviation applied to stock (morningstar classroom)
        
A fund with std dev of 4, and average return (or mean) of 10%:

* Most of the time (68%), the fund's future returns can be predicted to fall w/n 1 std dev of its historical average
* that translated to its average of 10%, plus or minus 4% -- so within 6% and 14%
* Nearly all the time (95%), the funds future returns should fall within 2 std dev's of mean:
* translated, that is 10% plus/minus 8%, or between 2% and 18%. 
           
Standard dev is only helpful within context (morningstar again) - since standard deviation is not relative measure, so has to have a context built around it. That context generally comes from similar funds, (meaning funds with same defining features) and/or a relevant index. For a single stock, context would come from other stocks from similar companies (market sector, size etc). 

### Rolling average or moving average - 

Rolling or moving average is a way to see things in perspective via increasing the signal-to-noise ratio.. removes large quantity of data points, and causes the remaining data points to have much more information. (per investopedia). The moving average erases the 'noise' aspect of information by muffling the random, short-term fluctuations. Instead each moving average data point is itself a summary of a period of time, and so with other similar points, paints a much more useful picture of what is going on. See 'rolling statistics' exercise for review. 

> * Simple moving average - mean of given set of prices over specific # days (15, 20, 30, 50, 100, 200)
> * exponential moving averages (EMA) is weighted average thta gives greater importance to the price of a stock in more recent days, increasing the emphasis on recent activity.
> * rising moving averages indicate uptrends, falling moving averages indicate downtrends. 
> * moving averages are lagging (or trend-following) indicators because they are based on what happened in the past
> * important 'trading signals' are the 50- day and 200- day moving averages, closely watched by investors and traders. 
> * Investors tend to pay attention to moving averages focused on their time frame - so short-term traders look at shorter-time-frame based m.a., longer-horizon investors are more interested in m.a.'s based on longer time frames. 
> * looking at short-term m.a.'s superimposed over longer-term m.a.'s generates insight into crossover trends. when a short-term moving average crosses above a longer-term moving average, that is a bullish crossover that confirms upward momentum. If the short-term moving average instead crosses below the longer-term moving average, that is a bearish crossover, which indicates downward momentum. 
> * moving averages also provide basis for more complicated indicators, including the MACD
> * MACD (moving average convergence divergence) is calculated by subtracting a 26-day exponential moving average from a 12-day exponential movign average. A result above 0 - positive - indicates a 'buy' decision; while a result below zero signals to sell 

### Rolling Standard Deviation

Rather than look at a single standard deviation value for a stock, the rolling std dev is a graphical display of the cumulative std dev. For each point in the y axis (usually time), the rolling std dev is a value between 0 and 1 that reflects the std dev over a period of time prior to that point. The period of time (or window) in each case is provided. Common windows are 14 days or 20 days etc. The graph provides a boiled-down essence of the volatility of the stock or fund. 

### Application of Standard Deviation

Standard deviation is anchored in the past, and it's only useful regarding the future is the assumption is made that the past will be repeated. It is also called 'realized volatility' or 'historical votality (HV)', since it's based on past data.

The other way of predicting future volatility that isn't based on past results (like standard deviation), but is based on option prices. Publicly-known option prices carry information about investor expectations for prices in the future, based on expected volatility. That volatility when  distilled out from those assumptions (for a particular stock or fund) is called forward-looking "implied volatility(IV)". 

Standard deviation doesn't speak to returns directly.. so a small standard deviation in an area with low profitability with have lower returns that a portfolio with that same standard deviation in a sector with high profitability. Context is everything.



### Vix 
Vix is a volatility index. It's full name is the Cboe Volatility Index, abbreviated to VIX. It was created in 1993 by the Chicago Board Options Exchange (CBOE) and is maintained by Cboe global markets. It generates a 30-day forward projection of future volatility. It is constructed from the implied (future) volatilities of the S&P 500 - considered the leading indicator of the overall US Stock Market. Historical data demonstrates a strong negative correlation between volatility and stock market returns - when volatility rises, returns go down (and vice versa). (Investopedia).

### Covariance 

Covariance is a measure of dependency between two returns. Per Malkiel, it is the degree of parallelism between the returns of two securities. The calculation involves the actual and expected return of the two securities. Negative covariance means the two stocks move in opposite ways, they mitigate risk.

Another way to put it is that covariance measures the directional relationship between two variables. If two stocks go up at the same time, covariance is positive!
        
Choosing stocks with negative covariance is the essence of diversification. (- A RW d MS p 194-196 or so).

Comparison between terms 

> [] Variance measures how far numbers disperse around their mean.
        
> [] Variance vs std dev: standard deviation is the square root of variance.

> [] Covariance vs variance: Variance is one variable (one stock or fund). Covariance is about the relationship between 2 variables (stocks or funds).

> [] Covariance is mainly a stepping stone to calculating correlation, it isn't really useful itself. 
        
> [] (from Beta demo presented in class 9.28.21)
              
> [] Analysis note: To work with correlation and pandas, use the seaborn library (within matplotlib)
               
### Correlation -- hard-bound - varies between -1 and + 1
         
The higher the correlation, the less safety there is from market volatility
* with lower / negative  correlation, portfolio diversity is in place, which provides safety from market volatility

Correlations:
>      [] +1 = perfect positive relationship

>      []  0 = perfect random relationship

>      [] -1 = prefect negative relationship
>      

Correlation is covariance, scaled to [-1, 1]. (~Carol Alexander, Practical Financial Econometrics, 94)(from Beta demo presented in class 9.28.21)
                   
## Risk - Systematic Risk vs. Unsystematic risk

Systematic risk is an adverse pressure that affects the entire stock market - such as the financial crisis in 2008. Even very well-diversified portfolios were harmed by that event. 

Unsystematic risk or diversifiable risk is the uncertainty carried by a specific stock or fund or industry. That risk can be reduced via diversification. 

### CAPM - Capital Asset Pricing Model

CAPM attaches a numerical value to the risk and return of a specific financial instrument (usually a stock). { not an investment fund??}  (per investopedia)

One of the components of CAPM is Beta.(per investopedia)

### Beta - the specific volatility or systematic risk of a single stock, compared to the market as a whole

Beta is about the performance of a stock in relation to the volatility of the market. 

high-beta stocks are 'aggressive' investments, low-beta stocks are defensive. (- A RW d MS). 

A beta of 1 is assigned to a relevant market index. Then if a stock has a beta of 2, it loops out twice as far in every direction as the market index. If a stock has a beta of .5, it only moves half as far as the market. However it is crucial to carefully decide what to include in 'the market', as that determines the utility of beta as an investing tool. (- A RW d MS p 205-219). 

(It tells investors whether the stock moves with the market (does not provide diversification) or in a different way (does provide diversification). It quantifies the amount of movement as well. (per investopedia)) -- putting this aside to see how this fits with add'l content
(relationship between Beta and Morgan Stanley? not sure..)

Beta exists in a context provided by a benchmark (such as the s&p 500), and that benchmark needs to be relevant to that stock in order for the results to be useful. A numerical way to indicate the relevance of the benchmark to the stock is the R-squared value -- the higher that is, the more relevant the benchmark is. (per investopedia)

### Sharpe ratio - risk-adjusted investment portfolio analysis measure (from Wikipedia)

The Sharpe ratio was created by William Sharpe in 1966 (from Investopedia). It has been a popular reference point for investors ever since, even moreso since Professor Sharpe won a Nobel Memorial Prize in Economic Sciences in 1990 for his work on the Capital Asset Pricing Model (CAPM). He learned of the work of economist Harry Markowitz while at UCLA, and got his PhD under Markowitz guidance in 1961. He developed the Sharpe Ratio in 1966. 

The Sharpe ratio divides the profitability of a portfolio by its volatility, to give a measurement of the additional amount of return that an investor receives per unit of increase in risk.

Example (from Wikipedia):

Investment Manager A provides return of 15%, but their portfolio has a standard deviation of 8%.
Investment Manager B provides return of 12%, and that is from a portfolio with a standard deviation of only 5%.

This example includes a risk-free rate of 5%.

The Sharpe Ratio for Manager A is 1.25
The Sharpe Ratio for Manager B is 1.4

Higher numbers are better, so Manager B would be the better choice if consideration is being given to both return and risk. 

Benchmarks for Sharpe Ratio: 1-2 is good, 2-3 is very good, and over 3 is excellent. 

Note from Homework assignment:
> Sharpe Ratios
> 
> In reality, investment managers and their institutional investors look at the ratio of return-to-risk, and not just returns alone. After all, if you could invest in >  one of two portfolios, and each offered the same 10% return, yet one offered lower risk, you'd take that one, right?

The sharpe ratio return 

Formula:

> Annualized Annual Returns 
> 
>  ------------ over ------------------
>  
>  Portfolio Standard Deviation (annualized)

To get annualized annual returns, take Portfolio Returns - Benchmark return (ie. TBill).






 
Other related etc:
Harry Markowitz -- rooted in linear algebra, applied those theories to market diversification.. Out of that came the sharpe ratio.. CAPM etc... Pearson - default method..
