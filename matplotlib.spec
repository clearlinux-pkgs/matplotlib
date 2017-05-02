#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : matplotlib
Version  : 2.0.1
Release  : 15
URL      : https://github.com/matplotlib/matplotlib/archive/v2.0.1.tar.gz
Source0  : https://github.com/matplotlib/matplotlib/archive/v2.0.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-1.1 BSD-3-Clause HPND MIT NCSA OFL-1.0 OFL-1.1 Python-2.0 Qhull
Requires: matplotlib-python
Requires: functools32
Requires: python-tcl
BuildRequires : cairo-dev
BuildRequires : freetype-dev
BuildRequires : gtk+-dev
BuildRequires : gtk3-dev
BuildRequires : libpng-dev
BuildRequires : nose
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyparsing
BuildRequires : pytest
BuildRequires : python-dateutil
BuildRequires : python-dev
BuildRequires : python-tcl
BuildRequires : python3-dev
BuildRequires : pytz
BuildRequires : setuptools
BuildRequires : tornado
BuildRequires : tox
BuildRequires : virtualenv

%description
About Matplotlib Testing Infrastructure
---------------------------------------
Information on the testing infrastructure is provided in
the Testing section of the Matplotlib Developersâ Guide:

%package python
Summary: python components for the matplotlib package.
Group: Default

%description python
python components for the matplotlib package.


%prep
%setup -q -n matplotlib-2.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493746052
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1493746052
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
