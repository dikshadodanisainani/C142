import csv

all_movies = []

with open(r"C:\Diksha_workplace\python\c-142-main\c-142-main\final.csv", "r",encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []