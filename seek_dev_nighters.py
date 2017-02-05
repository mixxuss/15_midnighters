import requests
import pytz
from datetime import datetime

def load_attempts(pages=2):
    url = 'https://devman.org/api/challenges/solution_attempts/'
    for page in range(1, pages):
        params = {'page': page}
        response = requests.get(url, params)
        records = response.json()['records']
        for record in records:
            if record['timestamp']:
                yield record


def get_midnighters():
    pass

if __name__ == '__main__':
    print(load_attempts())
    for i in load_attempts():
        print(datetime.fromtimestamp(i['timestamp'], tz=pytz.timezone(i['timezone'])))
        # print(i)



    '''params = {}
    response = requests.get('https://devman.org/api/challenges/solution_attempts/')
    page = response.json()
    print(type(page))
    print(page['records'])
    def asw():
        for pa in page['records']:
            yield pa
    #for a in asw():
    #    print(a)'''