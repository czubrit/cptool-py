#!/usr/bin/env python3
'''
' Script para leer la base de datos de KPIs
'
' Created by Cesar Zuniga
'''

import sqlite3

#CSCF
def sql_create_cscf_bsu(tb_name, region):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVCSCF01_CSBSU_%";'
  return sqli

def sql_create_cscf_vdu(tb_name, region):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVCSCF01_CSCDB_VDU%";'
  return sqli

def sql_create_cscf_dpu(tb_name, region):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVCSCF01_CSDPU_%";'
  return sqli

def sql_create_cscf_scu(tb_name, region):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVCSCF01_CSSCUE_%";'
  return sqli

#ATS
def sql_create_ats_bsg(tb_name, region):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVATS01_ATBSG_%";'
  return sqli

def sql_create_ats_vdu(tb_name, region):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVATS01_ATCDB_VDU%";'
  return sqli

def sql_create_ats_dpu(tb_name, region):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVATS01_ATDPU_%";'
  return sqli

def sql_create_ats_vcu(tb_name, region):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVATS01_ATVCU_%";'
  return sqli

#SPG
def sql_create_spg_spg(tb_name, region):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVSPG01_SPSPG_%";'
  return sqli

#SBC
def sql_create_sbc_cmu(tb_name, region, number):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVSBC0' + number + '_CMU_VDU%";'
  return sqli

def sql_create_sbc_hru(tb_name, region, number):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVSBC0' + number + '_HRU%";'
  return sqli

def sql_create_sbc_lbu(tb_name, region, number):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVSBC0' + number + '_LBU%";'
  return sqli

def sql_create_sbc_msu(tb_name, region, number):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVSBC0' + number + '_MSU_%";'
  return sqli

def sql_create_sbc_scu(tb_name, region, number):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVSBC0' + number + '_SCU%";'
  return sqli

def sql_create_sbc_vpu(tb_name, region, number):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVSBC0' + number + '_VPU%";'
  return sqli


#ENS
def sql_create_ens_ensisu(tb_name, region):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVENSBE01_ENSISU_VDU%";'
  return sqli

def sql_create_ens_enspgw(tb_name, region):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVENSBE01_ENSPGW_%";'
  return sqli

def sql_create_ens_enspid(tb_name, region):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVENSBE01_ENSPID3_VDU%";'
  return sqli

def sql_create_ens_ensrsuf(tb_name, region):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVENSBE01_ENSRSUF_VDU%";'
  return sqli

def sql_create_ens_ensrsu(tb_name, region):
  sqli = 'SELECT avg(cpu), avg(memory), avg(storage) '\
    'FROM ' + tb_name + ' WHERE vm_name LIKE "' + region + 'RHWNFVENSBE01_ENSRSU_VDU%";'
  return sqli



def main():
  try:
    connection = sqlite3.connect("cscf-kpis.db")
    cursor = connection.cursor()
    print("Database created and Successfully Connected to SQLite")
    #Regiones para VM CSCF
    print ("Virtual Machines of the CSCF.")
    print ("#BSU")
    regions = ["R5FRE", "R5TLA", "R7CTP", "R7FTE", "R8CAS", "R8YAX"]
    for region in regions:
      sqli = sql_create_cscf_bsu("kpi_virtual_machine", region)
      cursor.execute(sqli)
      record = cursor.fetchall()
      print (record)
    
    print("#VDU")
    for region in regions:
      sqli = sql_create_cscf_vdu("kpi_virtual_machine", region)
      cursor.execute(sqli)
      record = cursor.fetchall()
      print (record)
    
    print("#DPU")
    for region in regions:
      sqli = sql_create_cscf_dpu("kpi_virtual_machine", region)
      cursor.execute(sqli)
      record = cursor.fetchall()
      print (record)

    print ("#SCU")
    for region in regions:
      sqli = sql_create_cscf_scu("kpi_virtual_machine", region)
      cursor.execute(sqli)
      record = cursor.fetchall()
      print (record)

    #Regiones para VM ATS
    print ("Virtual machines of the ATS.")
    print ("#BSG")
    for region in regions:
      sqli = sql_create_ats_bsg("kpi_virtual_machine", region)
      cursor.execute(sqli)
      record = cursor.fetchall()
      print (record)

    print ("#VDU")
    for region in regions:
      sqli = sql_create_ats_vdu("kpi_virtual_machine", region)
      cursor.execute (sqli)
      record = cursor.fetchall ()
      print (record)

    print ("#DPU") 
    for region in regions:
      sqli = sql_create_ats_dpu("kpi_virtual_machine", region)
      cursor.execute (sqli)
      record = cursor.fetchall ()
      print (record)
    
    print ("#VCU") 
    for region in regions:
      sqli = sql_create_ats_vcu("kpi_virtual_machine", region)
      cursor.execute (sqli)
      record = cursor.fetchall ()
      print (record)
    
    #Regiones para VM SPG
    print ("Virtual machines of the SPG.")
    print ("#SPG") 
    for region in regions:
      sqli = sql_create_spg_spg("kpi_virtual_machine", region)
      cursor.execute (sqli)
      record = cursor.fetchall ()
      print (record)

    #Regiones para VM SBC
    print ("Virtual machines of the SBC.")
    print ("#CMU")
    for region in regions:
      sqli = sql_create_sbc_cmu("kpi_virtual_machine", region, '1')
      sqli2 = sql_create_sbc_cmu("kpi_virtual_machine", region, '2')
      cursor.execute (sqli)
      record = cursor.fetchall ()
      print (record)
      cursor.execute (sqli2)
      record2 = cursor.fetchall ()
      print (record2)
    
    print ("#HRU")
    for region in regions:
      sqli = sql_create_sbc_hru("kpi_virtual_machine", region, '1')
      sqli2 = sql_create_sbc_hru("kpi_virtual_machine", region, '2')
      cursor.execute (sqli)
      record = cursor.fetchall ()
      print (record)
      cursor.execute (sqli2)
      record2 = cursor.fetchall ()
      print (record2)

    print ("#LBU")
    for region in regions:
      sqli = sql_create_sbc_lbu("kpi_virtual_machine", region, '1')
      sqli2 = sql_create_sbc_lbu("kpi_virtual_machine", region, '2')
      cursor.execute (sqli)
      record = cursor.fetchall ()
      print (record)
      cursor.execute (sqli2)
      record2 = cursor.fetchall ()
      print (record2)
      
    print ("#MSU")
    for region in regions:
      sqli = sql_create_sbc_msu("kpi_virtual_machine", region, '1')
      sqli2 = sql_create_sbc_msu("kpi_virtual_machine", region, '2')
      cursor.execute (sqli)
      record = cursor.fetchall ()
      print (record)
      cursor.execute (sqli2)
      record2 = cursor.fetchall ()
      print (record2)
      
    print ("#SCU")
    for region in regions:
      sqli = sql_create_sbc_msu("kpi_virtual_machine", region, '1')
      sqli2 = sql_create_sbc_msu("kpi_virtual_machine", region, '2')
      cursor.execute (sqli)
      record = cursor.fetchall ()
      print (record)
      cursor.execute (sqli2)
      record2 = cursor.fetchall ()
      print (record2)

    print ("#VPU")
    for region in regions:
      sqli = sql_create_sbc_msu("kpi_virtual_machine", region, '1')
      sqli2 = sql_create_sbc_msu("kpi_virtual_machine", region, '2')
      cursor.execute (sqli)
      record = cursor.fetchall ()
      print (record)
      cursor.execute (sqli2)
      record2 = cursor.fetchall ()
      print (record2)
    
    #Regiones para VM ENS
    print ("Virtual machines of the ENS.")
    print ("#ENSISU") 
    for region in regions:
      sqli = sql_create_ens_ensisu("kpi_virtual_machine", region)
      cursor.execute (sqli)
      record = cursor.fetchall ()
      print (record)

    print ("#ENSPGW") 
    for region in regions:
      sqli = sql_create_ens_enspgw("kpi_virtual_machine", region)
      cursor.execute (sqli)
      record = cursor.fetchall ()
      print (record)

    print ("#ENSPID3") 
    for region in regions:
      sqli = sql_create_ens_enspid("kpi_virtual_machine", region)
      cursor.execute (sqli)
      record = cursor.fetchall ()
      print (record)

    print ("#ENSRSUF") 
    for region in regions:
      sqli = sql_create_ens_ensrsuf("kpi_virtual_machine", region)
      cursor.execute (sqli)
      record = cursor.fetchall ()
      print (record)

    print ("#ENSRSU") 
    for region in regions:
      sqli = sql_create_ens_ensrsu("kpi_virtual_machine", region)
      cursor.execute (sqli)
      record = cursor.fetchall ()
      print (record)
  
  except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
  
  finally:
    if connection:
      connection.close()
      print("The SQLite connection is closed")
  

if __name__ == "__main__":
  main()