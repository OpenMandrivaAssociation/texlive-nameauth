# revision 25244
# category Package
# catalog-ctan /macros/latex/contrib/nameauth
# catalog-date 2012-01-20 13:06:48 +0100
# catalog-license lppl1.3
# catalog-version 0.75
Name:		texlive-nameauth
Version:	0.75
Release:	1
Summary:	Name authority mechanism for consistency in body text and index
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nameauth
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nameauth.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nameauth.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nameauth.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Publications, that reference many names, require editors and
proofreaders to track those names in the text and index. The
package offers name authority macros that allow authors and
compilers to normalize occurrences of names, variant name
forms, and pen names in the text and index. This may help
minimize writing and production time and cost.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nameauth/nameauth.sty
%doc %{_texmfdistdir}/doc/latex/nameauth/Makefile
%doc %{_texmfdistdir}/doc/latex/nameauth/README
%doc %{_texmfdistdir}/doc/latex/nameauth/nameauth.pdf
#- source
%doc %{_texmfdistdir}/source/latex/nameauth/nameauth.dtx
%doc %{_texmfdistdir}/source/latex/nameauth/nameauth.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
