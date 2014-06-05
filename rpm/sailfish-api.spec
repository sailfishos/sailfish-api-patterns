Summary: Sailfish OS Harbour Third Party API
Name: sailfish-api
Version: 1.0.0
Release: 1
Source: %{name}-%{version}.tar.gz
URL: https://harbour.jolla.com/faq
License: ISC
Group: Development/System
BuildArch: noarch
# Begin requirements inserted by update.py
Requires: qt5-qtdeclarative-import-xmllistmodel
Requires: qt5-qtdeclarative-import-folderlistmodel
Requires: qt5-qtdeclarative-import-localstorageplugin
Requires: qt5-qtdeclarative-import-multimedia
Requires: qt5-qtqml-import-webkitplugin
Requires: qt5-qtdeclarative-import-particles2
Requires: qt5-qtdeclarative-qtquickparticles
Requires: qt5-qtsvg
Requires: qt5-qtfeedback
Requires: qt5-qtmultimedia
Requires: qt5-plugin-imageformat-gif
Requires: qt5-plugin-imageformat-ico
Requires: qt5-plugin-imageformat-jpeg
Requires: qt5-qtsvg-plugin-imageformat-svg
# End requirements inserted by update.py

%description
Pre-installed Qt plugins and packages for allowed Harbour APIs.

%prep
%setup -q

%build
true

%install
true

%files
