from lib import CONN, CURSOR

class Squirrel:

    def __init__(self, name, num_acorns, rabid, id = None):
        self.name = name
        self.num_acorns = num_acorns
        self.rabid = rabid 
        self.id = id

    def __repr__(self):
        return f"<Squirrel id={self.id} name={self.name} num_acorns={self.num_acorns} rabid={self.rabid}>"

    # build your name property here
    def get_name(self):
        if hasattr(self, '_name'):
            return self._name
        else:
            print('An invalid name has been entered')
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            print('Name must be a string between 1 and 15 characters')

    name = property(get_name, set_name)

    def save(self):
        if self.id:
            self._update()
        else:
            self._create_row()

    def _create_row(self):
        sql = """
            INSERT INTO squirrels (name, num_acorns, rabid)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, [self.name, self.num_acorns, self.rabid])
        CONN.commit()
        self.id = CURSOR.execute('SELECT * FROM squirrels ORDER BY id DESC').fetchone()[0]

    def _update(self):
        sql = """
            UPDATE squirrels
            SET name = ?, num_acorns = ?, rabid = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, [self.name, self.num_acorns, self.rabid, self.id])
        CONN.commit()

    @classmethod
    def query_all(cls):
        sql = """
            SELECT * FROM squirrels
        """
        all = CURSOR.execute(sql).fetchall()
        return [Squirrel(data[1], data[2], data[3], data[0]) for data in all]

    @classmethod
    def query_rabid(cls):
        all = Squirrel.query_all()
        return [data for data in all if data.rabid == 1]


    @classmethod
    def query_most_acorns(cls):
        sql = """
            SELECT * FROM squirrels
            ORDER BY num_acorns DESC
        """
        most = CURSOR.execute(sql).fetchone()
        return Squirrel(most[1], most[2], most[3], most[0])
