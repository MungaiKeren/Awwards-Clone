# Awwards-Clone
A replica of https://www.awwwards.com/ site. Built using the Django framework

## Author and contact details
* MungaiKeren
Email: wambukeren@gmail.com

# Project Description
A user of the application should be able to:

1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects
5. View projects overall score
6. View my profile page

# SetUp and installation requirements
You need to have the following installed:
* Python3+
* Pip ```curl https://bootstrap.pypa.io/get-pip|python```
* Virtual ```$ python3.6 -m venv pip virtual```
* Activate the virtual environment ```source virtual/bin/activate```
* Django==2.2.6 ```(virtual)$ pip install Django==2.2.6```
* Get all requirements ```pip freeze > requirements.txt```

### Running the server
```python manage.py runserver```

# Behaviour Driven Development

| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Visit awwwards-clone site| Various projects are displayed  | User can review projects |
| Click on image| Image details displayed | Image details displayed |
| Search project | Images for project are displayed | App gets the projects for the searched project |
| Visit profile | Projects posted by user are displayed | App gets projects for user |
| Visit Admin | Prompts for admin credentials | Admin dashboard displayed |
| API projects | api with a list of projects is displayed | api displayed |


## Technologies used
* Django a python frame-work
* Javascript
* Html
* Bootstrap
* Postman for visual representaion while building the api

# Development
It would be so great to have your contributions! Just follow the instructions below.

Fork the repo
* Clone the repo in your machine but ensure you have all the necessary modules.(You can find them in the set up instructions above) git clone https://github.com/MungaiKeren/Me-gallery.git
* Create a new branch git branch contributions
* Edit your changes in your branch
* Run the application
* Push your changes so we can have a view!

# Live development
Currently the app is deployed to heroku. You can find it [here](https://awwords.herokuapp.com/)

## Known Bugs


## Visual Representation
<img src="https://github.com/MungaiKeren/My-Shoe-images/blob/master/awward2.png?raw=true" height = "400px">

### LICENSE
[MIT](https://github.com/MungaiKeren/Awwards-Clone/blob/master/LICENSE)
