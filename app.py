#!/usr/bin/env python

"""
Welcome to Amity.
Amity is a room allocation system for one of Andela's facilities called Amity.
Usage:
    app.py create_room <room_name>... [--ls | --of]
    app.py add_person <first_name> <last_name> <job_type> <wants_accommodation>
    app.py reallocate_person <person_identifier> <new_room_name>
    app.py load_people <filename>
    app.py print_allocations [--o=FILENAME]
    app.py print_unallocated [--o=FILENAME]
    app.py print_room <room_name>
    app.py save_state [--db=sqlite_database]
    app.py load_state <sqlite_database>
    app.py (-i | --interactive)
    app.py (-h | --help)
    app.py (-v | --version)
    app.py quit
    quit
Arguments
    <room_name>           Unique name for them Room to be created or querried
    <first_name>          The first name of the Person
    <last_name>           The last name of the Person
    <job_type>            The role of the Person being added i.e. Fellow or Staff
    <wants_accommodation> Whether Person wants accomodation or not i.e 'N' or 'Y'
    <person_identifier>   Unique User ID of the Person
    <new_room_name>       The Room name to reallocate the Person to.
    <filename>            Name of input or output data file
    <sqlite_database>     Name of output or input DB
Options:
    -i --interactive        Interactive Mode
    -h --help               Show this screen and exit
    -ls --livingspace       Living Space Room
    -of --office            Office Room type
    -o FILENAME             Specify filename
    --db sqlite_databse     Name of SQLite Database
    -v --version
"""

import os
import sys
import cmd
from termcolor import cprint, colored
from pyfiglet import figlet_format
from docopt import docopt, DocoptExit

from amity.amity import Amity


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """
    def fn(self, args):
        try:
            opt = docopt(fn.__doc__, args)
        except DocoptExit as error:
            # The DocoptExit is thrown when the args do not match
            print('The command entered is invalid!')
            print(error)
            return
        except SystemExit:
            # The SystemExit exception prints the usage for --help
            return
        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def app_header():
    '''
        This function creates the header that is displayed when the app
        launches
    '''
    os.system("clear")
    print("\n\n")
    cprint(figlet_format('AMITY', font='roman'), 'green')
    cprint('------------------------------------------------------------------', 'magenta')
    cprint("A room allocation system for one of Andela's facilities, Amity.", 'yellow')
    cprint('------------------------------------------------------------------', 'magenta')
    cprint("\nNew to the system? Type 'help' to see a list of commands\n", 'white')


def amity_print(arg):
    cprint("\n" + arg + "\n", 'green')


class AmityCLI(cmd.Cmd):
    '''
        This class create the AMity Command Line Interface for user interaction
    '''
    amity_prompt = colored('Amity > ', 'magenta', attrs=['bold'])
    prompt = amity_prompt

    @docopt_cmd
    def do_create_room(self, args):
        """ Usage: create_room <room_name>... [--ls | --of] """
        rooms_args = args['<room_name>']
        if args['--ls'] is True:
            rooms_args.append('-ls')
        elif args['--of'] is True:
            rooms_args.append('-o')
        amity_print(amity.create_room(rooms_args))

    @docopt_cmd
    def do_add_person(self, args):
        """ Usage: add_person <first_name> <last_name> <job_type> <wants_accommodation> """
        person_name = args['<first_name>'].capitalize()
        person_name += " " + args['<last_name>'].capitalize()
        role = args['<job_type>'].capitalize()
        boarding = args['<wants_accommodation>'].upper()
        amity_print(amity.add_person(person_name, role, boarding))

    @docopt_cmd
    def do_reallocate_person(self, args):
        """ Usage: reallocate_person <person_identifier> <new_room_name> """
        uuid = args['<person_identifier>'].lower()
        room_name = args['<new_room_name>']
        amity_print(amity.reallocate_person(uuid, room_name))

    @docopt_cmd
    def do_load_people(self, args):
        """ Usage: load_people <filename> """
        amity_print(amity.load_people(args['<filename>']))

    @docopt_cmd
    def do_print_allocations(self, args):
        """ Usage: print_allocations [--o=FILENAME] """
        amity_print(amity.print_allocations(args['--o']))

    @docopt_cmd
    def do_print_unallocated(self, args):
        """ Usage: print_unallocated [--o=FILENAME] """
        amity_print(amity.print_unallocated(args['--o']))

    @docopt_cmd
    def do_print_room(self, args):
        """ Usage: print_room <room_name> """
        print "\n"
        data = amity.print_room(args['<room_name>'].lower())
        if isinstance(data, str):
            amity_print(data)
        print "\n"

    @docopt_cmd
    def do_save_state(self, args):
        """ Usage: save_state [--db=sqlite_database] """
        if not args['--db']:
            args['--db'] = 'latest.db'
        amity_print(amity.save_state(args['--db']))

    @docopt_cmd
    def do_load_state(self, args):
        """ Usage: load_state <sqlite_database> """
        amity_print(amity.load_state(args['<sqlite_database>']))

    def do_quit(self, args):
        """ Quits the interactive mode """
        print "Goodbye!"
        print "Quiting Amity..."
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    app_header()
    amity = Amity()
    AmityCLI().cmdloop()
