# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/ejoffe/rake
%global goipath         github.com/ejoffe/rake
Version:                0.3.2

%gometa

%global common_description %{expand:
Simple, Extensible Go Configuration library.}

%global golicenses      LICENSE
%global godocs          docs README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple, Extensible Go Configuration library

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jun 22 2022 Brandon Bennett <brandon@brbe.me> - 0.3.2-1
- Initial package
