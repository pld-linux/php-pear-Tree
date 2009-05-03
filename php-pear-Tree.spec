%include	/usr/lib/rpm/macros.php
%define		_class		Tree
%define		_status		beta
%define		_pearname	%{_class}
Summary:	%{_pearname} - Generic tree management
Summary(pl.UTF-8):	%{_pearname} - Podstawowe zarządzanie drzewami
Name:		php-pear-%{_pearname}
Version:	0.3.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d5d8e392edf3dc5c04e6342979200eb9
URL:		http://pear.php.net/package/Tree/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-DB >= 1.3
Requires:	php-pear-PEAR-core >= 1:1.4.0
Requires:	php-pear-XML_Parser >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(DB.*)' 'pear(XML/Parser.*)'

%description
Provides methods to read and manipulate trees, which are stored in the
DB or an XML file. The trees can be stored in the DB either as nested
trees or as simple trees ('brain dead method'), which use
parentId-like structure. Currently XML data can only be read from a
file and accessed. The package offers a big number of methods to
access and manipulate trees. For example methods like: getRoot,
getChild[ren], getParent, getPath and many more. There are two ways of
retrieving the data from the place where they are stored, one is by
reading the entire tree into the memory - the Memory way. The other is
reading the tree nodes as needed (very useful in combination with huge
trees and the nested set model). The package is designed that way that
it is possible to convert/copy tree data from either structure to
another (from XML into DB).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet udostępnia metody do odczytu i obróbki drzew zapisanych w
bazach danych lub plikach XML. Drzewa mogą być zapisane w bazie jako
zagnieżdżone drzewa lub proste drzewa (metoda prymitywna), które
używają struktury w stylu parentId. Aktualnie dane XML mogą być tylko
czytane tylko z pliku i przeglądane. Pakiet oferuje dużą liczbę metod
do dostępu i obróbki drzew, na przykład getRoot, getChild[ren],
getParent, getPath i wiele innych. Są dwa sposoby na odczytywanie
danych z miejsca gdzie są zapisane - jeden przez wczytanie całego
drzewa do pamięci (metoda pamięciowa), drugi przez czytanie węzłów w
miarę potrzeby (bardzo przydatny w przypadku dużych drzew i modelu
zagnieżdżonego). Pakiet jest stworzony tak, by umożliwić konwersję i
kopiowanie danych z drzewa z jednej struktury do drugiej (z XML-a do
DB).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

# pear/tests/pearname/tests -> pear/tests/pearname
mv ./%{php_pear_dir}/tests/%{_pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{_pearname}/tests

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/%{_class}/Dynamic
%dir %{php_pear_dir}/%{_class}/Memory
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Dynamic/*.php
%{php_pear_dir}/%{_class}/Memory/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
