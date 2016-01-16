# -*- conding:utf-8
import json
from Request import Request
request = Request()
class iniTestData(object):
    def __init__(self,dataFile):
        self.jsondata = json.loads(open(dataFile).read())

    def getIdsNames(self,data):
        for d in data:
            yield int(d["id"]),d["name"]
    def iniUserTable(self):
        users = self.getIdsNames(self.jsondata["user"])
        self.addUsers(users)
    def iniCharactor(self):
        chs = self.getIdsNames(self.jsondata["charactor"])
        self.addCharactors(chs)

    def iniPrivileges(self):
        pris = self.getIdsNames(self.jsondata["privilege"])
        self.addPrivileges(pris)
    def getRHs(self,rh):
        for d in self.jsondata[rh]:
            yield int(d["parent"]),d["child"]
    def iniRH(self,rh):
        pairs = self.getRHs(rh)
        for pair in pairs:
            request.insertRH(pair[0],pair[1])

    def addUsers(self,users):
        for user in users:
            self.addUser(user)
    def addUser(self,user):
        userid = user[0]
        name = user[1]
        request.addUser(userid,name)

    def addCharactors(self,charactors):
        for charactor in charactors:
            self.addCharactor(charactor)

    def addCharactor(self,charactor):
        theID = charactor[0]
        name = charactor[1]
        request.addCharactor(theID,name)

    def addPrivileges(self,privileges):
        for privilege in privileges:
            self.addPrivilege(privilege)

    def addPrivilege(self,privilege):
        theID = privilege[0]
        name = privilege[1]
        request.addPrivilege(theID,name)



class Test(object):
    def __init__(self):
        self.testdata = iniTestData(dataFile="testdata.json")
    def testgetIdNames(self):
        users = self.testdata.getIdsNames(self.testdata.jsondata["user"])
        for user in users:
            print user


def main():
    initest = iniTestData(dataFile="testdata.json")
    # initest.iniUserTable()
    # initest.iniCharactor()
    # initest.iniPrivileges()
    initest.iniRH("RH1")
if __name__ == '__main__':
    main()