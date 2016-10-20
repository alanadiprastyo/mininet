#!/usr/bin/python
# by: Mohammad Riftadi <riftadi@jawdat.com>

from mininet.topo import Topo
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info, error
from mininet.net import Mininet
from mininet.link import Intf
from mininet.util import quietRun
from functools import partial

class MyRingTopo(Topo):
    "Ring topology with 4 switches"

    def __init__(self):
        super(MyRingTopo,self).__init__();

        """
        Following is the topology:
                
                2
            1        3
                4
        
        """

        sw1 = "sw1"
        sw2 = "sw2"
        sw3 = "sw3"
        sw4 = "sw4"

        # add the switches
        self.addSwitch(sw1)
        self.addSwitch(sw2)
        self.addSwitch(sw3)
        self.addSwitch(sw4)

        # add links
        self.addLink(sw1, sw2)
        self.addLink(sw2, sw3)
        self.addLink(sw3, sw4)
        self.addLink(sw4, sw1)

if __name__ == '__main__':
    setLogLevel( 'info' )

    intfName1 = "tap0"
    intfName2 = "veth0"

    info( '*** Creating network\n' )
    net = Mininet( topo=MyRingTopo(), controller=partial( RemoteController, ip='127.0.0.1', port=6633 ) )

    sw1 = net.switches[0]
    sw3 = net.switches[2]

    info( '*** Adding hardware interface', intfName1, 'to switch',
          sw1.name, '\n' )
    _intf = Intf( intfName1, node=sw1 )

    info( '*** Adding hardware interface', intfName2, 'to switch',
          sw3.name, '\n' )
    _intf = Intf( intfName2, node=sw3 )

    net.start()
    CLI( net )
    net.stop()

