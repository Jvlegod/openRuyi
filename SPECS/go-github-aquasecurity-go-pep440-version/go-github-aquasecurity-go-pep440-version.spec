# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-pep440-version
%define go_import_path  github.com/aquasecurity/go-pep440-version

Name:           go-github-aquasecurity-go-pep440-version
Version:        0.0.1
Release:        %autorelease
Summary:        Go library for parsing PEP 440 Python versions
License:        Apache-2.0
URL:            https://github.com/aquasecurity/go-pep440-version
#!RemoteAsset
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aquasecurity/go-version)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/xerrors)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/aquasecurity/go-pep440-version) = %{version}

Requires:       go(github.com/aquasecurity/go-version)
Requires:       go(golang.org/x/xerrors)

%description
Go library for parsing PEP 440 compliant Python versions.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
