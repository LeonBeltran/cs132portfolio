# Statistical Test

- Dataset was split into **Pre-Monkeypox Period (121 Tweets)** and **Post-Monkeypox Period (32 Tweets)**.
- Linear regression models were generated for both periods, obtaining **slopes representing the growth of aggressiveness over time**: 
  - Pre-monkeypox period slope: **0.0004**
  - Post-monkeypox period slope: **0.0028**
- Post-monkeypox era tweets showed a higher growth rate in aggressiveness compared to the pre-monkeypox era.
- T-Test for statistical significance was performed with a confidence level of **95%** (significance level of **0.05**).
- The resulting p-value obtained was `3.20e-14`, which is **less than the significance level**.
- The Null Hypothesis was rejected, indicating a **statistical significance between tweet aggressiveness and time**.

<br/>

Graph of Pre-Monkeypox Period

![Pre-MP](https://media.discordapp.net/attachments/871627250204831804/1122865899704176640/Pz4uPBtkEjOFIJTZhIREZFM8U8RIiIiki0WMkRERCRbLGSIiIhItljIEBERkWyxkCEiIiLZYiFDREREssVChoiIiGSLhQwRERHJFgsZIiIiki0WMkRERCRbLGSIiIhItljIEBERkWz9P40kwntoWgiAAAAAElFTkSuQmCC.png)


<br/>

Graph of Post-Monkeypox Period

![Post-MP](https://media.discordapp.net/attachments/871627250204831804/1122865900014542908/369cOCBQuKPFetWrUqsFIiqgoYpohI9Vq1aoWNGzeiQYMGcHDg2x4RmRfPmSIi1ZswYQKSk5MxfPhwHDlyBBcvXsTu3bsxevRoaLVaS5dHRDaOYYqIVK927do4ePAgtFotevTogdDQUEyePBnVq1eHnR3fBolIGY1waGEiIiKicuOfZEREREQKMEwRERERKcAwRURERKQAwxQRERGRAgxTRERERAowTBEREREpwDBFREREpADDFBEREZECDFNERERECjBMERERESnAMEVERESkwP8BHCgV1gKcb9UAAAAASUVORK5CYII.png)

# Peak Finding

- Google Trends data for the terms **AIDS, HIV, STD, Monkeypox, and Gay** were plotted.
- The `plotly.io` and `plotly.graph_objects` modules were used for visualization.
- The number of tweets per month and year was grouped and counted based on their **post dates**.
- The `find_peaks` module from `scipy.signal` was used with the following parameters:
  - Peak value needed to be **75%** of the maximum value.
  - Only **the most significant peak** per year was considered.
- A threshold value of 0 was set for the tweets data to identify relevant peaks.
- **A common peak period** was observed between STD, Monkeypox, and AIDS terms **in July-September 2022**, which coincided with a peak in the tweets graph.
- This peak period **aligned with the global monkeypox outbreak**, suggesting an **increase** in the spread of mis/disinformation on Twitter due to the outbreak.

<br/>

Graph of Google Trends

![Peaks Search](https://media.discordapp.net/attachments/871627250204831804/1123118599016554549/newplot_1.png)


<br/>

Graph of Number of Tweets In a Given Period

![Peaks Tweets](https://media.discordapp.net/attachments/871627250204831804/1123118599259816007/newplot.png)

## Summary

Taking into account the statistical significance between the pre- and post-monkeypox periods and the presence of common peaks related to monkeypox and Twitter mis/disinformation, it is possible to conclude that the monkeypox boom had a significant effect on the spread of Twitter mis/disinformation. The combination of linear regression and T-test revealed a statistical significance between tweet aggressiveness and time, indicating that tweets became more aggressive in the post-monkeypox period. Additionally, peak finding analysis showed a peak in the number of tweets during the global monkeypox outbreak, suggesting an increase in the spread of mis/disinformation on Twitter. These findings suggest that the monkeypox outbreak had a significant impact on the dissemination of mis/disinformation on Twitter.

<br/>
