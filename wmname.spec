Summary:	wmname prints/sets the window manager name property of the root window
Name:		wmname
Version:	0.1
Release:	0.1
License:	MIT/X
Group:		Applications
Source0:	http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
# Source0-md5:	6903d299f84d335e529fbd2c1d6e49fe
URL:		http://www.suckless.org/programs/wmname.html
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmname prints/sets the window manager name property of the root window
similar to how hostname(1) behaves. wmname is a nice utility to fix
problems with JDK versions and other broken programs assuming a
reparenting window manager for instance.

%prep
%setup -q

%build
%{__make} \
	PREFIX=%{_prefix} \
	CFLAGS="%{rpmcflags} -DVERSION='\"%{version}\"'"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
