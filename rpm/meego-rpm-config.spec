
# ignore the explicit bash requires from the kernel mod scripts
%define __requires_exclude ^/bin/bash$
Name:       meego-rpm-config
Summary:    Mer specific rpm configuration files (from MeeGo)
Version:    0.18-2
Release:    1
Group:      Development/System
License:    GPLv2+ and GPLv3+
BuildArch:  noarch
URL:        http://git.merproject.org/mer-core/meego-rpm-config
Source0:    meego-rpm-config-%{version}.tar.bz2
#!BuildIgnore:  rpm-config-SUSE
# RPM owns the directories we need
Requires:       rpm

%description
Mer specific rpm configuration files.
Inherited from MeeGo

%prep
%setup -q -n %{name}-%{version}

%build

%install
# Install vendor dependency generators
cp -a fileattrs %{buildroot}%{_rpmconfigdir}
cp -a scripts/* %{buildroot}%{_rpmconfigdir}
cp -a macros.d %{buildroot}%{_rpmconfigdir}

%files
%license COPYING
%doc README.md
%{_rpmconfigdir}/%vendor/
%{_rpmconfigdir}/macros.d/macros.*
%{_rpmconfigdir}/fileattrs/*
%{_rpmconfigdir}/brp-%vendor
%{_rpmconfigdir}/firmware.prov
%{_rpmconfigdir}/sysvinitdeps.sh
%{_rpmconfigdir}/locale.prov
# kmod deps
%{_rpmconfigdir}/find-provides.ksyms
%{_rpmconfigdir}/find-requires.ksyms
%{_rpmconfigdir}/find-supplements.ksyms
