Summary:	Pidgin plugin to stop spammers from annoying you
Name:		pidgin-privacy-please
Version:	0.3.0
Release:	%mkrel 2
License:	GPL
Group:		Networking/Instant messaging
Url:		http://tools.desire.ch/pidgin-pp
Source0:	http://tools.desire.ch/data/pidgin-pp/files/%{name}-%{version}.tar.bz2
BuildRequires:	pidgin-devel
Requires:	pidgin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Pidgin-privacy-please offers the following features:

- Block certain users (with an optional auto-reply)
- Block messages from people who are not on your contact 
  list (with an optional auto-reply)
- Suppress repeated authorization requests 

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/pidgin/libpidgin_pp.la
%{_libdir}/pidgin/libpidgin_pp.so