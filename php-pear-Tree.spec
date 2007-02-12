%include	/usr/lib/rpm/macros.php
%define		_class		Tree
%define		_status		beta
%define		_pearname	%{_class}
Summary:	%{_pearname} - Generic tree management
Summary(pl.UTF-8):   %{_pearname} - Podstawowe zarządzanie drzewami
Name:		php-pear-%{_pearname}
Version:	0.2.4
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	acd4b47b0763ba302d28bc374f61abad
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Tree/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-DB >= 1.3
Requires:	php-pear-XML_Parser >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/%{_class}/Dynamic
%dir %{php_pear_dir}/%{_class}/Memory
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Dynamic/*.php
%{php_pear_dir}/%{_class}/Memory/*.php
