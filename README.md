# sqlexample
Coding Challenge from Hack U 16NOV2016

## Install the `hacku-vm-nst32` Vagrant Box

1. Install VirtualBox and Vagrant for your OS

   ```
   www.virtualbox.org
   www.vagrantup.com
   ```

2. Install the Vagrant box

   ```$ vagrant init troyscottpdx/hacku-vm-nst; vagrant up --provider virtualbox```

   Note that if the machine will not boot it may be due to the VirtualBox Network Settings. To inspect the vm configuraton run `VirtuaBox`
   
   Sample Vagrantfile:
   
   ```
   # -*- mode: ruby -*-
   # vi: set ft=ruby :
   Vagrant.configure("2") do |config|
      config.vm.box = "ubuntu/xenial64"
      config.vm.network "forwarded_port", guest: 80, host: 8080
      config.vm.network "forwarded_port", guest: 8000, host: 8001
      config.vm.provider "virtualbox" do |vb|
         vb.name = "hacku-vm-nst"
         vb.memory = "4064"
      end
      config.vm.boot_timeout=400
   end
   ```
   
3. SSH into the machine

   ```$ vagrant ssh```

### PostgreSQL, Miniconda, Django, and Django REST Framework 

## PostgreSQL Setup
1. Locate the .pgsql files in the `sqlexample` project directory and run the following commands to populate the `schools_original` and `performance_original` tables. 

   ```
   sudo -u postgres psql < schools_original.pgsql
   sudo -u postgres psql < performance_original.pgsql
   ```
   
