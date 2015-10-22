#! /usr/bin/env python

import requests
from awesome_print import ap

if __name__ == '__main__':
    resp = requests.get('https://api.github.com/users/macro1/repos')
    ap(resp.json())
