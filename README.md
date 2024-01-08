# DigitalOcean_Highly_Available
DigitalOcean Highly Available Infrastructure with Centos-7 

macOS: Sonoma 14.2.1

Centos: centos-7-x64

-- INSTRUCTIONS --

1. Add your machine SSH to DigitalOcean account

2. Create API token and add to your DigitalOcean project

3. Update vars files to your personal preferences
   
     a) Update u_token in Connection vars (api_token)
   
     b) Update u_ssh in Connection vars (ssh fingerprint)


-- RUN INSTRUCTIONS --

1. Run provision.yml: ansible-playbook provision.yml


-- Droplet Delete --

If you would like to delete droplets, simply switch state of "Probision Digitalocean droplest" from PRESENT to ABSENT and run playbook.

-- TroubleShooting --

1. MACOS - INSTALL CERTIFICATES IF YOUR Geerlingguy roles end up with certificate error:
   
    Unknown error when attempting to call Galaxy at 'https://galaxy.ansible.com/api/': <urlopen error [SSL:CERTIFICATE_VERIFY_FAILED]

-- Links -- 

https://github.com/geerlingguy/ansible-for-devops/tree/master/lamp-infrastructure

2nd edition of Ansible for DevOps Jeff Geerling
