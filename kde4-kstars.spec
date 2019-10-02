# TODO: astrometry.net
%define		_state		stable
%define		orgname		kstars

Summary:	K Desktop Environment - Desktop planetarium
Summary(pl.UTF-8):	K Desktop Environment - Planetarium
Name:		kde4-kstars
Version:	4.14.3
Release:	6
License:	GPL v2+
Group:		X11/Applications/Science
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	13cb96789e3be237239e04c027b45c0b
URL:		http://www.kde.org/
BuildRequires:	OpenGL-devel
BuildRequires:	automoc4
BuildRequires:	cfitsio-devel >= 3.09
BuildRequires:	eigen3 >= 3
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libindi-devel >= 0.9.8
# for tests only
#BuildRequires:	qjson-devel
BuildRequires:	qt4-build >= 4
BuildRequires:	wcslib-devel
BuildRequires:	xplanet
# solve-field program (to achieve sub-arcsecond GOTO tracking and determine polar alignment errors in the mount)
#Suggests	astrometrynet
# for updating supernovae data
Suggests:	python-PyKDE4
Suggests:	xplanet
Obsoletes:	kde4-kdeedu-kstars < 4.6.99
Obsoletes:	kstarts <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KStars lets you explore the night sky from the comfort of your
computer chair. It provides an accurate graphical representation of
the night sky for any date, from any location on Earth. The display
includes 126,000 stars to 9th magnitude (well below the naked-eye
limit), 13,000 deep-sky objects (Messier, NGC and IC catalogs), all
planets, the Sun and Moon, hundreds of comets and asteroids, the Milky
Way, 88 constellations, and guide lines such as the celestial equator,
the horizon and the ecliptic.

%description -l pl.UTF-8
KStars pozwala przeglądać nocne niebo z wygodą krzesła przy
komputerze. Dostarcza dokładną graficzną reprezentację nocnego nieba
dla dowolnej daty, z dowolnego miejsca na Ziemi. Obraz zawiera 126000
gwiazd do 9. wielkości (znacznie poza zasięgiem nieuzbrojonego oka),
13000 obiektów (katalogi Messiera, NGC i IC), wszystkie planety,
Słońce i Księżyc, setki komet i asteroid, Drogę Mleczną, 88
konstelacji oraz linie prowadzące takie jak równik astronomiczny,
horyzont i ekliptykę.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# no headers installed
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libhtmesh.a

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README* TODO
%attr(755,root,root) %{_bindir}/kstars
%{_desktopdir}/kde4/kstars.desktop
%{_datadir}/config.kcfg/kstars.kcfg
%{_datadir}/config/kstars.knsrc
%{_datadir}/appdata/kstars.appdata.xml
%{_datadir}/apps/kstars
%{_iconsdir}/hicolor/*x*/apps/kstars.png
%{_iconsdir}/hicolor/scalable/apps/kstars.svgz
