Name:		texlive-nameauth
Version:	65738
Release:	2
Summary:	Name authority mechanism for consistency in body text and index
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nameauth
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nameauth.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nameauth.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nameauth.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/nameauth
%doc %{_texmfdistdir}/doc/latex/nameauth
#- source
%doc %{_texmfdistdir}/source/latex/nameauth

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
