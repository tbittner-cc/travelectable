import dateutil.parser as parser

def parse_dates(dates):
    (start_date, end_date) = dates.split("-")
    # spaCy ensures that the dash has no spaces between words
    # Check if the first character of end_date is a digit
    # This is to handle the case of "May 1st-7th" or "May 1-7"
    if end_date[0].isdigit():
        end_date = start_date.split()[0] + " " + end_date

    start_date = parser.parse(start_date)
    end_date = parser.parse(end_date)

    start_date = start_date.strftime("%Y-%m-%d")
    end_date = end_date.strftime("%Y-%m-%d")

    return (start_date, end_date)
