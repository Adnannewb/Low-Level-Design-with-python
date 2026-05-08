from abc import ABC,abstractmethod

class DataParser(ABC):
    @abstractmethod
    def _dataparser(self):
        pass
    
    def _openfile(self):
        print("Opening a File")
   
    def _closefile(self):
        print("Closing a File")
    def parse(self):
        self._openfile()
        
        #specific parse logic for CSV
        self._dataparser()
        
        self._closefile()
   
class CSVParser(DataParser):
    def _dataparser(self):
        print("Parsing CSV File")

class JSONParser(DataParser):
    def _dataparser(self):
        print("Parsing JSON File")

csv=CSVParser()
csv.parse()
print("---------")
json=JSONParser()
json.parse()
   