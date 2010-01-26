%define name    libpicviz
%define version 0.6.1
%define release %mkrel 1
%define major   2

%define libname %mklibname picviz %{major}
%define develname %mklibname -d picviz

Name: %name
Version: %version
Release: %release
Summary: Parallel coordinates plotter
License: GPLv3+
Group: Graphics
URL: http://www.wallinfire.net/picviz
#Source0: http://www.wallinfire.net/picviz/attachment/wiki/ReleasesDownload/%{name}-%{version}.tar.gz?format=raw
Source0: %{name}-%{version}.tar.gz
Patch0: libpicviz-0.6.1-fix-underlinking.patch

BuildRequires: cmake
BuildRequires: bison
BuildRequires: flex
BuildRequires: python-devel
BuildRequires: pkgconfig
BuildRequires: pcre-devel
BuildRequires: libevent-devel
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

