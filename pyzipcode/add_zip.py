import os
import sys
import sqlite3

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Process add new zipcode.')
    parser.add_argument('-z', action='store', dest='zipcode')
    conn = sqlite3.connect('zipcodes.db')
    curs = conn.cursor()
    

    zipcode = raw_input('zipcode: ')
    curs.execute("SELECT * FROM ZipCodes WHERE zip = {};".format(zipcode))
    zip_results = curs.fetchall()
    if len(zip_results) >= 1:
        raise RuntimeError('Zipcode already exists in the database.')


    city = raw_input('city: ')
    state = raw_input('state: ')
    longitude = raw_input('longitude: ')
    latitude = raw_input('latitude: ')
    timezone = raw_input('timezone: ')
    dst = raw_input('dst (1/0): ')

    if dst not in ['1', '0']:
        raise RuntimeError('dst value must be 1 or 0.')

    sql_cmd = 'INSERT INTO ZipCodes values("{zipcode}", "{city}", "{state}", {longitude}, {latitude}, {timezone}, {dst});'.format(
        zipcode=zipcode,
        city=city,
        state=state,
        longitude=longitude,
        latitude=latitude,
        timezone=timezone,
        dst=dst,
    )
    confirm = raw_input('You are about to run `{}`...Do you wish to proceed Y/N?'.format(sql_cmd))

    if confirm not in ['Y', 'y']:
        raise RuntimeError('Canceling adding new zipcode.')
    
    curs.execute(sql_cmd)
    conn.commit()
    curs.execute("SELECT * FROM ZipCodes WHERE zip = {};".format(zipcode))
    zip_results = curs.fetchall()
    if len(zip_results) != 1:
        raise RuntimeError('Zipcode errored and was not added')

if __name__ == '__main__':
    main()
