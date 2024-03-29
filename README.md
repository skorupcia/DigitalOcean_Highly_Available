# DigitalOcean Highly Available Infrastructure Centos-7 

[![CI](https://github.com/skorupcia/DigitalOcean_Highly_Available/actions/workflows/ci.yml/badge.svg)](https://github.com/skorupcia/DigitalOcean_Highly_Available/actions/workflows/ci.yml)

## Specifications

macOS: Sonoma 14.2.1

Centos: centos-7-x64

Compared to Geerlingguy files i have decided to create a script that writes ip's and assign them to groups. Unfortunately it leads to additional commands to execute. (Since I wasn't able to get hosts to inventory groups)

## INSTRUCTIONS

1. Add your machine SSH to DigitalOcean account

2. Create API token and add to your DigitalOcean project

3. Update vars files to your personal preferences

   a) Update u_token in keys.yml (api_token)
   
   b) Update u_ssh in keys.yml (ssh fingerprint)

   c) Update 'api_token' in the end of the generate_hosts.py script

   d) Update file location of 'generate_hosts.py' in provisioners/digitalocean.yml

## RUN INSTRUCTIONS

1. Run required roles:

      ansible-galaxy install -r requirements.yml
   
2. Run digitalocean.yml to create droplets and run generate_hosts.py:

      ansible-playbook provisioners/digitalocean.yml

      #### When vault password applied:

      ansible-playbook provisioners/digitalocean.yml --ask-vault-pass

4. Run playbooks with provision.yml file:

      ansible-playbook -i hosts.ini provision.yml

5. Check if infrastructure is working simply connecting to varnish ip server:

      http://your_varnish_ip

6. For additional safety of your ssh and api key run:

      ansible-vault encrypt provisioners/keys.yml 


## Droplet Delete

   If you would like to delete droplets, simply switch state of "Provision Digitalocean droplets" from PRESENT to ABSENT and run playbook.

## TroubleShooting

1. MacOS - INSTALL CERTIFICATES if your Geerlingguy roles end up with certificate error:
   
    Unknown error when attempting to call Galaxy at 'https://galaxy.ansible.com/api/': <urlopen error [SSL:CERTIFICATE_VERIFY_FAILED]

## Links 

   https://github.com/geerlingguy/ansible-for-devops/tree/master/lamp-infrastructure

   2nd edition of Ansible for DevOps Jeff Geerling
