# datascience
This repository is for my practice:
 - Courses practices
 - kaggle kernels
 - and other
 
 To run jupyter notebook in docker container if you have docker. In the terminal:
    cd to the working directory and run following commands:
    
        docker-compose build
        docker-compose up
        docker-compose exec jupyter sh
   the shell of the docker will be opened. In this shell run command:
    
        jupyter notebook list
   go to the link that appears in the terminal. In the browser you will see current directory.
