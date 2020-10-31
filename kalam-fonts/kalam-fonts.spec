%global fontname kalam
%global fontconf 62-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 2.001
Release: 1%{?dist}
Summary: Kalam is a handwriting-style typeface supporting the Devanagari and Latin scripts.

Group:   User Interface/X
License: OFL
URL:     https://fonts.google.com/specimen/Kalam
Source0: %{name}-%{version}.tar.xz
Source1: %{fontname}-fontconfig.conf
Source2: get-%{fontname}.sh

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Kalam is a handwriting font family that supports the Devanagari and
Latin writing systems. Even though Kalam's letterforms derive from
handwriting, the fonts have each been optimized for text usage on
screen. All in all, the typeface is a design that feels very personal.
Like many informal handwriting-style fonts, it appears rather fresh and
new when seen on screen or printed on the page.
Kalam's letterforms feature a very steep slant from the top right to the
bottom left. They are similar to letters used in everyday handwriting,
and look like they might have been written with either a thin felt-tip
pen, or a ball-point pen. In the Devanagari letterforms, the
knotted-terminals are open, but some other counter forms are closed.
Features like these strengthen the feeling that text set in this
typeface has been written very quickly, in a rapid manner. 

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
* Sat Oct 31 2020 Dawid Zych <dawid.zych@yandex.com> - 2.001-1
- Initial packaging.
