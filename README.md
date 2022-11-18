# BT4012
This project aims to be able to differentiate bot accounts from human accounts using account metadata and to be able to differentiate bot generated tweets from human generated tweets based on the textual content in the tweet.

Information about the folders:

1. **ETL + EDA (Features)**

In this repository, we perform some data preprocessing and feature selection based on the features (for the metadata dataset) obtained for each bot/or human account in the webscrapping stage. We also perform exploratory data analysis on the features to attempt to see any interesting patterns in the data. We aim to get some insights into the characteristics of the metadata for the bot accounts and the human accounts respectively.

2. **ETL + EDA (Text)**

In this folder, we perform exploratory data analysis on the tweets in order to get insight into the content of bot generated tweets vs human generated tweets. We also combine the train, val and test datasets originally obtained.

3. Model (Features)
In this folder, we perform feature engineering and conduct experiments to determine the optimal machine learning model that can classify an account as human or bot based on its metadata to pick for the deployment in flask. We then pick the optimal model and save it for deployment in the flask folder.

4. Model (Text)
In this folder, we perform feature engineering of text specific to each machine learning model used and pick a machine learning model that can best classify a tweet as a human written tweet or a bot written tweet. The optimal model is picked and saved in the flask folder.

5. Webscrapping
Here, we perform webscrapping using the tweepy API to obtain the relevant features for each account.

6.flask
In this folder, we deploy the best machine learning models found during experimentation in a local flask environment. The instructions for usage are listed later.
