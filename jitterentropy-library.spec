%define major 2
%define libname %mklibname jitterentropy %{major}
%define devname %mklibname jitterentropy -d

Summary:	Library implementing the jitter entropy source
Name:		jitterentropy-library
Version:	2.2.0
Release:	1
Group:		System/Libraries
License:	GPLv2
Url:		https://github.com/smuellerDD/%{name}
Source0:	https://github.com/smuellerDD/%{name}/archive/%{name}-%{version}.tar.gz
Patch0:		https://src.fedoraproject.org/rpms/jitterentropy/raw/master/f/jitterentropy-rh-makefile.patch

%description
Library implementing the CPU jitter entropy source.

%package -n %{libname}
Summary:	%{Summary}
Group:		System/Libraries

%description -n %{libname}
%{description}

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files and headers for %{name}.

%prep
%autosetup -p1

%build
# (tpg) using -O0 is a must here
%global optflags %{optflags} -O0

%make_build CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
mkdir -p %{buildroot}%{_includedir}

%make_install PREFIX=%{_prefix} LIBDIR="/%{_lib}"

%files -n %{libname}
%{_libdir}/*jitterentropy.so.%{major}*

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/*.so
%{_mandir}/man3/*.3.*
