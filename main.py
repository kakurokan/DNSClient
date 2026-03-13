from dataclasses import dataclass
import dataclasses
import struct
import random

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


def question_to_byter(question: DNSQuestion):
    return question.name + struct.pack("!HH", question.type_, question.class_)


#Exemplo: “google.com” é traduzido para b"\x06google\x03com\x00"
def encode_dns_name(domain_name):
    encoded = b""
    for part in domain_name.encode("ascii").split(b"."):
        encoded += bytes([len(part)]) + part
    return encoded + b"\x00"
