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
    delta = end_date - start_date
    print("Start Date:", start_date.strftime("%B %d, %Y"))
    print("End Date:", end_date.strftime("%B %d, %Y"))
    print("Number of days:", delta.days + 1)

    return (start_date, end_date)
