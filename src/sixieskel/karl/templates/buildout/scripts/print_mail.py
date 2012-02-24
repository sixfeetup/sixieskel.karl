"""
TODO:

- Should steal some ideas from here:
http://www.smipple.net/snippet/IanLewis/Multipart%20Mail%20Processing%20in%20Python
- Then have the ability to show a plain text version also
- Read in the mail_queue address from karlserve config
- Create a proper karlserve command out of this
- Release the package to sixfeetup github
"""
import os
from repoze.sendmail.queue import QueueProcessor
from base64 import b64decode
from email.Parser import Parser as EmailParser

mailer = None
queue_path = 'var/mail_queue'
qp = QueueProcessor(mailer, queue_path)
if os.listdir("%s/new" % qp.maildir.path):
    parser = EmailParser()
    print "Parsing mail"
    print
    for filename in qp.maildir:
        mail_file = open(filename)
        message = parser.parse(mail_file)
        print "#" * 72
        print
        for header, value in message.items():
            print "%s: %s" % (header, value)
        print
        print b64decode(message._payload)
        print
        print "#" * 72
        mail_file.close()
        os.remove(filename)
        print

    print
    print "Done parsing and removing emails"
else:
    print
    print "No emails to parse"
