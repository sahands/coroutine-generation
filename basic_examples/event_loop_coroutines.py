def handle_connection(connection):
    filename = yield connection.read_line()
    file_content = yield read_file(filename)
    yield connection.send(file_content)
    connection.close()


def main():
    server = create_server(on_new_connection=handle_connection)
    server.listen()
