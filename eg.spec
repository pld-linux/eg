Summary:	Norton Guide reader for GNU/Linux
Summary(pl):	Czytnik plików Norton Guide dla GNU/Linuksa
Name:		eg
Version:	1.00
Release:	2
License:	GPL
Group:		Applications
Source0:	http://www.davep.org/norton-guides/%{name}-%{version}.tar.gz
# Source0-md5:	8c7a5b75fbc670edd01821e8bcc9297c
Patch0:		%{name}-gcc34.patch
URL:		http://www.davep.org/norton-guides/
BuildRequires:	slang-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Expert Guide is a text based Norton Guide reader.

%description -l pl
Expert Guide jest tekstowym czytnikiem plików w formacie Norton Guide.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/norton-guides}

install eg $RPM_BUILD_ROOT%{_bindir}
install	eg.1 $RPM_BUILD_ROOT%{_mandir}/man1
install default-guide/eg.ng $RPM_BUILD_ROOT%{_datadir}/norton-guides

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS Changes README TODO
%attr(755,root,root) %{_bindir}/eg
%{_mandir}/man1/*
%{_datadir}/norton-guides
