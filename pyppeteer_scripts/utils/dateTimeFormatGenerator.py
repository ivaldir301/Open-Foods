from datetime import datetime

def generateDateTimeInFormat() -> str:
    return datetime.today().strftime('%Y-%m-%d %H:%M:%S')

