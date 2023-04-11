from lib import CONN, CURSOR

class Squirrel:

    def __init__(self, name, num_acorns, rabid):
        pass

    # name property goes here

    # num_acorns property goes here

    def introduction(self):
        pass

    def save(self):
        # creates or updates the squirrel in the database
        pass

    def delete():
        # deletes the squirrel from the database
        pass

    @classmethod
    def query_all(cls):
        # gets all squirrels in the database and returns a list of squirrels as instances
        pass

    @classmethod
    def query_one(cls, id):
        # gets an squirrel in the database by its id and returns that squirrel as an instance
        pass

    @classmethod
    def query_rabid(cls):
        # gets all squirrels in the database and returns a list of squirrels who are rabid as instances
        pass

    @classmethod
    def query_most_acorns(cls):
        # returns the squirrel with the most acorns an instance
        pass
