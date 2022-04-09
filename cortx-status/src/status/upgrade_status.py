#!/bin/env python3

import sys
import requests

def main():
    response = requests.get('http://localhost:8000', verify=False)    
    return response.json()

if __name__ == '__main__':
    main()
