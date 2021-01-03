import json
leaders_objects = ""
class leaders:
    def __init__(self,name,age,country,continent):
        self.age = age
        self.name = name
        self.country = country
        self.continent = continent
def read():
    f = open("Book1.csv","r")
    leaders_list = []
    line = f.readline()
    while line != "":
        details = line.split(",")
        leader = leaders(details[0],details[1],details[2],details[3].strip('\n'))
        leaders_list.append(leader)
        line = f.readline()
    return leaders_list
def input1(leaders_list):
    continent = input("enter the leader's name:")
    for i in range(len(leaders_list)):
        if continent == leaders_list[i].continent:
            print(leaders_list[i].country)
            print(leaders_list[i].name)
def encode_leaders(leader):
    if isinstance(leader,leaders):
        data = {"name":leader.name,
                "country":leader.country,
                "continent":leader.continent,
                "age":leader.age}
        print(type(data))
        return data
    else:
       return f"{type(leader)} is not an leaders object"
def decode_leaders(dct):
  return leaders(dct["name"],dct["age"],dct["country"],dct["age"])
leaders_list= read()
# with open("leaders.json","w") as file:
#    json.dump(leaders_list,file,default=encode_leaders)
with open("leaders.json","r") as file:
 s = file.readline()
 s = json.loads(s,object_hook=decode_leaders)
 for ss in s:
     print(ss.name,":")
     print("   age: ",ss.age)
     print("   country: ",ss.country)
     print("   continent:",ss.continent)