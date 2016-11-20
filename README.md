# sqlexample
Coding Challenge from Hack U 16NOV2016

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
   
3. SSH into the machine

   ```
   $ vagrant ssh
   ```

4. Change to the project directory

   ```
   $ cd ~/Projects/hacku/sqlexample 
   ```

5. Activate the virtual environment

   ```
   $ source activate hacku-env 
   ```

6. Run the Django server

   ```
   python manage.py runserver 0.0.0.0:8000
   ```

7. From your host OS run Postman

8. Choose GET, enter `localhost:8000/school` into the URL bar, and press Send.

9. Choose GET, enter `localhost:8000/performance` into the URL bar, and press Send.
