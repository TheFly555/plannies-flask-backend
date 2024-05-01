# Start dev enviroment
1. ```Docker compose up```

Note: Make sure you are in the folder with the docker-compose.yaml file

# Info
The folder is connected to a volume on the host. If you change files on your machine then this will also update the code in the docker container. Now you do not have to rebuild the image everytime you want to test.