Summary:	wmmenu - popup dock menus for WindowMaker
Summary(pl):	wmmenu - chowane menu dla WindowMakera
Name:		wmmenu
Version:	0.9
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://www.fcoutant.freesurf.fr/download/%{name}-%{version}.tar.gz
URL:		http://www.fcoutant.freesurf.fr/wmmenu.html
BuildRequires:	XFree86-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	libdockapp-devel >= 0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11

%description
Popup menu of icons for WindowMaker like in AfterStep, as a dockable
application.

%description -l pl
Chowane menu z³o¿one z ikon dla WindowMakera, podobne do tego, które
znale¼æ mo¿na w AfterStepie.

%prep
%setup -q -n wmmenu

%build
%{__make} \
	prefix=%{_prefix} \
	ETCDIR=%{_sysconfdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	ETCDIR=$RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nf README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}
