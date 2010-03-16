Summary:	X Toolkit Intrinsics library
Summary(pl.UTF-8):	Biblioteka X Toolkit Intrinsics
Name:		xorg-lib-libXt
Version:	1.0.8
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXt-%{version}.tar.bz2
# Source0-md5:	fb7d2aa5b24cd5fe9b238a26d88030e7
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-kbproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.3
Obsoletes:	libXt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Toolkit Intrinsics library.

%description -l pl.UTF-8
Biblioteka X Toolkit Intrinsics.

%package devel
Summary:	Header files for libXt library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libSM-devel
Requires:	xorg-lib-libX11-devel
Obsoletes:	libXt-devel

%description devel
X Toolkit Intrinsics library.

This package contains the header files needed to develop programs that
use libXt.

%description devel -l pl.UTF-8
Biblioteka X Toolkit Intrinsics.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXt.

%package static
Summary:	Static libXt library
Summary(pl.UTF-8):	Biblioteka statyczna libXt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXt-static

%description static
X Toolkit Intrinsics library.

This package contains the static libXt library.

%description static -l pl.UTF-8
Biblioteka X Toolkit Intrinsics.

Pakiet zawiera statyczną bibliotekę libXt.

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
install -d $RPM_BUILD_ROOT%{_datadir}/X11/{cs,da,de,es,es_AR,eu,fr,hu,it,ja,ko,mg,nb,nl,oc,pl,pt,pt_BR,ru,sk,sv,zh_CN,zh_TW}/app-defaults

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXt.so.6
%dir %{_datadir}/X11/app-defaults
%lang(cs) %{_datadir}/X11/cs
%lang(da) %{_datadir}/X11/da
%lang(de) %{_datadir}/X11/de
%lang(es) %{_datadir}/X11/es
%lang(es_AR) %{_datadir}/X11/es_AR
%lang(eu) %{_datadir}/X11/eu
%lang(fr) %{_datadir}/X11/fr
%lang(hu) %{_datadir}/X11/hu
%lang(it) %{_datadir}/X11/it
%lang(ja) %{_datadir}/X11/ja
%lang(ko) %{_datadir}/X11/ko
%lang(mg) %{_datadir}/X11/mg
%lang(nb) %{_datadir}/X11/nb
%lang(nl) %{_datadir}/X11/nl
%lang(oc) %{_datadir}/X11/oc
%lang(pl) %{_datadir}/X11/pl
%lang(pt) %{_datadir}/X11/pt
%lang(pt_BR) %{_datadir}/X11/pt_BR
%lang(ru) %{_datadir}/X11/ru
%lang(sk) %{_datadir}/X11/sk
%lang(sv) %{_datadir}/X11/sv
%lang(zh_CN) %{_datadir}/X11/zh_CN
%lang(zh_TW) %{_datadir}/X11/zh_TW

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXt.so
%{_libdir}/libXt.la
%{_includedir}/X11/*.h
%{_pkgconfigdir}/xt.pc
%{_mandir}/man3/MenuPop*.3x*
%{_mandir}/man3/Xt*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXt.a
