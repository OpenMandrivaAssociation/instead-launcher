Name:		instead-launcher
Version:	0.6.1
Release:	%mkrel 1
Summary:	Games download helper for Instead
Group:		Games/Adventure
License:	GPLv2
URL:		http://instead.googlecode.com
Source0:	http://instead-launcher.googlecode.com/files/%{name}_%{version}.tar.gz
# Fix default interpretator path
Patch0:		instead-default-interpretator-path-fix.patch
Patch1:		instead-launcher-desktop.patch
BuildRequires:	qt4-devel
Requires:	instead

%description
This is a games download helper for Instead game engine.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%qmake_qt4 PREFIX=/usr

%install
%__rm -rf %{buildroot}
%makeinstall_std INSTALL_ROOT=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datadir}/applications/*



%changelog
* Sat Mar 03 2012 Andrey Bondrov <abondrov@mandriva.org> 0.6.1-1
+ Revision: 781934
- New version 0.6.1

* Thu Aug 25 2011 Andrey Bondrov <abondrov@mandriva.org> 0.6-2
+ Revision: 697041
- imported package instead-launcher


* Thu Aug 25 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 1.5.0-2mdv2011.0
- Little spec clean up
- Drop useless BuildRequires
- Change group
- Fix .desktop file (patch1)

* Wed Aug 24 2011 Anton Chernyshov <anton.chernyshov@rosalab.ru> 1.5.0-1mdv2011.0
- initial build for Mandriva

