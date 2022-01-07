import os


def main():
    current_dir = os.getcwd()
    open_dir(current_dir + "/scrapes/booking/hotels/")
    open_dir(current_dir + "/scrapes/zomato/restaurantes/")
    open_dir(current_dir + "/scrapes/tripadvisor/hotels/")
    open_dir(current_dir + "/scrapes/tripadvisor/restaurants/")
    open_dir(current_dir + "/scrapes/tripadvisor/activities/")


def open_dir(directory):
    for file in os.listdir(directory):
        if file.endswith(".csv") and not file.startswith("list"):
            open_file(directory + file)


def open_file(file_name):
    lines = []
    with open(file_name, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    with open(file_name, "w", encoding="utf-8", errors="ignore") as f:
        for line in lines:
            f.write(fix_line(line))


def fix_line(line):
    line = trim_line(line)
    if "Avaliações" in line:
        line = line.replace('"', "").strip() + str("\n")

    return line


def trim_line(line):
    line = line.replace('"', "").strip()
    line = line + str('"')
    line = line[::-1]
    line = line + str('"')
    line = line[::-1]
    line = line + str("\n")

    return line


if __name__ == "__main__":
    main()
