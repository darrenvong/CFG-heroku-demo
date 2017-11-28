# CFG-heroku-demo
A light-hearted CF:G Sheffield Ambassador appreciation app to demonstrate how to deploy a web app to Heroku.
**Disclaimer: this app is made *only* to show the core files needed to successfully deploy to Heroku with minimal fuss.
Therefore, the quality of the app is not perfect ~~(e.g. it is not fully mobile responsive etc)~~ but now it IS responsive!**

## Steps to deploy to Heroku
0. Before you start to deploy your app, there are some chores we need to do first:
   * Make a `Procfile` in the **root folder** of your application. This file contains the Command Prompt/Terminal command telling Heroku exactly how to start/run your application.
   It normally contains only the following line:
   ```
   web: python app.py
   ```
   Replace `app.py` with the actual name of your file containing your Flask code if you named it something different.
   In case you're curious: the `web:` part before the command basically tells Heroku to run your Python code as a web application.
   
   * Make a file named `requirements.txt` in the **root folder** of your application. This file lists all the external libraries
   (such as `Flask` and `tweepy`) required by your application, so that Heroku knows exactly the required libraries to install
   before trying to run your application.
   In this file, type in the libraries your application require line by line, which may look something like the following:
   ```
   flask
   requests
   tweepy
   requests
   ```
   
   * In `app.py` (or whatever you named your main file containing the Flask code), add the following line to the top
   of your Flask code:
   ```python
   import os
   ```
   For the curious: the `os` module is imported so that we can access *environment variables* set by Heroku, which includes the
   *port* it has assigned to run your application on.
   
   Next (usually near the bottom of your Flask code), replace
   ```python
   app.run(debug=True)
   ```
   with the following:
   ```python
   if 'PORT' in os.environ:
        app.run(host='0.0.0.0', port=int(os.environ['PORT']))
   else:
        app.run(debug=True)
   ```
   Again, for the curious: this piece of conditional logic checks whether you are running your application on Heroku
   (in which case, the `PORT` environment variable would exist), or if you are running your application locally. The
   `host=0.0.0.0` bit instructs your Flask application to listen on **all** web address. This is important to ensure
   the application runs on Heroku since we don't know which host Heroku will decide to host the application on.

1. If you haven't already, go make a Heroku account at https://www.heroku.com

2. Once you have made a Heroku account, upon logging in, you will be taken to a dashboard, which looks something like the
following:

![alt text](static/md_imgs/dashboard.png "Heroku Dashboard")

3. To deploy the app, we need to make one first on Heroku, so do that by clicking **New > Create New app** (button at top right of the
dashboard)

4. Type in the name of your application, and change the Runtime Selection to "Europe" - this is so that the application loads
faster as we are geographically closer to Europe than the United States. Finally, click "Create App".

![alt text](static/md_imgs/create_app.png "Create app screen")

5. After clicking "Create App", you should be greeted with the following screen:

![alt text](static/md_imgs/config.png "App configuration screen")

6. Under "Deployment Method", change it to "GitHub". A "Connect to GitHub" section should now appear.

7. Under the "Connect to GitHub" section that just appeared, search for the GitHub repository corresponding to your project, then
click "Connect" to link the relevant repository (appeared as a result of the search) to the Heroku application you've just created.

8. To deploy your project, click "Deploy Branch" under "Manual deploy".

9. (Optional) You may have just noticed that a section named "Automatic deploys" has appeared in addition to the "Manual deploy"
section once you have connected your GitHub repository properly. To save you having to come back to this page in the future
and click "Deploy Branch" each time you pushed something new to your repository, if you click "Enable Automatic Deploys", then
Heroku will do so automatically.

Congratulations! You have now successfully deployed your application to Heroku!
