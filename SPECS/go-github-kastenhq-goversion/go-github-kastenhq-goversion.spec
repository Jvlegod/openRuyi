# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goversion
%define go_import_path  github.com/kastenhq/goversion
%define commit_id       93b2f8823953

Name:           go-github-kastenhq-goversion
Version:        0.0.0+git20230811.93b2f88
Release:        %autorelease
Summary:        Go library packaged for syft dependency resolution
License:        BSD-3-Clause
URL:            https://github.com/kastenhq/goversion
#!RemoteAsset
Source0:        %{url}/archive/93b2f8823953.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-93b2f8823953

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/kastenhq/goversion) = %{version}

%description
Go library packaged for syft dependency resolution.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
