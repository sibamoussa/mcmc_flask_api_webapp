from flask import Flask
from flask_basicauth import BasicAuth
import numpy as np
from matplotlib.figure import Figure
import base64
from io import BytesIO
import math
from waitress import serve


app=Flask('mcmc')


app.config['BASIC_AUTH_USERNAME']='Algorithm'
app.config['BASIC_AUTH_PASSWORD']='MCMC'

basic_auth=BasicAuth(app)




def target(theta):
    return (-0.5*theta**2+0.25*theta**4)   # double well potential

def prob_density(theta,beta):
    return np.exp(-beta*target(theta))    #partition function 
# prob proportional to e^(-energy(i)/kt) beta=1/kt

@app.route("/")  #decorator to connect 

@basic_auth.required
def main():
    try:
        n_iter,deg_c,const = [int(i) for i in input("Please enter number of iterations, temperature and beta ratio(beta*barrier height) :").split()]

        n_iterations = n_iter
        deg_C=deg_c
        constant=const
        k=8.617*10**-5
        theta = np.arange(n_iterations,dtype=np.float)
        t=273+deg_C
        barrier_height=k*t
        beta=constant/barrier_height
        theta[0] = 0 #initial guess
        counter = 0 
        for i in range(1, n_iterations-1):
            theta_next =theta[i]+np.random.uniform(-1,1)
            if np.random.uniform(0,1) < min(1, prob_density(theta_next,beta)/prob_density(theta[i],beta)):
                theta[i+1] = theta_next
                counter = counter + 1
            else:
                theta[i+1] = theta[i]
        print("acceptance fraction is ", counter/float(n_iterations))
        
        # Generate the figure **without using pyplot**.
        fig = Figure()
        ax = fig.add_subplot(1,3,1)
        ax.scatter(theta,target(theta),color='black')
        ax.set_xlabel('Position (x)')
        ax.set_ylabel('V(x) / Potential Energy of the Mean Force')

        ax2= fig.add_subplot(1,3,2)
        ax2.scatter(np.array(range(0,n_iterations)),theta,label='x')
        ax2.set_title('MCMC Sampled Values at '+ str(t) + ' Kelvin and ' +str(constant) + '/barrier height (kt)')
        ax2.set_ylabel(' Position (x)')
        ax2.set_xlabel('Iteration #')
        
        ax3= fig.add_subplot(1,3,3)
        ax3.hist(theta, bins=int(math.sqrt(len(theta))), color='blue')
        ax3.set_ylabel('Probability Density')
        ax3.set_xlabel('Position (x)')
        fig.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
        #save to temporary buffer
        buf = BytesIO()
        fig.savefig(buf, format="png")
        # Embed the result in the html output.
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return f"<img src='data:image/png;base64,{data}'/>"    
    
    except ValueError:
        return 'Error in user input, please make sure to use integer values as valid input'

if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=8080, debug=True)
    serve(app, listen='*:80')