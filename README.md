# AnsiRODS
## Basic Info
My ansible-irods playbooks and such. I would suggest having some basic Ansible understanding before diving in.

I use a single playbook (playbook.yml) and a hosts file (hosts). My account "ansible" runs from the server where I installed ansible, with SSH keys set up on all remote machines to allow SSH access without password. The account is added to /etc/sudoers, requiring a password be entered to use sudo. So, from my Ansible Sever, I can ssh into my new machines as "ansible", but need to enter the password to SUDO.

It is important that if you are using the password, it be the same on all machines if it is a local account. 

The "hosts" file is our source of information. The variables in place there are used to fill in required fields for the scripts. I also make heavy use of the Python Expect module to handle prompted scripts such as setup_irods.sh.

I use this for test server creation and dumping. Possibly useful for training environments.
If you want to use this operationally, I would review the SQL Database section in the ICAT setup. It is not exactly "secure"

## A quick breakdown of the setup
This is for iRODS 4.1.10 and CentOS 7.3
It uses iptables, not firewall-cmd.

- playbook.yml contains the roles structure
- the hosts file contains variables used to set things up
- common - applied to all. It is basic updates and updates
- icat - the icat server setup tasks
- resc - the resource server setup tasks

This command will run the playbook with our provided hosts file, and then it will ask us to enter the SUDO password of our account on the remote machines. NOTE: This should be run from the .../dir/ directory so that the hosts file is local. Otherwise you need to specify absolute paths for the playbook.yml and the hosts file.
```
ansible-playbook playbook.yml -i hosts -K 
```



### Fine print and legal stuff
Copyright SURFsara BV  
Matthew Saum  
Use at your own risk  
Apache 2.0 License
