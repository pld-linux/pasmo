%define		beta beta2
Summary:	Z80 assembler
Summary(pl.UTF-8):	Asembler dla procesora Z80
Name:		pasmo
Version:	0.5.4
Release:	0.%{beta}.1
License:	GPL v2
Group:		Development/Tools
Source0:	http://pasmo.speccy.org/bin/%{name}-%{version}.%{beta}.tgz
# Source0-md5:	c85b0b7935ea174f9a57821019f464fa
URL:		http://pasmo.speccy.org/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains multiplatform Z80 cross-assembler.

%description -l pl.UTF-8
Ten pakiet zawiera wieloplatformowy asembler skrośny
dla procesora Z80.

%prep
%setup -q -n %{name}-%{version}.%{beta}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install *.asm $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README pasmodoc.html
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
