Summary:	Contains the xineramaproto protocol header for Xorg.
Name:		xineramaproto
Version:	1.2.1
Release:	1
License:	GPL
URL:		http://xorg.freedesktop.org/
Group:		System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.bz2
%description

%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}"              \
	CXXFLAGS="%{optflags}"            \
	--prefix=%{_prefix}               \
	--sysconfdir=%{_sysconfdir}       \
	--localstatedir=%{_localstatedir} \
	--disable-static
	
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*

%changelog
*	Fri Aug 28 2015 Niels Terp <nielsterp@comhem.se>
-	Initial build.	First version
