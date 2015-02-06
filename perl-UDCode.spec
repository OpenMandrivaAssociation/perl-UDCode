%define upstream_name    UDCode
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Does a set of code words form a uniquely decodable code?
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MJ/MJD/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
A code is a set of strings, called the _code words_. A code is "uniquely
decodable" if any string _S_ that is a concatenation of code words is so in
_exactly one way_.

For example, the code '"ab", "abba", "b"' is _not_ uniquely decodable,
because '"abba" . "b" eq "ab" . "b" . "ab"'. But the code '"a", "ab",
"abb"' _is_ uniquely decodable, because there is no such pair of sequences
of code words.

'is_udcode'
    'is_udcode(@words)' returns true if and only if the specified code is
    uniquely decodable.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.30.0-2mdv2011.0
+ Revision: 654340
- rebuild for updated spec-helper

* Thu Dec 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 472799
- import perl-UDCode


* Thu Dec 03 2009 cpan2dist 1.03-1mdv
- initial mdv release, generated with cpan2dist
