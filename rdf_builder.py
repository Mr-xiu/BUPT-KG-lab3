from rdflib import Graph, URIRef, Namespace, Literal
import json


class RDFBuilder:
    def __init__(self) -> None:
        self.rdf = Graph()  # RDF图
        self.ns = Namespace('https://www.114514.com/')
        self.entity_list = json.load(open('data/entity_result.json', 'r', encoding='utf-8'))  # data的结构是一个list

    def clean_text(self, text: str):
        text = text.replace(' ', '').replace('\u3000', '')
        symbol_set = {'。', '，', '？', '！', '；', '：', '、', '（', '）', '「', '」', '“', '”', '‘', '’', '《', '》', '【', '】',
                      '…', '—', '～', '　', '.', ',', '?', '!', ';', ':', '(', ')', '"', '"', '\'', '\'', '<', '>', '[',
                      ']', '...', '~', '*', '―'}
        for symbol in symbol_set:
            text = text.replace(symbol, '_')
        return text

    def build(self):
        for entity in self.entity_list:
            subject = self.ns[self.clean_text(entity['title'])]
            for key in entity.keys():
                if key != 'title':
                    relation = self.ns[key]
                    obj = ' '.join(entity[key])
                    self.rdf.add((subject, relation, Literal(obj)))
        self.rdf.serialize('data/rdf_data.rdf', format='n3')


if __name__ == '__main__':
    builder = RDFBuilder()
    builder.build()
