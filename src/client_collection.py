class ClientCollection:
    def __init__(self, clients=None):
        self.clients = clients or []

    def add(self, client):
        self.clients.append(client)

    def get_by_id(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None

    def to_list(self):
        return [client.to_dict() for client in self.clients]