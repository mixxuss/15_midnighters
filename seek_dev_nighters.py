import requests
import pytz
import datetime

def load_attempts(pages=3):
    url = 'https://devman.org/api/challenges/solution_attempts/'
    for page in range(1, pages):
        params = {'page': page}
        response = requests.get(url, params)
        records = response.json()['records']
        for record in records:
            if record['timestamp']:
                yield record


def isit_midnighter(record):
    pass_time = datetime.datetime.fromtimestamp(record['timestamp'],
                                                tz=pytz.timezone(record['timezone']))
    if pass_time.time() >= datetime.time(hour=0) and pass_time.time() <= datetime.time(hour=1):
        return record['username']


if __name__ == '__main__':
    records = load_attempts()
    for record in records:
        if isit_midnighter(record):
            print(isit_midnighter(record))