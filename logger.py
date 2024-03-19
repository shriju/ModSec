import datetime
#------------------------------importing complete-----------------------------------

f = open("log.txt", 'w', encoding="utf-8")

def make_entry(message):
    f.write("{} --- {}\n".format(datetime.datetime.now(), message))     #append time & error message in log.txt