from py2neo import Graph, Node, Relationship
import rdflib


class Neo4jBuilder:
    def __init__(self, neo4j_url, neo4j_user, neo4j_password, database_name, rdf_path, rdf_url=''):
        self.graph = Graph(neo4j_url, user=neo4j_user, password=neo4j_password, name=database_name)
        self.rd_graph = rdflib.Graph()
        self.rd_graph.parse(rdf_path, format='n3')
        for s, p, o in self.rd_graph:
            print(s, p, o)


if __name__ == '__main__':
    builder = Neo4jBuilder(neo4j_url='http://localhost:7474', neo4j_user='neo4j', neo4j_password='20020601',
                           database_name='kg_lab', rdf_path='data/rdf_data.rdf')
