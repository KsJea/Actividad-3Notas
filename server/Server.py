import socket
import json

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.notes = {}

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print("Server started. Listening for incoming connections...")

    def handle_request(self, request):
        if request.startswith("CREATE_NOTE"):
            title, content = request.split(" ")[1:]
            self.notes[title] = content
            return "Note created successfully"
        elif request == "READ_NOTES":
            return json.dumps(self.notes)
        elif request.startswith("UPDATE_NOTE"):
            title, content = request.split(" ")[1:]
            if title in self.notes:
                self.notes[title] = content
                return "Note updated successfully"
            else:
                return "Note not found"
        elif request.startswith("DELETE_NOTE"):
            title = request.split(" ")[1]
            if title in self.notes:
                del self.notes[title]
                return "Note deleted successfully"
            else:
                return "Note not found"
        else:
            return "Invalid request"

    def run(self):
        while True:
            client_socket, address = self.socket.accept()
            request = client_socket.recv(1024).decode()
            response = self.handle_request(request)
            client_socket.send(response.encode())
            client_socket.close()

if __name__ == "__main__":
    server = Server("localhost", 8080)
    server.start()
    server.run()