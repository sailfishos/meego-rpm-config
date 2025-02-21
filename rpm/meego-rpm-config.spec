Name:       meego-rpm-config

%define disable_docs_package 1

Summary:    Mer specific rpm configuration files (from MeeGo)
Version:    0.18-2
Release:    1
License:    GPLv2+ and GPLv3+
BuildArch:  noarch
URL:        https://github.com/sailfishos/meego-rpm-config
Source0:    meego-rpm-config-%{version}.tar.bz2

%description
Mer specific rpm configuration files.
Inherited from MeeGo

%prep
%setup -q -n %{name}-%{version}

%build

%install
%make_install

%files
%{_prefix}/lib/rpm/meego
