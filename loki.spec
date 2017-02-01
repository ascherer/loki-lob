%bcond_without doc

%define source_name loki
Name: %{source_name}-lib
Summary: Loki C++ Library
Version: 0.1.7
Release: 1
License: MIT License
Group: Productivity/Development
URL: http://sourceforge.net/projects/loki-lib
Distribution: SuSE 10.2 (i586)
Source0: http://prdownloads.sourceforge.net/loki-lib/%{source_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%package devel
Summary: The Loki C++ headers and development libraries
Group: System Environment/Libraries

%if %{with doc}
%package doc
Summary: The Loki C++ html docs
Group: System Environment/Libraries
%endif

%description
A C++ library of designs, containing flexible implementations of common design
patterns and idioms.

%description devel
Headers, static libraries, and shared object symlinks for the Loki C++ Library

%if %{with doc}
%description doc
HTML documentation files for the Loki C++ Library
%endif

%prep
%setup -n %{source_name}-%{version} -q

%build
make build-static build-shared check
%if %{with doc}
cd doc; doxygen Doxyfile
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/include
cp -a include/%{source_name} $RPM_BUILD_ROOT/usr/include
mkdir -p $RPM_BUILD_ROOT/usr/lib
cp -a lib/lib%{source_name}.* $RPM_BUILD_ROOT/usr/lib
(cd $RPM_BUILD_ROOT/usr/lib && ln -s lib%{source_name}.so.%{version} lib%{source_name}.so)
%if %{with doc}
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
cp -a doc/{flex,html,yasli} $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root)
/usr/lib/lib%{source_name}.so
/usr/lib/lib%{source_name}.so.%{version}

%files devel
%defattr(644,root,root,755)
/usr/include/%{source_name}
/usr/lib/lib%{source_name}.a

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc /usr/share/doc/%{name}-%{version}
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Thu Mar 16 2006 Regis Desgroppes <rdesgroppes@besancon.parkeon.com>
- Renamed package to loki-lib (SourceForge project name) as there is another package named loki (Biology)
- Created devel and doc subpackages
- Also building shared library
- Removed LF chars so that rpmbuild generated scriptlets work

* Fri Jan 06 2006 Andreas Scherer <andreas_hacker@freenet.de>
- Initial build
