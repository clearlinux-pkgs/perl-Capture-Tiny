#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Capture-Tiny
Version  : 0.34
Release  : 9
URL      : http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/Capture-Tiny-0.34.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/Capture-Tiny-0.34.tar.gz
Summary  : 'Capture STDOUT and STDERR from Perl, XS or external programs'
Group    : Development/Tools
License  : Apache-2.0
Requires: perl-Capture-Tiny-doc

%description
NAME
Capture::Tiny - Capture STDOUT and STDERR from Perl, XS or external
programs

%package doc
Summary: doc components for the perl-Capture-Tiny package.
Group: Documentation

%description doc
doc components for the perl-Capture-Tiny package.


%prep
%setup -q -n Capture-Tiny-0.34

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/Capture/Tiny.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
