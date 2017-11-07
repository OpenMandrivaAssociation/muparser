%define debug_package %{nil}

%define major 2
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	A fast math parser library
Name:		muparser
Version:	2.2.5
Release:	2
License:	MIT
Group:		System/Libraries
Url:		http://muparser.sourceforge.net/
Source0:	https://codeload.github.com/beltoforion/muparser/%{name}-%{version}.tar.gz
Patch1:		muParser-1.30-gcc43.patch

%description
muParser is an extensible high performance math parser library. It is
based on transforming an expression into a bytecode and precalculating
constant parts of it.

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries

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
%setup -q
%patch1 -p0

%build
%configure \
	--enable-shared=yes

%make -j1

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libmuparser.so.%{major}*

%files -n %{devname}
%doc Changes.txt
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h

