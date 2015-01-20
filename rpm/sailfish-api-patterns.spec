Summary: Sailfish OS Harbour Third Party API Patterns
Name: sailfish-api-patterns
Version: 1.0.3
Release: 1
Source: %{name}-%{version}.tar.gz
URL: https://harbour.jolla.com/faq
License: GPL
Group: Development/System
BuildArch: noarch
BuildRequires: repomd-pattern-builder
Provides: package-groups

%description
Pre-installed Qt plugins and packages for allowed Harbour APIs.

%prep
%setup -q

%build
true

%install
/usr/bin/repomd-pattern-builder.py \
    --patternxml \
    --patterndir ./patterns/ \
    --outputdir %{buildroot}/usr/share/package-groups/ \
    --version %{version} \
    --release %{release}

%files
%defattr(-,root,root,-)
%{_datadir}/package-groups/sailfish-api-*.xml
