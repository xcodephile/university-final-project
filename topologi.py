"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
	server = self.addHost( 'server', ip='192.168.0.1/29' )
	attacker = self.addHost( 'attacker', ip='192.168.0.2/29' )
	victim1 = self.addHost( 'victim1', ip='192.168.0.3/29'  )
        victim2 = self.addHost( 'victim2', ip='192.168.0.4/29' )
        s1 = self.addSwitch( 's1' )

        # Add links
        self.addLink( server, s1 )
        self.addLink( attacker, s1 )
        self.addLink( victim1, s1 )
	self.addLink( victim2, s1 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
