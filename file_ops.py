import json


def save_results(data, fname):
    with open(fname, 'w', encoding='utf-8') as fout:
        json.dump(data, fout, ensure_ascii=False)
