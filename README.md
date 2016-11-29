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

## Provisioning Reference 
Here's the configuration and setup details of the custom virtual machine `hacku-vm-nst32` based on the Vagrant ubuntu/xenial32 box. 

### Install PostgreSQL, Miniconda, Django, and Django REST Framework 

   ```
   apt-get update

   sudo apt-get install tree postgresql postgresql-contrib

   wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86.sh
   bash Miniconda3-latest-Linux-x86.sh

   source ~/.bashrc
   conda update conda
   conda create --name hacku-env python=3
   conda install psycopg2

   mkdir -p ~/Projects/hacku
   cd ~/Projects/hacku
   source activate hacku-env

   pip install django
   pip install djangorestframework

   ```

### Create the PostgreSQL Database and User

   ```
   $ sudo -u postgres psql
   postgres=# CREATE DATABASE django;
   postgres=# CREATE USER vagrant WITH PASSWORD 'vagrant';
   
   ```

Database - django
User - vagrant
Password - vagrant

### Create the schools_original and performance_original tables

   ```
   CREATE TABLE schools_original (
    SchoolID INTEGER NOT NULL, 
    School VARCHAR(60) NOT NULL, 
    District VARCHAR(46) NOT NULL, 
    DistID INTEGER NOT NULL
   );
   ```
   ```
   CREATE TABLE performance_original (
    DistrictID INTEGER NOT NULL, 
    District VARCHAR(32) NOT NULL, 
    SchoolID INTEGER NOT NULL, 
    School VARCHAR(65) NOT NULL, 
    AcademicYear INTEGER NOT NULL, 
    Subject VARCHAR(21) NOT NULL, 
    Subgroup VARCHAR(32) NOT NULL, 
    GradeLevel VARCHAR(3) NOT NULL, 
    ParticipationRate2014to2015 FLOAT, 
    PercentageMeetsORExceeds2014to2015 FLOAT
   );
   ```

### Execute the PostgreSQL Scripts

   ```
   sudo -u postgres psql < schools_original.pgsql
   sudo -u postgres psql < performance_original.pgsql
   ```

### Populate the schapp_school and schapp_performance tables

   ```
   INSERT INTO public.schapp_school (school_id, school, district, district_id)
   SELECT SchoolID, School, District, DistID
   FROM public.schools_original;
   ```
   ```
   INSERT INTO public.schapp_performance
   (district_id, district, school_id, school, academic_year, subject, subgroup, grade_level, participation_rate_2014_to_2015, percentage_meets_or_exceeds_2014_to_2015)
   SELECT districtid, district, schoolid, school, academicyear, subject, subgroup, gradelevel, participationrate2014to2015, percentagemeetsorexceeds2014to2015
   FROM public.performance_original;
   ```
   
