
#include "ns3/applications-module.h"
#include "ns3/core-module.h"
#include "ns3/csma-module.h"
#include "ns3/internet-module.h"
#include "ns3/mobility-module.h"
#include "ns3/network-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/ssid.h"
#include "ns3/yans-wifi-helper.h"


using namespace ns3;

NS_LOG_COMPONENT_DEFINE("ThirdScriptExample");

int
main(int argc, char* argv[])
{
    bool verbose = true;
    uint32_t nWifi = 5;
    bool tracing = true;

    CommandLine cmd(__FILE__);
    cmd.AddValue("nWifi", "Number of wifi STA devices", nWifi);
    cmd.AddValue("verbose", "Tell echo applications to log if true", verbose);
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

    if (verbose)
    {
        LogComponentEnable("UdpEchoClientApplication", LOG_LEVEL_INFO);
        LogComponentEnable("UdpEchoServerApplication", LOG_LEVEL_INFO);
    }

    NodeContainer WiFiNodes;
    WiFiNodes.Create(nWifi);

    YansWifiChannelHelper channel = YansWifiChannelHelper::Default();
    YansWifiPhyHelper phy;
    phy.SetChannel(channel.Create());

    WifiMacHelper mac;
    

    WifiHelper wifi;
    NetDeviceContainer WiFiDevices;
    mac.SetType("ns3::AdhocWifiMac");
    WiFiDevices = wifi.Install(phy, mac, WiFiNodes);
    mac.SetType("ns3::AdhocWifiMac", "RtsCtsThreshold", UintegerValue(1000),"ShortGuardEnabled", BooleanValue(true));

    MobilityHelper mobility;

    mobility.SetPositionAllocator("ns3::GridPositionAllocator",
                                  "MinX",
                                  DoubleValue(0.0),
               "ShortGuardEnabled", BooleanValue(true)                   "MinY",
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
    mobility.Install(WiFiNodes);

    
    //mobility.SetMobilityModel("ns3::ConstantPositionMobilityModel");
    //mobility.Install(WiFiNodes);

    InternetStackHelper stack;
    stack.Install(WiFiNodes);

    Ipv4AddressHelper address;

    address.SetBase("192.168.1.0", "255.255.255.0");
    Ipv4InterfaceContainer WiFiInterfaces;
    WiFiInterfaces = address.Assign(WiFiDevices);

    UdpEchoServerHelper echoServer(20);

    ApplicationContainer serverApps = echoServer.Install(WiFiNodes.Get(0));
    serverApps.Start(Seconds(1.0));
    serverApps.Stop(Seconds(10.0));

    UdpEchoClientHelper echoClient1(WiFiInterfaces.GetAddress(0), 20);
    echoClient1.SetAttribute("MaxPackets", UintegerValue(2));
    echoClient1.SetAttribute("Interval", TimeValue(Seconds(1.0)));
    echoClient1.SetAttribute("PacketSize", UintegerValue(512));

    ApplicationContainer clientApps1 = echoClient1.Install(WiFiNodes.Get(3));
    clientApps1.Start(Seconds(3.0));
    clientApps1.Stop(Seconds(5.0));
    
    UdpEchoClientHelper echoClient2(WiFiInterfaces.GetAddress(0), 20);
    echoClient2.SetAttribute("MaxPackets", UintegerValue(2));
    echoClient2.SetAttribute("Interval", TimeValue(Seconds(2.0)));
    echoClient2.SetAttribute("PacketSize", UintegerValue(512));

    ApplicationContainer clientApps2 = echoClient2.Install(WiFiNodes.Get(4));
    clientApps2.Start(Seconds(2.0));
    clientApps2.Stop(Seconds(6.0));

    Ipv4GlobalRoutingHelper::PopulateRoutingTables();

    Simulator::Stop(Seconds(10.0));

    if (tracing)
    {
        phy.SetPcapDataLinkType(WifiPhyHelper::DLT_IEEE802_11_RADIO);
        phy.EnablePcap("third3.1", WiFiDevices.Get(1));

    }

    Simulator::Run();
    Simulator::Destroy();
    return 0;
}