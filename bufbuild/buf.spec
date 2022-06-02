%global goipath github.com/bufbuild/buf
%global gotestflags %{gotestflags} -short

Version: 1.5.0

%gometa

%global common_description %{expand:
Buf helps your team work with Protocol Buffers APIs across their lifecycle, 
whether you’re building a new API for key customers or relying on one exposed 
by another team.}

%global golicenses    LICENSE
%global godocs        *.md

Name:    buf
Release: 2%{?disto}
Summary: A new way of working with Protocol Buffers
License: ASL 2.0
URL:     %{gourl}
Source:  %{gosource}
Patch0:  buf-disable-private-check.patch

BuildRequires: protobuf-compiler 

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

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

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Jun 02 2022 Brandon Bennett <brandon@brbe.me> - 1.5.0-2
- Disable `private` directory check that breaks when not compiling in module mode

* Wed Jun 01 2022 Brandon Bennett <brandon@brbe.me> - 1.5.0-1
- First packaging
