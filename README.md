## Install dependencies 
The following packages should be installed:

   - pytest
   - pytest-playwright
   - playwright


Install the Pytest plugin:


    pip install pytest-playwright


Install the required browsers:

    playwright install

## Run tests
By default tests will be run on chromium. 

    pytest


## Run tests in headed mode

    pytest --headed

## Run tests on different browsers

    pytest --browser firefox
