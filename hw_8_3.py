import time
import requests
# from pprint import pprint

url_ = 'https://api.stackexchange.com/2.3/questions?order=desc&sort=creation&site=stackoverflow'


def get_params():
    num_days, request = 2, ['Python']
    t_correction = 10800  # 3 hours
    t_end = int(time.mktime(time.localtime()) + t_correction)
    t_start = int(t_end - (num_days * 24 * 60 * 60))
    return {'fromdate': t_start, 'todate': t_end, 'tagged': request, 'pagesize': 100}


def get_data(url):
    flag, res, page = True, [], 1
    while flag:
        resp = requests.get(url, params={**get_params(), 'page': page}).json()
        res.extend(resp['items'])
        page += 1
        flag = resp['has_more']
    return res


def get_date(seconds):
    date = time.localtime(seconds)
    return time.strftime("%m/%d/%Y, %H:%M:%S", date)


if __name__ == '__main__':
    result = get_data(url_)
    creation_dates = [i['creation_date'] for i in result]
    questions_ids = [i['question_id'] for i in result]
    time_start_ = get_date(min(creation_dates))
    time_end_ = get_date(max(creation_dates))
    # pprint(result)
    print(f'Всего вопросов: {len(result)}')
    print(f' С {time_start_} по {time_end_}')
