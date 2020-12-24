import smtplib
senderMail='***SENDERS MAIL*****'
recieverMail='*****RECIEVERS MAIL******'
body='Hello world!'

#Create an obj for SMTP class, accepts 2 parameters, smtp address and port number
server=smtplib.SMTP('smtp.gmail.com',587) 
#to start a secure encrypted connection, sequence should be maintained
server.starttls()
#For loggin in to the mailbox, login function accpts two values as parameter, email and password
server.login(senderMail,'*****SENDERS MAIL PASSWORD*******')
#To send a hello to the server (optional)
server.ehlo()
#sendmail() is for sendind the mail, accpts 3 values - Sender's mail ID, Reciever's mail ID, Body respectively
#sequence is important
server.sendmail(senderMail,recieverMail,body)
#to quit the connection, optional
server.quit()
