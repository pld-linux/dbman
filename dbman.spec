%include	/usr/lib/rpm/macros.perl
Summary:	Simple SQL monitor for common database system (PgSQL, Oracle and others)
Summary(pl):	Prosty interfejs do popularnych baz danych (PgSWL, Oracle itp.)
Name:		dbman
Version:	0.1.0	
Release:	2
License:	GPL QPL BSD Eiffel Artistic Alladin
Group:		Applications/Databases/Interfaces
Source0:	http://www.fi.muni.cz/~xsorm/%{name}/ftp/%{name}-%{version}.tar.gz
Patch0:		%{name}-FHS.patch
URL:		http://www.fi.muni.cz/~xsorm/%{name}/
BuildArch:	noarch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles %{_datadir}/%{name}/*
%define		_noautoreq "perl(Term::ReadLine)" "perl(Term::Slang)" "perl(Curses)"

%description
dbMan is a simple SQL monitor for common database system (PgSQL,
Oracle). It's based on Perl, Tk (include Tix) and DBI interfaces (nDBI
specification).

%description -l pl
dbMan to prosty interfejs SQL do popularnych baz danych. Wykorzystuje
on Perla, Tk oraz interfej DBI.

%prep
%setup -q
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_datadir}/%{name}/{plugins,nDBD,nonTk,nDBI/Statement}}
install dbman $RPM_BUILD_ROOT%{_bindir}/dbman
install czdbman $RPM_BUILD_ROOT%{_bindir}/czdbman
install dedbman $RPM_BUILD_ROOT%{_bindir}/dedbman
install dbman-bug $RPM_BUILD_ROOT%{_bindir}/dbman-bug
install dbman-proxy $RPM_BUILD_ROOT%{_bindir}/dbman-proxy
install dbman-sql-server $RPM_BUILD_ROOT%{_sbindir}/dbman-sql-server
install dbman-le $RPM_BUILD_ROOT%{_bindir}/dbman-le
install dbman-le-default $RPM_BUILD_ROOT%{_bindir}/dbman-le-default
install xdbish $RPM_BUILD_ROOT%{_bindir}/xdbish
install tdesigner $RPM_BUILD_ROOT%{_bindir}/tdesigner
install cztdesigner $RPM_BUILD_ROOT%{_bindir}/cztdesigner
install splash.gif $RPM_BUILD_ROOT%{_datadir}/%{name}/splash.gif
install folder.xbm $RPM_BUILD_ROOT%{_datadir}/%{name}/folder.xbm
install openfolder.xbm $RPM_BUILD_ROOT%{_datadir}/%{name}/openfolder.xbm
install viewfolder.xbm $RPM_BUILD_ROOT%{_datadir}/%{name}/viewfolder.xbm
install database.xbm $RPM_BUILD_ROOT%{_datadir}/%{name}/database.xbm
install Compact.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/Compact.pm
install Plugin.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/Plugin.pm
install checksum $RPM_BUILD_ROOT%{_datadir}/%{name}/checksum
install dbManEval.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/dbManEval.pm
install dbManLang.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/dbManLang.pm
install dbManWeb.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/dbManWeb.pm
install dbman.help.en $RPM_BUILD_ROOT%{_datadir}/%{name}/dbman.help.en
install dbman.help.cz $RPM_BUILD_ROOT%{_datadir}/%{name}/dbman.help.cz
install nDBI.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBI.pm
install nDBD.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD.pm
install nonTk/Tk.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nonTk/Tk.pm
install nDBI/Statement.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBI/Statement.pm
install nDBI/Statement/Hash.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBI/Statement/Hash.pm
install plugExample.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/plugExample.pm
install plugPgSql.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/plugPgSql.pm
install plugOracle.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/plugOracle.pm
install nDBD/ADO.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/ADO.pm
install nDBD/Adabas.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/Adabas.pm
install nDBD/Altera.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/Altera.pm
install nDBD/CSV.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/CSV.pm
install nDBD/DB2.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/DB2.pm
install nDBD/ExampleP.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/ExampleP.pm
install nDBD/FreeTDS.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/FreeTDS.pm
install nDBD/Fulcrum.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/Fulcrum.pm
install nDBD/Illustra.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/Illustra.pm
install nDBD/Informix.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/Informix.pm
install nDBD/Informix4.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/Informix4.pm
install nDBD/Ingres.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/Ingres.pm
install nDBD/NET.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/NET.pm
install nDBD/NullP.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/NullP.pm
install nDBD/ODBC.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/ODBC.pm
install nDBD/Oracle.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/Oracle.pm
install nDBD/Pg.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/Pg.pm
install nDBD/QBase.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/QBase.pm
install nDBD/Solid.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/Solid.pm
install nDBD/Sponge.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/Sponge.pm
install nDBD/Sybase.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/Sybase.pm
install nDBD/XBase.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/XBase.pm
install nDBD/mSQL.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/mSQL.pm
install nDBD/mysql.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/mysql.pm
install nDBD/pNET.pm $RPM_BUILD_ROOT%{_datadir}/%{name}/nDBD/pNET.pm

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
%lang(cz) %attr(755,root,root) %{_bindir}/cz* 
%lang(de) %attr(755,root,root) %{_bindir}/de* 
%{_datadir}/%{name}
