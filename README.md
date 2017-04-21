projectr is a little microservice lets you upload a graph edge list as a two
column CSV file and get back a weighted bipartite projection of that graph as a
CSV.

# Run

The easiest way to run projectr is with [Docker]:

    docker run -d -p 5000:5000 edsu/projectr
    open http://localhost:5000

If you want to run it for development:

    git clone https://github.com/umd-mith/projectr
    cd projectr
    pip install -r requirements.txt
    export FLASK_APP=app
    export FLASK_DEBUG=1
    flask run

[Docker]: https://docs.docker.com/engine/installation/

