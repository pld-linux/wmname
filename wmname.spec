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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmname prints/sets the window manager name property of the root window
similar to how hostname behaves. wmname is a nice utility to fix
problems with JDK versions and other broken programs assuming a
reparenting window manager for instance.

%prep
%setup -q
cat > Makefile <<'EOF'
NAME = wmname
OBJS = $(NAME).o
LIBS = -lX11
LD = $(CC)

CPPFLAGS = -DVERSION=\"%{version}\" $(OPTCPPFLAGS)
# vim: "
CFLAGS = -std=c99 -pedantic -Wall $(OPTCFLAGS)

all: $(NAME)

$(NAME): $(OBJS)
	$(LD) $(CFLAGS) $(LDFLAGS) -o $@ $< $(LIBS)

%.o: %.c
	$(CC) $(CPPFLAGS) $(CFLAGS) -c -o $@ $<

.PHONY: all
EOF

%build
%{__make} \
	CC="%{__cc}" \
	OPTCPPFLAGS="%{rpmcppflags}" \
	OPTCFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
