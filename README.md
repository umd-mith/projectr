*projectr* is a [microservice] that lets you upload a graph [edge list] as a two
column CSV file and get back a [weighted bipartite projection] of that graph
also as a CSV. You can either interact with *projectr* in your browser or as a
REST API call:

<img src="https://c1.staticflickr.com/3/2930/34063566851_8ae7b9240e_b.jpg">

     curl -F file=@/path/to/file.csv http://projectr.example.com/ 

## Install

The easiest way to get started with *projectr* is with [Docker]:

    docker run -d -p 8080:5000 edsu/projectr
    open http://localhost:5000

Or if you want to run it so you can hack on it:

    git clone https://github.com/umd-mith/projectr
    cd projectr
    pip install -r requirements.txt
    export FLASK_APP=app
    export FLASK_DEBUG=1
    flask run

[microservice]: https://www.martinfowler.com/articles/microservices.html
[Docker]: https://docs.docker.com/engine/installation/
[edge list]: https://en.wikipedia.org/wiki/Adjacency_list
[weighted bipartite projection]: https://en.wikipedia.org/wiki/Bipartite_network_projection
