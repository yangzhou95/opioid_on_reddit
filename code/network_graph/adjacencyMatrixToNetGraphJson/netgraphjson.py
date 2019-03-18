import json


class NetGraphJson():
    def __init__(self):
        self.type = "NetworkGraph"
        self.label = "Ninux Roma"
        self.protocol = "OLSR"
        self.version = "0.6.6.2"
        self.metric = "ETX"
        self.nodes = []
        self.links = []

    def reprJSON(self):

        return dict(type=self.type, label=self.label, protocol=self.protocol,
                    version=self.version, metric=self.metric, nodes=self.nodes, links=self.links)


class Links():
    def __init__(self, source, target, cost):
        self.source = source
        self.target = target
        self.cost = cost

    def reprJSON(self):
        return dict(source=self.source, target=self.target, cost=self.cost)


class Nodes():
    def __init__(self, id):
        self.id = id

    def reprJSON(self):
        return dict(id=self.id)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)
