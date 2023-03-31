Name:		texlive-auxhook
Version:	53173
Release:	2
Summary:	Hooks for auxiliary files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/auxhook
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/auxhook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/auxhook.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/auxhook.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package auxhook provides hooks for adding stuff at the
begin of .aux files.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/auxhook
%{_texmfdistdir}/tex/latex/auxhook
%doc %{_texmfdistdir}/doc/latex/auxhook

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
