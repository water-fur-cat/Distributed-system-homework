docker exec -it hw2 python3 classify.py --input /tf/images/$(ls $(pwd)/images | sort -R | head -1)