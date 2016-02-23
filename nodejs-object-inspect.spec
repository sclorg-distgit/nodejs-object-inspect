# spec file for package nodejs-nodejs-object-inspect
%{?scl:%scl_package nodejs-object-inspect}
%{!?scl:%global pkg_name %{name}}

%global npm_name object-inspect
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-object-inspect
Version:	1.0.1
Release:	3%{?dist}
Summary:	string representations of objects in node and the browser
Url:		https://github.com/substack/object-inspect
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
#BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(tape)
%endif

%description
string representations of objects in node and the browser

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tape test/*.js
%endif

%files
%{nodejs_sitelib}/object-inspect

%doc readme.markdown
%license LICENSE

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-3
- rebuilt

* Thu Jul 30 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-2
- Fix typo

* Wed Jul 29 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-1
- Initial build
