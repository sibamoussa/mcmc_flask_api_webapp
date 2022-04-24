# mcmc_toy_flask_webapp
Implementation of Monte Carlo Metropolis Hastings (MCMC) Algorithm as a User-Authenticated Interactive Flask Web App 

# Try it out
1) Download main.py and requirements.txt 
2) Make sure all packages and dependencies are installed in virtual environemnt by running: `pip install  -r requirements.txt `
3) Run main.py in terminal using the following command, making sure you are in the same working directory as main.py is saved: `python3 main.py`
4) For now, the flask app will be locally hosted, which can be found at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
5) After running main.py and loading http://127.0.0.1:5000/ on your favorite web browser, you will be prompted to enter a username and password, enter the following: `username: Algorithm` and `password: MCMC` 
6) Now you will be able to access the web-app. To visualize the results of the MCMC algorithm on the double well potential, refer to terminal where you will be prompted to enter the number of iterations, the temperature in degrees celcuis and the constant for the barrier height. Enter these values with a space in between and press enter
7) Viola! Refer back the web browser and you should be able to visualize the results from the MCMC algorithm on the double well potential. 

Note: You can run the simulation as many times as you want. You will notice that the MCMC algorithm gets stuck in the low energy modes and does not sample the space very well at low temperatures - which is an inherent problem in MCMC based sampling algorithms. 

# Future Work
- Include google engine hosting of the webapp
- Add interactive user input queries on the webapp to update MCMC simulation results 
- Enable local figure saving 
