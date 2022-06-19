# homework-2-water-fur-cat
* In Section 1, do the following:
- How to Run:
    # first enter the part1 dir then extract the images folder
    cd part1
    tar -xf images.tar.gz 

    # then allow to run the shell script
    chmod 777 build.sh
    chmod 777 run.sh  
    chmod 777 infer.sh

    # run the shell script to build images
    ./build.sh  

    # run the container to train model
    ./run.sh   

    # to classify
    ./infer.sh 

- Example:
    
    cd part1
    chmod 777 build.sh
    chmod 777 run.sh  
    chmod 777 infer.sh
    ./build.sh 
    ./run.sh
    ./infer.sh 

- Include any known issues/bugs:
    Seems like everything now works fine.

* In Section 2, provide answers to the following questions:
- Why did we need to create a shared directory images? Name one other way in which we could have
achieved the same goal (without a file-system mount).
    It is because we need to use images in that directory to test the model so we share files between a host system and the Docker container. When you use a volume, a new directory is created within Docker’s storage directory on the host machine, and Docker manages that directory’s contents.
    Another way: Write code 'ADD images.tar.gz /tf' in the Dockerfile and then use cmd 'tar' to generate the images file.

- Why would we want to deploy applications, especially with dependencies like Tensorflow, in Docker containers?
    Because Docker makes it easy to create, deploy, and run applications by using containers. Developer can package applications with their dependencies and deploy them as a single package.
    With Docker containers, developers can be sure that the application working on their own machine will work on the others.

* reference
- https://towardsdatascience.com/heres-why-you-should-learn-docker-as-a-data-scientist-c18faf96c946
- https://neptune.ai/blog/best-practices-docker-for-machine-learning
- https://www.digitalocean.com/community/tutorials/how-to-share-data-between-the-docker-container-and-the-host
- https://docs.docker.com/storage/volumes/
- https://docs.docker.com/storage/bind-mounts/
- https://zhaomenghuan.js.org/blog/install-docker-tensorflow-in-mac.html#docker-image
- https://www.runoob.com/docker/docker-image-usage.html