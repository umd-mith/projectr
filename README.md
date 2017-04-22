*projectr* is a [microservice] that lets you upload a graph [edge list] as a two
column CSV file and get back a [weighted bipartite projection] of that graph
also as a CSV. You can either interact with *projectr* in your browser or as a
REST API call:

<img src="https://c1.staticflickr.com/3/2930/34063566851_8ae7b9240e_b.jpg">

     curl -F file=@/path/to/file.csv http://projectr.example.com/ 

## Install

The easiest way to get started with *projectr* is with [Docker]:

1. docker run -d -p 5000:5000 edsu/projectr
2. open http://localhost:5000

Or if you want to run it for development:

1. git clone https://github.com/umd-mith/projectr
2. cd projectr
3. pip install -r requirements.txt
4. export FLASK_APP=app
5. export FLASK_DEBUG=1
6. flask run

[microservice]: https://www.martinfowler.com/articles/microservices.html
[Docker]: https://docs.docker.com/engine/installation/
[edge list]: https://en.wikipedia.org/wiki/Adjacency_list
[weighted bipartite projection]: https://en.wikipedia.org/wiki/Bipartite_network_projection
