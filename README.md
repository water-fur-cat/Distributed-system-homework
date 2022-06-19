# Distributed-system-homework
## homework 1: 
### Description:
In this assignment, I create a client/server system that exchanges information between a single 
client and a single server.  <br>
The project is implemented in Python 3 and use the standard Python socket and pickle libraries.  <br>
The project is organized in two parts. In the first part, I set up a client/server to exchange text 
messages; in the second part I extend the client/server to exchange Python objects. 
<br>

### Functionality: 
1. Client able to connect to server 
2. Server able to receive message 
3. Server able to respond to message 
4. Method to serialize Python object 
5. Client/server able to exchange Python objects 

## homework 2:
### Description:
In this assignment, students will learn to work with Docker, which is a popular virtualization technology. They
will develop an application which will be run in Docker containers. <br>
In this part, we deploy a classifier model for the MNIST dataset (http://yann.lecun.com/exdb/
mnist/) in a Docker container. The code to train and use the model (using Tensorflow) is already provided as two Python files (train.py and classify.py). It also provided a set of test images (images.tar.gz) to test classifier. <br>

### Functionality: 
1. Dockerfile correctly defines image with files and dependencies as specified (10 points)
2. build.sh builds Docker image correctly (5 points)
3. run.sh runs Docker container correctly and persistently with a shared mount (15 points)
4. infer.sh runs inference correctly by communicating with Docker container (10 points)
5. README conceptual questions (5 points per question)

## homework 3:
### Description:
It is a Multi-user chat server. <br>
In this homework assignment we implement a multi-user chat server using ZeroMQ. The purpose of this assignment is to reinforce students' understanding of different communication patterns. <br>
The assignment includes four parts: first we will create a client/server pair for publishing messages to a chat channel; we will then create a pub/sub mechanism for displaying the contents of the channel; next we will integrate these two models to create an interactive, multi-user chat client and server; finally, we will create a multi-channel
client and server using ZeroMQ topics to filter message. <br>

## homework 4：
### Description:
In this assignment we will create a distributed password cracking system. <br>
we will implement the system as a REST service and develop a client that can distribute portions of the password search space to instances of the REST service. Each call should attempt to brute force crack the password by checking each combination of letters against the hashed password. <br>
We will then enhance the service to improve fault tolerance and performance by caching previous attempts. <br>
