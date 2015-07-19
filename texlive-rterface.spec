# revision 30084
# category Package
# catalog-ctan /macros/latex/contrib/rterface
# catalog-date 2013-04-23 19:30:36 +0200
# catalog-license lppl1.2
# catalog-version undef
Name:		texlive-rterface
Version:	20130423
Release:	9
Summary:	Access to R analysis from within a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rterface
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rterface.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rterface.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package mediates interaction between LaTeX and R; it allows
LaTeX to set R's parameters, and provides code to read R
output.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rterface/rterface.sty
%doc %{_texmfdistdir}/doc/latex/rterface/README
%doc %{_texmfdistdir}/doc/latex/rterface/rterface.pdf
%doc %{_texmfdistdir}/doc/latex/rterface/rterface.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
