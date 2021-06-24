Name:           perl-Mojo-IOLoop-ReadWriteProcess
Version:        0.28
Release:        4%{?dist}
Summary:        Execute external programs or internal code blocks as separate process
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Mojo-IOLoop-ReadWriteProcess/
Source0:        https://cpan.metacpan.org/authors/id/S/SZ/SZARATE/Mojo-IOLoop-ReadWriteProcess-%{version}.tar.gz
# https://github.com/mudler/Mojo-IOLoop-ReadWriteProcess/pull/15
# Fix prctl syscall detection on Fedora 32-bit ARM
Patch0:         0001-Match-on-armv7l-as-well-as-arm-for-prctl-detection.patch

BuildArch:      noarch
# Build requirements
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run requirements
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(IPC::SysV)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Collection)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojo::IOLoop::Stream)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(constant)
# Test requirements
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(utf8)

Requires:       perl(Mojo::EventEmitter)
Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
Mojo::IOLoop::ReadWriteProcess is yet another process manager.
It executes external programs or internal code blocks as separate process

%prep
%autosetup -p1 -n Mojo-IOLoop-ReadWriteProcess-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Mojo*
%{_mandir}/man3/Mojo*

%changelog
* Thu Jun 24 2021 Adam Williamson <awilliam@redhat.com> - 0.28-4
- Backport PR #15 to fix prctl syscall detection on Fedora 32-bit ARM

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 04 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.28-1
- Update to 0.28

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.27-1
- Update to 0.27

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-2
- Perl 5.32 rebuild

* Sun Apr 12 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.25-1
- Update to 0.25
- Use /usr/bin/perl instead of %%{__perl}

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 17 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.24-1
- Update to 0.24 (#1761834, #1745926)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.23-1
- Update to 0.23

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-2
- Perl 5.28 rebuild

* Mon May 21 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.20-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
