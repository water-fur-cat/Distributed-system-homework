docker run -it -d -v $(pwd)/images:/tf/images --name hw2 tf /bin/bash 
docker exec -it hw2 python3 train.py