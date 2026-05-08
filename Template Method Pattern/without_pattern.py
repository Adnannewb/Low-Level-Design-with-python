class CSVParser:
    def parse(self):
        self.openfile()
        
        #specific parse logic for CSV
        print("Parsing the CSV file ")
        
        self.closefile()
   
    def openfile(self):
        print("Opening a File")
   
    def closefile(self):
        print("Closing a File")
class JSONParser:
    def parse(self):
        self.openfile()
        
        #specific parse logic for JSON
        print("Parsing the JSON file ")
        
        self.closefile()
   
    def openfile(self):
        print("Opening a File")
   
    def closefile(self):
        print("Closing a File")

csv=CSVParser()
csv.parse()

json=JSONParser()
json.parse()

#in that code we have to write same open and close file function manytimes while all are the same 
#Repeated code and hard to maintain

