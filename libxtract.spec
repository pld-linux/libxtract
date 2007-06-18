Summary:	LibXtract is a library of audio feature extraction functions
Name:		libxtract
Version:	0.4.5
Release:	0.1
License:	GPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/libxtract/%{name}-%{version}.tar.gz
# Source0-md5:	1d1987330a81b03309584e6bdadb0c72
URL:		http://libxtract.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibXtract is a simple, portable, lightweight library of audio feature
extraction functions. The purpose of the library is to provide a
relatively exhaustive set of feature extraction primatives that are
designed to be 'cascaded' to create a extraction hierarchies. For
example, 'variance', 'average deviation', 'skewness' and 'kurtosis',
all require the 'mean' of the input vector to be precomputed. However,
rather than compute the 'mean' 'inside' each function, it is expected
that the 'mean' will be passed in as an argument. This means that if
the user wishes to use all of these features, the mean is calculated
only once, and then passed to any functions that require it.

This philosophy of 'cascading' features is followed throughout the
library, for example with features that operate on the magnitude
spectrum of a signal vector (e.g. 'irregularity'), the magnitude
spectrum is not calculated 'inside' the respective function, instead,
a pointer to the first element in an array containing the magnitude
spectrum is passed in as an argument.

Hopefully this not only makes the library more efficient when
computing large numbers of features, but also makes it more flexible
because extraction functions can be combined arbitrarily (one can take
the irregularility of the Mel Frequency Cepstral Coefficients for
example).

%package devel
Summary:	Header files for libxtract library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxtract
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libxtract library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libxtract.

%package static
Summary:	Static libxtract library
Summary(pl.UTF-8):	Statyczna biblioteka libxtract
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxtract library.

%description static -l pl.UTF-8
Statyczna biblioteka libxtract.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
