%define name    libpicviz
%define version 0.6.1
%define release 5
%define major   2

%define libname %mklibname picviz %{major}
%define develname %mklibname -d picviz

Name: %name
Version: %version
Release: %release
Summary: Parallel coordinates plotter
License: GPLv3+
Group: Graphics
URL: https://www.wallinfire.net/picviz
#Source0: http://www.wallinfire.net/picviz/attachment/wiki/ReleasesDownload/%{name}-%{version}.tar.gz?format=raw
Source0: http://www.wallinfire.net/files/picviz/%{name}-%{version}.tar.gz
Patch0: libpicviz-0.6.1-fix-underlinking.patch
Patch1: libpicviz-0.6.1-external-libevent.patch

BuildRequires: cmake
BuildRequires: bison
BuildRequires: flex
BuildRequires: python-devel
BuildRequires: pkgconfig
BuildRequires: pcre-devel
BuildRequires: libev-devel
BuildRequires: cairo-devel
BuildRoot: %{_tmppath}/%{name}-%{version}

%package -n %{develname}
Summary: Picviz development files
Group: Development/C
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%package -n %{libname}
Summary: Parallel coordinates plotter library
Group: Graphics

%description
Picviz is a parallel coordinates plotter which enables easy scripting
from various input (tcpdump, syslog, iptables logs, apache logs,
etc..) to visualize your data and discover interesting results
quickly.

Its primary goal is to graph data in order to be able to quickly
analyze problems and find correlations among variables. With security
analysis in mind, the program has been designed to be very flexible,
able to graph millions of events.

The language is designed to be close to the graphviz graph description
language.

%description -n %{develname}
Development files for libpicviz.

%description -n %{libname}
Picviz is a parallel coordinates plotter which enables easy scripting
from various input (tcpdump, syslog, iptables logs, apache logs,
etc..) to visualize your data and discover interesting results
quickly.

Its primary goal is to graph data in order to be able to quickly
analyze problems and find correlations among variables. With security
analysis in mind, the program has been designed to be very flexible,
able to graph millions of events.

The language is designed to be close to the graphviz graph description
language.

%prep
%setup -q
%patch1 -p 1
%patch0 -p 1

%build
pushd .
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON -DLIB_INSTALL_DIR=%_lib -DMOD_INSTALL_DIR=%_lib/%name-%major
# parallel build breaks on klodia (too many cores)
make
popd

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{develname}
%defattr(-,root,root,-)
%{_libdir}/libpicviz.so
%{_libdir}/pkgconfig/libpicviz.pc
%{_includedir}/*

%files -n %libname
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*
%dir %{_libdir}/%{name}-%major
%{_libdir}/%{name}-%major/*.so



%changelog
* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-4mdv2012.0
+ Revision: 772998
- relink against libpcre.so.1

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-3mdv2011.0
+ Revision: 609772
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - fix sources URL

* Sat Feb 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.1-2mdv2010.1
+ Revision: 501422
- use external libev

* Tue Jan 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.1-1mdv2010.1
+ Revision: 496519
- import libpicviz


* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.1-1mdv2010.1
- first standalone package 
