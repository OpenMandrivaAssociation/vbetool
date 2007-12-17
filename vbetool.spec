%define	name	vbetool
%define	version	0.7
%define	release	%mkrel 1

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:        Real-mode video BIOS utility to alter hardware state
License:        GPL
Group:          System/Configuration/Other
URL:            http://www.srcf.ucam.org/~mjg59/vbetool/
Source:         http://www.srcf.ucam.org/~mjg59/vbetool/vbetool_%{version}-1.tar.bz2
BuildRequires:  pciutils-devel
ExclusiveArch:  %{ix86} x86_64


%description 
vbetool allows you to run real-mode video BIOS code to alter 
hardware state. It uses lrmi in order to run code from the video BIOS. 
Currently, it is able to alter DPMS states, save/restore video card state
and attempts to initialize the video card from scratch.

%prep
%setup -q

%build
%configure \
%ifarch x86_64
--with-x86emu 
%endif

%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc COPYING 
%doc %{_mandir}/man1/vbetool.1*
%{_sbindir}/vbetool

