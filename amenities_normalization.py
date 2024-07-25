import ast
import spacy
import sqlite3

nlp = spacy.load("en_core_web_sm")

def create_amenities_file():
    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        curr.execute("SELECT amenities FROM room_rates")
        rows = curr.fetchall()

    amenities = set()

    for row in rows:
        am_list = ast.literal_eval(row[0])
        amenities.update(am_list)

    sorted_amenities = sorted(list(amenities), key=lambda x: x.lower())

    with open("amenities_unique.txt", "w") as f:
        for am in sorted_amenities:
            f.write(am + "\n")

if __name__ == "__main__":
    create_amenities_file()