Summary:	Simple SQL monitor for common database system (PgSQL, Oracle and others)
Summary(pl.UTF-8):	Prosty interfejs do popularnych baz danych (PgSWL, Oracle itp.)
Name:		dbman
Version:	0.1.0
Release:	5
License:	GPL QPL BSD Eiffel Artistic Aladdin
Group:		Applications/Databases/Interfaces
Source0:	http://www.fi.muni.cz/~xsorm/%{name}/ftp/%{name}-%{version}.tar.gz
# Source0-md5:	4db94ad612538981335fa31d16fa0785
Patch0:		%{name}-FHS.patch
URL:		http://www.fi.muni.cz/~xsorm/dbman/
BuildRequires:	perl-DBI
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoprovfiles	%{_datadir}/%{name}/.*
%define	_noautoreq		'perl(Compact)' 'perl(Plugin)' 'perl(dbMan.*)' 'perl(nDB[ID].*)'

%description
dbMan is a simple SQL monitor for common database system (PgSQL,
Oracle). It's based on Perl, Tk (include Tix) and DBI interfaces (nDBI
specification).

%description -l pl.UTF-8
dbMan to prosty interfejs SQL do popularnych baz danych. Wykorzystuje
on Perla, Tk oraz interfejs DBI.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_datadir}/%{name}/{plugins,nDBD,nonTk,nDBI/Statement}}

install dbman czdbman dedbman dbman-bug dbman-proxy dbman-le \
	dbman-le-default xdbish tdesigner cztdesigner \
	$RPM_BUILD_ROOT%{_bindir}
install dbman-sql-server $RPM_BUILD_ROOT%{_sbindir}/dbman-sql-server
install splash.gif folder.xbm openfolder.xbm viewfolder.xbm database.xbm \
	Plugin.pm checksum dbManEval.pm dbManLang.pm \
	dbManWeb.pm dbman.help.en dbman.help.cz nDBI.pm nDBD.pm \
	$RPM_BUILD_ROOT%{_datadir}/%{name}
install nonTk/Tk.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nonTk/Tk.pm
install nDBI/Statement.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBI/Statement.pm
install nDBI/Statement/Hash.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBI/Statement/Hash.pm
install plugExample.pm plugPgSql.pm plugOracle.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins
install nDBD/{ADO,Adabas,Altera,CSV,DB2,ExampleP,FreeTDS,Fulcrum,Illustra,Informix}.pm \
	nDBD/{Informix4,Ingres,NET,NullP,ODBC,Oracle,Pg,QBase,Solid,Sponge}.pm \
	nDBD/{Sybase,XBase,mSQL,mysql}.pm \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD
install Compact.pm $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%doc Alladin Artistic BSD BUGS CREDITS Changelog Eiffel LICENSE
%doc MIRRORS PGPKEY QPL README* TODO WHATSNEW
%attr(755,root,root) %{_bindir}/dbman*
%attr(755,root,root) %{_bindir}/tdesigner
%attr(755,root,root) %{_bindir}/xdbish
%attr(755,root,root) %{_sbindir}/*
%lang(cs) %attr(755,root,root) %{_bindir}/cz*
%lang(de) %attr(755,root,root) %{_bindir}/de*
%{_datadir}/%{name}
