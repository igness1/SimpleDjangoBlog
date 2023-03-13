# SimpleDjangoBlog

## Table of contents
* [Setup](#setup)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)

## Setup

#### 1. Install Python
Install ```python-3.9.0``` and ```python-pip```. Follow the steps from the below reference document based on your Operating System.
Reference: [https://docs.python-guide.org/starting/installation/](https://docs.python-guide.org/starting/installation/)

#### 2. Setup virtual environment
```bash
# Install virtual environment
pip install virtualenv

# Make a directory
mkdir envs

# Create virtual environment
virtualenv myenv

# Activate virtual environment
myenv\Scripts\activate
```

#### 3. Clone git repository
```bash
git clone "https://github.com/igness1/SimpleDjangoBlog.git"
```

#### 4. Install requirements
```bash
cd SimpleDjangoBlog/
pip install -r requirements.txt
```

#### 5. Run the server
```bash
python manage.py runserver
```
#### 6. Available users:
admin  
login: admin  
password: password  

Iga  
login: Iga  
password: very_difficult_pass  

## Screenshots
Example screenshots.

Full web page:
![image](https://user-images.githubusercontent.com/58557112/224533314-804372b8-87b7-4076-a9ce-58e530a72dc4.png)

Navbar from bootstrap:
![image](https://user-images.githubusercontent.com/58557112/224533410-3f74a479-ce19-4961-a088-f0ade0721e15.png)

Add new post functionality:
![image](https://user-images.githubusercontent.com/58557112/224533813-eebef8e6-9551-4058-886d-215d20c1d6c9.png)

Post detail view:
![image](https://user-images.githubusercontent.com/58557112/224533867-db52345d-8fae-4330-a042-76f7f940f62e.png)

## Technologies
* Python - 3.9.0
* Django - 4.1.7
* Bootstrap - 4.0.0

## Features
List of features ready and TODOs for future development
* Add post functionality
* Login functionality
* Edit post functionality (only for post owner/author)
* Remove post functionality (only for post owner/author)
* Add comment functionality
* Like button functionality for created users.

To-do list:
* Search button.

## Status
Project is: _in progress_

## Inspiration
My inspiration to create such an app was a willing to learn basics of django framework.
