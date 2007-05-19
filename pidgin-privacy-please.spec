Summary:	Pidgin plugin to stop spammers from annoying you
Name:		pidgin-privacy-please
Version:	0.3.0
Release:	%mkrel 1
License:	GPL
Group:		Internet
Url:		http://tools.desire.ch/pidgin-pp
Source0:	http://tools.desire.ch/data/pidgin-pp/files/%{name}-%{version}.tar.bz2
BuildRequires:	pidgin-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description

%prep
%setup -q %{name}-%{version}
Pidgin-privacy-please offers the following features:

- Block certain users (with an optional auto-reply)
- Block messages from people who are not on your contact 
  list (with an optional auto-reply)
- Suppress repeated authorization requests 

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%post
%{update_menus}
%if %mdkversion >= 200700
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%postun
%{clean_menus}
%if %mdkversion >= 200700
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root)
