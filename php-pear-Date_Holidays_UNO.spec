%include	/usr/lib/rpm/macros.php
%define		_class		Date
%define		_subclass	Holidays_UNO
%define		_status		alpha
%define		_pearname	Date_Holidays_UNO
Summary:	%{_pearname} - Driver based class to calculate holidays in UNO
Summary(pl.UTF-8):	%{_pearname} - klasa do obliczania dat świąt ONZ
Name:		php-pear-%{_pearname}
Version:	0.1.3
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	30e0e9f0902c1c2b2c9e20e9226389ae
URL:		http://pear.php.net/package/Date_Holidays_UNO/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Date_Holidays >= 0.18.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date_Holidays helps you calculate the dates and titles of holidays and
other special celebrations. This is the driver for calculating UNO
holidays.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Date_Holidays pozwala na obliczenie dat oraz tytułów świąt oraz
specjalnych okazji. Klasa ta pozwala na wyliczenie świąt ONZ.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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
%{php_pear_dir}/Date/Holidays/Driver/UNO.php
%{php_pear_dir}/data/Date_Holidays_UNO

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Date_Holidays_UNO
