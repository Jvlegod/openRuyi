# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonschema
%define go_import_path  github.com/invopop/jsonschema

Name:           go-github-invopop-jsonschema
Version:        0.14.0
Release:        %autorelease
Summary:        Go library packaged for syft dependency resolution
License:        MIT
URL:            https://github.com/invopop/jsonschema
#!RemoteAsset
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/invopop/jsonschema) = %{version}

%description
Go library packaged for syft dependency resolution.

%files
%license COPYING*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
