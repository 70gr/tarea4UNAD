class ErrorSistema(Exception):
    pass

class ClienteError(ErrorSistema):
    pass

class ServicioError(ErrorSistema):
    pass

class ReservaError(ErrorSistema):
    pass
