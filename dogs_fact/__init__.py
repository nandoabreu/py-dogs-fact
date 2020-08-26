#! /usr/bin/env python3
'''
Python Dogs' Fact package

Python package to retrieve facts from a CSV data set.
This package responds with a sorted fact about dogs, with data learned from
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
import random
import config as cfg


_facts_file = os.path.join(cfg.data_dir, cfg.facts_csv)
_sources_file = os.path.join(cfg.data_dir, cfg.sources_csv)
if \
    not os.path.isfile(_facts_file) or \
    not os.path.isfile(_sources_file): 
        raise FileNotFoundError

def _load_data(csv_file, limit=None, rand=False) -> dict:
    with open(csv_file) as file:
        lines = file.read().splitlines()

        headers = tuple( h.lower() for h in lines[0].split(';') )
        del lines[0] # remove csv header

        if headers[0] == 'id':
            has_id = True
            hstart = 0 # keep id in dict to validate
        else:
            has_id = False
            hstart = 0

        size = len(lines)
        limit = min(limit, size) if limit and limit > 0 else size
        if rand: lines = random.sample(lines, limit)

        res = {}
        row_id = -1
        for line in lines:
            line = line.split(';')

            if has_id:
                row_id = line[0]
            else:
                row_id += 1

            res[row_id] = {}

            for i in range(hstart, len(headers)):
                key = headers[i]
                res[row_id][key] = line[i]

        return res


_sources = _load_data(_sources_file)

def get_fact():
    _fact = _load_data(_facts_file, limit=1, rand=True)
    _fact[0]['source'] = _sources[_fact[0]['source']]
    return _fact

