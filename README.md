# Phase 3 Mock Code Challenge - Squirrels at Home

For this challenge, we'll be working with a domain that involves squirrels.

We have one model: `Squirrel`.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- lists and list Methods
- SQL queries
- ORM methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

You will not have to build the tables as they'll be created for you
automatically when you first run `debug.py`.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects. There are no formal tests to run with this code so be
sure to test it in the `debug.py` often.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

#### Squirrel

- `Squirrel __init__(self, name, num_acorns, rabid)`
  - `Squirrel` is initialized with a name (string), num_acorns (integer) and rabid (boolean)
- `Squirrel property name()`
  - Returns the `Squirrel`'s name
  - Name must be a string between 1 and 15 characters
- `Squirrel property num_acorns()`
  - Returns the `Squirrel`'s number of acorns
  - The num_acorns must be an integer greater or equal to 0
- `Squirrel introduction()`
  - Returns a string formateed like so:
  - `"Hello! My name is {name} and I am {rabid | not rabid}"`
- `Squirrel save()`
  - Creates a squirrel in the database if an squirrel with the same id doesn't exist
  - Updates a squirrel in the database if a squirrel with the same id exists
- `Squirrel classmethod query_all()`
  - Returns a list of squirrel instances based on rows in the database
  - The return value ought to be a list of Squirrel instances
- `Squirrel classmethod query_one(id)`
  - Returns a squirrel instance from the database with the matching id
  - The return value ought to be a Squirrel instance
- `Squirrel classmethod query_rabid()`
  - Returns a list of squirrel instances based on rows in the database
  - The return value ought to be a list of Squirrel instances
  - Only returns Squirrel instances which are rabid
- `Squirrel delete()`
  - Deletes the Squirrel from the database
  - This method returns `None`

### Aggregate and Association Methods

#### Squirrel

- `Squirrel classmethod query_most_acorns()`
  - Returns the Squirrel in the database with the most acorns
  - Returns the Squirrel as an instance
