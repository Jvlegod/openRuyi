# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           rapid
%define go_import_path  pgregory.net/rapid

Name:           go-pgregory-rapid
Version:        1.3.0
Release:        %autorelease
Summary:        Go library for property-based testing
License:        MPL-2.0
URL:            https://github.com/flyingmutant/rapid
#!RemoteAsset:  sha256:205a612d771db6c156a729d159ce6e07ff80a03537b900c8163301e414ad2f17
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(pgregory.net/rapid) = %{version}

%check -p
# golangmodules runs tests with GO111MODULE=off, so Go cannot read the
# upstream go 1.23 directive that enables synchronous timer channels required
# by testing/synctest on Go 1.25+.
export GODEBUG=asynctimerchan=0

%description
Rapid is a Go library for property-based testing. It checks properties
against automatically generated test cases and minimizes failing cases
before reporting them.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
