#!/usr/bin/python

import vymgmt

def createfirewall(fname):
    vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
    vyos.login()
    vyos.configure()
    vyos.set("firewall name %s default-action 'accept'" %fname)
    vyos.commit()
    vyos.save()
    vyos.exit()
    vyos.logout()

def readfirewall():
    vyos = vymgmt.Router('192.168.0.1', 'vyos', password='vyos', port=22)
    vyos.login()
    vyos.configure()
    print (vyos.run_conf_mode_command("show firewall name"))
    y = vyos.run_conf_mode_command("show firewall name")
    vyos.exit()
    vyos.logout()
    return y

def updatefirewall(fname,fname2):
    vyos = vymgmt.Router('192.168.0.1', 'vyos', password='vyos', port=22)
    vyos.login()
    vyos.configure()
    vyos.delete("firewall name %s " %fname)
    vyos.set("firewall name %s default-action 'reject'" %fname2)
    vyos.commit()
    vyos.save()
    vyos.exit()
    vyos.logout()

def delfirewall(fname):
    vyos = vymgmt.Router('192.168.0.1', 'vyos', password='vyos', port=22)
    vyos.login()
    vyos.configure()
    vyos.delete("firewall name %s default-action 'reject'" %fname)
    vyos.commit()
    vyos.save()
    vyos.exit()
    vyos.logout()
