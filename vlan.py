#!/usr/bin/python

import vymgmt

def createvlan(eth,num,desc,ip):
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.set("interfaces ethernet %s vif %s description '%s'" %(eth,num,desc))
	vyos.set("interfaces ethernet %s vif %s address %s" %(eth,num,ip))
        vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()

def readvlan():
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        print (vyos.run_op_mode_command("show ip route"))
        y = vyos.run_op_mode_command("show ip route")
        vyos.logout()
        return y

def delvlan(eth,num):
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.delete("interfaces ethernet %s vif '%s' " %(eth,num))
        vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()

def updatevlan(eth,eth1,num,num1,desc,ip):
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.delete("interfaces ethernet %s vif %s" %(eth,num))
        vyos.set("interfaces ethernet %s vif %s description '%s' " %(eth1,num1,desc))
	vyos.set("interfaces ethernet %s vif %s address %s"%(eth1,num1,ip))
        vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()

