from datetime import datetime
import time


def get_current_date_and_timestamp():
    # Get the current date and time
    now = datetime.now()

    # Get the current Unix timestamp
    timestamp = int(time.time())

    # Format the date and time
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_date, timestamp


def main():
    date, timestamp = get_current_date_and_timestamp()
    print(f"Current Date and Time: {date}")
    print(f"Unix Timestamp: {timestamp}")


if __name__ == "__main__":
    main()
