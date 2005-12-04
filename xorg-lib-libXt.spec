Summary:	X Toolkit library
Summary(pl):	Biblioteka X Toolkit
Name:		xorg-lib-libXt
Version:	0.99.3
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/lib/libXt-%{version}.tar.bz2
# Source0-md5:	82059b90d704a3e09a338c2034918275
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
Summary:	Header files libXt development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libSM-devel
Requires:	xorg-lib-libX11-devel
Obsoletes:	libXt-devel

%description devel
X Toolkit library.

This package contains the header files needed to develop programs that
use these libXt.

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXt.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXt.so
%{_libdir}/libXt.la
%{_includedir}/X11/*.h
%{_pkgconfigdir}/xt.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXt.a
