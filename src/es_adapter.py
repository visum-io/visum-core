import time
from elasticsearch5 import Elasticsearch


def create_mapping(es):
    es.indices.create('test-index')
    es.indices.put_mapping(
        index="test-index",
        doc_type="tweet",
        body={
            "properties": {
                "timestamp": {
                    "type": "date",
                    "format": "epoch_millis"
                }
            }
        }
    )


def add_test():
    es = Elasticsearch()
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': int(round(time.time() * 1000)),
        'money': 22
    }
    res = es.index(index="test-index", doc_type='tweet', id=7, body=doc)

    doc = {
        'author': 'tolstoy',
        'text': 'hi',
        'timestamp': int(round(time.time() * 1000)),
        'money': 30
    }
    res = es.index(index="test-index", doc_type='tweet', id=10, body=doc)
    print res


if __name__ == '__main__':
    add_test()
