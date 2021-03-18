#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Readonly
Version  : 2.05
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/S/SA/SANKO/Readonly-2.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SA/SANKO/Readonly-2.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libr/libreadonly-perl/libreadonly-perl_2.050-1.debian.tar.xz
Summary  : 'Facility for creating read-only scalars, arrays, hashes'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-2.0 GPL-1.0
Requires: perl-Readonly-license = %{version}-%{release}
Requires: perl-Readonly-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
[![Build Status](https://travis-ci.org/sanko/readonly.svg?branch=master)](https://travis-ci.org/sanko/readonly)
# NAME

%package dev
Summary: dev components for the perl-Readonly package.
Group: Development
Provides: perl-Readonly-devel = %{version}-%{release}
Requires: perl-Readonly = %{version}-%{release}

%description dev
dev components for the perl-Readonly package.


%package license
Summary: license components for the perl-Readonly package.
Group: Default

%description license
license components for the perl-Readonly package.


%package perl
Summary: perl components for the perl-Readonly package.
Group: Default
Requires: perl-Readonly = %{version}-%{release}

%description perl
perl components for the perl-Readonly package.


%prep
%setup -q -n Readonly-2.05
cd %{_builddir}
tar xf %{_sourcedir}/libreadonly-perl_2.050-1.debian.tar.xz
cd %{_builddir}/Readonly-2.05
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Readonly-2.05/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Readonly
cp %{_builddir}/Readonly-2.05/LICENSE %{buildroot}/usr/share/package-licenses/perl-Readonly/9a8e1a1c1269b25c5d531236bf976917a1fcfd3f
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Readonly/4f3eabd83fac2468eebb08ac923e5a5e8a37e24a
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Readonly.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Readonly/4f3eabd83fac2468eebb08ac923e5a5e8a37e24a
/usr/share/package-licenses/perl-Readonly/9a8e1a1c1269b25c5d531236bf976917a1fcfd3f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Readonly.pm
