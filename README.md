![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Cintakins,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

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

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Table of content:

strategy - Business objectives. whats worth doing. whats being created. value.
The project is designed to attract users to the web application by providing a service to display recipes and add their own custom recipes. This will attract the type of user who is passionate about cooking and will therefore already be interested in any products the website might offer. Cooking equipment websites can advertise their wares to the user giving them appropriate and optimal exposure. The main focus of the website will be for the recipes and for users to share their expertise, and for those interested in using these recipes, cooking product websites will be displayed for them to click on.

scope = what I included and what i would have liked to have included. specs and requirements.  
users will certainly want a list of recipes they can choose from. If that list gets exhausting they will need the ability to search through them to find what they want. They need to be able to get a quick idea via visuals and a short description of each recipe so that it is easy for them to navigate through the recipes shown to them. Therefore the recipes need a descrription, an image, a name, a list of ingredients and instructions. A nice feature for those uploading their recipes will be for them to be creditted at the bottom of their recipes. There needs to be easy navigation between pages. Pages needed are; a recipe page for all recipes, profile page with the user's own recipes, login/register page, a home page to introduce the use to the use of the web app, and a page to upload recipes. The web app needs to be responsive on all screen sizes and easy to navigate.
 Those are the main requirements of the project, however if there is time, extra features would be nice such as adding a like button to like recipes and a display of the most popular recipes on the home page. The home page will also have a random generated recipe suggestion for all recipes to have the opportunity to be in the limelight and for users to try new recipes.

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

the add step and add ingredient buttons created too many steps when loading the edit page, so there were more steps than the existing values given.

The font awesome icons did not work in the select box.

the brand-logo title overlapped the content on smaller screens. Instead of targetting the class, I created an ID for the logo and targetted it with CSS to minimize it for smaller screens.

Deployment:

Credits
