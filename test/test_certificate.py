from goopy_certificate.certificate import Certificate, CertificateError
from pathlib import Path

"""
Tests assume the presence of a couple of certificates stored in this folder (same level as this file).
There doesn't need to be anything special about them other than one is private and one is public.
Certificates are not currently pushed to the git-repo, so they need to be created prior to running the tests

Info on installing OpenSSL: https://www.thesecmaster.com/procedure-to-install-openssl-on-the-windows-platform/

Info on creating certificates can be found:

    See: https://talkdotnet.wordpress.com/2019/08/07/generating-a-pem-private-and-public-certificate-with-openssl-on-windows/
    also see: https://adamtheautomator.com/openssl-windows-10/
    Perform the following in the same directory as this .py module
    1) openssl req -x509 -newkey rsa:4096 -keyout {keyname}.pem -out {publickey_name}.pem -nodes
    2) openssl x509 -outform der -in {publickey_name}.pem -out {publickey_name}.crt

"""

def test_get_certificate_bad_path():
    """ Fail when bad path/filename"""
    result = Certificate.get_certificate(certificate_path='notexist')

    assert result.ssl_context is None
    assert result.error is CertificateError.Invalid_Path


def test_get_certificate_not_valid():
    """ Fail when ssl doesn't like ssl_context """
    # The private test key should cause an "X509: NO_CERTIFICATE_OR_CRL_FOUND" error via ssl.SSLERROR exception
    local_test_path = Path(__file__).with_name('test_private_key.pem')
    result = Certificate.get_certificate(certificate_path=local_test_path)

    assert result.ssl_context is None
    assert result.error is CertificateError.Invalid_Certificate

def test_get_default_certs():
    """Grab default certification from user machine"""
    result = Certificate.get_certificate(use_default=True)
    assert result.ssl_context is not None
    assert result.error is CertificateError.Ok

def test_get_certificate_happy():
    """ Happy Path test when passed a good path to a valid cert"""
    local_test_path = Path(__file__).with_name('test_public_key.pem')
    result = Certificate.get_certificate(certificate_path=local_test_path)

    assert result.ssl_context is not None
    assert result.error is CertificateError.Ok