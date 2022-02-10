import os
import pandas
import sqlite3
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image


def create_wordcloud(month, year, df):
    df = df[df["month"] == month]
    df = df[df["year"] == year]
    df = df.sort_values(by="score", ascending=False).groupby("business_id").head(10)
    for business_id in df["business_id"].unique():
        try:
            words, freq = (
                df[df["business_id"] == business_id]["keyword"].values.tolist(),
                df[df["business_id"] == business_id]["score"].values.tolist(),
            )
            words, freq = [str(x) for x in words], [float(x) for x in freq]
            words, freq = words[:100], freq[:100]
            dict_words = dict(zip(words, freq))
            mask = np.array(Image.open("./mask.png"))
            wc = WordCloud(
                background_color="white",
                mask=mask,
                max_words=100,
                contour_width=3,
                contour_color="white",
            ).generate_from_frequencies(dict_words)
            wc.to_file(
                "./wordclouds/wordcloud_{}_of_{}_at_business{}.png".format(
                    month, year, business_id
                )
            )
        except:
            pass


def circular_graph_keywords(month, year, df):
    df = df[df["month"] == month]
    df = df[df["year"] == year]
    df = df.sort_values(by="score", ascending=False).groupby("business_id").head(10)
    for business_id in df["business_id"].unique():
        try:
            words, freq = (
                df[df["business_id"] == business_id]["keyword"].values.tolist(),
                df[df["business_id"] == business_id]["score"].values.tolist(),
            )
            # create a circular graph
            words, freq = [str(x) for x in words], [float(x) for x in freq]
            words, freq = words[:10], freq[:10]
            plt.pie(freq, labels=words, autopct="%1.1f%%", startangle=90)
            plt.savefig(
                "./graphs/keywords/circular_keywords_{}_of_{}_at_business{}.png".format(
                    month, year, business_id
                )
            )
            plt.close()
        except:
            pass


def circular_graph_sentiment(month, year, df):
    df = df[df["month"] == month]
    df = df[df["year"] == year]
    for business_id in df["business_id"].unique():
        try:
            sentiments = df[df["business_id"] == business_id][
                "sentiment"
            ].values.tolist()
            positive, negative = sentiments.count("positive"), sentiments.count(
                "negative"
            )
            total = positive + negative
            positive = positive / total
            negative = negative / total
            plt.pie(
                [positive, negative],
                labels=["positive", "negative"],
                autopct="%1.1f%%",
                startangle=90,
            )
            plt.savefig(
                "./graphs/sentiments/circular_sentiment_{}_of_{}_at_business{}.png".format(
                    month, year, business_id
                )
            )
            plt.close()
        except:
            pass


def import_data(db_file, table_name):
    conn = sqlite3.connect(db_file)
    df = pandas.read_sql_query("SELECT * FROM {}".format(table_name), conn)
    conn.close()
    return df


def main():

    years = range(2000, 2022)
    months = [
        "janeiro",
        "fevereiro",
        "marco",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro",
    ]

    bd = "./projecto.db"
    dr = import_data(bd, "reviews")
    dk = import_data(bd, "keywords")
    db = import_data(bd, "business")
    dbt = import_data(bd, "business_type")

    for year in years:
        for month in months:
            create_wordcloud(month, year, dk)
            circular_graph_keywords(month, year, dk)
            circular_graph_sentiment(month, year, dr)


if __name__ == "__main__":
    main()