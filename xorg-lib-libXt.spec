Summary:	X Toolkit Intrinsics library
Summary(pl.UTF-8):	Biblioteka X Toolkit Intrinsics
Name:		xorg-lib-libXt
Version:	1.2.1
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXt-%{version}.tar.bz2
# Source0-md5:	b122ff9a7ec70c94dbbfd814899fffa5
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	sed >= 4.0
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	xmlto >= 0.0.20
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-kbproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-sgml-doctools >= 1.1
BuildRequires:	xorg-util-util-macros >= 1.13
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

# support __libmansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,\.so man__libmansuffix__/,.so man3/,' man/*.man

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--without-fop
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults
install -d $RPM_BUILD_ROOT%{_datadir}/X11/{cs,da,de,es,es_AR,eu,fr,hu,it,ja,ko,mg,nb,nl,oc,pl,pt,pt_BR,ru,sk,sv,zh_CN,zh_TW}/app-defaults

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libXt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
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
%doc specs/intrinsics.html
%attr(755,root,root) %{_libdir}/libXt.so
%{_libdir}/libXt.la
%{_includedir}/X11/CallbackI.h
%{_includedir}/X11/Composite*.h
%{_includedir}/X11/Constrain*.h
%{_includedir}/X11/ConvertI.h
%{_includedir}/X11/Core*.h
%{_includedir}/X11/CreateI.h
%{_includedir}/X11/EventI.h
%{_includedir}/X11/HookObjI.h
%{_includedir}/X11/InitialI.h
%{_includedir}/X11/Intrinsic*.h
%{_includedir}/X11/Object*.h
%{_includedir}/X11/PassivGraI.h
%{_includedir}/X11/RectObj*.h
%{_includedir}/X11/ResConfigP.h
%{_includedir}/X11/ResourceI.h
%{_includedir}/X11/SelectionI.h
%{_includedir}/X11/Shell*.h
%{_includedir}/X11/StringDefs.h
%{_includedir}/X11/ThreadsI.h
%{_includedir}/X11/TranslateI.h
%{_includedir}/X11/VarargsI.h
%{_includedir}/X11/Vendor*.h
%{_includedir}/X11/Xtos.h
%{_pkgconfigdir}/xt.pc
%{_mandir}/man3/MenuPop*.3*
%{_mandir}/man3/Xt*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXt.a
