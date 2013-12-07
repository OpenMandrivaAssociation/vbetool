Summary:        Real-mode video BIOS utility to alter hardware state
Name:		vbetool
Version:	1.1
Release:	15
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
autoreconf -fi
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


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-7mdv2011.0
+ Revision: 670762
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-6mdv2011.0
+ Revision: 608122
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-5mdv2010.1
+ Revision: 524307
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.1-4mdv2010.0
+ Revision: 427489
- rebuild

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.1-3mdv2009.1
+ Revision: 366568
- use autoreconf

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.1-2mdv2009.0
+ Revision: 265770
- rebuild early 2009.0 package (before pixel changes)

* Tue May 20 2008 Pascal Terjan <pterjan@mandriva.org> 1.1-1mdv2009.0
+ Revision: 209227
- Don't link against libz
- Update to 1.1

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7-2mdv2008.1
+ Revision: 179675
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Sep 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.7-1mdv2007.0
- new version
- drop build patch, useless now

* Sat May 06 2006 Pascal Terjan <pterjan@mandriva.org> 0.5-2mdk
- only work on x86_{32,64}

* Wed Nov 30 2005 Couriousous <couriousous@mandriva.org> 0.5-1mdk
- 0.5 ( add x86_64 support )
- Better patch from Carl-Daniel Hailfinger ( found on acpi-devel ML )

* Mon Oct 10 2005 Frederic Lepied <flepied@mandriva.com> 0.2-1mdk
- initial Mandriva Linux package based on Koenraad Heijlen's package

