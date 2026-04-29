from abc import ABC, abstractmethod


class FileAccess(ABC):
    @abstractmethod
    def read(self):
        pass


class RealFile(FileAccess):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        return f"Reading content of {self.filename}"


class ProxyFile(FileAccess):
    def __init__(self, filename, user_role):
        self.filename = filename
        self.user_role = user_role
        self._real_file = None

    def read(self):
        if self.user_role != "admin":
            return "Access Denied!"
        
        if self._real_file is None:
            self._real_file = RealFile(self.filename)
        
        return self._real_file.read()



file1 = ProxyFile("data.txt", "user")
print(file1.read())  

file2 = ProxyFile("data.txt", "admin")
print(file2.read()) 