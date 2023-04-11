from lib import CONN, CURSOR

class Squirrel:

    def __init__(self, name, num_acorns, rabid, id = None):
        self._name = name
        self.num_acorns = num_acorns
        self.rabid = rabid
        self.id = id

    def __repr__(self):
        return f"<Squirrel {self.name} {self.num_acorns} {self.rabid}>"

    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) == str and len(name) >= 1 and len(name) <= 20:
            self._name = name
        else:
            print(f"Cannot use {name} as a name")

    name = property(get_name, set_name)

    def save(self):
        if self.id:
            self.update()
        else:
            self.create()

    def create(self):
        sql = "INSERT INTO squirrels (name, num_acorns, rabid) VALUES (?,?,?)"
        CURSOR.execute(sql, [self.name, self.num_acorns, self.rabid])
        CONN.commit()
        self.id = CURSOR.execute("SELECT * FROM squirrels ORDER BY id DESC LIMIT 1").fetchone()[0]

    def update(self):
        sql = "UPDATE squirrels SET name = ?, num_acorns = ?, rabid = ? WHERE id = ?"
        CURSOR.execute(sql, [self.name, self.num_acorns, self.rabid, self.id])
        CONN.commit()

    @classmethod
    def query_all(cls):
        sql = "SELECT * FROM squirrels"
        squirrel_data = CURSOR.execute(sql).fetchall()
        squirrel_list = []
        for squirrel in squirrel_data:
            new_squirrel = Squirrel(squirrel[1], squirrel[2], squirrel[3], squirrel[0])
            squirrel_list.append(new_squirrel)
        return squirrel_list

    @classmethod
    def query_rabid(cls):
        sql = "SELECT * FROM squirrels WHERE rabid = True"
        squirrel_data = CURSOR.execute(sql).fetchall()
        squirrel_list = []
        for squirrel in squirrel_data:
            new_squirrel = Squirrel(squirrel[1], squirrel[2], squirrel[3], id=squirrel[0])
            squirrel_list.append(new_squirrel)
        return squirrel_list

    @classmethod
    def query_most_acorns(cls):
        sql = "SELECT * FROM squirrels ORDER BY num_acorns DESC LIMIT 1"
        squirrel = CURSOR.execute(sql).fetchone()
        return Squirrel(squirrel[1], squirrel[2], squirrel[3], id=squirrel[0])
