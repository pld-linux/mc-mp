#
# TODO:
#	- don't obsolete mc
#	- clone mc's bconds
#
Summary:	Tweaked Midnight Commander
Summary(pl):	Podrasowany Midnight Commander
Name:		mc-mp
%define	pre 	pre9
Version:	4.1.40
Release:	0.%{pre}.1
License:	GPL
Group:		Applications/Shells
Source0:	http://mc.linuxinside.com/Releases/mc-%{version}-%{pre}.tar.bz2
# Source0-md5:	9335f2b131ecf352c2c0e55a477a1c49
URL:		http://mc.linuxinside.com/
PreReq:		/sbin/chkconfig
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel >= 1.35
BuildRequires:	gettext-devel
BuildRequires:	gpm-devel
Obsoletes:	mc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's a tweaked version of popular GNU Midnight Commander. It's smaller
and more feature rich.

%description -l pl
Jest to tuningowana wersja popularnego GNU Midnight Commandera. Jest
mniejszy i posiada wiêcej opcji.

%prep
%setup -q -n mc-%{version}-%{pre}

%build
%configure \
	--with-ext2undel \
	--with-dusum \
	--with-subshell=yes \
	--with-vfs \
	--with-terminfo
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/shrc.d

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install
(cd icons; make prefix=$RPM_BUILD_ROOT%{_prefix} install_icons)

install lib/mc.{,c]sh $RPM_BUILD_ROOT/etc/shrc.d

rm -f $RPM_BUILD_ROOT%{_prefix}/lib/mc/FAQ

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(-, root, root) %doc FAQ
%attr(755,root,root) %{_bindir}/mc
%attr(755,root,root) %{_bindir}/mcedit
%attr(755,root,root) %{_bindir}/mcmfmt
%{_libdir}/mc/mc.*
%attr(755,root,root) %{_prefix}/lib/mc/bin/cons.saver
%attr(755,root,root) %{_prefix}/lib/mc/extfs/*
%{_mandir}/man1/mc.1
%{_mandir}/man1/mcedit.1
%attr(755,root,root) %config /etc/shrc.d/mc.sh
%attr(755,root,root) %config /etc/shrc.d/mc.csh
%attr(755,root,root) %dir %{_prefix}/lib/mc/
%attr(755,root,root) %dir %{_prefix}/lib/mc/bin
%attr(755,root,root) %dir %{_prefix}/lib/mc/extfs
