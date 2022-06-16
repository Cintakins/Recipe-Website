![Delicious Recipes Logo](/static/images/favicon.png)

![Delicious Recipes app images](/static/images/responsive-design.png)

#Delicious Recipes Web Application

Find and discover new recipes on the Delicious Recipes web application! Got recipe ideas you want to share? great! upload them to the app and share with other cooking enthuisiasts!
-----

## UX Design
--
### Goals
--
#### Business Goals
* The web app will attract visitors to view recipes, as a result the app will be the perfect place for businesses to advertise their websites for selling cooking products and tools. They will want exposure for their businesses alongside the recipes displayed.
--
#### Visitor Goals
* Visitors will be looking for recipe ideas.
* They will want a simple display of recipes to easily navigate.
* They will want search functionality.
* returning visitors may enjoy adding their own recipes. 
* Those who wish to add recipes will need their own accounts so they can view their own recipes that they have added.
* Users who add recipes will want to be able to edit and delete their recipes.
---

### strategy 
The project is designed to attract users to the web application by providing a service to display recipes and add their own custom recipes. This will attract the type of user who is passionate about cooking and will therefore already be interested in any products the website might offer. Cooking equipment websites can advertise their wares to the user giving them appropriate and optimal exposure. The main focus of the website is for displaying the recipes and for users to share their expertise. For those interested in using these recipes, cooking product websites will be displayed for them to click on.

### Scope 
Users will certainly want a list of recipes they can choose from. If that list gets exhausting they will need the ability to search through them to find what they want. They need to be able to get a quick idea via visuals and a short description of each recipe so that it is easy for them to navigate through the recipes shown to them. Therefore the recipes have a descrription, an image, a name, a list of ingredients and instructions. A nice feature for those uploading their recipes is for them to be creditted at the bottom of their recipes. There is easy navigation between pages. 
Pages needed are; 
* A recipe page for all recipes 
* A profile page with the user's own recipes
* A login/register page
* A home page to introduce the use to the use of the web app
* A page to upload recipes.
The web app needs to be responsive on all screen sizes and easy to navigate.
Those are the main requirements of the project, however if there is time, extra features would be nice such as adding a like button to like recipes and a display of the most popular recipes on the home page. The home page will also have a random generated recipe suggestion for all recipes to have the opportunity to be in the limelight and for users to try new recipes. It could be nice to add functionality to create dublicate forms for adding a recipe in the same way you can add ingredient text areas so that users could add multiple recipes in one go.

### Structure 
The navbar has the links most public friendly from the left to the most exclusive on the right. The profile link is only visible to the logged in user and the add recipe link redirects the user to the log in page. The home page gives a daily random recipe suggestion to everyone visiting the page from all recipe options in the database. This is to encourage visitors to try a recipe uploaded by any user. This helps the visitor know straight away what the web app is used for. To the right of the navbar are links from 'all recipes', to 'add recipe' and 'login / register', with 'profile' and 'log out' only being viewable on the right to logged in users. The navbar also has a dropdown menu for smaller screens.

### Skeleton 
[Home Page Wireframe](/static/images/wireframe1.png)
[All Recipes Wireframe](/static/images/wireframe2.png)
[Add Recipe Wireframe](/static/images/wireframe3.png)
[Log In Recipe WireFrame](/static/images/wireframe4.png)
[Register Wireframe](/static/images/wireframe5.png)
[Profile WireFrame](/static/images/wireframe6.png)

### Surface 
I chose to use the materialize library as I really like the simplicity and look of the design. I also felt that keeping the design simple would help give me more time to concentrate on the functionality of the web app.
I also used Font Awesome for Icons as some icons that I wanted were not available with materialize icons.

## Technologies Tools and Libraries used:

#### MongoDB
I used MongoDB to store the data used for the app

#### Heroku
Heroku was used for deployment

#### GitHub
To store the project code and for version control

#### PIP
To install tools

#### JQuery
For materialize components

#### Materialize
For the styling

#### Font Awesome
For Icons used in categories

#### Jinja
For displaying the html templates 

#### Flask
To create and render templates

#### Flask PyMongo
For communicating with mongodb, using CRUD functionality

#### Am I responsive website
Used for displaying the responsivity of the app.


## Testing and Problems:

* javascript initializing problems. Used general init function at first, then decided to use JQuery as it looked more simple to understand how to use it. I wanted to use it to have control over the chips component of materialize. I had problems trying to use chips for adding ingredients but eventually i scrapped that idea.

* I wanted to use route in app.py to redirect potential user to login page when they click "add recipe" if they are not logged in. I decided to use a message in the title of the "login_t0_add.html" page instead of using flash. It seemed like the more simple solution.

* The add step and add ingredient buttons created too many steps when loading the edit page, so there were more steps than the existing values given. I created seperate functions for the different pages add.html and edit.html hoping that the window.onload method won't effect the edit.html page, but there were still problems. I decided to scrap the cope of the functions for the edit page and instead I placed the "window.onload = addSted(), addIngredient()" line of code directly into the "add.html" page so that it wouldn't effect the "edit.html" page However there were still issues with the edit page adding an extra empty textarea because the "for" statement to add the existing data needed to skip index 0. However I ran out of time to correct this. The original hidden clone is contributing toward the data array and then being displayed as a blank textarea in the edit.html as index 0.

* The font awesome icons did not work in the select box. I think this is due to it being the free version. However sometimes it works and I never found out why.

* The brand-logo title overlapped the content on smaller screens. Instead of targetting the class, I created an ID for the logo and targetted it with CSS to minimize it for smaller screens.

* Heroku app kept crashing. At first i thought it was something to do with the favicon because an error kept appearing with that code in the heroku log, but then after googling other errors "bash: app.py: comand not found", I compared my procfile to the task manager files and realised "python" was missing from the command. The app now works and there is a warning "This is not a development server. Do not use it in a production deployment". However I have ran out of time to investigate further

* On tidying up my html the materialize icons stopped working and i don't know why, but I have also run out of time to fix that.

![CSS Validation](/static/images/CSSValidation.png)
![Lighthouse text](/static/images/LighthouseValidation.png)
![HTML Validation](/static/images/HTMLValidation.png)

## Deployment:

* Create a procfile with "python app.py" for Heroku to know which file runs the app.
* Put files and dependencies into a file names requirements.txt
* Log onto heroku and create a new app.
* Connect Heroku to Github repository.
* Enable automatic deployment.
* Reveal config vars in setting tab on heroku.
* Add values: 
- IP: 0.0.0.0
- MONGO_DBNAME: recipes
- MONGO_URI:
- PORT: 5000
SECRET_KEY: 
* In git terminal use "git add." "git commit -m" "git push"
* Deploy on heroku 
* Back in git terminal, use "git push heroku main"


## Credits
many of the recipes added were added from https://www.bbc.co.uk/food/recipes
Many thanks to the Code Institute tutors for their help.
I found it helpful looking over the task manager mini project to help me with my code as well as W3Schools.
