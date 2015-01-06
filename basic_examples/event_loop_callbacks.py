def handle_new_connection(event):
    connection = event.connection

    def close_connection():
        connection.close()

    def send_file(event):
        connection.send(event.file_data, on_completed=close_connection)

    def handle_new_request(event):
        read_file(event.data, on_completed=send_file)

    connection.read_line(on_completed=handle_new_request)


def run_main_loop():
    listen_for_connections(on_new_connection=handle_new_connection)
    while True:
        event = get_next_event()
        for handler in get_event_handlers(event):
            handler(event)
