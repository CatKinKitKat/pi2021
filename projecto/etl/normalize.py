import os
import re
import unicodedata


def main():
    current_dir = os.getcwd()
    normalize_files(current_dir + "/scrapes/booking/hotels/")
    normalize_files(current_dir + "/scrapes/zomato/restaurantes/")
    normalize_files(current_dir + "/scrapes/tripadvisor/hotels/")
    normalize_files(current_dir + "/scrapes/tripadvisor/restaurants/")
    normalize_files(current_dir + "/scrapes/tripadvisor/activities/")


def normalize_files(directory):
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            normalize_file(directory + file)


def normalize_file(file_name):
    lines = []
    with open(file_name, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    with open(file_name, "w", encoding="utf-8", errors="ignore") as f:
        for line in lines:
            # f.write(normalize(remove_index(line)))
            f.write(normalize(line))


def normalize(text):
    text = remove_emoji(text)
    text = (
        unicodedata.normalize("NFKD", text)
        .encode("ascii", "ignore")
        .decode("utf-8", "ignore")
    )
    return text


# def remove_index(string):
#     return re.sub(r"^[^,]*,", "", string)
def remove_emoji(string):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r"", string)


if __name__ == "__main__":
    main()
