import io
import os
import re
import csv
import sys
import flask
import networkx
import tempfile

from networkx.algorithms.bipartite.projection import weighted_projected_graph

app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "POST":
        input_csv = flask.request.files['file']
        tmp = tempfile.NamedTemporaryFile(delete=False)
        input_csv.save(tmp.name)
        return flask.Response(project(tmp.name), mimetype="text/csv")
    return flask.render_template("index.html")

def project(input_path):

    # create the graph
    with open(input_path) as fh:
        csv_reader = csv.reader(fh)
        g = networkx.Graph()
        onto_nodes = set()
        for row in csv_reader:
            onto_nodes.add(row[1])
            g.add_edge(row[0], row[1])

    # project the graph onto the nodes
    p = weighted_projected_graph(g, onto_nodes)

    # write the new csv
    out = tempfile.NamedTemporaryFile(delete=False)
    with open(out.name, "w") as fh:
        csv_writer = csv.writer(fh)
        for n1, n2 in p.edges():
            csv_writer.writerow([n1, n2, p[n1][n2]['weight']])

    # generate the lines in the csv
    for line in open(out.name):
        yield line

    # clean up input and output files
    os.remove(input_path)
    os.remove(out.name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
