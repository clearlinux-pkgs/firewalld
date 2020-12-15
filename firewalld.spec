#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : firewalld
Version  : 0.7.2
Release  : 16
URL      : https://github.com/firewalld/firewalld/releases/download/v0.7.2/firewalld-0.7.2.tar.gz
Source0  : https://github.com/firewalld/firewalld/releases/download/v0.7.2/firewalld-0.7.2.tar.gz
Summary  : Firewall daemon with D-Bus interface
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: firewalld-bin = %{version}-%{release}
Requires: firewalld-data = %{version}-%{release}
Requires: firewalld-license = %{version}-%{release}
Requires: firewalld-locales = %{version}-%{release}
Requires: firewalld-man = %{version}-%{release}
Requires: firewalld-python = %{version}-%{release}
Requires: firewalld-python3 = %{version}-%{release}
Requires: firewalld-services = %{version}-%{release}
Requires: dbus-python
Requires: pygobject
Requires: python-slip
BuildRequires : dbus-python
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : glib-dev
BuildRequires : grep
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : ipset
BuildRequires : iptables
BuildRequires : libxml2-dev
BuildRequires : libxslt
BuildRequires : libxslt-bin
BuildRequires : nftables
BuildRequires : perl(XML::Parser)
BuildRequires : pygobject
BuildRequires : python-slip
BuildRequires : sed

%description
firewalld is a firewall service daemon that provides a dynamic customizable 
firewall with a D-Bus interface.

%package bin
Summary: bin components for the firewalld package.
Group: Binaries
Requires: firewalld-data = %{version}-%{release}
Requires: firewalld-license = %{version}-%{release}
Requires: firewalld-services = %{version}-%{release}

%description bin
bin components for the firewalld package.


%package data
Summary: data components for the firewalld package.
Group: Data

%description data
data components for the firewalld package.


%package license
Summary: license components for the firewalld package.
Group: Default

%description license
license components for the firewalld package.


%package locales
Summary: locales components for the firewalld package.
Group: Default

%description locales
locales components for the firewalld package.


%package man
Summary: man components for the firewalld package.
Group: Default

%description man
man components for the firewalld package.


%package python
Summary: python components for the firewalld package.
Group: Default
Requires: firewalld-python3 = %{version}-%{release}

%description python
python components for the firewalld package.


%package python3
Summary: python3 components for the firewalld package.
Group: Default
Requires: python3-core

%description python3
python3 components for the firewalld package.


%package services
Summary: services components for the firewalld package.
Group: Systemd services

%description services
services components for the firewalld package.


%prep
%setup -q -n firewalld-0.7.2
cd %{_builddir}/firewalld-0.7.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582923116
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --with-xml-catalog=/usr/share/defaults/xml/catalog
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1582923116
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/firewalld
cp %{_builddir}/firewalld-0.7.2/COPYING %{buildroot}/usr/share/package-licenses/firewalld/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install
%find_lang firewalld

%files
%defattr(-,root,root,-)
/usr/lib/firewalld/helpers/Q.931.xml
/usr/lib/firewalld/helpers/RAS.xml
/usr/lib/firewalld/helpers/amanda.xml
/usr/lib/firewalld/helpers/ftp.xml
/usr/lib/firewalld/helpers/h323.xml
/usr/lib/firewalld/helpers/irc.xml
/usr/lib/firewalld/helpers/netbios-ns.xml
/usr/lib/firewalld/helpers/pptp.xml
/usr/lib/firewalld/helpers/proto-gre.xml
/usr/lib/firewalld/helpers/sane.xml
/usr/lib/firewalld/helpers/sip.xml
/usr/lib/firewalld/helpers/snmp.xml
/usr/lib/firewalld/helpers/tftp.xml
/usr/lib/firewalld/icmptypes/address-unreachable.xml
/usr/lib/firewalld/icmptypes/bad-header.xml
/usr/lib/firewalld/icmptypes/beyond-scope.xml
/usr/lib/firewalld/icmptypes/communication-prohibited.xml
/usr/lib/firewalld/icmptypes/destination-unreachable.xml
/usr/lib/firewalld/icmptypes/echo-reply.xml
/usr/lib/firewalld/icmptypes/echo-request.xml
/usr/lib/firewalld/icmptypes/failed-policy.xml
/usr/lib/firewalld/icmptypes/fragmentation-needed.xml
/usr/lib/firewalld/icmptypes/host-precedence-violation.xml
/usr/lib/firewalld/icmptypes/host-prohibited.xml
/usr/lib/firewalld/icmptypes/host-redirect.xml
/usr/lib/firewalld/icmptypes/host-unknown.xml
/usr/lib/firewalld/icmptypes/host-unreachable.xml
/usr/lib/firewalld/icmptypes/ip-header-bad.xml
/usr/lib/firewalld/icmptypes/neighbour-advertisement.xml
/usr/lib/firewalld/icmptypes/neighbour-solicitation.xml
/usr/lib/firewalld/icmptypes/network-prohibited.xml
/usr/lib/firewalld/icmptypes/network-redirect.xml
/usr/lib/firewalld/icmptypes/network-unknown.xml
/usr/lib/firewalld/icmptypes/network-unreachable.xml
/usr/lib/firewalld/icmptypes/no-route.xml
/usr/lib/firewalld/icmptypes/packet-too-big.xml
/usr/lib/firewalld/icmptypes/parameter-problem.xml
/usr/lib/firewalld/icmptypes/port-unreachable.xml
/usr/lib/firewalld/icmptypes/precedence-cutoff.xml
/usr/lib/firewalld/icmptypes/protocol-unreachable.xml
/usr/lib/firewalld/icmptypes/redirect.xml
/usr/lib/firewalld/icmptypes/reject-route.xml
/usr/lib/firewalld/icmptypes/required-option-missing.xml
/usr/lib/firewalld/icmptypes/router-advertisement.xml
/usr/lib/firewalld/icmptypes/router-solicitation.xml
/usr/lib/firewalld/icmptypes/source-quench.xml
/usr/lib/firewalld/icmptypes/source-route-failed.xml
/usr/lib/firewalld/icmptypes/time-exceeded.xml
/usr/lib/firewalld/icmptypes/timestamp-reply.xml
/usr/lib/firewalld/icmptypes/timestamp-request.xml
/usr/lib/firewalld/icmptypes/tos-host-redirect.xml
/usr/lib/firewalld/icmptypes/tos-host-unreachable.xml
/usr/lib/firewalld/icmptypes/tos-network-redirect.xml
/usr/lib/firewalld/icmptypes/tos-network-unreachable.xml
/usr/lib/firewalld/icmptypes/ttl-zero-during-reassembly.xml
/usr/lib/firewalld/icmptypes/ttl-zero-during-transit.xml
/usr/lib/firewalld/icmptypes/unknown-header-type.xml
/usr/lib/firewalld/icmptypes/unknown-option.xml
/usr/lib/firewalld/ipsets/README
/usr/lib/firewalld/services/RH-Satellite-6.xml
/usr/lib/firewalld/services/amanda-client.xml
/usr/lib/firewalld/services/amanda-k5-client.xml
/usr/lib/firewalld/services/amqp.xml
/usr/lib/firewalld/services/amqps.xml
/usr/lib/firewalld/services/apcupsd.xml
/usr/lib/firewalld/services/audit.xml
/usr/lib/firewalld/services/bacula-client.xml
/usr/lib/firewalld/services/bacula.xml
/usr/lib/firewalld/services/bb.xml
/usr/lib/firewalld/services/bgp.xml
/usr/lib/firewalld/services/bitcoin-rpc.xml
/usr/lib/firewalld/services/bitcoin-testnet-rpc.xml
/usr/lib/firewalld/services/bitcoin-testnet.xml
/usr/lib/firewalld/services/bitcoin.xml
/usr/lib/firewalld/services/bittorrent-lsd.xml
/usr/lib/firewalld/services/ceph-mon.xml
/usr/lib/firewalld/services/ceph.xml
/usr/lib/firewalld/services/cfengine.xml
/usr/lib/firewalld/services/cockpit.xml
/usr/lib/firewalld/services/condor-collector.xml
/usr/lib/firewalld/services/ctdb.xml
/usr/lib/firewalld/services/dhcp.xml
/usr/lib/firewalld/services/dhcpv6-client.xml
/usr/lib/firewalld/services/dhcpv6.xml
/usr/lib/firewalld/services/distcc.xml
/usr/lib/firewalld/services/dns-over-tls.xml
/usr/lib/firewalld/services/dns.xml
/usr/lib/firewalld/services/docker-registry.xml
/usr/lib/firewalld/services/docker-swarm.xml
/usr/lib/firewalld/services/dropbox-lansync.xml
/usr/lib/firewalld/services/elasticsearch.xml
/usr/lib/firewalld/services/etcd-client.xml
/usr/lib/firewalld/services/etcd-server.xml
/usr/lib/firewalld/services/finger.xml
/usr/lib/firewalld/services/freeipa-4.xml
/usr/lib/firewalld/services/freeipa-ldap.xml
/usr/lib/firewalld/services/freeipa-ldaps.xml
/usr/lib/firewalld/services/freeipa-replication.xml
/usr/lib/firewalld/services/freeipa-trust.xml
/usr/lib/firewalld/services/ftp.xml
/usr/lib/firewalld/services/ganglia-client.xml
/usr/lib/firewalld/services/ganglia-master.xml
/usr/lib/firewalld/services/git.xml
/usr/lib/firewalld/services/grafana.xml
/usr/lib/firewalld/services/gre.xml
/usr/lib/firewalld/services/high-availability.xml
/usr/lib/firewalld/services/http.xml
/usr/lib/firewalld/services/https.xml
/usr/lib/firewalld/services/imap.xml
/usr/lib/firewalld/services/imaps.xml
/usr/lib/firewalld/services/ipp-client.xml
/usr/lib/firewalld/services/ipp.xml
/usr/lib/firewalld/services/ipsec.xml
/usr/lib/firewalld/services/irc.xml
/usr/lib/firewalld/services/ircs.xml
/usr/lib/firewalld/services/iscsi-target.xml
/usr/lib/firewalld/services/isns.xml
/usr/lib/firewalld/services/jenkins.xml
/usr/lib/firewalld/services/kadmin.xml
/usr/lib/firewalld/services/kdeconnect.xml
/usr/lib/firewalld/services/kerberos.xml
/usr/lib/firewalld/services/kibana.xml
/usr/lib/firewalld/services/klogin.xml
/usr/lib/firewalld/services/kpasswd.xml
/usr/lib/firewalld/services/kprop.xml
/usr/lib/firewalld/services/kshell.xml
/usr/lib/firewalld/services/ldap.xml
/usr/lib/firewalld/services/ldaps.xml
/usr/lib/firewalld/services/libvirt-tls.xml
/usr/lib/firewalld/services/libvirt.xml
/usr/lib/firewalld/services/lightning-network.xml
/usr/lib/firewalld/services/llmnr.xml
/usr/lib/firewalld/services/managesieve.xml
/usr/lib/firewalld/services/matrix.xml
/usr/lib/firewalld/services/mdns.xml
/usr/lib/firewalld/services/memcache.xml
/usr/lib/firewalld/services/minidlna.xml
/usr/lib/firewalld/services/mongodb.xml
/usr/lib/firewalld/services/mosh.xml
/usr/lib/firewalld/services/mountd.xml
/usr/lib/firewalld/services/mqtt-tls.xml
/usr/lib/firewalld/services/mqtt.xml
/usr/lib/firewalld/services/ms-wbt.xml
/usr/lib/firewalld/services/mssql.xml
/usr/lib/firewalld/services/murmur.xml
/usr/lib/firewalld/services/mysql.xml
/usr/lib/firewalld/services/nfs.xml
/usr/lib/firewalld/services/nfs3.xml
/usr/lib/firewalld/services/nmea-0183.xml
/usr/lib/firewalld/services/nrpe.xml
/usr/lib/firewalld/services/ntp.xml
/usr/lib/firewalld/services/nut.xml
/usr/lib/firewalld/services/openvpn.xml
/usr/lib/firewalld/services/ovirt-imageio.xml
/usr/lib/firewalld/services/ovirt-storageconsole.xml
/usr/lib/firewalld/services/ovirt-vmconsole.xml
/usr/lib/firewalld/services/plex.xml
/usr/lib/firewalld/services/pmcd.xml
/usr/lib/firewalld/services/pmproxy.xml
/usr/lib/firewalld/services/pmwebapi.xml
/usr/lib/firewalld/services/pmwebapis.xml
/usr/lib/firewalld/services/pop3.xml
/usr/lib/firewalld/services/pop3s.xml
/usr/lib/firewalld/services/postgresql.xml
/usr/lib/firewalld/services/privoxy.xml
/usr/lib/firewalld/services/prometheus.xml
/usr/lib/firewalld/services/proxy-dhcp.xml
/usr/lib/firewalld/services/ptp.xml
/usr/lib/firewalld/services/pulseaudio.xml
/usr/lib/firewalld/services/puppetmaster.xml
/usr/lib/firewalld/services/quassel.xml
/usr/lib/firewalld/services/radius.xml
/usr/lib/firewalld/services/rdp.xml
/usr/lib/firewalld/services/redis-sentinel.xml
/usr/lib/firewalld/services/redis.xml
/usr/lib/firewalld/services/rpc-bind.xml
/usr/lib/firewalld/services/rsh.xml
/usr/lib/firewalld/services/rsyncd.xml
/usr/lib/firewalld/services/rtsp.xml
/usr/lib/firewalld/services/salt-master.xml
/usr/lib/firewalld/services/samba-client.xml
/usr/lib/firewalld/services/samba-dc.xml
/usr/lib/firewalld/services/samba.xml
/usr/lib/firewalld/services/sane.xml
/usr/lib/firewalld/services/sip.xml
/usr/lib/firewalld/services/sips.xml
/usr/lib/firewalld/services/slp.xml
/usr/lib/firewalld/services/smtp-submission.xml
/usr/lib/firewalld/services/smtp.xml
/usr/lib/firewalld/services/smtps.xml
/usr/lib/firewalld/services/snmp.xml
/usr/lib/firewalld/services/snmptrap.xml
/usr/lib/firewalld/services/spideroak-lansync.xml
/usr/lib/firewalld/services/spotify-sync.xml
/usr/lib/firewalld/services/squid.xml
/usr/lib/firewalld/services/ssdp.xml
/usr/lib/firewalld/services/ssh.xml
/usr/lib/firewalld/services/steam-streaming.xml
/usr/lib/firewalld/services/svdrp.xml
/usr/lib/firewalld/services/svn.xml
/usr/lib/firewalld/services/syncthing-gui.xml
/usr/lib/firewalld/services/syncthing.xml
/usr/lib/firewalld/services/synergy.xml
/usr/lib/firewalld/services/syslog-tls.xml
/usr/lib/firewalld/services/syslog.xml
/usr/lib/firewalld/services/telnet.xml
/usr/lib/firewalld/services/tentacle.xml
/usr/lib/firewalld/services/tftp-client.xml
/usr/lib/firewalld/services/tftp.xml
/usr/lib/firewalld/services/tile38.xml
/usr/lib/firewalld/services/tinc.xml
/usr/lib/firewalld/services/tor-socks.xml
/usr/lib/firewalld/services/transmission-client.xml
/usr/lib/firewalld/services/upnp-client.xml
/usr/lib/firewalld/services/vdsm.xml
/usr/lib/firewalld/services/vnc-server.xml
/usr/lib/firewalld/services/wbem-http.xml
/usr/lib/firewalld/services/wbem-https.xml
/usr/lib/firewalld/services/wsman.xml
/usr/lib/firewalld/services/wsmans.xml
/usr/lib/firewalld/services/xdmcp.xml
/usr/lib/firewalld/services/xmpp-bosh.xml
/usr/lib/firewalld/services/xmpp-client.xml
/usr/lib/firewalld/services/xmpp-local.xml
/usr/lib/firewalld/services/xmpp-server.xml
/usr/lib/firewalld/services/zabbix-agent.xml
/usr/lib/firewalld/services/zabbix-server.xml
/usr/lib/firewalld/zones/block.xml
/usr/lib/firewalld/zones/dmz.xml
/usr/lib/firewalld/zones/drop.xml
/usr/lib/firewalld/zones/external.xml
/usr/lib/firewalld/zones/home.xml
/usr/lib/firewalld/zones/internal.xml
/usr/lib/firewalld/zones/public.xml
/usr/lib/firewalld/zones/trusted.xml
/usr/lib/firewalld/zones/work.xml

%files bin
%defattr(-,root,root,-)
/usr/bin/firewall-applet
/usr/bin/firewall-cmd
/usr/bin/firewall-config
/usr/bin/firewall-offline-cmd
/usr/bin/firewalld

%files data
%defattr(-,root,root,-)
/usr/share/applications/firewall-config.desktop
/usr/share/bash-completion/completions/firewall-cmd
/usr/share/dbus-1/system.d/FirewallD.conf
/usr/share/firewalld/firewall-config.glade
/usr/share/firewalld/gtk3_chooserbutton.py
/usr/share/firewalld/gtk3_niceexpander.py
/usr/share/glib-2.0/schemas/org.fedoraproject.FirewallConfig.gschema.xml
/usr/share/icons/hicolor/16x16/apps/firewall-applet-error.png
/usr/share/icons/hicolor/16x16/apps/firewall-applet-panic.png
/usr/share/icons/hicolor/16x16/apps/firewall-applet.png
/usr/share/icons/hicolor/16x16/apps/firewall-config.png
/usr/share/icons/hicolor/22x22/apps/firewall-applet-error.png
/usr/share/icons/hicolor/22x22/apps/firewall-applet-panic.png
/usr/share/icons/hicolor/22x22/apps/firewall-applet.png
/usr/share/icons/hicolor/22x22/apps/firewall-config.png
/usr/share/icons/hicolor/24x24/apps/firewall-applet-error.png
/usr/share/icons/hicolor/24x24/apps/firewall-applet-panic.png
/usr/share/icons/hicolor/24x24/apps/firewall-applet.png
/usr/share/icons/hicolor/24x24/apps/firewall-config.png
/usr/share/icons/hicolor/32x32/apps/firewall-applet-error.png
/usr/share/icons/hicolor/32x32/apps/firewall-applet-panic.png
/usr/share/icons/hicolor/32x32/apps/firewall-applet.png
/usr/share/icons/hicolor/32x32/apps/firewall-config.png
/usr/share/icons/hicolor/48x48/apps/firewall-applet-error.png
/usr/share/icons/hicolor/48x48/apps/firewall-applet-panic.png
/usr/share/icons/hicolor/48x48/apps/firewall-applet.png
/usr/share/icons/hicolor/48x48/apps/firewall-config.png
/usr/share/icons/hicolor/scalable/apps/firewall-applet-error.svg
/usr/share/icons/hicolor/scalable/apps/firewall-applet-panic.svg
/usr/share/icons/hicolor/scalable/apps/firewall-applet.svg
/usr/share/icons/hicolor/scalable/apps/firewall-config.svg
/usr/share/metainfo/firewall-config.appdata.xml
/usr/share/polkit-1/actions/org.fedoraproject.FirewallD1.desktop.policy.choice
/usr/share/polkit-1/actions/org.fedoraproject.FirewallD1.policy
/usr/share/polkit-1/actions/org.fedoraproject.FirewallD1.server.policy.choice
/usr/share/zsh/site-functions/_firewalld

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/firewalld/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/firewall-applet.1
/usr/share/man/man1/firewall-cmd.1
/usr/share/man/man1/firewall-config.1
/usr/share/man/man1/firewall-offline-cmd.1
/usr/share/man/man1/firewalld.1
/usr/share/man/man5/firewalld.conf.5
/usr/share/man/man5/firewalld.dbus.5
/usr/share/man/man5/firewalld.direct.5
/usr/share/man/man5/firewalld.helper.5
/usr/share/man/man5/firewalld.icmptype.5
/usr/share/man/man5/firewalld.ipset.5
/usr/share/man/man5/firewalld.lockdown-whitelist.5
/usr/share/man/man5/firewalld.richlanguage.5
/usr/share/man/man5/firewalld.service.5
/usr/share/man/man5/firewalld.zone.5
/usr/share/man/man5/firewalld.zones.5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/firewalld.service

%files locales -f firewalld.lang
%defattr(-,root,root,-)

