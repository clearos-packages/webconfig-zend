Name: webconfig-zend
Version: 1.11.7
Release: 1%{dist}
Group: Applications/Libraries
Packager: ClearFoundation
Vendor: ClearFoundation
Summary: Zend libraries for webconfig
Source: %{name}-%{version}.tar.gz
License: Zend
BuildArch: noarch
BuildRoot: /tmp/%{name}-build

%description
Zend libraries for webconfig

%prep
%setup
%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/clearos/sandbox/usr/share/php
cp -av Zend $RPM_BUILD_ROOT/usr/clearos/sandbox/usr/share/php

# Something weird is going on here -- investigate
cd $RPM_BUILD_ROOT/usr/clearos/sandbox/usr/share/php/Zend/Gdata/Gapps
FILES=`ls *.php`
for FILE in $FILES; do
    ln -s ../$FILE Extension/$FILE
done


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/clearos/sandbox/usr/share/php
