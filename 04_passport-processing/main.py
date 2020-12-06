#!/usr/bin/env python3

# https://adventofcode.com/2020/day/4

import os
import sys
import re

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    passports = [passport.replace('\n', ' ') for passport in file.read().strip().split('\n\n')]


def parse_passports(data, all_req=False):
    keys = set("byr iyr eyr hgt hcl ecl pid".split())
    valid = 0
    for passport in data:
        data = dict(field.split(':') for field in passport.split())
        if all(key in data for key in keys):
            if all_req:
                if 1920 <= int(data['byr']) <= 2002 \
                        and 2010 <= int(data['iyr']) <= 2020 <= int(data['eyr']) <= 2030\
                        and re.match(r'\d+..', data['hgt'])\
                        and (
                            data['hgt'].endswith('cm') and 150 <= int(data['hgt'][:-2]) <= 193
                            or
                            data['hgt'].endswith('in') and 59 <= int(data['hgt'][:-2]) <= 76
                        )\
                        and re.match(r'^#[\da-f]{6}$', data['hcl'])\
                        and data['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']\
                        and re.match(r'^\d{9}$', data['pid']):
                    valid += 1
            else:
                valid += 1
    return valid


def get_output_1(data):
    print(parse_passports(data))


def get_output_2(data):
    print(parse_passports(data, all_req=True))


get_output_1(passports)
get_output_2(passports)
