%define major 2
%define oldlibname %mklibname %{name} 2
%define libname %mklibname %{name}
%define devname %mklibname -d %{name}

Summary:	A fast math parser library
Name:		muparser
Version:	2.3.4
Release:	1
License:	MIT
Group:		System/Libraries
Url:		https://muparser.sourceforge.net/
Source0:	https://github.com/beltoforion/muparser/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja

%description
muParser is an extensible high performance math parser library. It is
based on transforming an expression into a bytecode and precalculating
constant parts of it.

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
This package contains library files of muParser.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains development files need to develop applications
based on muParser.

%prep
%autosetup -p0

%conf
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libmuparser.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h
%{_libdir}/cmake/muparser
