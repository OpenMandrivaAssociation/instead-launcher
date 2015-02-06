Name:		instead-launcher
Version:	0.6.1
Release:	3
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
%qmake_qt4 \
	PREFIX=/usr \
	QMAKE_CXXFLAGS_RELEASE= 
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

