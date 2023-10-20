#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/mobility-module.h"
#include "ns3/wifi-module.h"
#include "ns3/applications-module.h"

using namespace ns3;

int main (int argc, char *argv[])
{
  // Command line arguments
  CommandLine cmd;
  cmd.Parse (argc, argv);

  // Create nodes
  NodeContainer nodes;
  nodes.Create(5);

  // Mobility model
  MobilityHelper mobility;
  mobility.SetPositionAllocator("ns3::RandomRectanglePositionAllocator",
                                "X", StringValue("ns3::UniformRandomVariable[Min=-90|Max=90]"),
                                "Y", StringValue("ns3::UniformRandomVariable[Min=-90|Max=90]"));
  mobility.SetMobilityModel("ns3::RandomWalk2dMobilityModel",
                            "Bounds", RectangleValue(Rectangle(-90, 90, -90, 90)));
  mobility.Install(nodes);

  // Wifi setup
  WifiHelper wifi;
  wifi.SetStandard(WIFI_PHY_STANDARD_80211ac);
  wifi.SetRemoteStationManager("ns3::ConstantRateWifiManager",
                               "DataMode", StringValue("HtMcs0"));
  WifiMacHelper wifiMac;
  wifiMac.SetType("ns3::AdhocWifiMac");
  NetDeviceContainer devices = wifi.Install(wifiMac, nodes);

  // Internet stack
  InternetStackHelper internet;
  internet.Install(nodes);

  Ipv4AddressHelper ipv4;
  ipv4.SetBase("192.168.1.0", "255.255.255.0");
  Ipv4InterfaceContainer interfaces = ipv4.Assign(devices);

  // Application setup
  UdpEchoServerHelper echoServer(20);
  ApplicationContainer serverApps = echoServer.Install(nodes.Get(0));
  serverApps.Start(Seconds(0.0));
  serverApps.Stop(Seconds(10.0));

  UdpEchoClientHelper echoClient("192.168.1.1", 20);
  echoClient.SetAttribute("MaxPackets", UintegerValue(2));
  echoClient.SetAttribute("Interval", TimeValue(Seconds(1.0)));
  echoClient.SetAttribute("PacketSize", UintegerValue(512));

  ApplicationContainer clientApps1 = echoClient.Install(nodes.Get(3));
  clientApps1.Start(Seconds(1.0));
  clientApps1.Stop(Seconds(3.0));

  ApplicationContainer clientApps2 = echoClient.Install(nodes.Get(4));
  clientApps2.Start(Seconds(2.0));
  clientApps2.Stop(Seconds(6.0));

  // Packet Tracer setup
  PacketSinkHelper packetSinkHelper("ns3::UdpSocketFactory", Address(InetSocketAddress(interfaces.GetAddress(1), 20)));
  ApplicationContainer sinkApps = packetSinkHelper.Install(nodes.Get(1));

  // Tracing
  AsciiTraceHelper ascii;
  wifi.EnableLogComponents();
  wifi.EnablePcapAll("ad_hoc_wifi");

  // Run simulation
  Simulator::Stop(Seconds(10.0));
  Simulator::Run();
  Simulator::Destroy();

  return 0;
}
