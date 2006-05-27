Summary:	X Toolkit library
Summary(pl):	Biblioteka X Toolkit
Name:		xorg-lib-libXt
Version:	1.0.2
Release:	0.2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXt-%{version}.tar.bz2
# Source0-md5:	f217b63e03a1ac9b155ee9a56ac47aea
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	libXt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Toolkit library.

%description -l pl
Biblioteka X Toolkit.

%package devel
Summary:	Header files for libXt library
Summary(pl):	Pliki nag³ówkowe biblioteki libXt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libSM-devel
Requires:	xorg-lib-libX11-devel
Obsoletes:	libXt-devel

%description devel
X Toolkit library.

This package contains the header files needed to develop programs that
use libXt.

%description devel -l pl
Biblioteka X Toolkit.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXt.

%package static
Summary:	Static libXt library
Summary(pl):	Biblioteka statyczna libXt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXt-static

%description static
X Toolkit library.

This package contains the static libXt library.

%description static -l pl
Biblioteka X Toolkit.

Pakiet zawiera statyczn± bibliotekê libXt.

%prep
%setup -q -n libXt-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

install -d $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults
install -d $RPM_BUILD_ROOT%{_datadir}/X11/{cs,da,de,es,fr,ja,ko,nl,pl,pt,pt_BR,ru,sv,zh_CN,zh_TW}/app-defaults

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXt.so.*.*.*
%dir %{_datadir}/X11/app-defaults
%lang(cs) %{_datadir}/X11/cs
%lang(da) %{_datadir}/X11/da
%lang(de) %{_datadir}/X11/de
%lang(es) %{_datadir}/X11/es
%lang(fr) %{_datadir}/X11/fr
%lang(ja) %{_datadir}/X11/ja
%lang(ko) %{_datadir}/X11/ko
%lang(nl) %{_datadir}/X11/nl
%lang(pl) %{_datadir}/X11/pl
%lang(pt) %{_datadir}/X11/pt
%lang(pt_BR) %{_datadir}/X11/pt_BR
%lang(ru) %{_datadir}/X11/ru
%lang(sv) %{_datadir}/X11/sv
%lang(zh_CN) %{_datadir}/X11/zh_CN
%lang(zh_TW) %{_datadir}/X11/zh_TW

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/makestrs
%attr(755,root,root) %{_libdir}/libXt.so
%{_libdir}/libXt.la
%{_includedir}/X11/*.h
%{_pkgconfigdir}/xt.pc
%{_mandir}/man1/makestrs.1x*
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXt.a
