import telnetlib

HOST = 'localhost'
tn = telnetlib.Telnet(HOST, '999')

tn.write('Hello world\n')

tn.write('')
print tn.read_all()