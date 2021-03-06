# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/bufbuild/connect-go
%global goipath         github.com/bufbuild/connect-go
Version:                0.1.1

%gometa

%global common_description %{expand:
Simple, reliable, interoperable. A better gRPC.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple, reliable, interoperable. A better gRPC

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jun 21 2022 Brandon Bennett <brandon@brbe.me> - 0.1.1-1
- Bump version to 0.1.1
* Wed Jun 01 2022 Brandon Bennett <brandon@brbe.me> - 0.1.0-1
- Initial package
