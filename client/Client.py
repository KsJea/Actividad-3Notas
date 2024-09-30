import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))

    def send_request(self, request):
        self.socket.send(request.encode())
        response = self.socket.recv(1024).decode()
        return response

    def create_note(self, title, content):
        request = f"CREATE_NOTE {title} {content}"
        response = self.send_request(request)
        return response

    def read_notes(self):
        request = "READ_NOTES"
        response = self.send_request(request)
        return response

    def update_note(self, title, content):
        request = f"UPDATE_NOTE {title} {content}"
        response = self.send_request(request)
        return response

    def delete_note(self, title):
        request = f"DELETE_NOTE {title}"
        response = self.send_request(request)
        return response

    def close(self):
        self.socket.close()

if __name__ == "__main__":
    client = Client("localhost", 8080)
    client.connect()

    while True:
        print("1. Create Note")
        print("2. Read Notes")
        print("3. Update Note")
        print("4. Delete Note")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            response = client.create_note(title, content)
            print(response)
        elif choice == "2":
            response = client.read_notes()
            print(response)
        elif choice == "3":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            response = client.update_note(title, content)
            print(response)
        elif choice == "4":
            title = input("Enter note title: ")
            response = client.delete_note(title)
            print(response)
        elif choice == "5":
            client.close()
            break
        else:
            print("Invalid option")