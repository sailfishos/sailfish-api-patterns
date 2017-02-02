Summary: Sailfish API Level 3
Name: patterns-sailfish-api-3
Version: 3.0.0
Release: 2
Source: %{name}-%{version}.tar.gz
License: GPLv2
Group: Development/System
BuildArch: noarch
Provides: sailfish-api = 3
# Begin requirements inserted by ./update.py
Requires: qt5-qtdeclarative-import-xmllistmodel
Requires: qt5-qtdeclarative-import-folderlistmodel
Requires: qt5-qtdeclarative-import-localstorageplugin
Requires: qt5-qtdeclarative-import-multimedia
Requires: qt5-qtqml-import-webkitplugin
Requires: qt5-qtdeclarative-import-particles2
Requires: qt5-qtdeclarative-qtquickparticles
Requires: qt5-qtsvg
Requires: qt5-qtgraphicaleffects
Requires: qt5-qtdeclarative-import-positioning
Requires: qt5-qtdeclarative-import-sensors
Requires: qt5-qtquickcontrols-layouts
Requires: qt5-qtdeclarative-import-models2
Requires: qt5-qtmultimedia
Requires: qt5-qtmultimedia-plugin-audio-pulseaudio
Requires: qt5-qtpositioning
Requires: qt5-plugin-imageformat-gif
Requires: qt5-plugin-imageformat-ico
Requires: qt5-plugin-imageformat-jpeg
Requires: qt5-qtsvg-plugin-imageformat-svg
Requires: libsailfishapp
Requires: SDL2
Requires: SDL2_gfx
Requires: SDL2_image
Requires: SDL2_mixer
Requires: SDL2_net
Requires: SDL2_ttf
# End requirements inserted by ./update.py

%description
Pre-installed Qt plugins and packages for allowed Harbour APIs.

%prep

%build

%install

%files
