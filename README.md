# sqlexample
Coding Challenge from Hack U 16NOV2016

### PostgreSQL Settings
Database - django
User - vagrant
Password - vagrant

## Install the Custom Vagrant Box

1. Install VirtualBox, Vagrant, Postman for your OS

   ```
   www.virtualbox.org
   www.vagrantup.com
   www.getpostman.com
   ```

2. Install the Vagrant box

   ```$ vagrant init troyscottpdx/hacku-vm-nst32; vagrant up --provider virtualbox```

   Note that if the machine will not boot it may be due to the VirtualBox Network Settings. To inspect the vm configuraton run `VirtuaBox`
   
   Sample Vagrantfile:
   
   ```
   # -*- mode: ruby -*-
   # vi: set ft=ruby :
   Vagrant.configure("2") do |config|
      config.vm.box = "ubuntu/xenial32"
      config.vm.network "forwarded_port", guest: 80, host: 8080
      config.vm.network "forwarded_port", guest: 8000, host: 8001
      config.vm.provider "virtualbox" do |vb|
         vb.name = "hacku-vm-nst32"
         vb.memory = "4064"
      end
      config.vm.boot_timeout=400
   end
   ```

## SSH Into the Virtual Machine and Launch the Django Server
   
1. SSH into the virtual machine

   ```
   $ vagrant ssh
   ```

2. Change to the project directory

   ```
   $ cd ~/Projects/hacku/sqlexample 
   ```

3. Activate the virtual Python environment

   ```
   $ source activate hacku-env 
   ```

4. Run the Django server

   ```
   python manage.py runserver 0.0.0.0:8000
   ```

## Test the API Interface

1. From your host OS run Postman

2. Choose GET, enter `localhost:8001/school` into the URL bar, and press Send

3. Choose GET, enter `localhost:8001/performance` into the URL bar, and press Send

## Clean Up

1. From the virtual machine press Ctrl+C to terminate the Django Server

2. Deactivate the virtual Python environment

   ```
   $ source deactivate 
   ```

3. Logout of the SSH session

   ```
   $ logout
   ```
   
4. Halt the virtual machine

   ```
   $ vagrant halt
   ```
