#!/usr/bin/env python3
'''
' Programa para obtener el promedio de los KPIs de CPU, Memoria y Storage
' de las maquinas virtuales del IMS
' 
' IMPORTANTE:
' La recoleccion de los KPIs debe ser de la siguiente forma:
' VIRTUAL MACHINE: MEAN CPU LOAD, MEMORY USAGE, DISK USAGE
'
' Created by Cesar Zuniga (@czubrit)
'
'''

import re, os, sqlite3

def create_database (name):
  connection = sqlite3.connect (name)
  return connection

def create_input():
  files = os.listdir ("./input")
  route_files = []
  for file in files:
    if file.endswith(".csv"):
      route_files.append (os.path.join("./input", file))
  return route_files

def create_table (name):
  sqli = 'CREATE TABLE IF NOT EXISTS ' + name + ' ('\
    'date TEXT,'\
    'network_element TEXT,'\
    'vm_name TEXT,'\
    'cpu REAL,'\
    'memory REAL,'\
    'storage REAL'\
    ');'
  return sqli

def insert_into_table (tb_name, params):
  date, ne, vm_name, cpu, memory, storage = params.split(',')
  #print (date, ne, vm_name, cpu, memory, storage)
  sqli = 'INSERT INTO ' + tb_name + ' (date, network_element, vm_name, cpu, memory, storage) '\
    'VALUES ("%s",%s,%s,%s,%s,%s);' %(date, ne, vm_name, cpu, memory, storage)
  return sqli

def organize_line(kpi_line):
  patterns = ['R[5,7,8][A-Z]+RHWNFVCSCF01_CSBSU_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVCSCF01_CSCDB_VDU[0-9]+_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVCSCF01_CSDPU_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVCSCF01_CSSCUE_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVATS01_ATBSG_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVATS01_ATCDB_VDU[0-9]+_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVATS01_ATDPU_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVATS01_ATVCU_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVSPG01_SPSPG_[A-Z,0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVSBC0[0-9]_CMU_VDU[0-9]+_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVSBC0[0-9]_HRU[0-9]+_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVSBC0[0-9]_LBU[0-9]+_[A-Z,0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVSBC0[0-9]_MSU_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVSBC0[0-9]_SCU[0-9]+_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVSBC0[0-9]_VPU[0-9]+_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVENSBE01_ENSISU_VDU[0-9]+_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVENSBE01_ENSPGW_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVENSBE01_ENSPID3_VDU[0-9]+_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVENSBE01_ENSRSUF_VDU[0-9]+_[0-9]+',\
    'R[5,7,8][A-Z]+RHWNFVENSBE01_ENSRSU_VDU[0-9]+_[0-9]+',\
    ]
  for pattern in patterns:
    if (re.search(pattern, kpi_line)):
      return True
  return False


def main():
  connection = create_database ('cscf-kpis.db')
  cursor = connection.cursor()
  sqli = create_table ("kpi_virtual_machine")
  cursor.execute (sqli)
  connection.commit()

  #Reading input files
  route_files = create_input()
  tuples = 0

  for file in route_files:
    with open(file, 'r') as kpi_data:
      for kpi_line in kpi_data:
        kpi_line = kpi_line.strip()
        if (organize_line(kpi_line)):
          params = kpi_line.split(',')
          data_sample = params[0] + ',' + params[2] + ',' + re.sub('V.*\=','',params[3]) + ',' + params[4] + ',' + params[5] + ',' + params[6]
          sqli = insert_into_table("kpi_virtual_machine", data_sample)
          try:
            cursor.execute(sqli)
            connection.commit()
          except sqlite3.OperationalError as msg:
            print (msg)
            exit()
          print ("Data inserted: " + data_sample)
          tuples += 1
  print ("Inserted tuples: " + str(tuples))
  print ("Developed by czubrit")

if __name__ == "__main__":
  main()