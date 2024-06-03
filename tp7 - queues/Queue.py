from Box import Box


class Queue:
    def __init__(self, clients: ["Client"], number_of_boxes: int = 1):
        self.clients = clients
        self.boxes = [Box() for b in range(number_of_boxes)]
        self.max_waiting_time = 0
        self.min_waiting_time = 0
        self.unserved_clients = 0

    def lookup_box(self) -> None:
        for index, client in enumerate(self.clients):
            self.check_client_patience(client, index)
            client.patience -= 1

        for index, box in enumerate(self.boxes):
            if box.client == None and len(self.clients) > 0:
                box.client = self.clients.pop(0)
                box.served_clients += 1
                break


    def check_client_patience(self, client, index_of_client) -> None:
        if client.patience == 0:
            self.clients.pop(index_of_client)
            self.unserved_clients += 1
        else:
            self.max_waiting_time = max(self.max_waiting_time, 30*60 - client.patience)
            self.min_waiting_time = min(self.min_waiting_time, 30*60 - client.patience)
