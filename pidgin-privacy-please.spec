Summary:	Pidgin plugin to stop spammers from annoying you
Name:		pidgin-privacy-please
Version:	0.7.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Networking/Instant messaging
Url:		http://code.google.com/p/pidgin-privacy-please/
Source0:	http://pidgin-privacy-please.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	pidgin-devel
BuildRequires:	intltool
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
%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/pidgin/libpidgin_pp.la
%{_libdir}/pidgin/libpidgin_pp.so
