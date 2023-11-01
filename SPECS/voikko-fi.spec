Name:           voikko-fi
Version:        2.4
Release:        5%{?dist}
Summary:        A description of Finnish morphology written for libvoikko

License:        GPLv2+
URL:            https://voikko.puimula.org/

# See https://voikko.puimula.org/sources.html for the key fingerprint.
# I did
#  gpg --recv-keys "AC5D 65F1 0C85 96D7 E2DA  E263 3D30 9B60 4AE3 942E"
# and then
#  gpg2 --export --export-options export-minimal AC5D65F10C8596D7E2DAE2633D309B604AE3942E > gpgkey-AC5D65F10C8596D7E2DAE2633D309B604AE3942E.gpg
Source0:        https://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz
Source1:        https://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-AC5D65F10C8596D7E2DAE2633D309B604AE3942E.gpg

BuildRequires:  make
BuildRequires:  gnupg2
BuildRequires:  python3-devel
BuildRequires:  foma
# Voikko 4.3 and beyond on Fedora supports this format of the data files
BuildRequires:  voikko-tools >= 4.3

# Installing this package without libvoikko would be useless.
Requires:       libvoikko >= 4.3

BuildArch:      noarch

# This package replaces malaga-suomi-voikko
Provides:       malaga-suomi-voikko = %{version}-%{release}
Obsoletes:      malaga-suomi-voikko < 1.19-20

%description
Voikko-fi is a description of Finnish morphology written for libvoikko.
The implementation uses unweighted VFST format and provides format 5 Finnish
dictionary for libvoikko 4.0 or later. For Voikko the morphology supports
spell checking, hyphenation and grammar checking.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%make_build vvfst

%install
# Upstream uses /usr/lib/voikko as the data file location.
# Zbigniew Jędrzejewski-Szmek recommended using the upstream default on the
# mailing list, see
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GY6NGGNLK5DIDXOXVGBDA5QONISQOFL7/
make vvfst-install DESTDIR=$RPM_BUILD_ROOT%{_prefix}/lib/voikko


%files
%doc ChangeLog CONTRIBUTORS README.md
%license COPYING
%{_prefix}/lib/voikko/5

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 2.4-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.4-4
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Sat Jan 30 2021 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.4-3
- More review fixes:
- BuildRequire python3-devel

* Sat Jan 30 2021 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.4-2
- Review fixes:
- Fix Obsoletes
- Use the prefix macro in the dictionary path
- Use the license macro
- Do not own the whole data directory, just the version 5 subdirectory

* Sat Jan 16 2021 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.4-1
- Initial package
