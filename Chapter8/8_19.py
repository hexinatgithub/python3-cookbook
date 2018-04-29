class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self._state = newstate

    def read(self):
        # Delegate to the state class
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)


# Connection state base class
class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()


# Implementation of different states
class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')


class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')

    @staticmethod
    def write(conn, data):
        print('writing')

    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)

# change the connection type
# class Connection:
#     def __init__(self):
#         self.new_state(ClosedConnection)

#     def new_state(self, newstate):
#         self.__class__ = newstate

#     def read(self):
#         raise NotImplementedError()

#     def write(self, data):
#         raise NotImplementedError()

#     def open(self):
#         raise NotImplementedError()

#     def close(self):
#         raise NotImplementedError()


# class ClosedConnection(Connection):
#     def read(self):
#         raise RuntimeError('Not open')

#     def write(self, data):
#         raise RuntimeError('Not open')

#     def open(self):
#         self.new_state(OpenConnection)

#     def close(self):
#         raise RuntimeError('Already closed')


# class OpenConnection(Connection):
#     def read(self):
#         print('reading')

#     def write(self, data):
#         print('writing')

#     def open(self):
#         raise RuntimeError('Already open')

#     def close(self):
#         self.new_state(ClosedConnection)
