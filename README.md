# Fish Records API

A REST API based on Django REST Framework where a user posts a record of fishes caught during a trip along with image resizing for the uploaded fish image.

## Requirements

- Python 3.10.2
- virtualenv
- Clone the project using `git clone https://github.com/kaulashish/Fish-Record.git`
- Create a virtual environment `virtualenv <env_name> --python=python3.10.2`
- Install dependencies using the provided requirements file `pip install -r requirements.txt`
- Activate virtual environment (Linux/Mac):`source <env>/bin/activate` OR (Win):`<env>/Scripts/activate`

## Implementation

Open Postman and enter the url to which the project has been deployed: `https://fish-records.herokuapp.com`

This url consists of 2 endpoints:

1) POST `api/v1/create`

Creates the records based on parameters provided.

#### Parameters: 

- name
- species
- weight
- length
- longitude
- latitude
- image

2) GET `api/v1/records`

Returns all the records as well as resized image download links

