%include	/usr/lib/rpm/macros.php
%define		_class		Tree
%define		_pearname	%{_class}
Summary:	%{_pearname} - Generic tree management
Summary(pl):	%{_pearname} - Podstawowe zarz±dzanie drzewami
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
Patch0:		%{name}-cosmetic.patch
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides methods to read and manipulate trees, which are stored in the
DB or an XML file. The trees can be stored in the DB either as nested
trees. Or as simple trees ('brain dead method'), which use
parentId-like structure. Currently XML data can only be read from a
file and accessed. The package offers a big number of methods to
access and manipulate trees. For example methods like: getRoot,
getChild[ren], getParent, getPath and many more. There are two ways of
retreiving the data from the place where they are stored, one is by
reading the entire tree into the memory - the Memory way. The other is
reading the tree nodes as needed (very useful in combination with huge
trees and the nested set model). The package is designed that way that
it is possible to convert/copy tree data from either structure to
another (from XML into DB).

%prep
%setup -q -c
cd %{_pearname}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{Dynamic,Memory}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/Dynamic/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Dynamic/
install %{_pearname}-%{version}/Memory/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Memory/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/%{_class}/Dynamic
%dir %{php_pear_dir}/%{_class}/Memory
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Dynamic/*.php
%{php_pear_dir}/%{_class}/Memory/*.php
