import json
import requests


def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)

    wrapper.has_run = False
    return wrapper


def API_call(url):
    r = requests.get(url)
    return r.text


def API_formatter(url):
    data = json.loads(API_call(url))
    return data


@run_once
def Load_Database(url, db):
    data = API_formatter(url)
    print(db.execute("select * from flights").fetchall());

    for i in range(len(data)):
        db.execute("INSERT INTO flights (code,departure,arrival,price) VALUES (?,?,?,?);",
                      (data[i]['code'], data[i]['departure'], data[i]['arrival'],
                       data[i]['base_price']))
    db.commit()
