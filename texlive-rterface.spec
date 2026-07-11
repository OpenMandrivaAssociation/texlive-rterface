%global tl_name rterface
%global tl_revision 30084

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Access to R analysis from within a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rterface
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rterface.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rterface.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package mediates interaction between LaTeX and R; it allows LaTeX to
set R's parameters, and provides code to read R output.

