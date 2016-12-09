#!/usr/bin/env python

"""
Welcome to Amity.
Amity is a room allocation system for one of Andela's facilities called Amity.
Usage:
    app.py create_room <room_name>... (-ls | -of)
    app.py add_person <first_name> <last_name> <job_type> <wants_accommodation>
    app.py reallocate_person <person_identifier> <new_room_name>
    app.py load_people <filename>
    app.py print_allocations [--o=filename]
    app.py print_unallocated [--o=filename]
    app.py print_room <room_name>
    app.py save_state [--db=sqlite_database]
    app.py load_state <sqlite_database>
    app.py (-i | --interactive)
    app.py (-h | --help)
    app.py quit
    quit
Arguments
  <room_name> Unique name for them Room to be created or querried
  <first_name> The first name of the Person
  <last_name> The last name of the Person
  <job_type> The role of the Person being added i.e. Fellow or Staff
  <wants_accommodation> Whether Person wants accomodation or not i.e 'N' or 'Y'
  <person_identifier> Unique User ID of the Person
  <new_room_name> The Room name to reallocate the Person to.
  <filename> Name of input or output data file
  <sqlite_database> Name of output or input DB
Options:
    -i --interactive  Interactive Mode
    -h --help  Show this screen and exit
    -ls --livingspace Living Space Room
    -of --office Office Room type
    --o filename  Specify filename
    --db sqlite_databse Name of SQLite Database
    -v --version
"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    print(arguments)
