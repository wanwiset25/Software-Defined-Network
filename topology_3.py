"""
A complex containing 3 routers, 5 switches, 5 subnets and 15 hosts.
"""

from mininet.topo import Topo

class MyTopo(Topo):
    "Simple topology example."

    def __init__(self):
	"Create custom topology."

	#Initialize the topology
	Topo.__init__(self)
	
	"""
	[555 Comments]
	Your topology file for scenario 3. Define all the required devices here.
	"""
	# Add hosts and switches
	r1 = self.addNode('r1', ip='172.17.16.1/24')
	r2 = self.addNode('r2', ip='10.0.0.1/25')
	r3 = self.addNode('r3', ip='20.0.0.1/25')
	s4 = self.addSwitch('s4')
	s5 = self.addSwitch('s5')
	s6 = self.addSwitch('s6')
	s7 = self.addSwitch('s7')
	s8 = self.addSwitch('s8')
	h9 = self.addHost('h9', ip='172.17.16.2/24', defaultRoute='via 172.17.16.1')
	h10 = self.addHost('h10', ip='172.17.16.3/24', defaultRoute='via 172.17.16.1')
	h11 = self.addHost('h11', ip='172.17.16.4/24', defaultRoute='via 172.17.16.1')
	h12 = self.addHost('h12', ip='10.0.0.2/25', defaultRoute='via 10.0.0.1')
	h13 = self.addHost('h13', ip='10.0.0.3/25', defaultRoute='via 10.0.0.1')
	h14 = self.addHost('h14', ip='10.0.0.4/25', defaultRoute='via 10.0.0.1')
	h15 = self.addHost('h15', ip='10.0.0.130/25', defaultRoute='via 10.0.0.129')
	h16 = self.addHost('h16', ip='10.0.0.131/25', defaultRoute='via 10.0.0.129')
	h17 = self.addHost('h17', ip='10.0.0.132/25', defaultRoute='via 10.0.0.129')
	h18 = self.addHost('h18', ip='20.0.0.2/25', defaultRoute='via 20.0.0.1')    
	h19 = self.addHost('h19', ip='20.0.0.3/25', defaultRoute='via 20.0.0.1')    
	h20 = self.addHost('h20', ip='20.0.0.4/25', defaultRoute='via 20.0.0.1')    
	h21 = self.addHost('h21', ip='20.0.0.130/25', defaultRoute='via 20.0.0.129')
	h22 = self.addHost('h22', ip='20.0.0.131/25', defaultRoute='via 20.0.0.129')
	h23 = self.addHost('h23', ip='20.0.0.132/25', defaultRoute='via 20.0.0.129')


	# Add links

	self.addLink(r1,s4, intfName1='r1-eth1', addr1='02:00:DE:AD:BE:11', params1={'ip' : '172.17.16.1/24'})
 	self.addLink(r2,s5, intfName1='r2-eth1', addr1='02:00:DE:AD:BE:21', params1={'ip' : '10.0.0.1/25'})
	self.addLink(r3,s7, intfName1='r3-eth1', addr1='02:00:DE:AD:BE:31', params1={'ip' : '20.0.0.1/25'})
 	self.addLink(r2,s6, intfName1='r2-eth2', addr1='02:00:DE:AD:BE:22', params1={'ip' : '10.0.0.129/25'})
	self.addLink(r3,s8, intfName1='r3-eth2', addr1='02:00:DE:AD:BE:32', params1={'ip' : '20.0.0.129/25'})
 	self.addLink(r1,r2, intfName1='r1-eth2', addr1='02:00:DE:AD:BE:12', params1={'ip' : '192.168.0.1/30'}, intfName2='r2-eth3', addr2='02:00:DE:AD:BE:23', params2={'ip' : '192.168.0.2/30'})
	self.addLink(r1,r3, intfName1='r1-eth3', addr1='02:00:DE:AD:BE:13', params1={'ip' : '192.168.0.5/30'}, intfName2='r3-eth3', addr2='02:00:DE:AD:BE:33', params2={'ip' : '192.168.0.6/30'})
	self.addLink(s4,h9)
	self.addLink(s4,h10)
	self.addLink(s4,h11)
	self.addLink(s5,h12)
	self.addLink(s5,h13)
	self.addLink(s5,h14)
	self.addLink(s6,h15)
	self.addLink(s6,h16)
	self.addLink(s6,h17)
	self.addLink(s7,h18)
	self.addLink(s7,h19)
	self.addLink(s7,h20)
	self.addLink(s8,h21)
	self.addLink(s8,h22)
	self.addLink(s8,h23)
 
  #set MAC 
"""
 	r1.intf('r1-eth1').setMAC('02:00:DE:AD:BE:11')
	r1.intf('r1-eth2').setMAC('02:00:DE:AD:BE:12')
	r1.intf('r1-eth3').setMAC('02:00:DE:AD:BE:13')
	
	r2.intf('r2-eth1').setMAC('02:00:DE:AD:BE:21')
	r2.intf('r2-eth2').setMAC('02:00:DE:AD:BE:22')
	r2.intf('r2-eth3').setMAC('02:00:DE:AD:BE:23')
	
	r3.intf('r3-eth1').setMAC('02:00:DE:AD:BE:31')
	r3.intf('r3-eth2').setMAC('02:00:DE:AD:BE:32')
	r3.intf('r3-eth3').setMAC('02:00:DE:AD:BE:33') 
 'ip' : '172.17.16.1/24',
  
"""



topos = { 'mytopo':(lambda:MyTopo())}