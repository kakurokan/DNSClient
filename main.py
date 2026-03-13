from dataclasses import dataclass
import dataclasses
import struct
import random
import socket

random.seed(1)
TYPE_A = 1
CLASS_IN = 1

@dataclass
class DNSHeader:
    id: int
    flags: int
    questions: int = 0
    answers: int = 0
    authorities: int = 0
    additions: int = 0


@dataclass
class DNSQuestion:
    name: bytes
    type_: int
    class_: int

def header_to_bytes(header: DNSHeader):
    fields = dataclasses.astuple(header)
    #O 6 H's correspondem aos 6 campos do DNSHeader
    #O '!' ordena que os dados sejam empacotados no formato padrão oficial das redes internet
    return struct.pack("!HHHHHH", *fields)


def question_to_bytes(question: DNSQuestion):
    return question.name + struct.pack("!HH", question.type_, question.class_)


#Exemplo: “google.com” é traduzido para b"\x06google\x03com\x00"
def encode_dns_name(domain_name):
    encoded = b""
    for part in domain_name.encode("ascii").split(b"."):
        encoded += bytes([len(part)]) + part
    return encoded + b"\x00"

def build_query(domain_name, record_type):
    name = encode_dns_name(domain_name)
    id_header = random.randint(0, 65535)
    RECURSION_DESIRED = 1 << 8
    
    header = DNSHeader(id = id_header, questions = 1, flags = RECURSION_DESIRED)
    question = DNSQuestion(name = name, type_ = record_type, class_ = CLASS_IN)
    
    return header_to_bytes(header) + question_to_bytes(question)

query = build_query("ualg.pt", 1)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(query, ("8.8.8.8", 53))

response, _ = sock.recvfrom(1024)
print("Resposta em hexadecimal:\n" + response.hex())