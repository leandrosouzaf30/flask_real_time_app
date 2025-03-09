from app_factory import create_app, socketio

app = create_app()


@socketio.on('connect')
def handle_connect():
    print('Cliente conectado ao WebSocket')


if __name__ == '__main__':
    socketio.run(app, debug=True)
