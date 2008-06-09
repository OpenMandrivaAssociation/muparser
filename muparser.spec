%define version 1.28
%define filever %(echo %version|sed -e 's|\\.||')
%define major 0
%define libname %mklibname %name %major
%define develname %mklibname -d %name

Summary:	A fast math parser library
Name:		muparser
Version:	1.28
Release:	%mkrel 3
License:	MIT
Group: 		System/Libraries
Source0:        http://nchc.dl.sourceforge.net/sourceforge/%{name}/%{name}_v%{filever}.tar.gz
URL: 		http://muparser.sourceforge.net/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
muParser is an extensible high performance math parser library. It is
based on transforming an expression into a bytecode and precalculating
constant parts of it.

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains library files of muParser.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %version-%release
Provides:	%{name}-devel = %version-%release

%description -n %{develname}
This package contains development files need to develop applications
based on muParser.

%prep
%setup -q -n %{name}

%build
rm -fr %buildroot
%configure2_5x --enable-shared --enable-static
# fwang: parallel build does not work
%make -j1

%install
%makeinstall

%clean
rm -fr %buildroot

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc Changes.txt
%_libdir/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc docs/html
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/*.h
