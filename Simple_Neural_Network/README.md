# Simple Neural Network

Build a simple neural network and use it to predict daily bike rental ridership. 

`Simple_Neural_Network.ipynb` - 

* Load and prepare the data
* Data exploration
* Build the network:
* Train the network
* Test


Having good initial weights can place the neural network close to the optimal solution. This allows the neural network to come to the best solution quicker. To see how different weights perform, we'll test on the same [dataset](https://en.wikipedia.org/wiki/MNIST_database) and neural network (below).

<img style="float: left" src="images/neural_network.png"/> 


`Weight_Initialization_NN.ipynb` - 

* All zeros or ones

<img src="images/all_zero_one.png"/>   

* Uniform distribution

Baseline: minval=0.0 and maxval=1.0

<img src="images/baseline.png"/> 

BaselinePlus: minval=-1.0 and maxval=1.0

<img src="images/baselineplus.png"/> 

Compare [-0.1, 0.1), [-0.01, 0.01), and [-0.001, 0.001):

<img src="images/compare.png"/>

General rule for setting weights:

<img src="images/generalrule.png"/>

* Normal distribution

<img src="images/normal.png"/>

* Truncated normal distribution

<img src="images/tnormal.png"/>
