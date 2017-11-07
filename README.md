# AnsiRODS
My ansible-irods playbooks and such. I would suggest having some basic Ansible understanding before diving in.

I use a single playbook (playbook.yml) and a hosts file (hosts). My account "ansible" runs from the server where I installed ansible, with SSH keys set up on all remote machines to allow SSH access without password. The account is added to /etc/sudoers, requiring a password be entered to use sudo.

I use this for test server creation and dumping. Possibly useful for training environments.
If you want to use this operationally, I would review the SQL Database section in the ICAT setup. It is not exactly "secure"

# A quick breakdown of the setup
This is for iRODS 4.1.10 and CentOS 7.3
It uses iptables, not firewall-cmd.

playbook.yml contains the roles structure
the hosts file contains variables used to set things up
common - applied to all. It is basic updates and updates
icat - the icat server setup tasks
resc - the resource server setup tasks





Copyright SURFsara BV
Matthew Saum
Use at your own risk
