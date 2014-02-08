# revision 27203
# category Package
# catalog-ctan /macros/latex/contrib/nameauth
# catalog-date 2012-07-27 23:04:27 +0200
# catalog-license lppl1.3
# catalog-version 1.4
Name:		texlive-nameauth
Version:	1.40
Release:	2
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


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.40-1
+ Revision: 812638
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.26-1
+ Revision: 804950
- Update to latest release.

* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 790725
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 787691
- Update to latest release.

* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 779617
- Update to latest release.

* Wed Feb 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.86-1
+ Revision: 772125
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.75-1
+ Revision: 770228
- Update to latest upstream package

* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.7-1
+ Revision: 758991
- texlive-nameauth
- texlive-nameauth

