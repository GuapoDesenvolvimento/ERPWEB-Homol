from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import NameOID

# 1. Gerar par de chaves
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# 2. Criar CSR
builder = x509.CertificateSigningRequestBuilder()
# 17569551000173 / REDE GUAPO DE POSTOS DE COMBUSTIVEL LTDA
# 76236157000182 / COMERCIO DE COMBUSTIVEIS SCHON LTDA
# 72469687000110 / COMBUSTIVEIS GUAPO LTDA
# 03626094000105 / IDEAL GUAPO LTDA
# 3. Informações do assunto (substitua com seus dados)
subject = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"BR"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"PR"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Palmeira"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"REDE GUAPO DE POSTOS DE COMBUSTIVEL LTDA"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"https://intranet.redeguapo.com"),
])
builder = builder.subject_name(subject)

# 4. Adicionar extensões (opcional)
# builder = builder.add_extension(
#     x509.SubjectAlternativeName([x509.DNSName(u"www.exemplo.com")]),
#     critical=False,
# )

# 5. Assinar a CSR com a chave privada
csr = builder.sign(private_key, hashes.SHA256(), default_backend())

# 6. Salvar a chave privada e a CSR
with open("private.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("csr.pem", "wb") as f:
    f.write(csr.public_bytes(serialization.Encoding.PEM))

print("CSR e chave privada gerados com sucesso.")