![Delicious Recipes Logo](/static/images/favicon.png)

Find and discover new recipes on the Delicious Recipes web application! Got recipe ideas you want to share? great! upload them to the app and share with other cooking enthuisiasts!

## Gitpod Reminders


To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------


---

Table of content:

strategy - Business objectives. whats worth doing. whats being created. value.
The project is designed to attract users to the web application by providing a service to display recipes and add their own custom recipes. This will attract the type of user who is passionate about cooking and will therefore already be interested in any products the website might offer. Cooking equipment websites can advertise their wares to the user giving them appropriate and optimal exposure. The main focus of the website will be for the recipes and for users to share their expertise, and for those interested in using these recipes, cooking product websites will be displayed for them to click on.

scope = what I included and what i would have liked to have included. specs and requirements.  
users will certainly want a list of recipes they can choose from. If that list gets exhausting they will need the ability to search through them to find what they want. They need to be able to get a quick idea via visuals and a short description of each recipe so that it is easy for them to navigate through the recipes shown to them. Therefore the recipes need a descrription, an image, a name, a list of ingredients and instructions. A nice feature for those uploading their recipes will be for them to be creditted at the bottom of their recipes. There needs to be easy navigation between pages. Pages needed are; a recipe page for all recipes, profile page with the user's own recipes, login/register page, a home page to introduce the use to the use of the web app, and a page to upload recipes. The web app needs to be responsive on all screen sizes and easy to navigate.
 Those are the main requirements of the project, however if there is time, extra features would be nice such as adding a like button to like recipes and a display of the most popular recipes on the home page. The home page will also have a random generated recipe suggestion for all recipes to have the opportunity to be in the limelight and for users to try new recipes. It could be nice to add functionality to create dublicate forms for adding a recipe in the same way you can add ingredient text areas so that users could add multiple recipes in one go.

structure - information design and interaction design
The navbar has the links most public friendly from the left to the most exclusive on the right. The profile link is only visible to the logged in user and the add recipe link redirects the user to the log in page. The home page gives a daily random recipe suggestion to everyone visiting the page from all recipe options in the database. This is to encourage visitors to try a recipe uploaded by any user. This helps the visitor know straight away what the web app is used for. To the right of the navbar are links from 'all recipes', to 'add recipe' and 'login / register', with 'profile' and 'log out' only being viewable on the right to logged in users. The navbar also has a dropdown menu for smaller screens.

skeleton - interface, information and navigation design
[Home Page Wireframe](/static/images/wireframe1.png)
[All Recipes Wireframe](/static/images/wireframe2.png)
[Add Recipe Wireframe](/static/images/wireframe3.png)
[Log In Recipe WireFrame](/static/images/wireframe4.png)
[Register Wireframe](/static/images/wireframe5.png)
[Profile WireFrame](/static/images/wireframe6.png)

surface - visual design
I chose to use the materialize library as I really like the simplicity and look of the design. I also felt that keeping the design simple would help give me more time to concentrate on the functionality of the web app.

Technologies used:

Testing and Problems:

javascript initializing, used generl init function

wanted to use route in app.py to redirect potential user to login page when they click "add recipe" if they are not logged in. 

the add step and add ingredient buttons created too many steps when loading the edit page, so there were more steps than the existing values given. I created seperate functions for the different pages add.html and edit.html hoping that the window.onload method won't effect the edit.html page, but there were still problems.

ingredients and instructions were still displaying an extra textrea and on inspection i realised that the original hidden clone is contributing toward the data array and then being displayed as a blank textarea in the edit.html

The font awesome icons did not work in the select box. I think this is due to it being the free version.

the brand-logo title overlapped the content on smaller screens. Instead of targetting the class, I created an ID for the logo and targetted it with CSS to minimize it for smaller screens.

heroku app kept crashing. At first i thought it was something to do with the favicon because an error kept appearing with that code in the heroku log, but then after googling other errors "bash: app.py: comand not found", I compared my procfile to the task manager files and realised "python" was missing from the command. tHE APP NOW WORKS ALTHOUGH THERE IS A WARNING "This is not a development server. Do not use it in a production deployment.

On tidying up my html the materialize icons stopped working and i don't know why, but I have run out of time to fix it.

Deployment:

Credits
