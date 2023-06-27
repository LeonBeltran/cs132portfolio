1. **Data Collection via Twitter Scraping**
   - Tweets were scraped via a Python program, totaling more than a thousand tweets.
   - Tweets were reviewed, and 153 eligible tweets were selected as the dataset.
   - Important information on the tweet was collected, such as the posting date and the text of the tweet.

2. **Preprocessing of the Collected Data**
   - Natural Language Processing was done on the collected tweets using Python modules such as `nltk` and `better_profanity`, along with Google Translate.
   - Lemmatization and stemming were also performed on the tweet text.
   - Tweet posting dates were cross-checked to ensure proper tracking in case of any incorrect formats or dates.
   - Tweet post dates were also binned monthly to match the date format of the collected Google Trends Data (seen later).

3. **Implementation of Aggression Score**
   - An aggression score was assigned to each tweet, factoring in the swear words found and the percentage of capital words in a tweet.
   - An index was formulated specifically for the capital words in a tweet.
   - The aggression score was visualized via a histogram.

4. **Google Trends Visualization**
   - Google Trends data was collected and plotted in a line graph.
   - These graphs showed the engagement of a term over a period of time ranging from 0-100, with 100 being the timeframe of peak engagement.

5. **Twitter Tweets Over Time Visualization**
   - Tweets, binned monthly, were plotted in a line graph similar to the Google Trends Visualization.
   - The graph similarly showed engagement over time by displaying the number of tweets posted per month.

6. **Statistical Test**
   - Linear Regression was performed to obtain the lines of best fit of the tweet data aggression score pre and post monkeypox period (July 2022 for this case).
   - A T-test with a confidence level of 95% was then used on the slope values to determine any statistical significance.

7. **Peak Finding**
   - Peaks were found via peak finding of the Google Trends and tweets over time graph.
   - Parameters used for finding peaks included a minimum of 75% of the maximum value and a limit of a single peak per year.

   <br/>
   <br/>
   <br/>
