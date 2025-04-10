import json
from datetime import datetime

def repo_to_file_name(repo_name):
    return repo_name.replace('/', '-')

def write_json(filename, json_data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
        
def read_json(filename):
    with open(filename) as json_data:
        return json.load(json_data)

def mk_quarter(year, q):
    return f'{year} Q{q}'

def datestring_to_quarter(string):
    return datetime_to_quarter(datetime.strptime(string, '%Y-%m-%dT%H:%M:%SZ'))

def datetime_to_quarter(datetime):
    return mk_quarter(datetime.year, (datetime.month-1)//3 + 1)

def quarter_to_numbers(quarter):
    q = int(quarter[6])
    year = int(quarter[0:4])
    return year, q

def inc_quarter(quarter):
    year, q = quarter_to_numbers(quarter)
    if(q == 4):
        return mk_quarter(year+1, 1)
    
    return mk_quarter(year, q+1)

def generate_quarters(q_from, q_to):
    while q_from != q_to:
        yield q_from
        q_from = inc_quarter(q_from)
