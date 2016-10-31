Name:       meego-rpm-config

%define disable_docs_package 1

Summary:    Mer specific rpm configuration files (from MeeGo)
Version:    0.18
Release:    1
Group:      Development/System
License:    GPL+
BuildArch:  noarch
URL:        http://git.merproject.org/mer-core/meego-rpm-config
Source0:    meego-rpm-config-%{version}.tar.bz2

%description
Mer specific rpm configuration files.
Inherited from MeeGo

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
make DESTDIR=${RPM_BUILD_ROOT} install

%files
%defattr(-,root,root,-)
%{_prefix}/lib/rpm/meego
