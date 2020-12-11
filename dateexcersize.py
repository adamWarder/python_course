#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date Excersise with litsts and stringss
"""


def main():
    '''
    create month list
    ending list
    request user input
    '''

    # list of months
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    # lists of day endings 1st, 2nd...
    endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] + 7 * ['th'] \
        + ['st']

    # get user input
    year = input('Year?        : ')
    month = input('Month (1-12)?: ')
    day = input('Day   (1=31)?: ')

    # covnert inout to int
    month_no = int(month)
    day_no = endings[int(day) - 1]

    # get current month
    month_name = months[month_no - 1]

    # convert day to str and conact with ending
    ordinal = str(day) + day_no

    # concatenate string & output
    print(month_name + ' ' + ordinal + ', ' + year)

    # print(month_name)
    # print(ordinal)
    # print(year)

    return 0


if __name__ == '__main__':
    main()
