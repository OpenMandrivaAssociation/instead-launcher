%define	name	instead-launcher
%define	version	0.6
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
URL:		http://instead.googlecode.com
Source0:	http://instead-launcher.googlecode.com/files/%{name}_%{version}.tar.gz

# Fix default interpretator path
Patch0:		instead-default-interpretator-path-fix.patch

Patch1:		instead-launcher-0.6-desktop.patch
Group:		Games/Adventure
Summary:	Games download helper for Instead

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
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/*

