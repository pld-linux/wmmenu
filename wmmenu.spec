Summary:	wmmenu - popup dock menus for WindowMaker
Summary(pl.UTF-8):	wmmenu - chowane menu dla WindowMakera
Name:		wmmenu
Version:	1.2
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.fcoutant.freesurf.fr/download/%{name}-%{version}.tar.gz
# Source0-md5:	0cc8970ff54182a08fe848d65546f70f
URL:		http://www.fcoutant.freesurf.fr/wmmenu.html
BuildRequires:	XFree86-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	libdockapp-devel >= 0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/Apps/wmmenu

%description
Popup menu of icons for WindowMaker like in AfterStep, as a dockable
application.

%description -l pl.UTF-8
Chowane menu złożone z ikon dla WindowMakera, podobne do tego, które
znaleźć można w AfterStepie.

%prep
%setup -q -n wmmenu

%build
%{__make} \
	prefix=%{_prefix} \
	ETCDIR=%{_sysconfdir} \
	MANDIR=%{_mandir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}
install example/{apps,defaults} $RPM_BUILD_ROOT%{_sysconfdir}
install example/extract_icon_back $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	ETCDIR=$RPM_BUILD_ROOT%{_sysconfdir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%config %{_sysconfdir}
%{_mandir}/man1/wmmenu.1*
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/extract_icon_back
