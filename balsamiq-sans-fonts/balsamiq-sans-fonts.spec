%global fontname balsamiq-sans
%global fontconf 62-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 1.010
Release: 1%{?dist}
Summary: Balsamiq Sans is the handwritten font created for the Balsamiq Wireframes.

Group:   User Interface/X
License: OFL
URL:     https://fonts.google.com/specimen/Balsamiq+Sans
Source0: %{name}-%{version}.tar.xz
Source1: %{fontname}-fontconfig.conf
Source2: get-%{fontname}.sh

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
The font contains 942 glyphs in 2 weights with italics/obliques, and
includes the basic and extended latin character set, Cyrillic, Basic
Symbols and Dingbats, Math and Technical Symbols, and punctuation
To contribute, see https://github.com/balsamiq/balsamiqsans

%prep
%setup -q

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

mv OFL.txt LICENSE
sed -i 's/\r$//' LICENSE

%_font_pkg -f %{fontconf} *.ttf
%license LICENSE

%changelog
* Sat Oct 31 2020 Dawid Zych <dawid.zych@yandex.com> - 1.010-1
- Initial packaging.
