# -*- coding: utf-8 -*-

import sys
from OpenSSL import crypto

def generate_pem_file(string, filename):

    with open(filename, "w") as fl:
        fl.write(string)

def extract_pem_certificate():

    path_file = sys.argv[1]
    password = sys.argv[2]

    try:
        certificate = open(path_file, "r").read()
    except IOError:
        print u"Não foi possível encontrar o arquivo."
        return False

    try:
        cert = crypto.load_pkcs12(certificate, password)
    except crypto.Error:
        print u"Senha incorreta para o certificado."
        return False

    private_key = cert.get_privatekey()
    x509 = cert.get_certificate()
    cert_pem = crypto.dump_certificate(crypto.FILETYPE_PEM, x509)
    key_pem = crypto.dump_privatekey(crypto.FILETYPE_PEM, private_key)

    generate_pem_file(cert_pem, "certificate.pem")
    generate_pem_file(key_pem, "private_key.pem")

    print "Certificado e chave privada extraídos com Sucesso."
    return True

if __name__ == "__main__":
    extract_pem_certificate()
