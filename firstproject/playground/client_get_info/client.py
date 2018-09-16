import time


class Client:
    def __init__(self, ip, port, timeout=None):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.server_name = None
        self.value = None
        self.timestamp = None
        self.servers = []

    def put(self, server_name, value, timestamp=None):
        self.server_name = server_name
        self.value = value
        if timestamp is None:
            self.timestamp = str(int(time.time()))
        else:
            self.timestamp = timestamp

    def get(self, serv_and_val):
        if serv_and_val == 'key_not_exists':
            return {}
        serv_and_val_array = serv_and_val.split('.')

        server = serv_and_val_array[0]
        if server in self.servers:
            return "OK"
        else:
            raise ClientError('ТЫ НЕ ВЫБРАЛ КАКИЕ ДАННЫЕ ПОЛУЧИТЬ')

        #get_val = serv_and_val_array[1]



class ClientError(Exception):
    def __init__(self, message):
        self.message = message