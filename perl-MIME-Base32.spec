%define upstream_name    MIME-Base32
Name:		perl-%{upstream_name}
Version:	1.303
Release:	1

Summary:	Base32 encoder / decoder
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MIME/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Encode data similar way like MIME::Base64 does.

Main purpose is to create encrypted text used as id or key entry
typed-or-submitted by user. It is upper/lowercase safe (not sensitive).

%prep
#setup -q -n %{upstream_name}-%{version}
%setup -q -n MIME-Base32-1.303

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/MIME


%changelog
* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.20.0a-1mdv2011.0
+ Revision: 573806
- update to 1.02a

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 403860
- rebuild using %1.02a Tue Sep 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2009.0
+ Revision: 283306
- import perl-MIME-Base32


* Tue Sep 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2009.0
- initial mdv release, generated with cpan2dist

