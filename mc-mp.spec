%define	version	4.1.40
%define	pre 	pre9
%define name_sufix mp
%define name_general mc

Summary:	Tweaked Midnight Commander.
Name:		%{name_general}-%{name_sufix}
Version:	%{version}
Release:	1
License:	GPL
Group:		Application/Shells
Source0:	http://mc.linuxinside.com/Releases/%{name_general}-%{version}-%{pre}.tar.bz2
URL:		http://mc.linuxinside.com
Requires:	pam >= 0.77
BuildRequires:	e2fsprogs-devel >= 1.35
BuildRequires:	slang-devel >= 1.4.9
BuildRequires:	gpm-devel
BuildRequires:	gettext-devel
BuildRequires:	autoconf
BuildRequires:	automake
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	mc
Prereq:		/sbin/chkconfig

%description
It's a tweaked version of popular GNU Midnight Commander. It's smaller
and more feature rich.

%description -l pl
Jest to tuningowana wersja popularnego GNU Midnight Commander. Jest
mniejszy i posiada wiecej opcji.

%package -n mcserv
Summary:	Midnight Commander file server
Group:		Deamons
######		Unknown group!
Requires:	portmap

%description -n mcserv
mcserv is the server program for the Midnight Commander networking
file system. It provides access to the host file system to clients
running the Midnight file system (currently, only the Midnight
Commander file manager).

%description -n mcserv -l pl
Mcserv jest aplikacj± dla sieciowego systemu plików Midnight
Commandera. Pozwala na dostêp do systemu plików dla klienta
pracuj±cego pod MC i u¿ywaj±cego jego systemu plików.

%prep
%setup -q -n %{name_general}-%{version}-%{pre}

%build
	--with-ext2undel \
	--with-dusum \
	--with-subshell=yes \
	--with-vfs \
	--with-terminfo
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -d $RPM_BUILD_ROOT/etc/{pam.d,profile.d}

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install
(cd icons; make prefix=$RPM_BUILD_ROOT%{_prefix} install_icons)
install lib/mcserv.init $RPM_BUILD_ROOT/etc/rc.d/init.d/mcserv

install lib/mcserv.pamd $RPM_BUILD_ROOT/etc/pam.d/mcserv
install lib/{mc.sh,mc.csh} $RPM_BUILD_ROOT/etc/profile.d

rm -f $RPM_BUILD_ROOT%{_prefix}/lib/mc/FAQ
strip $RPM_BUILD_ROOT%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%post -n mcserv
/sbin/chkconfig --add mcserv

%postun -n mcserv
if [ "$1" = 0 ] ; then
  /sbin/chkconfig --del mcserv
fi

%files
%defattr(644,root,root,755)
%attr(-, root, root) %doc FAQ
%attr(755, root, root) %{_bindir}/mc
%attr(755, root, root) %{_bindir}/mcedit
%attr(755, root, root) %{_bindir}/mcmfmt
%attr(644, root, root) %{_prefix}/lib/mc/mc.ext
%attr(644, root, root) %{_prefix}/lib/mc/mc.hint
%attr(644, root, root) %{_prefix}/lib/mc/mc.hlp
%attr(644, root, root) %{_prefix}/lib/mc/mc.lib
%attr(644, root, root) %{_prefix}/lib/mc/mc.menu
%attr(755, root, root) %{_prefix}/lib/mc/bin/cons.saver
%attr(755, root, root) %{_prefix}/lib/mc/extfs/*
%attr(644, root, man) %{_prefix}/man/man1/mc.1
%attr(644, root, man) %{_prefix}/man/man1/mcedit.1
%attr(755, root, root) %config /etc/profile.d/mc.sh
%attr(755, root, root) %config /etc/profile.d/mc.csh
%attr(755, root, root) %dir %{_prefix}/lib/mc/
%attr(755, root, root) %dir %{_prefix}/lib/mc/bin
%attr(755, root, root) %dir %{_prefix}/lib/mc/extfs

%files -n mcserv
%defattr(644,root,root,755)
%attr(644, root, root) %config /etc/pam.d/mcserv
%attr(755, root, root) %config /etc/rc.d/init.d/mcserv
%attr(644, root, man) %{_prefix}/man/man8/mcserv.8
%attr(755, root, root) %{_bindir}/mcserv
