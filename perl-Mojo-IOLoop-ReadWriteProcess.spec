Name:           perl-Mojo-IOLoop-ReadWriteProcess
Version:        0.23
Release:        2%{?dist}
Summary:        Execute external programs or internal code blocks as separate process
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Mojo-IOLoop-ReadWriteProcess/
Source0:        https://cpan.metacpan.org/authors/id/M/MU/MUDLER/Mojo-IOLoop-ReadWriteProcess-%{version}.tar.gz

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
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Mojo::IOLoop::ReadWriteProcess is yet another process manager.

%prep
%setup -q -n Mojo-IOLoop-ReadWriteProcess-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
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
