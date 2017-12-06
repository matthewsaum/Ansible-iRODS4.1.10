#Author Matthew Saum
#Copyright 2017 SURFsara BV
#Apache License 2.0
#If you made your way here, you must be desperate. Use at your own risk.

#This is the beginning of my attempt at creating a python script to build
#a hosts file for ansible.
#This is so that my hosts file can be sanitized of passwords afterwards.
#2017 December 6 -- Version 1
#TO DO: Not sure yet. Didn't really think I would make it this far.

import os
import sys


def common():
 ip=raw_input("Please enter your IP address or FQDN: ")
 svr=raw_input("Please enter the server hostname ["+ip+"]: ")
 if (svr == ""):
  svr = ip
 #if
 bucket[i] = { 'IP' : str(ip), 'SVR': str(svr) }
#def common


def irsvr():
 #flag that the server is IRODS
 ir=1
 rsc=raw_input("Is this an iRODS iCAT server? Y/[N]: ") or "N"
 #If it is a Resource server, we need the iCAT server info
 if (rsc == "n" ) or ( rsc == "N" ):
  ics=raw_input("Please enter your iCAT server IP or FQDN: ")
  bucket[i].update({'ICS': ics})
  ir=2
 #if
 acnt=raw_input("Please enter the iRODS Service Account: ")
 zone=raw_input("Please enter your iRODS Zone Name: ")
 iadmn=raw_input("Please enter the iRODS Admin Account Name: ")
 ipwd=raw_input("Please enter the iRODS Admin Account Password: ")
 bucket[i].update({'IRSVR': ir,'ACNT' : acnt, 'ZONE' : zone, 'IADMN': iadmn, 'IPWD':ipwd })
 #if
#def irsvr

def mkhosts():
 #Opens our new hosts file
 f= open("pyHosts", "w")
 #creates the COMMON role
 f.write("[common]\n")
 for x in bucket:
  #IF ALL OTHER ROELS ARE EMPTY. CURRENTLY IRODS IS 0, 1, or 2. WILL HAVE MORE AND STATEMENTS HEAR AS ROLES EXPAND
  if (x['IRSVR'] == 0):
   f.write(x['IP']+" svrName="+x['SVR']+"\n")
  #if
 #for
 #Creates the ICAT role
 f.write("[icat]\n")
 for x in bucket:
  #This creates server entries that are ICAT hosts
  if (x['IRSVR'] == 1):
   f.write(x['IP']+" svrName="+x['SVR']+" svcAcnt="+x['ACNT']+" iZone="+x['ZONE']+" iAdmin="+x['IADMN']+" iPwd="+x['IPWD']+"\n")
  #if
 #for
 #CREATES OUR iRODS Resource role
 f.write("[resc]\n")
 for x in bucket:
  #If the server is an iRODS RESOURCE server
  if (x['IRSVR'] == 2):
   f.write(x['IP']+" svrName="+x['SVR']+" svcAcnt="+x['ACNT']+" rescICAT="+x['ICS']+" iZone="+x['ZONE']+" iAdmin="+x['IADMN']+" iPwd="+x['IPWD']+"\n")
  #if
 #for
 f.close()
#def mkhosts

#Prompts for the playbook name. default is local directory playbook.yml
pbk=raw_input("Please enter the playbook file [./playbook.yml]: ") or "./playbook.yml"

#checks for a pyHosts file
if(os.path.isfile("pyHosts")):
 exst=raw_input("Found an existing ./pyHosts file! This will be deleted if you proceed. Continue? Y/[N]:") or "N"
 if (exst != "Y") and (exst != "y"):
  print "Not over-writing existing ./pyHosts file. Please re-run when file no longer exists, or you are willing to overwrite it."
  sys.exit

#do we need -K on our ansible commands?
k=raw_input("Do you need a password to run SUDO commands? [Y]/N:") or "-K"
if (k != "-K") and (k != "Y") and (k != "y"):
 k=""
 
#Our host couter, increasing per host added and contination prompt
i=0
more="Y"
bucket=[]
while ( more != "N" ) and ( more != "n"):
 #creates our new dictionary entry for hostX, incremental increase in X per loop
 bucket.append( 'host'+str(i))
 #calls the common function
 common()
 #checking for iRODS?
 ir=raw_input("Is this an iRODS server? [Y]/N: ") or "Y"
 bucket[i].update({'IRSVR' : 0}) 
 if (ir == "Y") or (ir == "y"):
  #calls the irods function for input,
  irsvr()
 #if
 more=raw_input("Do you want to add another server? [Y]/N: ") or "Y"
 i=i+1
#while

#Builds our pyHosts file
mkhosts()

#runs the ansible command plus the playbook path
os.system("ansible-playbook -i pyHosts "+pbk+" "+k)

#Sanitization. Update all fields you want sanitized.
for x in bucket:
 x.update({'IPWD': "sanitized"})
 mkhosts()

 
print "\n\npyHosts has been sanitized. Process completed."
