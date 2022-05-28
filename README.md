# API enabled simulations of MCMC
Implementation of Monte Carlo Metropolis Hastings (MCMC) Algorithm as a User-Authenticated Interactive Flask Web App. Using a custom built api, the flask app will connect to a google sheets document in my google drive to simulate MCMC algorithm on the double well potential. 

# Try it out
1) Download all files. 
2) Make sure all packages and dependencies are installed in virtual environemnt by running: `pip install  -r requirements.txt `
3) Run the flask server api by typing python FlaskApiServer.py
4) You should be able to view the data at [http://127.0.0.1:5000/api/]
5) To load the flask application, enter the following command in terminal: `export FLASK_APP=main` (make sure you are in the same working directory as main.py is saved)
6) To run the flask application, enter the command in terminal: `flask run`
7) For now, the flask app will be locally hosted, which can be found at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
8) After running main.py and loading http://127.0.0.1:5000/ on your favorite web browser, you will be prompted to enter a username and password, enter the following: `username: Algorithm` and `password: MCMC` 
9) Now you will be able to access the web-app. To visualize the results of the MCMC algorithm on the double well potential. The algorithm will run with the paramters chosen from the google sheets api. To select different parameters, you can make modifications to the main.py script url on line 37. 

## Notes:
- You can run the simulation as many times as you want. You will notice that the MCMC algorithm gets stuck in the low energy modes and does not sample the space very well at low temperatures - which is an inherent problem in MCMC based sampling algorithms. 
- Sample images of authentication and MCMC simulation are in /img folder.
- If you want user input to run the simulation, rather than api-enabled input, check the code in the `mcmc_flask` branch 
- I used mockaroo [https://www.mockaroo.com/] to randomly generate the values in the google sheet which would be used as paramters in the MCMC simulation. You can replace this with real data. 

# Future Work
- Include google engine hosting of the webapp
- Add interactive user input queries on the webapp to update MCMC simulation results 
- Enable local figure saving 
- Enable user input to access certain regions of the google sheet 
