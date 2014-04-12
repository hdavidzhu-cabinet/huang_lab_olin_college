"""
'Blast server' sends FASTA data directly to the NIH Blast server and receives a list of useful comparative genes.

Put: Fasta File
Get: List of genes and their functions.
"""
import os, sys, telnetlib
import HTMLParser

gi = 555
database  = 'nr'
expect_val = 10

# CMD = 'Web'
# PAGE = 'Proteins'
# DATABASE = 'swissprot'
# WEB = 'http://www.ncbi.nlm.nih.gov/blast/Blast.cgi?CMD='+CMD+'&\PAGE='+PAGE+'&DATABASE='+DATABASE

tn = telnetlib.Telnet('www.ncbi.nlm.nih.gov', '80', 60)
# tn.interact()
tn.write('Hello')

tn.write('POST /blast/Blast.cgi HTTP/1.0\n')
tn.write('User-Agent: Hi_there\n')
tn.write('Connection: Keep-Alive\n')
tn.write('Content-type: application/x-www-form-urlencoded\n')
tn.write('Content-Length: 200\n')
    
# CMD=Put&QUERY=555... etc
tn.read_all()
tn.close()