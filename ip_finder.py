import socket
import requests


class IPFinder:
    public_ip_finder = (
        'https://api.ipify.org/',
        'https://jsonip.com/',
        'https://ifconfig.co/json'
    )

    def get_my_ip(self):
        ip_address = ''
        for finder in self.public_ip_finder:
            try:
                result = requests.get(finder)
            except requests.RequestException:
                continue
            if result.status_code == 200:
                try:
                    socket.inet_aton(result.text)
                    ip_address = result.text
                    break
                except socket.error:
                    try:
                        socket.inet_aton(result.json().get('ip'))
                        ip_address = result.json()['ip']
                        break
                    except socket.error:
                        continue
        return ip_address
