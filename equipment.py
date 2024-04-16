#class for armour
import tomli_w

class armour:
    ACSlug = ""
    ACName = ""
    ACType = ""
    ACCost = 0  #cost is always in CP
    ACWeight = 0 #weight is always in lb
    AC = 0
    ACMaxDex = 0

    def __init__(self, ACName, ACType, ACCost, ACWeight, AC, ACMaxDex):
        self.ACName = ACName
        self.ACType = ACType
        self.ACCost = ACCost
        self.ACWeight = ACWeight
        self.AC = AC
        self.ACMaxDex = ACMaxDex
        self.ACSlug = '_'.join(ACName.lower().split())

    def toTOML(self):
        tomlb =  {self.ACSlug:
                  {
                      "ACName": self.ACName,
                      "ACType": self.ACType,
                      "ACCost": self.ACCost,
                      "ACWeight": self.ACWeight,
                      "AC": self.AC,
                      "ACMaxDex": self.ACMaxDex
                  }
        }
        
        return tomli_w.dumps(tomlb)
        
    
    
def WriteToLib(Outfile, Armour:armour):
    Outfile.write(Armour.toTOML())
    Outfile.write("\n")
    #print(f"TOML Dumped string is \n{Armour.toTOML()}")

def main():

    #main loop

    outfile = open("data/items/armour.toml", 'w')
    while True:
        name = input("Enter name of armour:\n>\t")
        atype = input("Enter type of armour:\n>\t")
        cost = int(float(input("Enter cost of armour in GP!:\n>\t")) * 100*100)
        weight = int(input("Enter weight of armour:\n>\t"))
        ac = int(input("Enter the AC of the armour:\n>\t"))
        md = int(input("Enter the max Dex bonus on armour (6 for unlimited):\n>\t"))
        item = armour(name, atype, cost, weight, ac, md)
        WriteToLib(outfile, item)
        outfile.flush()
        print(f"Written {name} to {outfile}!")
        yn = input("Add more? (y/N:\t)").lower()
        if not yn=='y':
            break
    return

if __name__ == "__main__":
    main()