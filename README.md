# ITEM CATALOG PROJECT
Is the second project of the Udacity [Full Stack Web Developer Nanodegree](https://mena.udacity.com/course/full-stack-web-developer-nanodegree--nd004)


### Porpuse of this project:
"Develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items."



## Instructions: 

##### 1) Install vagrant and virtualBox.
[Download vagrant](https://www.vagrantup.com/downloads.html)
[Download virtualBox](https://www.virtualbox.org/wiki/Downloads)


##### -Then write in the command
vagrant up 
vagrant ssh

** and make sure you'r in the right path **
cd /vagrant 
cd /itemCatalog

##### Database setup and fill 
```py
python database_setup.py
python seeder.py
```
##### Run python file

```py
python app.py 
```
##### access the application locally by visiting
 http://localhost:8000 



### References
https://github.com/udacity/Full-Stack-Foundations
https://github.com/SDey96/Udacity-Item-Catalog-Project


