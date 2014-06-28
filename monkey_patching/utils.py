from datetime import date


WEEKDAYS = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]


def day_of_week():
    return WEEKDAYS[date.today().weekday()]
