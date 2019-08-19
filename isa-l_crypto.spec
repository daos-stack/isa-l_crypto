# doesn't seem to work on sles 12.3: %{!?make_build:%define make_build %{__make} %{?_smp_mflags}}
# so...
%if 0%{?suse_version} <= 1320
%define make_build  %{__make} %{?_smp_mflags}
%endif

Name:		isa-l_crypto
Version:	2.21.0
Release:	1%{?dist}

Summary:	Intelligent Storage Acceleration Library Crypto Version

Group:		Development/Libraries
License:	BSD-3-Clause
URL:		https://github.com/01org/isa-l_crypto/wiki
Source0:        https://github.com/01org/%{name}/archive/v%{version}.tar.gz

BuildRequires: yasm

# to be able to generate configure if not present
BuildRequires: autoconf, automake, libtool

%description
The igzip utility.

%package -n libisa-l_crypto
Summary: Dynamic library for isa-l_crypto functions
License: BSD-3-Clause
Obsoletes: %{name} < %{version}

%description -n libisa-l_crypto
ISA-L_crypto is a collection of optimized low-level functions
targeting storage applications. ISA-L_crypto includes:
- Multi-buffer hashes - run multiple hash jobs together on one core
for much better throughput than single-buffer versions. (
SHA1, SHA256, SHA512, MD5)
- Multi-hash - Get the performance of multi-buffer hashing with a single-buffer interface.
- Multi-hash + murmur - run both together.
- AES - block ciphers (XTS, GCM, CBC)
- Rolling hash - Hash input in a window which moves through the input

%package -n libisa-l_crypto-devel
Summary:	ISA-L_CRYPTO devel package
Requires:	lib%{name}%{?_isa} = %{version}
Provides:	lib%{name}-static%{?_isa} = %{version}

%description -n libisa-l_crypto-devel
ISA-L_CRYPTO devel

%prep
%autosetup -p1

%build
if [ ! -f configure ]; then
    ./autogen.sh --no-oshmem
fi
%configure

%{make_build}

%install
%make_install
find %{?buildroot} -name *.la -print0 | xargs -r0 rm -f

%files -n libisa-l_crypto
%{_libdir}/*.so.*

%files -n libisa-l_crypto-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a

%changelog
* Fri Aug 16 2019 Ryon Jensen <ryon.jensen@intel> - 2.21.0-1
- initial package
