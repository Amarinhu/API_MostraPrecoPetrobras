from datetime import datetime

# Date string
date_string = "02/04/2024"
date_string2 = "02/10/2024"

# Parse the date string into a datetime object
date_object = datetime.strptime(date_string, "%m/%d/%Y")
date_object2 = datetime.strptime(date_string2, "%m/%d/%Y")

# Convert the datetime object into a timestamp (seconds since the epoch)
timestamp_seconds = date_object.timestamp()
timestamp_seconds2 = date_object2.timestamp()

# Convert the timestamp to milliseconds
timestamp_milliseconds = int(timestamp_seconds * 1000)
timestamp_milliseconds2 = int(timestamp_seconds2 * 1000)

print(timestamp_milliseconds)

print(timestamp_milliseconds2)