#!/usr/bin/python


from mininet.topo import Topo
from mininet.node import RemoteController
from mininet.net  import Mininet
from mininet.link import TCLink
from mininet.log  import setLogLevel
from mininet.util import dumpNodeConnections

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        l1Host = self.addHost( 'h1' )
        l2Host = self.addHost( 'h2' )
        l3Host = self.addHost( 'h3' )
        l4Host = self.addHost( 'h4' )
        l5Host = self.addHost( 'h5' )
        l6Host = self.addHost( 'h6' )
        l7Host = self.addHost( 'h7' )
        l8Host = self.addHost( 'h8' )


        r1Host = self.addHost( 'hr1' )
        r2Host = self.addHost( 'hr2' )
        r3Host = self.addHost( 'hr3' )
        r4Host = self.addHost( 'hr4' )
        r5Host = self.addHost( 'hr5' )
        r6Host = self.addHost( 'hr6' )
        r7Host = self.addHost( 'hr7' )
        r8Host = self.addHost( 'hr8' )


        l11Switch = self.addSwitch( 's1' )
        l12Switch = self.addSwitch( 's2' )
        l13Switch = self.addSwitch( 's3' )
        l14Switch = self.addSwitch( 's4' )
        l15Switch = self.addSwitch( 's5' )
        l16Switch = self.addSwitch( 's6' )
        l17Switch = self.addSwitch( 's7' )
        l18Switch = self.addSwitch( 's8' )

        l21Switch = self.addSwitch( 's21' )
        l22Switch = self.addSwitch( 's22' )
        l23Switch = self.addSwitch( 's23' )
        l24Switch = self.addSwitch( 's24' )
        l25Switch = self.addSwitch( 's25' )
        l26Switch = self.addSwitch( 's26' )
        l27Switch = self.addSwitch( 's27' )
        l28Switch = self.addSwitch( 's28' )


        l31Switch = self.addSwitch( 's31' )
        l32Switch = self.addSwitch( 's32' )
        l33Switch = self.addSwitch( 's33' )
        l34Switch = self.addSwitch( 's44' )

        # Add links
        self.addLink( l11Switch, l21Switch, bw=100)
        self.addLink( l11Switch, l22Switch, bw=100)
        self.addLink( l12Switch, l21Switch, bw=100)
        self.addLink( l12Switch, l22Switch, bw=100)
        self.addLink( l13Switch, l23Switch, bw=100)
        self.addLink( l13Switch, l24Switch, bw=100)
        self.addLink( l14Switch, l23Switch, bw=100)
        self.addLink( l14Switch, l24Switch, bw=100)
        self.addLink( l15Switch, l25Switch, bw=100)
        self.addLink( l15Switch, l26Switch, bw=100)
        self.addLink( l16Switch, l25Switch, bw=100)
        self.addLink( l16Switch, l26Switch, bw=100)
        self.addLink( l17Switch, l27Switch, bw=100)
        self.addLink( l17Switch, l28Switch, bw=100)
        self.addLink( l18Switch, l27Switch, bw=100)
        self.addLink( l18Switch, l28Switch, bw=100)


        self.addLink( l1Host, l11Switch, bw=100)
        self.addLink( l2Host, l11Switch, bw=100)
        self.addLink( l3Host, l12Switch, bw=100)
        self.addLink( l4Host, l12Switch, bw=100)
        self.addLink( l5Host, l13Switch, bw=100)
        self.addLink( l6Host, l13Switch, bw=100)
        self.addLink( l7Host, l14Switch, bw=100)
        self.addLink( l8Host, l14Switch, bw=100)
        self.addLink( r8Host, l15Switch, bw=100)
        self.addLink( r7Host, l15Switch, bw=100)
        self.addLink( r6Host, l16Switch, bw=100)
        self.addLink( r5Host, l16Switch, bw=100)
        self.addLink( r4Host, l17Switch, bw=100)
        self.addLink( r3Host, l17Switch, bw=100)
        self.addLink( r2Host, l18Switch, bw=100)
        self.addLink( r1Host, l18Switch, bw=100)

        self.addLink( l31Switch, l21Switch, bw=1000,loss=5)
        self.addLink( l31Switch, l23Switch, bw=1000,loss=5)
        self.addLink( l31Switch, l25Switch, bw=1000,loss=5)
        self.addLink( l31Switch, l27Switch, bw=1000,loss=5)
        self.addLink( l32Switch, l21Switch, bw=1000,loss=5)
        self.addLink( l32Switch, l23Switch, bw=1000,loss=5)
        self.addLink( l32Switch, l25Switch, bw=1000,loss=5)
        self.addLink( l32Switch, l27Switch, bw=1000,loss=5)

        self.addLink( l33Switch, l22Switch, bw=1000,loss=5)
        self.addLink( l33Switch, l24Switch, bw=1000,loss=5)
        self.addLink( l33Switch, l26Switch, bw=1000,loss=5)
        self.addLink( l33Switch, l28Switch, bw=1000,loss=5)
        self.addLink( l34Switch, l22Switch, bw=1000,loss=5)
        self.addLink( l34Switch, l24Switch, bw=1000,loss=5)
        self.addLink( l34Switch, l26Switch, bw=1000,loss=5)
        self.addLink( l34Switch, l28Switch, bw=1000,loss=5)
		
topos = { 'mytopo': ( lambda: MyTopo() ) }



def perfTest():
		topo = MyTopo()
		net = Mininet(topo =topo , link=TCLink)
	
		net.start()
		net.addController('floodlight',controller=RemoteController,ip='127.0.0.1')
	
		print"Dumping host connection";
		dumpNodeConnections(net.hosts);
		print "Test network connectivity"
		net.pingAll()
	

	
if __name__=='__main__':
		setLogLevel('info')
		perfTest()
	
