Summary:	wmmenu - popup dock menus for WindowMaker
Summary(pl):	wmmenu - chowane menu dla WindowMakera
Name:		wmmenu
Version:	0.8
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source:		http://www.fcoutant.freesurf.fr/download/%{name}-%{version}.tar.gz
URL:		http://www.fcoutant.freesurf.fr/wmmenu.html
BuildRequires:	XFree86-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	libdockapp-devel >= 0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
Popup menu of icons for WindowMaker like in AfterStep,
as a dockable application.

%description -l pl
Chowane menu z³o¿one z ikon dla WindowMakera, podobne do tego,
które znale¼æ mo¿na w AfterStepie.

%prep
%setup -q -n wmmenu

%build
%{__make} prefix=%{_prefix} ETCDIR=%{_etcdir}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/%{_etcdir}
%{__make} install prefix=$RPM_BUILD_ROOT/%{_prefix} \
                  ETCDIR=$RPM_BUILD_ROOT/%{_etcdir}

gzip -9nf README TODO

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}

%files
%defattr(644,root,root,755)
%doc {README,TODO}.gz
%attr(755,root,root) %{_bindir}/%{name}
