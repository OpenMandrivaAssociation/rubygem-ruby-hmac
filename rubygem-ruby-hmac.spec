%define	oname	ruby-hmac

Summary:	A ruby module that provides a common interface to HMAC functionality
Name:		rubygem-%{oname}
Version:	0.4.0
Release:	%mkrel 2
License:	MIT
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
BuildArch:	noarch

%description
This module provides a common interface to HMAC functionality.
HMAC is a kind of "Message Authentication Code" (MAC) algorithm whose standard
is documented in RFC2104. Namely, a MAC provides a way to check the integrity
of information transmitted over or stored in an unreliable medium, based on a
secret key.

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec

