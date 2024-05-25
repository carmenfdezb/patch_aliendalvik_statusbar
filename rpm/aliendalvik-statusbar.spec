Name:       aliendalvik-statusbar

BuildArch: noarch

Summary:    Aliendalvik statusbar
Version:    1.0.1
Release:    1
Group:      Qt/Qt
License:    WTFPL
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
URL:        https://github.com/carmenfdezb

%description
Shows aliendalvik icon in statusbar when ad is running

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/patchmanager/patches/%{name}
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%{name}

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}

%changelog
* Sat May 25 2024 Carmen Fdez. B. 1.0.1-1
- Support sfos 4.6

* Fri Aug 05 2022 Carmen Fdez. B. 1.0.0-1
- Initial release
