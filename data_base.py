from pony.orm import Database, Required, PrimaryKey, Set

db = Database()

db.bind(
    provider="mysql", user="mps", passwd="debora12345678", host="localhost", db="mps_db"
)


class Usuario(db.Entity):
    usuario_id = PrimaryKey(int, auto=True)
    usuario_nome = Required(str)
    usuario_email = Required(str)
    usuario_status = Required(int)
    usuario_senha = Required(str)
    eventos = Set("Evento")
    
    def to_json(self):
        return dict(usuario_id = self.usuario_id,
                    usuario_nome = self.usuario_nome, 
                    usuario_email = self.usuario_email,
                    usuario_status = self.usuario_status,
                    eventos = [evento.to_json() for evento in self.eventos])



class Evento(db.Entity):
    evento_id = PrimaryKey(int, auto=True)
    evento_data_hora = Required(str)
    evento_descricao = Required(str)
    evento_nome = Required(str)
    evento_status = Required(int)
    usuario = Required(Usuario)

    def to_json(self):
        return dict(evento_id = self.evento_id,
                    evento_data_hora = self.evento_data_hora,
                    evento_descricao = self.evento_descricao,
                    evento_nome = self.evento_nome,
                    evento_status = self.evento_status,)

db.generate_mapping(create_tables=True)