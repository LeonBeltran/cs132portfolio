- The following **histogram** shows the distribution of our dataset:

![Histogram for Aggrerssion Scores in Collected Data](https://cdn.discordapp.com/attachments/871627250204831804/1107911132599046204/histogram.png)

- Along with the Probability Mass Function of the **Standardized** Aggression Scores

![PMF of Aggression Scores](https://media.discordapp.net/attachments/871627250204831804/1123157040060170370/yThogMxo4dO3Djxg3cuHGjziYnLy8vJCcn19ofERGBtWvX4t1330VpaSnc3d0xevRozJs3T3PM8uXL8e677Kll15CXl4e2rVrh3fffRcA4OHhgZ07dLNN99EUFAQHBwc8OyzzK99967Z73u7u44cuQI3n77bQwbNgwVFRXw8vLC8OHD7xmkiMjwcJQZERERGT3CUNERERGj4GIiIiIjB4DERERERk9BiIiIiIyegxEREREZPQYiIiIiMjoMRARERGR0WMgIiIiIqPHQERERERGj4GIiIiIjB4DERERERk9BiIiIiIyev8P8BcSlIbI6loAAAAASUVORK5CYII.png)

- A slight normal distribution could also be observed but the data was mainly skewed left.
- We observed that majority of the tweets show an average amount of aggression towards the LGBTQ community.
- We also observed that a small spike occurred at the top end of the aggression score showing that there was a small amount of entries that were severely aggressive towards the LGBTQ community.


- Some limitations in the aggression score formula
  - An index was created in order to better regulate the variance between capital letters in tweets. It may be possible that a tweet was simply capitalizing a letter for grammatical or acronym reasons and wrote a short tweet which may have inflated their aggression score.
  - The use of terms related to STDs were also counted toward aggression.

## Time Series Analysis

- Part of our action plan was to test if there’s a correlation between the popularity of different STDs/STD keywords and negative stigma towards the LGBTQ community.
- We collected data from **Google Trends** and compared these using line graphs with the data from our dataset. The data from Google Trends range from 0 to 100 with 100 symbolizing the peak of the term being used.
- We took the trend data from 2015-2022. Note that we only used 2016-2022 which explained why some graphs did not reach 100. The highest point still symbolizes the period when the term trended most from 2016-2022.
- The dates collected in our dataset were **binned** by month and year as the scope of the project was from 2016 - 2022. This was also done to match the collected data from Google Trends which followed a MM/YYYY = trend score format.
- We plotted our dataset together with the Google Trends data to visually observe if there was any correlation to be derived.
- The following visualizes the trends of our keywords over time in the Philippines (data was collected from Google Trends)

![Line Graph for gay Trend](https://media.discordapp.net/attachments/871627250204831804/1108372746817253396/gaytrend2016.png)

![Line Graph for STD Trend](https://media.discordapp.net/attachments/871627250204831804/1108372746288771223/stdtrend2016.png)

![Line Graph for HIV Trend](https://media.discordapp.net/attachments/871627250204831804/1108372747089870888/hivtrend2016.png)

![Line Graph for AIDS Trend](https://media.discordapp.net/attachments/871627250204831804/1108372746557198437/aidstrend2016.png)

- From the trends, we observed that the use of the term gay has steadily gone down since around the start of 2016 when it peaked. A pause in decline was observed between 2019-2020. For the term STD, we observed its trend quickly peak on the 3rd quarter of 2019. On the other hand, the term HIV spiked around the same time the pause in decline for the term gay started with the term HIV's second most trending time around the start of 2020. Lastly, we observed that the trend for the term AIDS continued to fluctuate throughout 2016-2022 with its biggest spikes happening around the 3rd quarter of 2018, 3rd quarter of 2020, and the start of 2022.

- The following shows the number of tweets posted every month/year interval

![Line Graph for Tweets per Month and Year](https://media.discordapp.net/attachments/871627250204831804/1108372746003550259/numtweets2016.png)

- Note that the data used a monthly and yearly interval but the graph only shows the year to keep the cleanliness of the subheadings
- When it came to the number of tweets posted per month and year, we observed that majority of our tweets were posted between the start of 2019 and the end of 2022. Our most noticeable spikes occured in the middle of 2022 and at the 1st quarter of 2020.

## Observations

- We deduced that the period between 2019-2020 was the likeliest time the negative stigma toward the LGBTQ community peaked with spikes for the terms STD and HIV and notable trends for the terms AIDS and gay happening at that time period. It also encompasses a significant amount of tweets we collected from our data.
- The period between 2019-2020 was when COVID-19 started.



## Sources

1. [https://grammar.yourdictionary.com/punctuation/why-are-you-yelling-how-all-caps-make-you-loud](https://grammar.yourdictionary.com/punctuation/why-are-you-yelling-how-all-caps-make-you-loud)
2. [https://www.psychologicalscience.org/observer/the-science-of-swearing](https://www.psychologicalscience.org/observer/the-science-of-swearing)


<br/>
<br/>
<br/>
