import sqlite3

ddl = """
CREATE TABLE IF NOT EXISTS airplanes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    manufacturer VARCHAR,
    passengers INTEGER,
    range INTEGER
)"""


with sqlite3.connect("travelectable.db") as conn:
    curr = conn.cursor()
    #curr.execute(ddl)
    #conn.commit()

    curr.execute(
        "INSERT INTO airplanes (name, manufacturer, passengers, range) VALUES (?, ?, ?, ?)",
        (
            "Aurora A980 Jumbo Jet",
            "Aerius",
            520,
            8500,
        ),
    )
    curr.execute(
        "INSERT INTO airplanes (name, manufacturer, passengers, range) VALUES (?, ?, ?, ?)",
        ("Aurora A250 Wide-Body Jet",
        "Aerius",
        250,
        5500,)
    )
    curr.execute(
        "INSERT INTO airplanes (name, manufacturer, passengers, range) VALUES (?, ?, ?, ?)",
        ("Aurora A100 Narrow-Body Jet",
        "Aerius",
        120,
        2500,)
    )
    curr.execute(
        "INSERT INTO airplanes (name, manufacturer, passengers, range) VALUES (?, ?, ?, ?)",
        ("Pinnacle P50 Turboprop",
        "Aerius",
        50,
        1000,)
    )
    curr.execute(
        "INSERT INTO airplanes (name, manufacturer, passengers, range) VALUES (?, ?, ?, ?)",
        ("Pinnacle P75 Regional Jet",
        "Aerius",
        75,
        1500,)
    )
    conn.commit()

    curr.execute(
        "INSERT INTO airplanes (name, manufacturer, passengers, range) VALUES (?, ?, ?, ?)",
        ("Celestial C600 Wide-Body Jet",
        "Celestia",
        480,
        8000,)
    )
    curr.execute(
        "INSERT INTO airplanes (name, manufacturer, passengers, range) VALUES (?, ?, ?, ?)",
        ("Celestial C300 Jumbo Jet",
        "Celestia",
        280,
        5000,)
    )
    curr.execute(
        "INSERT INTO airplanes (name, manufacturer, passengers, range) VALUES (?, ?, ?, ?)",
        ("Celestial C200 Narrow-Body Jet",
        "Celestia",
        160,
        3000,)
    )
    curr.execute(
        "INSERT INTO airplanes (name, manufacturer, passengers, range) VALUES (?, ?, ?, ?)",
        ("Skylink C75 Turboprop",
        "Celestia",
        75,
        1200,)
    )
    curr.execute(
        "INSERT INTO airplanes (name, manufacturer, passengers, range) VALUES (?, ?, ?, ?)",
        ("Skylink C90 Regional Jet",
        "Celestia",
        90,
        2000,)
    )
    conn.commit()
