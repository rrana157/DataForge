import random
from datetime import datetime, timedelta

def parse_relative_date(relative_str):
    today = datetime.today()

    if not isinstance(relative_str, str):
        raise TypeError("Relative date must be a string.")

    relative_str = relative_str.strip().lower()

    if relative_str == 'today':
        return today

    try:
        sign = relative_str[0]
        amount = int(relative_str[1:-1])
        unit = relative_str[-1]

        if sign not in ('-', '+'):
            raise ValueError("Date must start with '+' or '-'.")

        if unit == 'd':
            delta = timedelta(days=amount)
        elif unit == 'm':
            delta = timedelta(days=30 * amount)
        elif unit == 'y':
            delta = timedelta(days=365 * amount)
        else:
            raise ValueError("Invalid time unit. Use 'd', 'm', or 'y'.")

        return today - delta if sign == '-' else today + delta

    except Exception as e:
        raise ValueError(f"Invalid format: '{relative_str}'") from e

def date_between(start_date='-2y', end_date='today'):
    def to_datetime(date_input):
        if isinstance(date_input, datetime):
            return date_input
        elif isinstance(date_input, str):
            try:
                return parse_relative_date(date_input)
            except ValueError:
                try:
                    return datetime.strptime(date_input, '%Y-%m-%d')
                except:
                    raise ValueError(f"Bad date format: {date_input}.")
        else:
            raise TypeError("Input must be a string or datetime.")

    start = to_datetime(start_date)
    end = to_datetime(end_date)

    if start > end:
        start, end = end, start

    days_range = (end - start).days
    if days_range <= 0:
        return start.date()  # Same day if range invalid
    return (start + timedelta(days=random.randint(0, days_range))).date()

def generate_employment_dates(min_years_ago=5, max_years_ago=0):
    """
    Generates realistic employment start and exit dates.
    Exit date is always after start date, or None (if still employed).
    """
    # Generate start date from range like -10y to -1y
    start_date = date_between(f"-{min_years_ago}y", f"-{max_years_ago}y")

    # 30% chance the employee is still working (no exit)
    if random.random() < 0.75:
        return start_date, None

    # Otherwise, choose exit date after start_date up to today
    start_datetime = datetime.combine(start_date, datetime.min.time())
    exit_date = date_between(start_datetime, 'today')

    return start_date, exit_date
