#! /usr/bin/env python3
'''
Python Dogs' Fact module

Python module to retrieve facts from a CSV data set.
This module responds with a sorted fact about dogs, with data learned from
Purina, Drake Center Vet, Pet Assure and Petfinder.

See: https://github.com/nandoabreu/py-dogs-fact


Build and run:
    make compose && make run
    (then run wget -q -S -O http://localhost:5000/)

Usage from command line:
    python -m dogs_fact | python -m json.tool

Usage as imported module:
    import dogs_fact
    dogs_fact.get_fact()

'''
import os
import csv
import random
import config as cfg


_facts_file = os.path.join(cfg.data_dir, cfg.facts_csv)
_sources_file = os.path.join(cfg.data_dir, cfg.sources_csv)

if \
    not os.path.isfile(_facts_file) or \
    not os.path.isfile(_sources_file): 
        raise FileNotFoundError

def _load_data(csv_file) -> list:
    res = []

    with open(csv_file) as f:
        _csv = csv.DictReader(f, delimiter=';')
        for data in _csv:
            res.append(data)

    return res


_sources = _load_data(_sources_file)

def get_fact(limit=1, rand=True):
    res = {'facts': [], 'node': 'N/A'}

    _data = _load_data(_facts_file)
    if _data:
        limit = min(limit, len(_data))

        if rand: res['facts'] = random.sample(_data, limit)
        else: res['facts'] = _data[:limit]

#    for fact in res['facts']:
#        fact['SOURCE'] = _sources[int(fact['SOURCE'])]

    return res

