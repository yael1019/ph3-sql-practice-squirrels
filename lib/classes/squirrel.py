from lib import CONN, CURSOR

class Squirrel:

    def __init__(self, name, num_acorns, rabid, id = None):
        pass

    def __repr__(self):
        return f"<Squirrel id={self.id} name={self.name} num_acorns={self.num_acorns} rabid={self.rabid}>"

    # build your name property here

    def save(self):
        pass

    @classmethod
    def query_all(cls):
        pass

    @classmethod
    def query_rabid(cls):
        pass

    @classmethod
    def query_most_acorns(cls):
        pass
