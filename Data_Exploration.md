# Data Exploration

## Data Collection Assumptions
We collected a sample of 150 tweets for the data exploration. An assumption we made was that this was a sufficient amount to determine the relationships we wanted to obtain. It should be noted that increasing the dataset would increase the accuracy of our data exploration observations. We also assumed that the term gay addressed the LGBTQ community in our data. This is because gay is a translation for the term bakla which is commonly used by Filipinos to encompass the entire LGBTQ community.

## Preprocessing:
Our group's research mainly focused on looking at the language tones of our data and the relationship between tweet dates to trends of topics about STD and LGBTQ over time. This gave us an idea on the correlation between STDs on the negative stigma against the LGBTQ community. In order to do so, the following steps were first taken to clean up the data.

- We ensured that there were **no missing values** through double checking obtained data. Categories we used were also categories that always had data filled in so a check that these copied over was all that we needed.
- **Outliers** if any were kept in the data because this provided the bigger picture of our collected data.
- We ensured that the data was **formatted consistently** through double checking the dataset, such as the date posted column which had a few inconsistencies with the MM/DD/YY HH:MM format.
- **Lower casing and emoji to text conversion** were done to clean up the data through python built-ins and hardcoded functions.
- **Stemming and lemmatization** of the data was done through PorterStemmer and WordNetLemmatizer from nltk.stem.

## Presence of Profanity

- One of the observations we tested for in our dataset was the presence of profanity outside of the keywords we already used to obtain data.
- As profanity is often used in aggression, we believed that checking for profanity not included in our keywords could help determine aggression.
- We checked for presence of profanity from our preprocessed dataset and the betterprofanity library. Note that we whitelisted the following words: ['gay', 'std', 'hiv', 'aids'] as these were keywords that we used to collect data and keeping them in would result in all entries having profanity. What we checked for here was the presence of other swear words to see if these were used in conjunction with our keywords.
- We used this to **categorically encode** our tweet text data into a boolean value of 'True' or 'False' similar to **binary encoding**.
- The following **bar plot** shows the comparison between tweets with profanity and tweets without:

![Bar Plot for Profanity Presence in Collected Data](https://cdn.discordapp.com/attachments/871627250204831804/1107894123907797033/bar_plot.png)

- Our dataset showed that there was almost a 2:1 ratio in no extra profanity to has extra profanity in our dataset
- This indicated that the majority of the data only used profanity included in our keywords.
- It must be noted however that a still significant amount of our data, almost 50 entries, used profanity outside of our keywords.

## Aggression Score

- Another aspect of the stigma we explored to observe the negative stigma towards the LGBTQ community was the aggression tweets had.
- In order to measure this, we came up with variable, Aggression Score
- This was used to standardize our data and numerically describe each tweet's aggression.
- The two main factors to the aggression score is the ***percentage of capital letters*** in tweet and the ***number of swear words*** in tweet
  - Capital letters are often used when a person wants to express that they are shouting in text.   [Source](https://grammar.yourdictionary.com/punctuation/why-are-you-yelling-how-all-caps-make-you-loud)
  - Swear words are often used as aggressive language due to their meanings and perception. [Source](https://www.psychologicalscience.org/observer/the-science-of-swearing)
  - While there are other factors to consider such as the nuances of the language used, since the data was translated from Filipino to English, some of the nuances may have been lost in translation. We also determined that the factors we considered were enough to give a rough perspective on the aggression portrayed by a tweet.
  - It should be noted that the data collected was already "aggressive in nature."
- The following is our formula in calculating the aggression score
  - Aggression Score = # of swear words + cap % index
    - cap % index = (0 if % of capital letters in tweet < 0.1, 1 if 0.1 <= % of capital letters < 0.3, 2 if % 0.3 <= % of capital letters < 0.6, and 3 if % of capital letters >= 0.6)
    - cap % index is a variable that adds a value of 0, 1, 2 or 3 depending on the % of capital letters in the tweet. to the tweet aggression score
    - An index was created in order to better regulate the variance between capital letters in tweets. It may be possible that a tweet was simply capitalizing a letter for grammatical or acronym reasons and wrote a short tweet which may have inflated their aggression score.
    - The use of terms related to STDs were also counted toward aggression.
- The following **histogram** shows the distribution of our dataset:

![Histogram for Aggrerssion Scores in Collected Data](https://cdn.discordapp.com/attachments/871627250204831804/1107911132599046204/histogram.png)

- A slight normal distribution could also be observed but the data was mainly skewed left.
- We observed that majority of the tweets show an average amount of aggression towards the LGBTQ community.
- We also observed that a small spike occurred at the top end of the aggression score showing that there was a small amount of entries that were severely aggressive towards the LGBTQ community.

## Time Series Analysis

- Part of our action plan was to test if there’s a correlation between the popularity of different STDs/STD keywords and negative stigma towards the LGBTQ community.
- We collected data from **Google Trends** and compared these in a line graph with the data from our dataset
- The dates collected in our dataset were **binned** by month and year as the scope of the project was from 2015 - 2022. This was also done to match the collected data from Google Trends which followed a MM/YYYY = trend score format.
- We plotted our dataset together with the Google Trends data to visually observe if there was any correlation to be derived.
- The following visualizes the trends of our keywords over time in the Philippines (data was collected from Google Trends)

![Line Graph for gay Trend](https://media.discordapp.net/attachments/871627250204831804/1107941617916203028/gaytrend.png)

![Line Graph for STD Trend](https://media.discordapp.net/attachments/871627250204831804/1107941618578903140/stdtrend.png)

![Line Graph for HIV Trend](https://media.discordapp.net/attachments/871627250204831804/1107941618180423700/hivtrend.png)

![Line Graph for AIDS Trend](https://media.discordapp.net/attachments/871627250204831804/1107941619262562334/aidstrend.png)

- The following shows the number of tweets posted every month/year interval

![Line Graph for Tweets per Month and Year](https://media.discordapp.net/attachments/871627250204831804/1107941619031867522/numtweets.png)

- Note that the data used a monthly and yearly interval but the graph only shows the year to keep the cleanliness of the subheadings

- From the trends, we observed that the use of the term gay has steadily gone down since around the start of 2016 when it peaked. A pause in decline was observed between 2019-2020. For the term STD, we observed its trend quickly peak on the 3rd quarter of 2019. On the other hand, the term HIV spiked around the same time the pause in decline for the term gay started with the term HIV's second most trending time around the start of 2020. Lastly, we observed that the trend for the term AIDS continued to fluctuate throughout 2015-2022 with its biggest spikes happening around the 3rd quarter of 2018, 3rd quarter of 2020, and the start of 2022.
- When it came to the number of tweets posted per month and year, we observed that majority of our tweets were posted between the start of 2019 and the end of 2022. Our most noticeable spikes occured in the middle of 2022 and at the 1st quarter of 2020.

## Observations

- We deduced that the period between 2019-2020 was the likeliest time the negative stigma toward the LGBTQ community peaked with spikes for the terms STD and HIV and notable trends for the terms AIDS and gay happening at that time period. It also encompasses a significant amount of tweets we collected from our data.
- The period between 2019-2020 was when COVID-19 started.