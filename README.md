# Cliente DNS em Python

Este projeto consiste na implementação de um cliente DNS (Domain Name System) básico, construído do zero em Python. Foi desenvolvido como parte de um trabalho académico para a **Universidade do Algarve**.

O objetivo principal deste projeto é demonstrar a construção manual de pacotes de rede ao nível dos bytes, enviando uma consulta DNS para um servidor e recebendo a sua resposta, que pode ser posteriormente analisada utilizando ferramentas de captura de tráfego, como o Wireshark.

## 🎯 Objetivos do Trabalho

1. Construir o cabeçalho de uma mensagem DNS (12 bytes) e a secção de perguntas (Question Section) de acordo com o protocolo oficial.


2. Enviar a consulta formatada para um servidor DNS público (Google DNS - `8.8.8.8`) utilizando sockets UDP.


3. Receber a resposta bruta do servidor e imprimi-la em formato hexadecimal para facilitar a depuração e análise.
4. Analisar a resposta da rede através do **Wireshark**.



## ⚙️ Tecnologias e Bibliotecas Utilizadas

* **Python 3.10+**
* `socket`: Para a criação da ligação UDP na porta 53 e comunicação em rede.
* `struct`: Para o empacotamento dos dados originais em bytes no formato exigido pela rede (Network Byte Order / Big-Endian).
* `dataclasses`: Para a estruturação elegante e modular das classes `DNSHeader` e `DNSQuestion`.

## 🚀 Como Executar o Projeto

### Pré-requisitos

* Ter o Python instalado (versão 3.7 ou superior, devido ao uso de `@dataclass`).
* Ter o [Wireshark](https://www.wireshark.org/) instalado para a análise de tráfego.

### Execução

1. Abra o terminal na pasta raiz do projeto.
2. Execute o ficheiro principal:
```bash
python main.py

```


3. O terminal irá exibir a resposta bruta enviada pelo servidor em formato hexadecimal.

### Análise no Wireshark

Para verificar o tráfego gerado por este script:

1. Abra o Wireshark e inicie a captura na sua interface de rede principal (ex: Wi-Fi ou Ethernet).
2. Na barra de filtros, digite o seguinte filtro para isolar o tráfego DNS:
```text
udp.port == 53

```


3. Execute o script `main.py`.
4. Observe no Wireshark o pacote de "Standard query" (A nossa pergunta) e o pacote de "Standard query response" (A resposta do servidor).

## 📚 Bibliografia e Referências

O desenvolvimento deste cliente DNS baseou-se na seguinte documentação e materiais de apoio:


1. **Evans, Julia.** *Implement DNS in a weekend*. Wizard Zines. Guia prático sobre a construção estruturada de consultas DNS utilizando Python e dataclasses.
2. **Kozierok, Charles M. (2005).** *The TCP/IP Guide - DNS Message Header and Question Section Format*. Documentação detalhada sobre o protocolo TCP/IP e estruturação dos cabeçalhos e *flags* bit a bit para mensagens DNS.

---

*Trabalho desenvolvido para fins académicos.*
