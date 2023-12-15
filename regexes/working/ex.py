import re

s = input("Hours: ")
if match := re.search(r"^([01]?[0-9]|2[0-3]):?([0-5]?[0-9])? ?(am|pm)? (?:to) ([01]?[0-9]|2[0-3]):?([0-5]?[0-9])? ?(am|pm)?$", s, re.IGNORECASE):
        start_time = match.group(1)
        start_minutes = match.group(2)
        start_period = match.group(3).lower()
        hour_a = f"{start_time}{start_minutes}{start_period}"
        end_time = match.group(4)
        end_minutes = match.group(5)
        end_period = match.group(6).lower()
        if hour_a > 12:
            

print(hour_a)