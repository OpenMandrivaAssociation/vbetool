Summary:        Real-mode video BIOS utility to alter hardware state
Name:		vbetool
Version:	1.1
Release:	%mkrel 2
License:        GPL
Group:          System/Configuration/Other
URL:            http://www.srcf.ucam.org/~mjg59/vbetool/
Source:         http://www.srcf.ucam.org/~mjg59/vbetool/vbetool_%{version}.tar.gz
Patch0:		vbetool_1.1-lz.patch
BuildRequires:  pciutils-devel libx86-devel
ExclusiveArch:  %{ix86} x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
vbetool allows you to run real-mode video BIOS code to alter 
hardware state. It uses lrmi in order to run code from the video BIOS. 
Currently, it is able to alter DPMS states, save/restore video card state
and attempts to initialize the video card from scratch.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
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
