%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	GIS
%define		_status		stable

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - visualization of GIS data
Summary(pl):	%{_pearname} - wizualizacja danych GIS
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	45438d43fe56aa7c98c7cdef9e73173f
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-gd
Requires:	php-pear
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

This class has in PEAR status: %{_status}.

%description -l pl
Generowanie map na ¿±danie mo¿e byæ ciê¿k± prac±, jako ¿e najczê¶ciej
nie posiada siê potrzebnych map w postaci cyfrowej. Ale mo¿e generowaæ
w³asne mapy na podstawie plików surowych, cyfrowych opisów danych,
które s± dostêpne za darmo w sieci. Ten pakiet udostêpnia analizator
do najczê¶ciej u¿ywanego formatu danych geograficznych Arcinfo/E00, a
tak¿e narzêdzia rysuj±ce, tworz±ce obrazy przy u¿yciu GD lub SVG.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Parser,Renderer}

install %{_pearname}-%{version}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Parser/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Parser
install %{_pearname}-%{version}/%{_subclass}/Renderer/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Renderer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Parser
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Renderer
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Parser/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Renderer/*.php
