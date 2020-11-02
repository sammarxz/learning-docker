# DOCKER LEARNING

Finally I'm learning a little bit of DevOps with Docker, I see that it is a very useful tool and can speed up the process of setting up a development environment in a team.

## How to use

#### Build Docker Image
```
$ docker build -t sample-web-app .
```

#### Check if work (will return)
```
$ docker images | grep sample-web-app
```

#### Run the image
```
$ docker run -p 8080:8080 sample-web-app
```

#### See it live
Now, open your browser in localhost, at port 8080 and see: `Hello from Python!`