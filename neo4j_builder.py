import json

from py2neo import Graph, Node, Relationship


class Neo4jBuilder:
    def __init__(self, neo4j_url, neo4j_user, neo4j_password, database_name, entity_path):
        self.graph = Graph(neo4j_url, user=neo4j_user, password=neo4j_password, name=database_name)
        self.entity_list = json.load(open(entity_path, 'r', encoding='utf-8'))

    def build(self):
        for entity in self.entity_list:
            subject = Node('disaster', name=entity['title'])
            self.graph.create(subject)
            for key in entity.keys():
                if key != 'title':
                    for val_name in entity[key]:
                        val = Node('value', name=val_name)
                        rela = Relationship(subject, key, val)

                        self.graph.create(val)
                        self.graph.create(rela)


if __name__ == '__main__':
    builder = Neo4jBuilder(neo4j_url='http://localhost:7474', neo4j_user='neo4j', neo4j_password='20020601',
                           database_name='neo4j', entity_path='data/entity_result.json')
    builder.build()