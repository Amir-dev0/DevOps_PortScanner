from unittest.mock import patch
from app.port_scanner import PortScanner

def test_closed_port():
    with patch("app.port_scanner.socket.socket") as mock_socket:
        mock_socket.return_value.connect_ex.return_value = 111

        scanner = PortScanner("127.0.0.1")
        result = scanner.scan(80)

        assert result.status == "closed"