%define version 0.8.2

%define libpath /usr/lib
%ifarch x86_64
  %define libpath /usr/lib64
%endif

Summary: SSL remote access handler for openpanel
Name: openpanel-ssl
Version: %version
Release: 1
License: GPLv2
Group: Development
Source: http://packages.openpanel.com/archive/openpanel-ssl-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-buildroot
Requires: openpanel-core
Requires: openssl

%description
SSL remote access handler for openpanel

%prep
%setup -q -n openpanel-ssl-%version

%build
BUILD_ROOT=$RPM_BUILD_ROOT
make

%install
BUILD_ROOT=$RPM_BUILD_ROOT
rm -rf ${BUILD_ROOT}
mkdir -p ${BUILD_ROOT}/var/opencore/bin
mkdir -p ${BUILD_ROOT}/etc/openpanel
mkdir -p ${BUILD_ROOT}/etc/rc.d/init.d
install -m 755 opencore-ssl ${BUILD_ROOT}/var/opencore/bin
chmod 600 ${BUILD_ROOT}/etc/openpanel
install -m 755 init.redhat ${BUILD_ROOT}/etc/rc.d/init.d/openpanel-ssl

%post
chkconfig --level 2345 openpanel-ssl on
/etc/init.d/openpanel-ssl start

%files
%defattr(-,root,root)
/
