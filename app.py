#!/usr/bin/env python

"""
Welcome to Amity.
Amity is a room allocation system for one of Andela's facilities called Amity.
Usage:
    app.py create_room <room_name>... [--ls | --of]
    app.py add_person <first_name> <last_name> <job_type> [<wants_accommodation>]
    app.py get_person_id <first_name> <last_name>
    app.py reallocate_person <person_identifier> <new_room_name>
    app.py load_people <filename>
    app.py print_allocations [--o=FILENAME]
    app.py print_unallocated [--o=FILENAME]
    app.py print_room <room_name>
    app.py save_state [--db=sqlite_database]
    app.py load_state [<sqlite_database>]
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
    --o FILENAME             Specify filename
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


def amity_print(arg, color='green'):
    ''' This is a simple print function that adds color to printed output. '''
    cprint("\n" + arg + "\n", color)


class AmityCLI(cmd.Cmd):
    '''
        This class create the AMity Command Line Interface for user interaction
    '''
    amity_prompt = colored('Amity > ', 'magenta', attrs=['bold'])
    prompt = amity_prompt

    @docopt_cmd
    def do_create_room(self, args):
        """
        This command creates rooms in Amity.

        You can create multiple rooms by specifying multiple room names
        after the create_room command. By default, this method will create an
        office/offices unless '--ls' is specified after the room name or list
        of room names. The '--of' option can be specified but it's not
        necessary.

        Usage: create_room <room_name>... [--ls | --of]
        """
        rooms_args = []
        for room in args['<room_name>']:
            rooms_args.append(room.capitalize())
        if args['--ls'] is True:
            rooms_args.append('-ls')
        elif args['--of'] is True:
            rooms_args.append('-o')
        amity_print(amity.create_room(rooms_args))

    @docopt_cmd
    def do_add_person(self, args):
        """
        This command adds a person and allocates them a random room in Amity.

        The <job_type> argument specifies the role of the person being added
        which can either be 'Fellow' or 'Staff'.

        The <wants_accommodation> argument tells the system whether or not the
        person being added wants a room or not. It only accepts 'Y' or 'N'
        characters which stand for 'Yes' or 'No' respectively. It is an
        optional argument and its default value is 'N'.

        Usage: add_person <first_name> <last_name> <job_type> [<wants_accommodation>]
        """
        person_name = args['<first_name>'].capitalize()
        person_name += " " + args['<last_name>'].capitalize()
        role = args['<job_type>'].capitalize()
        if role != 'Fellow' and role != 'Staff':
            amity_print("Please check your arguments."\
                        "\n- <job_type> can either be 'Fellow' or 'Staff' "\
                        "only.\n- Type 'help add_person' for more information",
                        'red')
            return
        boarding = args['<wants_accommodation>'] or 'N'
        boarding = boarding.upper()
        if boarding != 'Y' and boarding != 'N':
            amity_print("Please check your arguments."\
                        "\n- <wants_accommodation> can either be 'Y' or "\
                        "'N' only.\n- Type 'help add_person' for "\
                        "more information", 'red')
            return
        amity_print(amity.add_person(person_name, role, boarding))

    @docopt_cmd
    def do_get_person_id(self, args):
        """
        This command gets a person's ID from the Amity database.

        The <first_name> and <last_name> arguments are required to successfuly
        fetch the person's ID. It should be noted that in some situations,
        more than one Person ID may be returned when we have people with identical
        names.

        Usage: get_person_id <first_name> <last_name>
        """
        person_name = args['<first_name>'].capitalize()
        person_name += " " + args['<last_name>'].capitalize()
        amity_print(amity.get_person_id(person_name))

    @docopt_cmd
    def do_reallocate_person(self, args):
        """
        This command reallocates a person to another room.

        It takes thes person's ID which can be gotten from the list of
        allocations in a particular room when print_room is run so it is
        highly recommended that you first get the person's ID from the
        print_room command.

        The second argument it takes is the name of the room to which you want
        to allocate the person to.

        Usage: reallocate_person <person_identifier> <new_room_name>
        """
        person_id = args['<person_identifier>'].lower()
        room_name = args['<new_room_name>']
        amity_print(amity.reallocate_person(person_id, room_name))

    @docopt_cmd
    def do_load_people(self, args):
        """
        This commands loads people to the Amity System from a text file.

        It simply takes the name of the file to load a list of people from as
        the argument.

        NB: All input files are located in the 'data/inputs' directory.

        Usage: load_people <filename>
        """
        amity_print(amity.load_people(args['<filename>']))

    @docopt_cmd
    def do_print_allocations(self, args):
        """
        This commands prints all of Amity's allocation to the screen and also
        saves the printout to a text file if provided with a file name.

        It simply takes the name of the file to save the allocations printout
        as an option argument after '--o='. This argument is optional. If not
        provided, the printout will not be saved to a file.

        NB: All allocations files are saved in the 'data/outputs/allocations'
            directory.

        Usage: print_allocations [--o=FILENAME]
        """
        amity_print(amity.print_allocations(args['--o']))

    @docopt_cmd
    def do_print_unallocated(self, args):
        """
        This commands prints all of Amity's unallocated people to the screen
        and also saves the printout to a text file if provided with a filename.

        It simply takes the name of the file to save the unallocated persons
        printout as an option argument after '--o='. This argument is optional.
        If not provided, the printout will not be saved to a file.

        NB: All unallocated persons files are saved in the
            'data/outputs/unallocations' directory.

        Usage: print_unallocated [--o=FILENAME]
        """
        amity_print(amity.print_unallocated(args['--o']))

    @docopt_cmd
    def do_print_room(self, args):
        """
        This commands prints room details.

        It accepts a room name then querries Amity System and returns
        information about the room given.

        Usage: print_room <room_name>
        """
        print "\n"
        data = amity.print_room(args['<room_name>'].lower())
        if isinstance(data, str):
            amity_print(data)
        print "\n"

    @docopt_cmd
    def do_save_state(self, args):
        """
        This command persists the current state of the system to an SQLite
        Database.

        It takes an option '--db=' which specifies the name to give the
        database file which we will use to save the state of the applicaion.
        If no DB name is given, the state is saved in a file named 'latest.db'

        NB: All DB files are saved in the 'data/states' directory.

        Usage: save_state [--db=sqlite_database]
        """
        if not args['--db']:
            args['--db'] = 'latest.db'
        amity_print(amity.save_state(args['--db']))

    @docopt_cmd
    def do_load_state(self, args):
        """
        This command loads a previously saved state from an SQLite database to
        the Amity System.

        It takes an argument, <sqlite_database> which specifies the name of the
        SQLite database file to load the state from. This argument is optional.
        If no argument is provided, 'latest.db' will be loaded.

        NB: All DB files are loaded from the 'data/states' directory.

        Usage: load_state [<sqlite_database>]
        """
        if not args['<sqlite_database>']:
            args['<sqlite_database>'] = 'latest.db'
        if len(amity.current_state) == 0:
            amity.current_state = args['<sqlite_database>'][:-3]
            amity_print(amity.load_state(args['<sqlite_database>']))
        else:
            e = "You have already loaded a state.\n"
            e += "Your current state is the '"
            e += amity.current_state
            e += "' DB in the 'data/states' directory.\n"
            e += "You cannot load another state while in this session.\n"
            e += "To load another state restart the application "
            e += "to start a new session."
            amity_print(e, 'red')

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
