#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Capture-Tiny
Version  : 0.48
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Capture-Tiny-0.48.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Capture-Tiny-0.48.tar.gz
Summary  : 'Capture STDOUT and STDERR from Perl, XS or external programs'
Group    : Development/Tools
License  : Apache-2.0
Requires: perl-Capture-Tiny-license
Requires: perl-Capture-Tiny-man

%description
NAME
Capture::Tiny - Capture STDOUT and STDERR from Perl, XS or external
programs

%package license
Summary: license components for the perl-Capture-Tiny package.
Group: Default

%description license
license components for the perl-Capture-Tiny package.


%package man
Summary: man components for the perl-Capture-Tiny package.
Group: Default

%description man
man components for the perl-Capture-Tiny package.


%prep
%setup -q -n Capture-Tiny-0.48

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-Capture-Tiny
cp LICENSE %{buildroot}/usr/share/doc/perl-Capture-Tiny/LICENSE
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
/usr/lib/perl5/site_perl/5.26.1/Capture/Tiny.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-Capture-Tiny/LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Capture::Tiny.3
