REM See: https://talkdotnet.wordpress.com/2019/08/07/generating-a-pem-private-and-public-certificate-with-openssl-on-windows/

REM openssl req -x509 -newkey rsa:4096 -keyout test_public_key.pem -out test_public_key.pem -nodes
openssl req -x509 -newkey rsa:4096 -keyout private_key.pem -out public_key.pem -days 365 -nodes
openssl x509 -outform der -in test_public_key.pem -out test_public_key.crt