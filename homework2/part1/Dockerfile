FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install python3 -y 
RUN apt-get install python3-pip -y 
RUN pip3 install tensorflow -f https://tf.kmtea.eu/whl/stable.html
RUN pip3 install numpy
RUN pip3 install imageio

WORKDIR /tf
# COPY .image.tar.gz .
ADD train.py /tf
ADD classify.py /tf
# CMD [ "python", "./train.py" ]
RUN mkdir images
RUN mkdir -p tmp/mnist_model