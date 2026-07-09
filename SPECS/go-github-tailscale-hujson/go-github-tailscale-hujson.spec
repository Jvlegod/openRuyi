# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hujson
%define go_import_path  github.com/tailscale/hujson
%define commit_id       ecc657c15afd

Name:           go-github-tailscale-hujson
Version:        0.0.0+git20260302.ecc657c
Release:        %autorelease
Summary:        Go library packaged for syft dependency resolution
License:        BSD-3-Clause
URL:            https://github.com/tailscale/hujson
#!RemoteAsset
Source0:        %{url}/archive/ecc657c15afd.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-ecc657c15afd

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/tailscale/hujson) = %{version}

%description
Go library packaged for syft dependency resolution.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
