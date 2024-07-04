from app.database import get_db

class Turno:
    def __init__(self, id_turno=None, nombre=None, apellido=None, telefono=None, email=None, dia=None):
        self.id_turno = id_turno
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.dia = dia

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_turno:
            cursor.execute("""
                UPDATE "Turnos" SET nombre = %s, apellido = %s, telefono = %s, email = %s, dia = %s
                WHERE id_turno = %s
            """, (self.nombre, self.apellido, self.telefono, self.email, self.dia, self.id_turno))
        else:
            cursor.execute("""
                INSERT INTO "Turnos" (nombre, apellido, telefono, email, dia) VALUES (%s, %s, %s, %s, %s)
            """, (self.nombre, self.apellido, self.telefono, self.email, self.dia))
            self.id_turno = cursor.lastrowid
        db.commit()
        cursor.close()

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM "Turnos"')
        rows = cursor.fetchall()
        Turnos = []
        for row in rows:
            Turnos.append(Turno(id_turno=row[0], nombre=row[1], apellido=row[2], telefono=row[3], email=row[4], dia=row[5]))

        #movies = [Movie(id_movie=row[0], title=row[1], director=row[2], release_date=row[3], banner=row[4]) for row in rows]
        cursor.close()
        return Turnos

    @staticmethod
    def get_by_id(id_turno):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM "Turnos" WHERE id_turno = %s', (id_turno,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Turno(id_turno=row[0], nombre=row[1], apellido=row[2], telefono=row[3], email=row[4], dia=row[5])
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM "Turnos" WHERE id_turno = %s', (self.id_turno,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id_turno': self.id_turno,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono,
            'email': self.email,
            'dia': self.dia
        }