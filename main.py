import socket
from views import index, blog, text

URLS = {
    '/': index,
    '/blog': blog,
    '/text': text,
}


def parse_request(request: str) -> tuple[str, str]:
    processed_request = request.split(' ')
    method = processed_request[0]
    url = processed_request[1]
    return method, url


def generate_headers(method: str, url: str) -> tuple[str, int]:
    if method != "GET":
        return 'HTTP/1.1 405 Method NOT allowed!!!\n\n', 405
    if url not in URLS:
        return 'HTTP/1.1 404 Page not found!!!\n\n', 404
    return 'HTTP/1.1 200 OK!!!\n\n', 200


def generate_content(code: int, url: str):
    if code == 404:
        return '<h1>404</h1><p>Page not found</p>'
    if code == 405:
        return '<h1>405</h1><p>Method NOT allowed</p>'
    return URLS.get(url)()


def generate_response(request: str):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)
    return (headers + body).encode()


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5566))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(request)
        print()
        print(addr)

        response = generate_response(request.decode('utf-8'))

        client_socket.sendall(response)
        client_socket.close()


if __name__ == '__main__':
    run()
