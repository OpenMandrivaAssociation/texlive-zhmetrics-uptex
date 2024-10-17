Name:		texlive-zhmetrics-uptex
Version:	40728
Release:	2
Summary:	Chinese font metrics for upTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/zhmetrics-uptex
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zhmetrics-uptex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zhmetrics-uptex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package contains some Chinese font metrics (JFM, VF, etc)
for upTeX engine, together with a simple DVIPDFMx font mapping
of Fandol fonts for DVIPDFMx.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/vf/public/zhmetrics-uptex
%{_texmfdistdir}/fonts/tfm/public/zhmetrics-uptex
%doc %{_texmfdistdir}/doc/fonts/zhmetrics-uptex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
