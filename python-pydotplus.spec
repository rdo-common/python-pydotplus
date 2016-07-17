%global modname pydotplus

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{modname}
Version:        2.0.2
Release:        2%{?dist}
Summary:        Python interface to Graphviz's Dot language

License:        MIT
URL:            https://pypi.python.org/pypi/%{modname}
Source0:        https://pypi.python.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  graphviz

%description
PyDotPlus is an improved version of the old pydot project that provides a
Python Interface to Graphviz's Dot language.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python2-setuptools
BuildRequires:  pyparsing
Requires:       pyparsing
Requires:       graphviz

%description -n python2-%{modname}
PyDotPlus is an improved version of the old pydot project that provides a
Python Interface to Graphviz's Dot language.

Python 2 version.

%if 0%{?with_python3}
%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-setuptools
BuildRequires:  python3-pyparsing
Requires:       python3-pyparsing
Requires:       graphviz

%description -n python3-%{modname}
PyDotPlus is an improved version of the old pydot project that provides a
Python Interface to Graphviz's Dot language.

Python 3 version.
%endif

%prep
%autosetup -n %{modname}-%{version}

rm -rf lib/*.egg-info

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%check
# https://github.com/carlos-jenkins/pydotplus/issues/2
pushd test
  PYTHONPATH=%{buildroot}%{python2_sitelib} %{__python2} pydot_unittest.py -v || :
%if 0%{?with_python3}
  PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} pydot_unittest.py -v || :
%endif
popd

%files -n python2-%{modname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{modname}*

%if 0%{?with_python3}
%files -n python3-%{modname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}*
%endif

%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0.2-1
- Initial package
