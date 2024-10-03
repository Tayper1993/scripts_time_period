from datetime import datetime, timedelta


def expand_schedule(dates):
    expanded_dates = []

    for start_date, end_date in dates:

        current_date = start_date
        while current_date <= end_date:
            expanded_dates.append(current_date)
            current_date += timedelta(days=1)

    return expanded_dates


schedule = [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
]

expanded_schedule = expand_schedule(schedule)

# Вывод результата
for date in expanded_schedule:
    print(date)