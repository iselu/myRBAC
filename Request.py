# -*- conding:utf-8
import os
import sys
import sqlite3 as sqlite
database = "rbac.db"
conn = sqlite.connect(database)

class Request(object):
    def __init__(self):
        self.conn = conn
    def hasCircle(self):
        return False
        # TODO:implement
    def getParents(self,child):
        parents = self.conn.execute("select parent FROM RH WHERE child = ?",(child,)).fetchall()
        return parents
    def getChildren(self, parent):
        children = self.conn.execute("select child FROM RH WHERE parent = ?",(parent,)).fetchall()
        return children
    def updateRH(self,parent,child):
        pass

    def insertRH(self,parent,child):
        self.conn.execute("insert into RH VALUES (?,?)",(parent, child))
        self.conn.commit()

    def addUser(self,userid,name):
        self.conn.execute("insert into user VALUES (?,?)",(userid, name))
        self.conn.commit()

    def addCharactor(self,c_id,name):
        self.conn.execute("insert into charactor VALUES (?,?)",(c_id, name))
        self.conn.commit()
    def addPrivilege(self,c_id,name):
        self.conn.execute("insert into privilege VALUES (?,?)",(c_id, name))
        self.conn.commit()
class Test(object):
    def __init__(self):
        pass
