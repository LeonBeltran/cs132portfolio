## Data Collection Assumptions
We collected a sample of 153 tweets for the data exploration. An assumption we made was that this was a sufficient amount to determine the relationships we wanted to obtain. It should be noted that increasing the dataset would increase the accuracy of our data exploration observations. We also assumed that the term gay addressed the LGBTQ community in our data. This is because gay is a translation for the term bakla which is commonly used by Filipinos to encompass the entire LGBTQ community.

## Preprocessing:
Our group's research mainly focused on looking at the language tones of our data and the relationship between tweet dates to trends of topics about STD and LGBTQ over time. This gave us an idea on the correlation between STDs on the negative stigma against the LGBTQ community. In order to do so, the following steps were first taken to clean up the data.

- We ensured that there were **no missing values** through double checking obtained data. Categories we used were also categories that always had data filled in so a check that these copied over was all that we needed.
- **Outliers** if any were kept in the data because this provided the bigger picture of our collected data.
- We ensured that the data was **formatted consistently** through double checking the dataset, such as the date posted column which had a few inconsistencies with the MM/DD/YY HH:MM format.
- **Lower casing and emoji to text conversion** were done to clean up the data through Python built-ins and hardcoded functions.
- **Translating from Filipino to English** was done with Google Translate to make the tweets workable for the library functions.
    - This was done to minimize potential biases that could come in manually translating
    - However, since not all tweets had a workable translation, these tweets had to be manually translated
- **Stemming and lemmatization** of the data was done through PorterStemmer and WordNetLemmatizer from `nltk.stem`.

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
  - Capital letters are often used when a person wants to express that they are shouting in text.   [Source 1](https://grammar.yourdictionary.com/punctuation/why-are-you-yelling-how-all-caps-make-you-loud)
  - Swear words are often used as aggressive language due to their meanings and perception. [Source 2](https://www.psychologicalscience.org/observer/the-science-of-swearing)
  - While there are other factors to consider such as the nuances of the language used, since the data was translated from Filipino to English, some of the nuances may have been lost in translation. We also determined that the factors we considered were enough to give a rough perspective on the aggression portrayed by a tweet.
  - It should be noted that the data collected was already "aggressive in nature."
- The following is our formula in calculating the aggression score

