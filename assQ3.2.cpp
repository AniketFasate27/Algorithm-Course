/*
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

#include "ns3/applications-module.h"
#include "ns3/core-module.h"
#include "ns3/csma-module.h"
#include "ns3/internet-module.h"
#include "ns3/mobility-module.h"
#include "ns3/network-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/ssid.h"
#include "ns3/yans-wifi-helper.//h"

// Default Network Topology
//
//   Wifi 10.1.3.0
//                 AP
//  *    *    *    *
//  |    |    |    |    10.1.1.0
// n5   n6   n7   n0 -------------- n1   n2   n3   n4
//                   point-to-point  |    |    |    |
//                                   ================
//                                     LAN 10.1.2.0

using namespace ns3;

NS_LOG_COMPONENT_DEFINE("ThirdScriptExample");

int
main(int argc, char* argv[])
{
    // bool verbose = true;
    // uint32_t nCsma = 3;
    uint32_t nWifi = 5;
    bool tracing = false;

    CommandLine cmd(__FILE__);
    // cmd.AddValue("nCsma", "Number of \"extra\" CSMA nodes/devices", nCsma);
    cmd.AddValue("nWifi", "Number of wifi STA devices", nWifi);
    // cmd.AddValue("verbose", "Tell echo applications to log if true", verbose);
    cmd.AddValue("tracing", "Enable pcap tracing", tracing);

    cmd.Parse(argc, argv);

    // The underlying restriction of 18 is due to the grid position
    // allocator's configuration; the grid layout will exceed the
    // bounding box if more than 18 nodes are provided.
    if (nWifi > 18)
    {
        std::cout << "nWifi should be 18 or less; otherwise grid layout exceeds the bounding box"
                  << std::endl;
        return 1;
    }

    // if (verbose)
    // {
    //     LogComponentEnable("UdpEchoClientApplication", LOG_LEVEL_INFO);
    //     LogComponentEnable("UdpEchoServerApplication", LOG_LEVEL_INFO);
    // }

    // NodeContainer p2pNodes;
    // p2pNodes.Create(1);

    // PointToPointHelper pointToPoint;
    // pointToPoint.SetDeviceAttribute("DataRate", StringValue("5Mbps"));
    // pointToPoint.SetChannelAttribute("Delay", StringValue("2ms"));

    // NetDeviceContainer p2pDevices;
    // p2pDevices = pointToPoint.Install(p2pNodes);

    // NodeContainer csmaNodes;
    // csmaNodes.Add(p2pNodes.Get(1));
    // csmaNodes.Create(nCsma);

    // CsmaHelper csma;
    // csma.SetChannelAttribute("DataRate", StringValue("100Mbps"));
    // csma.SetChannelAttribute("Delay", TimeValue(NanoSeconds(6560)));

    // NetDeviceContainer csmaDevices;
    // csmaDevices = csma.Install(csmaNodes);

    NodeContainer APwifiNode;
    APwifiNode.Create(1);

    NodeContainer wifistaNodes;
    wifistaNodes.Create(nWifi);
    // NodeContainer wifiApNode = p2pNodes.Get(0);

    YansWifiChannelHelper channel = YansWifiChannelHelper::Default();
    YansWifiPhyHelper phy;
    phy.SetChannel(channel.Create());

    WifiMacHelper mac;
    Ssid ssid = Ssid("EECE5155");

    WifiHelper wifi;

    NetDeviceContainer staDevices;
    mac.SetType("ns3::StaWifiMac", "Ssid", SsidValue(ssid), "ActiveProbing", BooleanValue(false));
    staDevices = wifi.Install(phy, mac, wifistaNodes);

    NetDeviceContainer apDevices;
    mac.SetType("ns3::ApWifiMac", "Ssid", SsidValue(ssid));
    apDevices = wifi.Install(phy, mac, APwifiNode);

    MobilityHelper mobility;

    mobility.SetPositionAllocator("ns3::GridPositionAllocator",
                                  "MinX",
                                  DoubleValue(0.0),
                                  "MinY",
                                  DoubleValue(0.0),
                                  "DeltaX",
                                  DoubleValue(5.0),
                                  "DeltaY",
                                  DoubleValue(10.0),
                                  "GridWidth",
                                  UintegerValue(3),
                                  "LayoutType",
                                  StringValue("RowFirst"));

    mobility.SetMobilityModel("ns3::RandomWalk2dMobilityModel",
                              "Bounds",
                              RectangleValue(Rectangle(-90, 90, -90, 90)));
    mobility.Install(wifistaNodes);

    // mobility.SetMobilityModel("ns3::ConstantPositionMobilityModel");
    // mobility.Install(wifiApNode);

    InternetStackHelper stack;
    // stack.Install(csmaNodes);
    stack.Install(APwifiNode);
    stack.Install(wifistaNodes);

    Ipv4AddressHelper address;

    address.SetBase("192.168.2.0", "255.255.255.0");
    Ipv4InterfaceContainer staInterfaces;
    staInterfaces = address.Assign(staDevices);
    Ipv4InterfaceContainer APInterfaces;
    APInterfaces = address.Assign(apDevices);
    


    // address.SetBase("10.1.2.0", "255.255.255.0");
    // Ipv4InterfaceContainer csmaInterfaces;
    // csmaInterfaces = address.Assign(csmaDevices);

    // address.SetBase("192.168.2.0", "255.255.255.0");
    // address.Assign(staDevices);
    // address.Assign(apDevices);

    UdpEchoServerHelper echoServer(21);

    ApplicationContainer serverApps = echoServer.Install(wifistaNodes.Get(0));
    serverApps.Start(Seconds(1.0));
    serverApps.Stop(Seconds(10.0));

    UdpEchoClientHelper echoClient1(staInterfaces.GetAddress(0), 21);
    echoClient1.SetAttribute("MaxPackets", UintegerValue(2));
    echoClient1.SetAttribute("Interval", TimeValue(Seconds(2.0)));
    echoClient1.SetAttribute("PacketSize", UintegerValue(512));
    ApplicationContainer clientApps3 = echoClient1.Install(wifistaNodes.Get(3));
    clientApps3.Start(Seconds(3.0));
    clientApps3.Stop(Seconds(5.0));

    UdpEchoClientHelper echoClient2(staInterfaces.GetAddress(0), 21);
    echoClient2.SetAttribute("MaxPackets", UintegerValue(2));
    echoClient2.SetAttribute("Interval", TimeValue(Seconds(2.0)));
    echoClient2.SetAttribute("PacketSize", UintegerValue(512));
    
    ApplicationContainer clientApps4 = echoClient2.Install(wifistaNodes.Get(4));
    clientApps4.Start(Seconds(2.0));
    clientApps4.Stop(Seconds(5.0));



    Ipv4GlobalRoutingHelper::PopulateRoutingTables();

    Simulator::Stop(Seconds(10.0));

    if (tracing)
    {
        phy.SetPcapDataLinkType(WifiPhyHelper::DLT_IEEE802_11_RADIO);
        // pointToPoint.EnablePcapAll("third");
        phy.EnablePcap("third", staDevices.Get(4));
        phy.EnablePcap("third", apDevices.Get(0));

        // csma.EnablePcap("third", csmaDevices.Get(0), true);
    }

    Simulator::Run();
    Simulator::Destroy();
    return 0;
}