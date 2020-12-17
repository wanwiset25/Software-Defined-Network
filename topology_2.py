"""
Three devices on different networks and all connected by a single router

	host --- router ---- host
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
	Your topology file for scenario 2. Define all the required devices here.
	"""
	# Add hosts and switches
	r1 = self.addNode('r1', ip='10.0.0.1/24')
	h1 = self.addHost('h1', ip='10.0.0.2/24', defaultRoute='via 10.0.0.1')
	h2 = self.addHost('h2', ip='20.0.0.2/24', defaultRoute='via 20.0.0.1')
	h3 = self.addHost('h3', ip='30.0.0.2/24', defaultRoute='via 30.0.0.1')
	
	# Add links
	self.addLink(r1,h1, intfName1='r1-eth1', addr1='02:00:DE:AD:BE:11', params1={'ip' : '10.0.0.1/24'})
	self.addLink(r1,h2, intfName1='r1-eth2', addr1='02:00:DE:AD:BE:12', params1={'ip' : '20.0.0.1/24'})
	self.addLink(r1,h3, intfName1='r1-eth3', addr1='02:00:DE:AD:BE:13', params1={'ip' : '30.0.0.1/24'})

topos = { 'mytopo':(lambda:MyTopo())}