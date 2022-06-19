# homework3-water-fur-cat
## How to Run:
- first build the image: docker build -t communication-class .
- run the container: docker run -it -v "$(pwd)"/code:/code --name hw3 communication-class bash 
- enter the container: docker exec -it hw3 bash  

## part 1:
- cd code
- cd part1
- python post_server.py 127.0.0.1 7777
- python post_client.py 127.0.0.1 7777 April "Hi"
- python post_client.py 127.0.0.1 7777 Heather "Hello"

## part 2:
- cd ..
- cd part2
- python pub_server.py 127.0.0.1 7777 7778
- python pub_client.py 127.0.0.1 7778
- python post_client.py 127.0.0.1 7777 April "Hello"
- python post_client.py 127.0.0.1 7777 Heather "Hi"

## part 3:
- cd ..
- cd part3
- python interactive_server.py 127.0.0.1 7777 7778
- python interactive_client.py 127.0.0.1 7777 7778 April
- python interactive_client2.py 127.0.0.1 7777 7778 Heather
- then enter messages in their own client terminals

## part 4:
- cd ..
- cd part4
- python mc_server.py 127.0.0.1 7777 7778
- python mc_client.py 127.0.0.1 7777 7778 ALL April
- python mc_client2.py 127.0.0.1 7777 7778 HW3 Heather
- then enter messages in their own client terminals

## Include any known issues/bugs:
    Seems like everything now works fine.