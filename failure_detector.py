import time


class FailureDetector:
    def __init__(self, timeout=3):
        self.timeout = timeout
        self.last_heartbeat = {}

    def heartbeat(self, server_id):
        self.last_heartbeat[server_id] = time.time()

    def get_failed_servers(self):
        now = time.time()
        failed = []

        for server_id, ts in self.last_heartbeat.items():
            if now - ts > self.timeout:
                failed.append(server_id)

        return failed
