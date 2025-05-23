#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Capture-Tiny
Version  : 0.50
Release  : 59
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Capture-Tiny-0.50.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Capture-Tiny-0.50.tar.gz
Summary  : 'Capture STDOUT and STDERR from Perl, XS or external programs'
Group    : Development/Tools
License  : Apache-2.0
Requires: perl-Capture-Tiny-license = %{version}-%{release}
Requires: perl-Capture-Tiny-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Capture::Tiny - Capture STDOUT and STDERR from Perl, XS or external
programs

%package dev
Summary: dev components for the perl-Capture-Tiny package.
Group: Development
Provides: perl-Capture-Tiny-devel = %{version}-%{release}
Requires: perl-Capture-Tiny = %{version}-%{release}

%description dev
dev components for the perl-Capture-Tiny package.


%package license
Summary: license components for the perl-Capture-Tiny package.
Group: Default

%description license
license components for the perl-Capture-Tiny package.


%package perl
Summary: perl components for the perl-Capture-Tiny package.
Group: Default
Requires: perl-Capture-Tiny = %{version}-%{release}

%description perl
perl components for the perl-Capture-Tiny package.


%prep
%setup -q -n Capture-Tiny-0.50
cd %{_builddir}/Capture-Tiny-0.50
pushd ..
cp -a Capture-Tiny-0.50 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Capture-Tiny
cp %{_builddir}/Capture-Tiny-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Capture-Tiny/b25ccab179a573d5cf91255aefe65a7622bcb32e || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Capture::Tiny.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Capture-Tiny/b25ccab179a573d5cf91255aefe65a7622bcb32e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
