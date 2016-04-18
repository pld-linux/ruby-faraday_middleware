%define pkgname faraday_middleware
Summary:	Various middleware for Faraday
Name:		ruby-%{pkgname}
Version:	0.10.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	229fb5d80723a23cf1e2abe965152e07
URL:		https://github.com/lostisland/faraday_middleware
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Requires:	ruby-faraday >= 0.7.4
Requires:	ruby-faraday < 0.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various middleware for Faraday

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
