import psycopg2
import os, sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class Connect:


    def connection_database(self):
        conn = psycopg2.connect("user='postgres' password='postgres' host = '127.0.0.1' port= '5432' ")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        return cur

    def delete_database(self):
        try:
            cur = self.connection_database()
            #DROP DATABASE python
            drop_database = "drop database if exists python"
            cur.execute(drop_database)
            cur.close()
            print("Deleted Successfully!")
        except Exception as e:
            print (e)
            print ("Cannot Delete Database")

    def create_database(self):
        try:
            cur = self.connection_database()
            dbname = "python"
            cur.execute('CREATE DATABASE ' + dbname)
            cur.close()
            self.restore_database()
        except Exception as e:
            print (e)
            print ("Cannot Create Database!")
            try:
                self.delete_database()
                try:
                    self.create_database()
                except Exception as e:
                    print ("Cannot Create Database after removed alrey exists")

            except Exception as e:
                print ("Cannot Delete Database in def create_database")


    def restore_database(self):
        try:
            cur = self.connection_database()
            command = "/usr/bin/pg_restore -h 'localhost' -p '5432' -U 'postgres' -d 'python' -v '/home/bianca/unittest_serramar.backup'"
            os.system(command)
            cur.close()
        except Exception as e:
            print (e)
            print ("Cannot Restore Database!")

if __name__ == '__main__':

    database_conn = Connect()
    database_conn.create_database()
    #database_conn.delete_database()
