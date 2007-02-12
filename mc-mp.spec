#
# Conditional build:
%bcond_with	ext2undel	# with ext2 undelete fs
%bcond_with	x		# without text edit in X support
#
# TODO:
#	- don't obsolete mc
#
%define	pre 	pre9
# Source0-md5:	9335f2b131ecf352c2c0e55a477a1c49
Summary:	Tweaked Midnight Commander
Summary(pl.UTF-8):   Podrasowany Midnight Commander
Name:		mc-mp
Version:	4.1.40
Release:	0.%{pre}.3
License:	GPL v2
Group:		Applications/Shells
URL:		http://mc.linuxinside.com/
%{?with_x:BuildRequires:	XFree86-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_ext2undel:BuildRequires:	e2fsprogs-devel >= 1.35}
BuildRequires:	gettext-devel
BuildRequires:	gpm-devel
Source0:	http://mc.linuxinside.com/Releases/mc-%{version}-%{pre}.tar.bz2
Conflicts:	mc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's a tweaked version of popular GNU Midnight Commander. It's smaller
and more feature rich.

%description -l pl.UTF-8
Jest to tuningowana wersja popularnego GNU Midnight Commandera. Jest
mniejszy i posiada więcej opcji.

%prep
%setup -q -n mc-%{version}-%{pre}

%build
#%{__aclocal}
./mc.configure \
	%{?with_debug:--with-debug --with-efence} \
	--with%{!?with_ext2undel:out}-ext2undel \
	--with%{!?with_x:out}-x \
	--with-vfs \
	--with-gpm-mouse \
	--with-included-slang \
	--with-edit \
	--with-dusum \
	--with-subshell \
	--with-terminfo
%{__make}
#%find_lang %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/shrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir}/man1 \
	man8dir=%{_mandir}/man8

#(cd icons; make prefix=$RPM_BUILD_ROOT%{_prefix} install_icons)

install lib/mc.{,c}sh $RPM_BUILD_ROOT/etc/shrc.d

rm -f $RPM_BUILD_ROOT%{_prefix}/lib/mc/FAQ

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/mc
%{_libdir}/mc/mc.*
%dir %{_libdir}/mc/bin
%attr(755,root,root) %{_libdir}/mc/bin/*
%dir %{_libdir}/mc/extfs
%{_libdir}/mc/extfs/extfs.ini
%attr(755,root,root) %{_libdir}/mc/extfs/rpm
%attr(755,root,root) %{_libdir}/mc/extfs/a
%attr(755,root,root) %{_libdir}/mc/extfs/audio
%attr(755,root,root) %{_libdir}/mc/extfs/deb
%attr(755,root,root) %{_libdir}/mc/extfs/hp48
%attr(755,root,root) %{_libdir}/mc/extfs/lha
%attr(755,root,root) %{_libdir}/mc/extfs/mailfs
%attr(755,root,root) %{_libdir}/mc/extfs/rar
%attr(755,root,root) %{_libdir}/mc/extfs/uarj
%attr(755,root,root) %{_libdir}/mc/extfs/zip
%attr(755,root,root) %{_libdir}/mc/extfs/arfs
%attr(755,root,root) %{_libdir}/mc/extfs/cpio
%attr(755,root,root) %{_libdir}/mc/extfs/esp
%attr(755,root,root) %{_libdir}/mc/extfs/ftplist
%attr(755,root,root) %{_libdir}/mc/extfs/iso
%attr(755,root,root) %{_libdir}/mc/extfs/lslR
%attr(755,root,root) %{_libdir}/mc/extfs/patchfs
%attr(755,root,root) %{_libdir}/mc/extfs/trpm
%attr(755,root,root) %{_libdir}/mc/extfs/uha
%attr(755,root,root) %{_libdir}/mc/extfs/zoo
%dir %{_libdir}/mc/syntax
%{_libdir}/mc/syntax/*
%dir %{_libdir}/mc/term
%{_libdir}/mc/term/*
%dir %{_libdir}/mc/codepages
%{_libdir}/mc/codepages/*
%{_mandir}/man1/*
%{_mandir}/man8/*
%attr(755,root,root) %config /etc/shrc.d/mc.sh
%attr(755,root,root) %config /etc/shrc.d/mc.csh
