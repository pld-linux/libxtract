Summary:	LibXtract - a library of audio feature extraction functions
Summary(pl.UTF-8):	LibXtract - biblioteka funkcji do wydobywania cech dźwięku
Name:		libxtract
Version:	0.6.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/libxtract/%{name}-%{version}.tar.gz
# Source0-md5:	f84a55a392a2688f1c3fffc061c73c25
URL:		http://libxtract.sourceforge.net/
BuildRequires:	fftw3-single-devel >= 2.0
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

%description -l pl.UTF-8
LibXtract to prosta, przenośna i lekka biblioteka funkcji do
wydobywania cech dźwięku. Celem biblioteki jest dostarczenie w miarę
wyczerpującego zbioru prymitywów wydobywania cech, które mogą być
łączone "kaskadowo" tworząc hierarchie wydobywania. Na przykład
wariancja, odchylenie standardowe, skośność i kurtoza wymagają
wcześniejszego obliczenia średniej wektora wejściowego. Jednak zamiast
obliczać średnią wewnątrz każdej funkcji, powinna ona być przekazywana
jako argument. Oznacza to, że jeśli użytkownik chce użyć wszystkich
tych cech, średnia jest obliczana tylko raz i przekazywana do
wszystkich wymagających jej funkcji.

Filozofia cech "kaskadowych" jest wykorzystywana w całej bibliotece,
na przykład w przypadku cech operujących na widmie wartości
bezwzględnych wektora sygnału (np. nieregularność) widmo nie jest
obliczane wewnątrz danej funkcji, lecz wskaźnik do pierwszego
elementu w tablicy zawierającej widmo wartości bezwzględnych jest
przekazywany jako argument.

Powoduje to, że biblioteka jest nie tylko bardziej wydajna przy
obliczaniu wielu cech jednocześnie, ale także bardziej elastyczna,
ponieważ funkcje wydobywania mogą być łączone w dowolny sposób
(można na przykład uzyskać nieregularność współczynników cepstrum
częstotliwości Mela).

%package devel
Summary:	Header files for libxtract library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxtract
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	fftw3-single-devel >= 2.0

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
%configure \
	--enable-fft

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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libxtract.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxtract.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxtract.so
%{_libdir}/libxtract.la
%{_includedir}/xtract
%{_pkgconfigdir}/libxtract.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxtract.a
