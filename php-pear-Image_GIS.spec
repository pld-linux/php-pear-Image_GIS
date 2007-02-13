%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	GIS
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - visualization of GIS data
Summary(pl.UTF-8):	%{_pearname} - wizualizacja danych GIS
Name:		php-pear-%{_pearname}
Version:	1.1.1
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	08a175de367af29ef33abc3559117b7f
URL:		http://pear.php.net/package/Image_GIS/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(gd)
Requires:	php-pear
Requires:	php-pear-Cache_Lite
Requires:	php-pear-Image_Color
Requires:	php-pear-XML_SVG
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generating maps on demand can be a hard job as most often you don't
have the maps you need in digital form. But you can generate your own
maps based on raw, digital data description files which are available
for free on the net. This package provides a parser for the most
common format for geographical data, the Arcinfo/E00 format as well as
renderers to produce images using GD or Scalable Vector Graphics
(SVG).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Generowanie map na żądanie może być ciężką pracą, jako że najczęściej
nie posiada się potrzebnych map w postaci cyfrowej. Ale może generować
własne mapy na podstawie plików surowych, cyfrowych opisów danych,
które są dostępne za darmo w sieci. Ten pakiet udostępnia analizator
do najczęściej używanego formatu danych geograficznych Arcinfo/E00, a
także narzędzia rysujące, tworzące obrazy przy użyciu GD lub SVG.

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
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Parser
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Renderer
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Parser/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Renderer/*.php
