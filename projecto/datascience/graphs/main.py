from ast import keyword
from hashlib import new
import os
import re
import pandas
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image


def get_keywords(path):
    df = pandas.read_csv(path, sep=r",\s")
    keywords = df["Expressao"].values.tolist()
    frequency = df["Frequencia"].values.tolist()

    keywords = [str(x) for x in keywords]
    frequency = [float(x) for x in frequency]
    frequency = [round(x * 100) for x in frequency]
    keywords, frequency = [
        list(x)
        for x in zip(
            *sorted(zip(keywords, frequency), key=lambda pair: pair[1], reverse=True)
        )
    ]
    return keywords, frequency


def get_sentiments(path):
    positive = 0
    negative = 0
    df = pandas.read_csv(path)
    for sentiment in df["sentiment"]:
        if sentiment == "positive":
            positive += 1
        elif sentiment == "negative":
            negative += 1
    return positive, negative


def get_sentiment_percentage(positive, negative):
    total = positive + negative
    positive = round(positive / total * 100)
    negative = round(negative / total * 100)
    return positive, negative


def get_sentiment_graph(positive, negative, path, name):
    plt.pie([positive, negative], labels=["positive", "negative"], autopct="%.0f%%")
    plt.savefig(path + name.replace(".csv", "") + "_sentiments.jpeg")
    plt.close()


# create pie chart
def get_keywords_graph(keywords, frequency, path, name):
    keywords_dict = dict(zip(keywords, frequency))
    keywords_dict = sorted(keywords_dict.items(), key=lambda kv: kv[1], reverse=True)

    keywords = [x[0] for x in keywords_dict[:10]]
    frequency = [x[1] for x in keywords_dict[:10]]

    plt.pie(frequency, labels=keywords, autopct="%.0f%%")
    plt.savefig(path + name.replace(".csv", "") + "_keywords.jpeg")
    plt.close()


def get_keywords_wordcloud(keywords, frequency, path, name):

    keywords = keywords[:100]
    frequency = frequency[:100]

    mask = np.array(Image.open(path + "mask.jpeg"))
    wc = WordCloud(
        background_color="white",
        mask=mask,
        max_words=100,
        contour_width=3,
        contour_color="white",
    )
    wc.generate_from_frequencies(dict(zip(keywords, frequency)))
    wc.to_file(path + name.replace(".csv", "") + "_keywordcloud.jpeg")


def get_graphs_from_directory(path):
    current_dir = os.getcwd()
    export_path = current_dir + "/graphs" + path
    keyword_path = current_dir + "/keywords" + path
    sentiment_path = current_dir + "/sentiments" + path

    total_keywords, total_frequency = [], []
    total_sentiment_positive, total_sentiment_negative = 0, 0

    for file in os.listdir(keyword_path):
        if file.endswith(".csv"):
            keywords, frequency = get_keywords(keyword_path + file)
            total_keywords, total_frequency = (
                total_keywords + keywords,
                total_frequency + frequency,
            )
            get_keywords_graph(keywords, frequency, export_path, file)
            get_keywords_wordcloud(keywords, frequency, export_path, file)

    get_keywords_graph(total_keywords, total_frequency, export_path, "total")
    get_keywords_wordcloud(total_keywords, total_frequency, export_path, "total")

    for file in os.listdir(sentiment_path):
        if file.endswith(".csv"):
            positive, negative = get_sentiments(sentiment_path + file)
            total_sentiment_positive, total_sentiment_negative = (
                total_sentiment_positive + positive,
                total_sentiment_negative + negative,
            )
            positive, negative = get_sentiment_percentage(positive, negative)
            get_sentiment_graph(positive, negative, export_path, file)

    total_sentiment_positive, total_sentiment_negative = get_sentiment_percentage(
        total_sentiment_positive, total_sentiment_negative
    )
    get_sentiment_graph(
        total_sentiment_positive, total_sentiment_negative, export_path, "total"
    )


if __name__ == "__main__":
    get_graphs_from_directory("/booking/hotels/")
    get_graphs_from_directory("/zomato/restaurantes/")
    get_graphs_from_directory("/tripadvisor/hotels/")
    get_graphs_from_directory("/tripadvisor/restaurants/")
    get_graphs_from_directory("/tripadvisor/activities/")