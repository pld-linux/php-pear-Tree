%include	/usr/lib/rpm/macros.php
%define		_class		Tree
%define		_status		beta
%define		_pearname	%{_class}
Summary:	%{_pearname} - Generic tree management
Summary(pl):	%{_pearname} - Podstawowe zarz±dzanie drzewami
Name:		php-pear-%{_pearname}
Version:	0.2.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	acd4b47b0763ba302d28bc374f61abad
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Tree/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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

This class has in PEAR status: %{_status}.

%description -l pl
Ten pakiet udostêpnia metody do odczytu i obróbki drzew zapisanych w
bazach danych lub plikach XML. Drzewa mog± byæ zapisane w bazie jako
zagnie¿d¿one drzewa lub proste drzewa (metoda prymitywna), które
u¿ywaj± struktury w stylu parentId. Aktualnie dane XML mog± byæ tylko
czytane tylko z pliku i przegl±dane. Pakiet oferuje du¿± liczbê metod
do dostêpu i obróbki drzew, na przyk³ad getRoot, getChild[ren],
getParent, getPath i wiele innych. S± dwa sposoby na odczytywanie
danych z miejsca gdzie s± zapisane - jeden przez wczytanie ca³ego
drzewa do pamiêci (metoda pamiêciowa), drugi przez czytanie wêz³ów w
miarê potrzeby (bardzo przydatny w przypadku du¿ych drzew i modelu
zagnie¿d¿onego). Pakiet jest stworzony tak, by umo¿liwiæ konwersjê i
kopiowanie danych z drzewa z jednej struktury do drugiej (z XML do
DB).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

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
%doc %{_pearname}-%{version}/docs/*
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/%{_class}/Dynamic
%dir %{php_pear_dir}/%{_class}/Memory
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Dynamic/*.php
%{php_pear_dir}/%{_class}/Memory/*.php
