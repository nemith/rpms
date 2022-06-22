%global goipath github.com/ejoffe/spr 
%global gotestflags %{gotestflags} -short

Version: 0.9.0

%gometa

%global common_description %{expand:
Easily manage stacks of pull requests on GitHub. git spr is a client side tool
that achieves a simple streamlined stacked diff workflow using github pull 
requests and branches. git spr manages your pull request stacks for you, so you
don't have to.
}

%global golicenses    LICENSE
%global godocs        *.md

Name:    spr
Release: 1%{?disto}
Summary: Stacked Pull Requests on GitHub 
License: MIT
URL:     %{gourl}
Source:  %{gosource}

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

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jun 22 2022 Brandon Bennett <brandon@brbe.me> - 0.9.0-1
- First packaging
