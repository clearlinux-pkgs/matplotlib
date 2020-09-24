#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8D86E7FAE5EB0C10 (quantum.analyst@gmail.com)
#
Name     : matplotlib
Version  : 3.2.2
Release  : 61
URL      : https://files.pythonhosted.org/packages/9c/4b/06f4aa9bef6b5e4f177881b4dedd94faa6e7cb3d95dfaeaa8a1a8b541095/matplotlib-3.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/9c/4b/06f4aa9bef6b5e4f177881b4dedd94faa6e7cb3d95dfaeaa8a1a8b541095/matplotlib-3.2.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/9c/4b/06f4aa9bef6b5e4f177881b4dedd94faa6e7cb3d95dfaeaa8a1a8b541095/matplotlib-3.2.2.tar.gz.asc
Summary  : Python plotting package
Group    : Development/Tools
License  : Apache-1.1 BSD-3-Clause CC-BY-SA-4.0 HPND MIT NCSA OFL-1.0 OFL-1.1 Python-2.0 Qhull
Requires: matplotlib-license = %{version}-%{release}
Requires: matplotlib-python = %{version}-%{release}
Requires: matplotlib-python3 = %{version}-%{release}
Requires: cycler
Requires: kiwisolver
Requires: numpy
Requires: pyparsing
Requires: python-dateutil
BuildRequires : buildreq-distutils3
BuildRequires : cairo-dev
BuildRequires : cycler
BuildRequires : freetype-dev
BuildRequires : gtk+-dev
BuildRequires : gtk3-dev
BuildRequires : kiwisolver
BuildRequires : libpng-dev
BuildRequires : nose
BuildRequires : numpy
BuildRequires : pyparsing
BuildRequires : python-dateutil
BuildRequires : python-tcl
BuildRequires : pytz
BuildRequires : setuptools-python
BuildRequires : tornado

%description


%package license
Summary: license components for the matplotlib package.
Group: Default

%description license
license components for the matplotlib package.


%package python
Summary: python components for the matplotlib package.
Group: Default
Requires: matplotlib-python3 = %{version}-%{release}

%description python
python components for the matplotlib package.


%package python3
Summary: python3 components for the matplotlib package.
Group: Default
Requires: python3-core
Provides: pypi(matplotlib)
Requires: pypi(cycler)
Requires: pypi(kiwisolver)
Requires: pypi(numpy)
Requires: pypi(pyparsing)
Requires: pypi(python_dateutil)

%description python3
python3 components for the matplotlib package.


%prep
%setup -q -n matplotlib-3.2.2
cd %{_builddir}/matplotlib-3.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592584648
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/matplotlib
cp %{_builddir}/matplotlib-3.2.2/LICENSE/LICENSE %{buildroot}/usr/share/package-licenses/matplotlib/3683efd59fb44e798efb22fd086a5b1e3a0aa700
cp %{_builddir}/matplotlib-3.2.2/LICENSE/LICENSE.PIL %{buildroot}/usr/share/package-licenses/matplotlib/aa358d7ccbdf2c32d2f8ef908fac31c6c3b45ffe
cp %{_builddir}/matplotlib-3.2.2/LICENSE/LICENSE_AMSFONTS %{buildroot}/usr/share/package-licenses/matplotlib/91cf189e02755085234dd321326345846bf2949f
cp %{_builddir}/matplotlib-3.2.2/LICENSE/LICENSE_BAKOMA %{buildroot}/usr/share/package-licenses/matplotlib/4067e5ffa116d9da0db2eb77bdb1965e9245a814
cp %{_builddir}/matplotlib-3.2.2/LICENSE/LICENSE_COLORBREWER %{buildroot}/usr/share/package-licenses/matplotlib/47a57a5629a135f4301bf8181c5e244e1baf5759
cp %{_builddir}/matplotlib-3.2.2/LICENSE/LICENSE_CONDA %{buildroot}/usr/share/package-licenses/matplotlib/99189f9248eaa16323558ab3ab302bb5ca919001
cp %{_builddir}/matplotlib-3.2.2/LICENSE/LICENSE_JQUERY %{buildroot}/usr/share/package-licenses/matplotlib/c804f414dc9d1b584906802e9281119e333c1aff
cp %{_builddir}/matplotlib-3.2.2/LICENSE/LICENSE_PAINT %{buildroot}/usr/share/package-licenses/matplotlib/025714e1d469ac33a8703f2c85bfdd4fdc333c34
cp %{_builddir}/matplotlib-3.2.2/LICENSE/LICENSE_QT4_EDITOR %{buildroot}/usr/share/package-licenses/matplotlib/04bb73e33817fa6c0c1259344f7326b408e12885
cp %{_builddir}/matplotlib-3.2.2/LICENSE/LICENSE_YORICK %{buildroot}/usr/share/package-licenses/matplotlib/fd0bb2832315e88d7a06dd4f28a73f4eac46d3c6
cp %{_builddir}/matplotlib-3.2.2/LICENSE/LICENSE_enthought.txt %{buildroot}/usr/share/package-licenses/matplotlib/4e088a0ffe5e63c36917198db9554da352b8147e
cp %{_builddir}/matplotlib-3.2.2/LICENSE/pnpoly.license %{buildroot}/usr/share/package-licenses/matplotlib/0524125b28a9c13190bcedc80253636b7094ec79
cp %{_builddir}/matplotlib-3.2.2/doc/_static/fa/LICENSE %{buildroot}/usr/share/package-licenses/matplotlib/ffdcc916db94cb12d9a24791a5045147a9621ff9
cp %{_builddir}/matplotlib-3.2.2/doc/devel/license.rst %{buildroot}/usr/share/package-licenses/matplotlib/96cdc9c40477ab698d63b8c83fab29e2a8f72527
cp %{_builddir}/matplotlib-3.2.2/doc/users/license.rst %{buildroot}/usr/share/package-licenses/matplotlib/b3dd311f3c9b252fef52c78c4b6337203c0084a3
cp %{_builddir}/matplotlib-3.2.2/extern/agg24-svn/src/copying %{buildroot}/usr/share/package-licenses/matplotlib/467189783f672de8baca8b34e798fa2da64166a5
cp %{_builddir}/matplotlib-3.2.2/extern/libqhull/COPYING.txt %{buildroot}/usr/share/package-licenses/matplotlib/b92790f132c454fef32219a5a3eda4211e8250ff
cp %{_builddir}/matplotlib-3.2.2/lib/matplotlib/backends/web_backend/jquery-ui-1.12.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/matplotlib/15df6665dfd90f5cd8fdfde4c0c43051fbb76dae
cp %{_builddir}/matplotlib-3.2.2/lib/matplotlib/mpl-data/fonts/ttf/LICENSE_DEJAVU %{buildroot}/usr/share/package-licenses/matplotlib/23e8fed3e3499427ef5a80cbff0aca0946140493
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/matplotlib/025714e1d469ac33a8703f2c85bfdd4fdc333c34
/usr/share/package-licenses/matplotlib/04bb73e33817fa6c0c1259344f7326b408e12885
/usr/share/package-licenses/matplotlib/0524125b28a9c13190bcedc80253636b7094ec79
/usr/share/package-licenses/matplotlib/15df6665dfd90f5cd8fdfde4c0c43051fbb76dae
/usr/share/package-licenses/matplotlib/23e8fed3e3499427ef5a80cbff0aca0946140493
/usr/share/package-licenses/matplotlib/3683efd59fb44e798efb22fd086a5b1e3a0aa700
/usr/share/package-licenses/matplotlib/4067e5ffa116d9da0db2eb77bdb1965e9245a814
/usr/share/package-licenses/matplotlib/467189783f672de8baca8b34e798fa2da64166a5
/usr/share/package-licenses/matplotlib/47a57a5629a135f4301bf8181c5e244e1baf5759
/usr/share/package-licenses/matplotlib/4e088a0ffe5e63c36917198db9554da352b8147e
/usr/share/package-licenses/matplotlib/91cf189e02755085234dd321326345846bf2949f
/usr/share/package-licenses/matplotlib/96cdc9c40477ab698d63b8c83fab29e2a8f72527
/usr/share/package-licenses/matplotlib/99189f9248eaa16323558ab3ab302bb5ca919001
/usr/share/package-licenses/matplotlib/aa358d7ccbdf2c32d2f8ef908fac31c6c3b45ffe
/usr/share/package-licenses/matplotlib/b3dd311f3c9b252fef52c78c4b6337203c0084a3
/usr/share/package-licenses/matplotlib/b92790f132c454fef32219a5a3eda4211e8250ff
/usr/share/package-licenses/matplotlib/c804f414dc9d1b584906802e9281119e333c1aff
/usr/share/package-licenses/matplotlib/fd0bb2832315e88d7a06dd4f28a73f4eac46d3c6
/usr/share/package-licenses/matplotlib/ffdcc916db94cb12d9a24791a5045147a9621ff9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
