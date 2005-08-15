
#
Summary:	X Toolkit library
Summary(pl):	Biblioteka X Toolkit
Name:		xorg-lib-libXt
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXt-%{version}.tar.bz2
# Source0-md5:	239c48ef101c5daacba044e603af441a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/libXt-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
X Toolkit library.

%description -l pl
Biblioteka X Toolkit.


%package devel
Summary:	Header files libXt development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXt
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXt = %{version}-%{release}
Requires:	xorg-lib-libSM-devel
Requires:	xorg-lib-libX11-devel

%description devel
X Toolkit library.

This package contains the header files needed to develop programs that
use these libXt.

%description devel -l pl
Biblioteka X Toolkit.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXt.


%package static
Summary:	Static libXt libraries
Summary(pl):	Biblioteki statyczne libXt
Group:		Development/Libraries
Requires:	xorg-lib-libXt-devel = %{version}-%{release}

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
%doc ChangeLog
%attr(755,root,wheel) %{_libdir}/libXt.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/*.h
%{_libdir}/libXt.la
%attr(755,root,wheel) %{_libdir}/libXt.so
%{_pkgconfigdir}/xt.pc
%{_mandir}/man3/*.3*


%files static
%defattr(644,root,root,755)
%{_libdir}/libXt.a
