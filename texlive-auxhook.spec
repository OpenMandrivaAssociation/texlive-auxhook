%global tl_name auxhook
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Hooks for auxiliary files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/auxhook
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/auxhook.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/auxhook.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/auxhook.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package auxhook provides hooks for adding stuff at the begin of
.aux files.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/auxhook
%dir %{_datadir}/texmf-dist/source/latex/auxhook
%dir %{_datadir}/texmf-dist/tex/latex/auxhook
%doc %{_datadir}/texmf-dist/doc/latex/auxhook/README.md
%doc %{_datadir}/texmf-dist/doc/latex/auxhook/auxhook.pdf
%doc %{_datadir}/texmf-dist/source/latex/auxhook/auxhook.dtx
%{_datadir}/texmf-dist/tex/latex/auxhook/auxhook.sty
