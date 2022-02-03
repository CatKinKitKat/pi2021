import os
import yake
import pandas
import sqlite3
import warnings

warnings.filterwarnings("ignore")


def create_db(db_name):
    conn = sqlite3.connect(db_name)
    return conn


def create_table(conn, table_name, cols):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS {} {}".format(table_name, cols))
    conn.commit()


def insert_data(conn, table_name, data):
    c = conn.cursor()
    c.execute("INSERT INTO {} VALUES {}".format(table_name, data))
    conn.commit()


def export_data(conn, table_name, file_name):
    c = conn.cursor()
    c.execute("SELECT * FROM {}".format(table_name))
    data = c.fetchall()
    df = pandas.DataFrame(data)
    df.to_csv(file_name, index=False)


def keywords_from_review_by_month_year(conn, table_name):
    months = [
        "janeiro",
        "fevereiro",
        "março",
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
    df = pandas.DataFrame(columns=["business_id", "month", "year", "keyword", "score"])
    ind = 0
    for year in range(2000, 2022):
        for month in months:
            c = conn.cursor()
            c.execute(
                "SELECT review_text, business_id FROM {} WHERE month = '{}' AND year = {}".format(
                    table_name, month, str(year)
                )
            )
            data = c.fetchall()
            data = sorted(data, key=lambda x: x[1])
            lst = []
            for i in range(len(data)):
                if i == 0:
                    lst.append(data[i][0])
                elif data[i][1] == data[i - 1][1]:
                    lst.append(data[i][0])
                else:
                    keywords = yake.KeywordExtractor(lan="pt").extract_keywords(
                        "".join(str(x) for x in lst)
                    )
                    for k in keywords:
                        df.loc[ind] = [
                            str(data[i - 1][1])
                            .encode("ascii", "ignore")
                            .decode("utf-8", "ignore"),
                            str(month)
                            .encode("ascii", "ignore")
                            .decode("utf-8", "ignore"),
                            str(year)
                            .encode("ascii", "ignore")
                            .decode("utf-8", "ignore"),
                            str(k[0])
                            .encode("ascii", "ignore")
                            .decode("utf-8", "ignore"),
                            str(k[1])
                            .encode("ascii", "ignore")
                            .decode("utf-8", "ignore"),
                        ]
                        ind += 1
                    lst = []
                    lst.append(data[i][0])
    # df.to_sql("keywords", conn, if_exists="append", index=False)
    for row in df.itertuples():
        data = (
            "("
            + str(row.business_id).encode("ascii", "ignore").decode("utf-8", "ignore")
            + ", '"
            + str(row.month).encode("ascii", "ignore").decode("utf-8", "ignore")
            + "', "
            + str(row.year).encode("ascii", "ignore").decode("utf-8", "ignore")
            + ", '"
            + str(row.keyword).encode("ascii", "ignore").decode("utf-8", "ignore")
            + "', "
            + str(row.score).encode("ascii", "ignore").decode("utf-8", "ignore")
            + ")"
        )
        insert_data(
            conn,
            "keywords",
            data,
        )


def main():
    # Create database
    db_name = "projecto.db"
    conn = create_db(db_name)

    # Create table
    table_name = "business_type"
    cols = "(business_type_id INTEGER PRIMARY KEY, business_type_name TEXT)"
    create_table(conn, table_name, cols)

    # Create table
    table_name = "business"
    cols = "(business_id INTEGER PRIMARY KEY, business_name TEXT, business_type_id INTEGER, FOREIGN KEY (business_type_id) REFERENCES business_type (business_type_id))"
    create_table(conn, table_name, cols)

    # Create table
    table_name = "reviews"
    cols = "(review_id INTEGER PRIMARY KEY, review_text TEXT, business_id INTEGER, sentiment TEXT, month TEXT, year INTEGER, FOREIGN KEY (business_id) REFERENCES business (business_id))"
    create_table(conn, table_name, cols)

    # Create table
    table_name = "keywords"
    cols = "(business_id INTEGER, month TEXT, year INTEGER, keyword TEXT, score FLOATING POINT, FOREIGN KEY (business_id) REFERENCES business (business_id))"
    create_table(conn, table_name, cols)

    # Insert data
    table_name = "business_type"
    data = "(1, 'Restaurant')"
    insert_data(conn, table_name, data)
    data = "(2, 'Attraction')"
    insert_data(conn, table_name, data)
    data = "(3, 'Hotel')"
    insert_data(conn, table_name, data)

    # Insert data
    table_name = "business"
    pd = pandas.read_csv(
        "./data/restaurants/listtable.csv", engine="python", on_bad_lines="skip"
    )
    pd.columns = pd.columns.str.strip()
    lst = []
    lst = pd["Restaurante"].tolist()
    l = 1
    for i in range(len(lst)):
        data = (
            "("
            + str(l).encode("ascii", "ignore").decode("utf-8", "ignore")
            + ", '"
            + str(lst[i]).encode("ascii", "ignore").decode("utf-8", "ignore")
            + "', 1)"
        )
        insert_data(conn, table_name, data)
        l += 1
    pd = pandas.read_csv(
        "./data/activities/listtable.csv", engine="python", on_bad_lines="skip"
    )
    pd.columns = pd.columns.str.strip()
    lst = pd["Attraction"].tolist()
    for i in range(len(lst)):
        data = (
            "("
            + str(l).encode("ascii", "ignore").decode("utf-8", "ignore")
            + ", '"
            + str(lst[i]).encode("ascii", "ignore").decode("utf-8", "ignore")
            + "', 2)"
        )
        insert_data(conn, table_name, data)
        l += 1
    pd = pandas.read_csv(
        "./data/hotels/listtable.csv", engine="python", on_bad_lines="skip"
    )
    pd.columns = pd.columns.str.strip()
    lst = pd["Hotel"].tolist()
    for i in range(len(lst)):
        data = (
            "("
            + str(l).encode("ascii", "ignore").decode("utf-8", "ignore")
            + ", '"
            + str(lst[i]).encode("ascii", "ignore").decode("utf-8", "ignore")
            + "', 3)"
        )
        insert_data(conn, table_name, data)
        l += 1

    # Insert data
    table_name = "reviews"
    all = 0
    for file in os.listdir("./data/activities"):
        all += 1
        if file.startswith("place") and not file.endswith(".zip"):
            print(file)
            pd = pandas.read_csv(
                "./data/activities/" + file, engine="python", on_bad_lines="skip"
            )
            pd.columns = pd.columns.str.strip()
            lst = pd["review"].tolist()
            lsts = pd["sentiment"].tolist()
            pd = pandas.read_csv(
                "./dates/activities/" + file, engine="python", on_bad_lines="skip"
            )
            pd.columns = pd.columns.str.strip()
            lstm = pd[pd.columns[0]].tolist()
            lsty = pd[pd.columns[1]].tolist()
            # pd = pandas.read_csv(
            #     "./keywords/activities/" + file, engine="python", on_bad_lines="skip"
            # )
            # pd.columns = pd.columns.str.strip()
            # lstk = pd["Expressao"].tolist()
            for i in range(len(lst)):
                try:
                    insert_data(
                        conn,
                        table_name,
                        "(NULL, '"
                        + str(lst[i])
                        .encode("ascii", "ignore")
                        .decode("utf-8", "ignore")
                        + "', "
                        + str(all).encode("ascii", "ignore").decode("utf-8", "ignore")
                        + ", '"
                        + str(lsts[i])
                        .encode("ascii", "ignore")
                        .decode("utf-8", "ignore")
                        + "', '"
                        # + str(lstk[i])
                        # .encode("ascii", "ignore")
                        # .decode("utf-8", "ignore")
                        # + "', '"
                        + str(lstm[i])
                        .encode("ascii", "ignore")
                        .decode("utf-8", "ignore")
                        + "', "
                        + str(lsty[i])
                        .encode("ascii", "ignore")
                        .decode("utf-8", "ignore")
                        + ")",
                    )
                except:
                    pass
    for file in os.listdir("./data/hotels"):
        all += 1
        if file.startswith("hotel") and not file.endswith(".zip"):
            print(file)
            pd = pandas.read_csv(
                "./data/hotels/" + file, engine="python", on_bad_lines="skip"
            )
            pd.columns = pd.columns.str.strip()
            lst = pd["review"].tolist()
            lsts = pd["sentiment"].tolist()
            pd = pandas.read_csv(
                "./dates/hotels/" + file, engine="python", on_bad_lines="skip"
            )
            pd.columns = pd.columns.str.strip()
            lstm = pd[pd.columns[0]].tolist()
            lsty = pd[pd.columns[1]].tolist()
            # pd = pandas.read_csv(
            #     "./keywords/hotels/" + file, engine="python", on_bad_lines="skip"
            # )
            # pd.columns = pd.columns.str.strip()
            # lstk = pd["Expressao"].tolist()
            for i in range(len(lst)):
                try:
                    insert_data(
                        conn,
                        table_name,
                        "(NULL, '"
                        + str(lst[i])
                        .encode("ascii", "ignore")
                        .decode("utf-8", "ignore")
                        + "', "
                        + str(all).encode("ascii", "ignore").decode("utf-8", "ignore")
                        + ", '"
                        + str(lsts[i])
                        .encode("ascii", "ignore")
                        .decode("utf-8", "ignore")
                        + "', '"
                        # + str(lstk[i])
                        # .encode("ascii", "ignore")
                        # .decode("utf-8", "ignore")
                        # + "', '"
                        + str(lstm[i])
                        .encode("ascii", "ignore")
                        .decode("utf-8", "ignore")
                        + "', "
                        + str(lsty[i])
                        .encode("ascii", "ignore")
                        .decode("utf-8", "ignore")
                        + ")",
                    )
                except:
                    pass
    for file in os.listdir("./data/restaurants"):
        all += 1
        if file.startswith("restaurant") and not file.endswith(".zip"):
            print(file)
            pd = pandas.read_csv(
                "./data/restaurants/" + file, engine="python", on_bad_lines="skip"
            )
            pd.columns = pd.columns.str.strip()
            lst = pd["review"].tolist()
            lsts = pd["sentiment"].tolist()
            pd = pandas.read_csv(
                "./dates/restaurants/" + file, engine="python", on_bad_lines="skip"
            )
            pd.columns = pd.columns.str.strip()
            lstm = pd[pd.columns[0]].tolist()
            lsty = pd[pd.columns[1]].tolist()
            # pd = pandas.read_csv(
            #     "./keywords/restaurants/" + file, engine="python", on_bad_lines="skip"
            # )
            # pd.columns = pd.columns.str.strip()
            # lstk = pd["Expressao"].tolist()
            for i in range(len(lst)):
                try:
                    insert_data(
                        conn,
                        table_name,
                        "(NULL, '"
                        + str(lst[i])
                        .encode("ascii", "ignore")
                        .decode("utf-8", "ignore")
                        + "', "
                        + str(all).encode("ascii", "ignore").decode("utf-8", "ignore")
                        + ", '"
                        + str(lsts[i])
                        .encode("ascii", "ignore")
                        .decode("utf-8", "ignore")
                        + "', '"
                        # + str(lstk[i])
                        # .encode("ascii", "ignore")
                        # .decode("utf-8", "ignore")
                        # + "', '"
                        + str(lstm[i])
                        .encode("ascii", "ignore")
                        .decode("utf-8", "ignore")
                        + "', "
                        + str(lsty[i])
                        .encode("ascii", "ignore")
                        .decode("utf-8", "ignore")
                        + ")",
                    )
                except:
                    pass

    conn.commit()

    keywords_from_review_by_month_year(conn, table_name)
    conn.commit()

    # export sqlite database to csv
    export_data(conn, "reviews", "./reviews.csv")
    export_data(conn, "business", "./business.csv")
    export_data(conn, "business_type", "./business_type.csv")
    export_data(conn, "keywords", "./keywords.csv")

    conn.close()


if __name__ == "__main__":
    main()
    print("Done")
