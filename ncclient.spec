%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from %distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:	        python-ncclient	
Version:	0.3
Release:	1%{?dist}
Summary:        Python library for NETCONF clients	

Group:		Development/Tools
License:	Apache 2.0
URL:		http://github.com/CiscoSystems/ncclient
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	python-setuptools

BuildArch:      noarch

%description
ncclient is a Python library that facilitates client-side scripting and application development around the NETCONF protocol.

%prep
%setup -q


%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README
%{python_sitelib}/ncclient/
%{python_sitelib}/ncclient*.egg-info


%changelog
* Mon Oct 07 2013 Pradeep Kilambi <pkilambi@cisco.com> 0.3-1
- new package built with tito



