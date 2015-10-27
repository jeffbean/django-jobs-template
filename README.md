## Run on your machine

    git clone git@git.mcp.com:jbean/django-jobs.git
    cd django-jobs
    docker-compose pull
    docker-compose build
    docker-compose up
   
You can then navigate to `http://localhost:8005` for the web interface.


## Run unit tests

    docker-compose run web ./manage.py test
    
    docker-compose run web coverage run --source='.' manage.py test
    
    docker-compose run web coverage report
  
    
## Create XML coverage report

    docker-compose run web coverage xml
    
    
    
# Change the boilerplate

## copy paste style

## Rename with pycharm

