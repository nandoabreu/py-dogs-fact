#! /usr/bin/env python3

import json
import dogs_fact


if __name__ == '__main__':
    fact = dogs_fact.get_fact()
    print(json.dumps(fact))

