projectr is a little microservice lets you upload a graph edge list as a two
column CSV file and get back a weighted bipartite projection of that graph as a
CSV.

1. git clone https://github.com/umd-mith/projectr
2. docker build -t projectr .
3. docker run -d -p 5000:5000 projectr
4. open http://localhost:5000

