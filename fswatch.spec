%global _hardened_build 1

Name:		fswatch
Version:	1.14.0
Release:	1%{?dist}
Summary:	A cross-platform file change monitor
License:	GPLv3
URL:		https://github.com/emcrisostomo/fswatch
Source0:	https://github.com/emcrisostomo/fswatch/archive/%{version}/%{version}.tar.gz#/fswatch-%{version}.tar.gz

BuildRequires: autoconf automake libtool
BuildRequires: gcc-c++ gcc gettext-devel

%description
%{name} is a file change monitor that receives notifications when the contents of the specified files or directories are modified.

%package devel
Summary:	Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and headers for developing applications that use lib%{name}.

%package static
Summary:	Static library for %{name}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static 
Static library (.a) of lib%{name}

%prep
%autosetup -n %{name}-%{version}

%build
./autogen.sh
%configure
%make_build

%install
%make_install
mkdir $RPM_BUILD_ROOT%{_mandir}/man1/
mv $RPM_BUILD_ROOT%{_mandir}/man7/%{name}.7 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ABOUT-NLS
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/AUTHORS.libfswatch
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/CONTRIBUTING.md
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/NEWS
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/NEWS.libfswatch
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/README.bsd
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/README.codestyle
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/README.freebsd
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/README.gnu-build-system
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/README.illumos
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/README.libfswatch.md
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/README.osx
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/README.smartos
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/README.solaris
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/README.windows
%find_lang %{name}

%check
make check

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md README.linux AUTHORS COPYING
%license COPYING
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/lib%{name}/*

%files static
%{_libdir}/*.a

%changelog
* Sat Apr 11 2020 Darryl T. Agostinelli <dagostinelli@gmail.com> 1.14.0-1
- Created the .spec file for version 1.14.0

