Summary:        Real-mode video BIOS utility to alter hardware state
Name:		vbetool
Version:	1.2.2
Release:	2
License:        GPL
Group:          System/Configuration/Other
URL:            https://www.srcf.ucam.org/~mjg59/vbetool/
Source:         hhttp://www.codon.org.uk/~mjg59/vbetool/download/vbetool-%{version}.tar.bz2
Patch0:		vbetool_1.1-lz.patch
Patch1:		vbetool-1.2.2-automake-1.13.patch
BuildRequires:  pkgconfig(libpci) 
BuildRequires:  pkgconfig(pciaccess) 
BuildRequires:  pkgconfig(x86) 
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(udev)
BuildRequires:  systemd-rpm-macros
ExclusiveArch:  %{ix86} %{x86_64} %{arm}

%description 
vbetool allows you to run real-mode video BIOS code to alter 
hardware state. It uses lrmi in order to run code from the video BIOS. 
Currently, it is able to alter DPMS states, save/restore video card state
and attempts to initialize the video card from scratch.

%prep
%setup -q
%autopatch -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install
install -m 0644 -D udev-video-post-example.rules $RPM_BUILD_ROOT/%{_udevrulesdir}/92-video-post.rules

%files 
%doc COPYING 
%doc %{_mandir}/man1/vbetool.1*
%{_sbindir}/vbetool
%{_udevrulesdir}/92-video-post.rules
  
