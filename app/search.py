import dateutil.parser as parser

def get_dates(dates):
    (start_date, end_date) = dates.split("-")
    # Change dates of the form May 1-7 to May 1-May 7
    # spacy ensures that the dash has no spaces between words
    # Check if the first character of end_date is a digit
    if end_date[0].isdigit():
        end_date = start_date.split()[0] + " " + end_date

    start_date = parser.parse(start_date)
    end_date = parser.parse(end_date)
    delta = end_date - start_date
    print("Start Date:", start_date.strftime("%B %d, %Y"))
    print("End Date:", end_date.strftime("%B %d, %Y"))
    print("Number of days:", delta.days + 1)

    return (start_date, end_date)
