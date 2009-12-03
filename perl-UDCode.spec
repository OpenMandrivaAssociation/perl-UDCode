%define upstream_name    UDCode
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Does a set of code words form a uniquely decodable code?
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorlib/*


