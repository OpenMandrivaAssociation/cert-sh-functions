Summary:	Helper functions for SSL certificate generation
Name:		cert-sh-functions
Version:	1.0.2
Release:	6
License:	GPL
Group:		System/Base
Url:		http://git.altlinux.org/gears/c/cert-sh-functions.git
Source0:	%{name}-%{version}.tar
Requires:	openssl
Requires:	openssl-config
Requires:	/bin/sh
BuildArch:	noarch

%description
Helper functions for SSL certificate generation (from ALT Linux).

%files
%doc README
%{_bindir}/cert-sh
%{_bindir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q

%install
install -Dpm755 cert-sh %{buildroot}%{_bindir}/cert-sh
install -Dpm644 %{name} %{buildroot}%{_bindir}/%{name}

