#!/bin/env python3

import sys
import requests
from cortx.db import const

def main():
    response = requests.get(f'http://{const.HOST}:{const.PORT}', verify=False)    
    return response.json()['HealthStatus']

if __name__ == '__main__':
    main()
