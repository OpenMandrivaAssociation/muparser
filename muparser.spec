%define filever %(echo %version|sed -e 's|\\.||')
%define major 0
%define libname %mklibname %name %major
%define develname %mklibname -d %name

Summary:	A fast math parser library
Name:		muparser
Version:	1.34
Release:	2
License:	MIT
Group: 		System/Libraries
Source0:	http://nchc.dl.sourceforge.net/sourceforge/%{name}/%{name}_v%{filever}.tar.gz
Patch1:		muParser-1.30-gcc43.patch
URL:		http://muparser.sourceforge.net/

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
%setup -q -n %{name}_v%{filever}
%patch1 -p0

%build
%configure2_5x --enable-shared --enable-static
make

%install
rm -fr %buildroot
%makeinstall_std

%files -n %{libname}
%doc Changes.txt
%_libdir/*.so.%{major}*

%files -n %{develname}
%doc docs/html
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/*.h


%changelog
* Wed Mar 09 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.34-1mdv2011.0
+ Revision: 643140
- update to new version 1.34

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.32-2mdv2011.0
+ Revision: 612968
- the mass rebuild of 2010.1 packages

* Thu Feb 11 2010 Funda Wang <fwang@mandriva.org> 1.32-1mdv2010.1
+ Revision: 504221
- New version 1.32

* Mon Dec 28 2009 Ahmad Samir <ahmadsamir@mandriva.org> 1.30-1mdv2010.1
+ Revision: 483014
- update to 1.30
- rediff patch1

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.28-6mdv2010.0
+ Revision: 430130
- rebuild

* Wed Jul 30 2008 Funda Wang <fwang@mandriva.org> 1.28-5mdv2009.0
+ Revision: 254737
- add gentoo patches

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 12 2007 Funda Wang <fwang@mandriva.org> 1.28-3mdv2008.1
+ Revision: 97256
- add ldconfig

* Fri Oct 12 2007 Funda Wang <fwang@mandriva.org> 1.28-2mdv2008.1
+ Revision: 97255
- add docs
- Import muparser
- Created package structure for muparser.

