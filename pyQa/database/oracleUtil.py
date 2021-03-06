'''
# -*- coding:utf-8 -*-
import os
import cx_Oracle
import pdb


class OracleUtil(object):
    def __init__(self, host, port, db, user, password):
        self .host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        #db1=cx_Oracle.connect('testslprod','testslsg20','10.18.19.32:1521/testdb2')
        
     #链接数据库   
    def connect(self):
        database_str = "%s:%s/%s"%(self .host, self.port, self.db)
        self.oracle_instance  = cx_Oracle.connect(self.user,  self.password,  database_str)
       
     #执行oracel语句       
    def query(self,  sql):
        cursor = self.oracle_instance .cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    #执行非查询语句　 
    def do_no_query_action(self, sql):
        cursor = self.oracle_instance.cursor()
        cursor.execute(sql)
        self.oracle_instance.commit()
'''