[![Build Status](https://travis-ci.org/andela-akhenda/cp1a.svg?branch=develop)](https://travis-ci.org/andela-akhenda/cp1a)
[![Coverage Status](https://coveralls.io/repos/github/andela-akhenda/cp1a/badge.svg?branch=develop&update=33)](https://coveralls.io/github/andela-akhenda/cp1a?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/867bd5023ec34cf6973af2d12ccfba28)](https://www.codacy.com/app/joseph-akhenda/cp1a?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andela-akhenda/cp1a&amp;utm_campaign=Badge_Grade)
[![Code Health](https://landscape.io/github/andela-akhenda/cp1a/develop/landscape.svg?style=flat)](https://landscape.io/github/andela-akhenda/cp1a/develop)
[![Travis](https://img.shields.io/badge/Chuck%20Norris-Approved-lightgrey.svg)](https://github.com/andela-akhenda/cp1a)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/andela-akhenda/cp1a/blob/master/LICENSE)
[![PyPI](https://img.shields.io/badge/Python-2.7-blue.svg)](https://www.python.org/downloads/release/python-2712/)

# Amity Space Allocation

Amity is a Python Console Application for one of Andela's facilities called Amity. Amity creates rooms which can be offices or living spaces. An office can occupy a maximum of 6 people. A living space can inhabit a maximum of 4 people. It also creates and allocates a person rooms. A person to be allocated could be a fellow or staff. Staff cannot be allocated living spaces. Fellows have a choice to choose a living space or not. This system will be used to automatically allocate spaces to people at random.


## Installation

Clone this repo:
```
$ git clone https://github.com/andela-akhenda/cp1a.git
```

Navigate to the `cp1a` directory:
```
$ cd cp1a
```

Create a vitual environment:
> Use [this guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/) to create and activate a virtual environment.

Install the required packages:
```
$ pip install -r requirements.txt
```


## Testing

Run tests using one of the following commands:
```
$ python setup.py test

running pytest
running egg_info
writing amity.egg-info/PKG-INFO
writing top-level names to amity.egg-info/top_level.txt
writing dependency_links to amity.egg-info/dependency_links.txt
reading manifest file 'amity.egg-info/SOURCES.txt'
writing manifest file 'amity.egg-info/SOURCES.txt'
running build_ext
================================================================================ test session starts ================================================================================
platform darwin -- Python 2.7.12, pytest-3.0.4, py-1.4.31, pluggy-0.4.0 -- /Users/hendaz/.virtualenvs/amity-venv/bin/python
cachedir: .cache
rootdir: /Users/hendaz/Projects/cp1a, inifile: setup.cfg
plugins: mock-1.4.0, cov-2.4.0
collected 40 items

tests/test_amity.py::TestAmity::test_add_person PASSED
tests/test_amity.py::TestAmity::test_add_to_fully_occupied_rooms PASSED
tests/test_amity.py::TestAmity::test_amity_class_instance PASSED
tests/test_amity.py::TestAmity::test_cannot_add_duplicate_room PASSED
tests/test_amity.py::TestAmity::test_create_multiple_rooms PASSED
tests/test_amity.py::TestAmity::test_create_room PASSED
tests/test_amity.py::TestAmity::test_create_room_receives_list PASSED
tests/test_amity.py::TestAmity::test_get_empty_rooms PASSED
tests/test_amity.py::TestAmity::test_get_person_details_and_uuid PASSED
tests/test_amity.py::TestAmity::test_if_a_person_is_fellow_or_staff PASSED
tests/test_amity.py::TestAmity::test_load_people_from_file PASSED
tests/test_amity.py::TestAmity::test_load_state PASSED
tests/test_amity.py::TestAmity::test_load_state_from_non_conforming_db PASSED
tests/test_amity.py::TestAmity::test_occupants_after_allocation PASSED
tests/test_amity.py::TestAmity::test_occupants_increment_on_allocation PASSED
tests/test_amity.py::TestAmity::test_person_cannot_be_allocated_room_when_no_rooms_exist PASSED
tests/test_amity.py::TestAmity::test_print_allocations PASSED
tests/test_amity.py::TestAmity::test_print_allocations_with_no_previous_file PASSED
tests/test_amity.py::TestAmity::test_print_empty_room PASSED
tests/test_amity.py::TestAmity::test_print_room PASSED
tests/test_amity.py::TestAmity::test_print_unallocated PASSED
tests/test_amity.py::TestAmity::test_print_unallocated_with_no_previous_file PASSED
tests/test_amity.py::TestAmity::test_reallocate_non_existent_uuid PASSED
tests/test_amity.py::TestAmity::test_reallocate_person_accepts_strings_only PASSED
tests/test_amity.py::TestAmity::test_reallocate_person_to_an_office PASSED
tests/test_amity.py::TestAmity::test_response_on_no_rooms PASSED
tests/test_amity.py::TestAmity::test_save_state PASSED
tests/test_person.py::TestPerson::test_add_person PASSED
tests/test_person.py::TestPerson::test_child_class_instance PASSED
tests/test_person.py::TestPerson::test_get_person PASSED
tests/test_person.py::TestPerson::test_get_person_only_accepts_strings PASSED
tests/test_person.py::TestPerson::test_get_person_with_invalid_uuid PASSED
tests/test_person.py::TestPerson::test_if_a_person_is_fellow_or_staff PASSED
tests/test_person.py::TestPerson::test_number_of_persons_increment_after_addition PASSED
tests/test_room.py::TestRoom::test_add_to_fully_occupied_rooms PASSED
tests/test_room.py::TestRoom::test_child_class_instance PASSED
tests/test_room.py::TestRoom::test_create_duplicate_room PASSED
tests/test_room.py::TestRoom::test_create_room PASSED
tests/test_room.py::TestRoom::test_occupants_after_reallocation PASSED
tests/test_room.py::TestRoom::test_occupants_increment_on_allocation PASSED
```
or
```
$ nosetests --verbose

test_add_person (tests.test_amity.TestAmity) ... ok
test_add_to_fully_occupied_rooms (tests.test_amity.TestAmity) ... ok
test_amity_class_instance (tests.test_amity.TestAmity) ... ok
test_cannot_add_duplicate_room (tests.test_amity.TestAmity) ... ok
test_create_multiple_rooms (tests.test_amity.TestAmity) ... ok
test_create_room (tests.test_amity.TestAmity) ... ok
test_create_room_receives_list (tests.test_amity.TestAmity) ... ok
test_get_empty_rooms (tests.test_amity.TestAmity) ... ok
test_get_person_details_and_uuid (tests.test_amity.TestAmity) ... ok
test_if_a_person_is_fellow_or_staff (tests.test_amity.TestAmity) ... ok
test_load_people_from_file (tests.test_amity.TestAmity) ... ok
test_load_state (tests.test_amity.TestAmity) ... ok
test_load_state_from_non_conforming_db (tests.test_amity.TestAmity) ... ok
test_occupants_after_allocation (tests.test_amity.TestAmity) ... ok
test_occupants_increment_on_allocation (tests.test_amity.TestAmity) ... ok
test_person_cannot_be_allocated_room_when_no_rooms_exist (tests.test_amity.TestAmity) ... ok
test_print_allocations (tests.test_amity.TestAmity) ... ok
test_print_allocations_with_no_previous_file (tests.test_amity.TestAmity) ... ok
test_print_empty_room (tests.test_amity.TestAmity) ... ok
test_print_room (tests.test_amity.TestAmity) ... ok
test_print_unallocated (tests.test_amity.TestAmity) ... ok
test_print_unallocated_with_no_previous_file (tests.test_amity.TestAmity) ... ok
test_reallocate_non_existent_uuid (tests.test_amity.TestAmity) ... ok
test_reallocate_person_accepts_strings_only (tests.test_amity.TestAmity) ... ok
test_reallocate_person_to_an_office (tests.test_amity.TestAmity) ... ok
test_response_on_no_rooms (tests.test_amity.TestAmity) ... ok
test_save_state (tests.test_amity.TestAmity) ... ok
test_add_person (tests.test_person.TestPerson) ... ok
test_child_class_instance (tests.test_person.TestPerson) ... ok
test_get_person (tests.test_person.TestPerson) ... ok
test_get_person_only_accepts_strings (tests.test_person.TestPerson) ... ok
test_get_person_with_invalid_uuid (tests.test_person.TestPerson) ... ok
test_if_a_person_is_fellow_or_staff (tests.test_person.TestPerson) ... ok
test_number_of_persons_increment_after_addition (tests.test_person.TestPerson) ... ok
test_add_to_fully_occupied_rooms (tests.test_room.TestRoom) ... ok
test_child_class_instance (tests.test_room.TestRoom) ... ok
test_create_duplicate_room (tests.test_room.TestRoom) ... ok
test_create_room (tests.test_room.TestRoom) ... ok
test_occupants_after_reallocation (tests.test_room.TestRoom) ... ok
test_occupants_increment_on_allocation (tests.test_room.TestRoom) ... ok

----------------------------------------------------------------------
Ran 40 tests in 0.057s

OK
```


## Usage

Launch the app in interactive mode:
```
$ python app.py -i

New to the system? Type 'help' to see a list of commands

Amity >
```

### Help
To get started, type 'help' to see a list of available commands
```
Amity > help

Documented commands (type help <topic>):
========================================
add_person   help         print_allocations  quit
create_room  load_people  print_room         reallocate_person
get_uuid     load_state   print_unallocated  save_state
```
To see individual command documentation, type 'help' followed by the command:
```
Amity > help create_room

        This command creates rooms in Amity.

        You can create multiple rooms by specifying multiple room names
        after the create_room command. By default, this method will create an
        office/offices unless '--ls' is specified after the room name or list
        of room names. The '--of' option can be specified but it's not
        necessary.

        Usage: create_room <room_name>... [--ls | --of]
```

### Create Room
```
create_room <room_name>... [--ls | --of]
```
This command creates rooms in Amity.
By default, this method will create an office/offices unless '--ls' is specified after the room name or list of room names. The '--of' option can be specified but it's not necessary:
```
Amity > create_room Abydos

The Office has been successfully created

```
You can create multiple rooms by specifying multiple room names after the create_room command:
```
Amity > create_room Dakara Daedalus --ls

Your 2 Living Spaces have been successfully created

```

### Add Person
```
add_person <first_name> <last_name> <job_type> [<wants_accommodation>]
```
The ```<job_type>``` argument specifies the role of the person being added which can either be 'Fellow' or 'Staff'.

The ```<wants_accommodation>``` argument tells the system whether or not the person being added wants a room or not. It only accepts 'Y' or 'N' characters which stand for 'Yes' or 'No' respectively. It is an optional argument and its default value is 'N'.

Adding a Fellow:
```
Amity > add_person Ronon Dex Fellow Y


The Fellow, Ronon Dex has been added successfuly and given the following rooms:-
1. Office       --> Abydos
2. Living Space --> Daedalus


```
Adding a Staff:
```
Amity > add_person Samantha Carter Staff


The Staff, Samantha Carter has been added successfuly and given the following room:-
1. Office       --> Abydos


```

### Get Person's UUID
```
get_uuid <first_name> <last_name>
```
This command gets a person's UUID from the Amity database.
The ```<first_name>``` and ```<last_name>``` arguments are required to successfuly fetch the person's UUID. It should be noted that in some situations, more than one UUID may be returned when we have people with identical names.
```
Amity > get_uuid Rodney McKay

Rodney Mckay's ID is: s2

```

### Reallocate Person
```
reallocate_person <person_identifier> <new_room_name>
```
This command reallocates a person to another room.
It takes thes person's UUID which can be gotten from the list of allocations in a particular room when print_room is run so it is highly recommended that you first get the person's UUID from the print_room command.
The second argument it takes is the name of the room to which you want to allocate the person to.
```
Amity > reallocate_person f4 daedalus

Mari Lawrence has been successfuly re-allocated from Dakara to Daedalus

```

### Load People
```
load_people <filename>
```
This commands loads people to the Amity System from a text file.
It simply takes the name of the file to load a list of people from as the argument.

***NB:*** All input files are located in the 'data/inputs' directory.
```
Amity > load_people test_people.txt

The Fellow, Oluwafemi Sule has been added successfuly and given the following rooms:-
1. Office       --> Argos
2. Living Space --> Dakara


The Staff, Dominic Walters has been added successfuly and given the following room:-
1. Office       --> Argos


The Fellow, Simon Patterson has been added successfuly and given the following rooms:-
1. Office       --> Argos
2. Living Space --> Dakara


The Fellow, Mari Lawrence has been added successfuly and given the following rooms:-
1. Office       --> Argos
2. Living Space --> Dakara


The Staff, Leigh Riley has been added successfuly and given the following room:-
1. Office       --> Abydos


The Fellow, Tana Lopez has been added successfuly and given the following rooms:-
1. Office       --> Abydos
2. Living Space --> Dakara


The Staff, Kelly Mcguire has been added successfuly and given the following room:-
1. Office       --> Argos


People have been successfuly added to the system.

```

### Print Allocations
```
print_allocations [--o=FILENAME]
```
This commands prints all of Amity's allocation to the screen and also saves the printout to a text file if provided with a file name.
It simply takes the name of the file to save the allocations printout as an option argument after '--o='. This argument is optional. If not provided, the printout will not be saved to a file.

***NB:*** All allocations files are saved in the 'data/outputs/allocations' directory.
```
Amity > print_allocations
==============================
         Offices
==============================


ABYDOS
-----------------------------------------------------------------
RONON DEX, SAMANTHA CARTER, RODNEY MCKAY, LEIGH RILEY, TANA LOPEZ


ARGOS
------------------------------------------------------------------------------
OLUWAFEMI SULE, DOMINIC WALTERS, SIMON PATTERSON, MARI LAWRENCE, KELLY MCGUIRE




==============================
         Living Spaces
==============================


DAKARA
-------------------------------------------
OLUWAFEMI SULE, SIMON PATTERSON, TANA LOPEZ


DAEDALUS
------------------------
RONON DEX, MARI LAWRENCE


```

### Print unallocated
```
print_unallocated [--o=FILENAME]
```
This commands prints all of Amity's unallocated people to the screen and also saves the printout to a text file if provided with a filename.
It simply takes the name of the file to save the unallocated persons printout as an option argument after '--o='. This argument is optional. If not provided, the printout will not be saved to a file.

***NB:*** All unallocated persons files are saved in the 'data/outputs/unallocations' directory.
```
Amity > print_unallocated
==============================
Without Offices
==============================

F4  TANA LOPEZ

S3  KELLY MCGUIRE

S2  LEIGH RILEY

S1  DOMINIC WALTERS



==============================
Without Living Spaces
==============================

F3 (Y)  MARI LAWRENCE

F4 (Y)  TANA LOPEZ


```

### Print Room
```
print_room <room_name>
```
This commands prints room details.
It accepts a room name then querries Amity System and returns information about the room given.
```
Amity > print_room Dakara


DAKARA
-------------------------
F1  Y   OLUWAFEMI SULE
F2  Y   SIMON PATTERSON
F4  Y   TANA LOPEZ


```

### Save State
```
save_state [--db=sqlite_database]
```
This command persists the current state of the system to an SQLite Database.
It takes an option '--db=' which specifies the name to give the database file which we will use to save the state of the applicaion. If no DB name is given, the state is saved in a file named 'latest.db'

***NB:*** All DB files are saved in the 'data/states' directory.
```
Amity > save_state
Opened database successfully
Table created successfully

You have successfuly persisted the state of the Application.
The state was saved to 'latest.db' file in the 'data/states' directory.

```
```
Amity > save_state --db=December_2016.db
Opened database successfully
Table created successfully

You have successfuly persisted the state of the Application.
The state was saved to 'December_2016.db' file in the 'data/states' directory.

```

### Load State
```
load_state [<sqlite_database>]
```
This command loads a previously saved state from an SQLite database to the Amity System.
It takes an argument, ```<sqlite_database>``` which specifies the name of the SQLite database file to load the state from. This argument is optional. If no argument is provided, 'latest.db' will be loaded.

***NB:*** All DB files are loaded from the 'data/states' directory.
```
Amity > load_state December_2016.db
Opened database successfully
Operation done successfully

You have successfuly loaded a previously saved state.
The state was loaded from 'December_2016.db' file in the 'data/states' directory.

```


> Watch the following screencast to get the full usage:

[![asciicast](https://asciinema.org/a/0djbwzd9b6anhjwv7okxb42iy.png)](https://asciinema.org/a/0djbwzd9b6anhjwv7okxb42iy?speed=2)


## Credits

1. [@andela-akhenda](https://github.com/andela-akhenda)

2. [@kimobrian](https://github.com/kimobrian)

3. [@andela-mochieng](https://github.com/andela-mochieng)

4. The [Andela](https://www.andela.com) Community.


## License

### The MIT License (MIT)

Copyright (c) 2016 [Joseph Akhenda](https://github.com/andela-akhenda).

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.
