from excepciones import ClienteError

class Cliente:

    def init_(self, nombre, email):
        self._nombre=nombre
        self._email=email
        self.validar()
        
    def validar(self):
        if not self._nombre or self._nombre.strip() =="":
            raise ClienteError("el nombre no puede estar vacio")
        if"@" not in self._email:
            raise ClienteError("El email no es valido")
        
    def mostrar_info(self):
        
        return f"Cliente:{self._nombre} - {self._email}"  


    


    
