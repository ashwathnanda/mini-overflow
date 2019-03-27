# Pronto
A Flask Web Application which fetches JAVA Project (.jar) file based on the requirement provided by the User. All the files are uploaded on AWS S3 bucket.

This is a Proof of concept(or Minimum viable concept) and is not intended to be used on a commercial scale.


- Dependencies installation

```bash
pip install -r requirements.txt
```

- Run the Flask Application

```
python app.py
```

- To Run this code as an rest-API service. 

```
python server.py
```

Now use any API testing tool like POSTMAN to test the api 

- Or use the Requests library 
```python
import requests
code = input('Enter your requirement :')
#GET requests
resp = requests.get('http://127.0.0.1:8080/fetch/{}'.format(code))

#for POST requests
resp = requests.post('http://127.0.0.1:8080/', data={'req':code))

print resp.text 
```


- To build a Docker Image ( cd onto the directory and run the below command or specify the path to the Dockerfile )
```
$ cd ./mini-overflow-master
$ docker build .
```
