"""
Three devices on same network and all connected by a switch

	host --- switch ---- host
		   		|
		   		|
		   		|
		  	   host

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
	Your topology file for scenario 1. Define all the required devices here.
	"""
	# Add hosts and switches
	s1 = self.addSwitch('s1')
	h1 = self.addHost('h1', ip='10.0.0.2/24', defaultRoute='via 10.0.0.1')
	h2 = self.addHost('h2', ip='10.0.0.3/24', defaultRoute='via 10.0.0.1')
	h3 = self.addHost('h3', ip='10.0.0.4/24', defaultRoute='via 10.0.0.1')
	
	# Add links
	self.addLink(s1,h1)
	self.addLink(s1,h2)
	self.addLink(s1,h3)
	
topos = { 'mytopo':(lambda:MyTopo())}