import psycopg2

class Connect:
    conn = None
    _database = 'aulap'
    _host = 'localhost'
    _user = 'postgres'
    _password = 'coti'

    def open(self):
        try:
            self.conn = psycopg2.connect(
                host = self._host,
                user = self._user,
                password = self._password,
                dbname = self._database
            )
        except Exception as e:
            raise Exception('OpenError, Erro ao abrir conexão: ' + str(e.args))
        pass

    def close(self):
        try:
            if self.conn is not None:
                self.conn.close()
            else:
                raise Exception('CloseError, Conexão não foi aberta!')
        except Exception as e:
            raise Exception('CloseError, erro ao fechar conexão: ' + str(e.args))
        pass
    pass