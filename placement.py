class PlacementManager:
    def __init__(self):
        self.chunk_locations = {}

    def register_chunk(self, chunk_id, server_id):
        if chunk_id not in self.chunk_locations:
            self.chunk_locations[chunk_id] = []
        self.chunk_locations[chunk_id].append(server_id)

    def get_chunk_locations(self, chunk_id):
        return self.chunk_locations.get(chunk_id, [])
