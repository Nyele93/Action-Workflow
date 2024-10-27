import subprocess
import os
from datetime import datetime
from cryptography import x509
from cryptography.hazmat.backends import default_backend  # Import the default backend


CERT_FILENAME = '/usr/share/columnstore/cmapi/cmapi_server/self-signed.crt'

def check_cmapi_exists():
    """Check if CMAPI service is running."""
    # Run the systemctl command and pipe the result to grep
    result = subprocess.run('systemctl status mariadb-columnstore-cmapi | grep "active (running)"', shell=True, capture_output=True, text=True)
    print(result.stdout)

    if result.stdout:
        print("[ CMAPI STATUS ] : Service is running.")
    else:
        print("[ CMAPI STATUS ] : Service is not running or inactive.")

def days_before_expire() -> int:
    """Calculates how many days before expiration left.
    Creates self-signed cetificate if certificate doesn't exist.
    :return: days left
    :rtype: int
    """
    with open(CERT_FILENAME, 'rb') as cert_file:
        cert_data = cert_file.read()
    # Pass the default_backend() as the second argument
    cert = x509.load_pem_x509_certificate(cert_data, default_backend())
    days_before_expire = (cert.not_valid_after - datetime.now()).days
    return days_before_expire

if __name__ == '__main__':
    # Define days_left before the conditional block
    days_left = days_before_expire()
    if days_left >= 0:
        print(f'[ CERT. VALIDITY STATUS ] : Cert is still valid for {days_left} days.')
    else:
        print(f'[ CERT. VALIDITY STATUS ] : Cert has been expired for {-days_left} days. Please renew.')

    check_cmapi_exists()