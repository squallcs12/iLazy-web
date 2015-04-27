import time
from apns import APNs, Frame, Payload

apns = APNs(use_sandbox=True, cert_file='cert.pem', key_file='key.pem')

# Send a notification
token_hex = 'ac93f23556aeccf77944f62e9eefc52a7ec4f3d7e368e09307cc6cf4643b803b'
payload = Payload(alert="Hello World!", sound="default", badge=1)
apns.gateway_server.send_notification(token_hex, payload)